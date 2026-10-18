from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash,
    send_file,
)
from models import (
    db,
    Tour,
    Usuario,
    Pedido,
    DescargaOffline,
    BlogPost,
    Valoracion,
    Suscripcion,
)
from werkzeug.security import generate_password_hash, check_password_hash
from app.schemas.auth import UsuarioRegisterSchema as RegisterSchema
from marshmallow import ValidationError
from datetime import datetime, timedelta
import io
import zipfile
import requests
from xhtml2pdf import pisa

web_bp = Blueprint("web", __name__)


@web_bp.route("/")
def home():
    countries = db.session.query(Tour.country, Tour.flag_url).distinct().all()
    tours = Tour.query.filter_by(activo=True).limit(4).all()
    return render_template("index.html", countries=countries, tours=tours)


@web_bp.route("/search")
def search():
    query = request.args.get("q", "")
    if query:
        tours = Tour.query.filter(
            (Tour.titulo.ilike(f"%{query}%"))
            | (Tour.city.ilike(f"%{query}%"))
            | (Tour.country.ilike(f"%{query}%"))
        ).all()
    else:
        tours = []
    return render_template("search.html", tours=tours, query=query)


@web_bp.route("/countries")
def all_countries():
    countries = db.session.query(Tour.country, Tour.flag_url).distinct().all()
    return render_template("countries.html", countries=countries)


@web_bp.route("/country/<country_name>")
def country(country_name):
    tours = Tour.query.filter_by(country=country_name).all()
    cities = {}
    for t in tours:
        cities[t.city] = t.city_description
    first_tour = tours[0] if tours else None
    flag = first_tour.flag_url if first_tour else ""
    desc = first_tour.city_description if first_tour else ""
    return render_template(
        "country.html", country=country_name, cities=cities, flag=flag, desc=desc
    )


@web_bp.route("/city/<city_name>")
def city(city_name):
    categoria = request.args.get("categoria")
    orden = request.args.get("orden", "nuevo")
    page = request.args.get("page", 1, type=int)
    query = Tour.query.filter_by(city=city_name)
    if categoria:
        query = query.filter_by(categoria=categoria)
    if orden == "precio_asc":
        query = query.order_by(Tour.precio.asc())
    elif orden == "precio_desc":
        query = query.order_by(Tour.precio.desc())
    else:
        query = query.order_by(Tour.id_tour.desc())
    pagination = query.paginate(page=page, per_page=2, error_out=False)
    tours = pagination.items
    first_tour = Tour.query.filter_by(city=city_name).first()
    city_desc = first_tour.city_description if first_tour else ""
    flag = first_tour.flag_url if first_tour else ""
    country = first_tour.country if first_tour else ""
    all_city_tours = Tour.query.filter_by(city=city_name).all()
    categories = list(set([t.categoria for t in all_city_tours]))
    return render_template(
        "catalogo.html",
        city=city_name,
        country=country,
        tours=tours,
        city_desc=city_desc,
        flag=flag,
        categories=categories,
        current_cat=categoria,
        current_orden=orden,
        pagination=pagination,
    )


@web_bp.route("/tour/<int:tour_id>")
def detalle_tour(tour_id):
    tour = db.get_or_404(Tour, tour_id)
    bought = False
    active_sub = None

    if session.get("user_id"):
        bought = (
            Pedido.query.filter_by(
                id_usuario=session["user_id"], id_tour=tour_id, estado="paid"
            ).first()
            is not None
        )
        active_sub = Suscripcion.query.filter_by(
            id_usuario=session["user_id"], estado="active"
        ).first()
        if active_sub and not active_sub.is_active:
            active_sub = None

    related_tours = (
        Tour.query.filter(Tour.city == tour.city, Tour.id_tour != tour.id_tour)
        .limit(3)
        .all()
    )
    reviews = Valoracion.query.filter_by(id_tour=tour.id_tour).all()

    return render_template(
        "tour.html",
        tour=tour,
        bought=bought,
        related_tours=related_tours,
        reviews=reviews,
        active_sub=active_sub,
    )


@web_bp.route("/my-tour/<int:tour_id>")
def my_tour(tour_id):
    if not session.get("user_id"):
        return redirect(url_for("web.login"))

    pedido = Pedido.query.filter_by(
        id_usuario=session["user_id"], id_tour=tour_id, estado="paid"
    ).first()

    suscripcion = Suscripcion.query.filter_by(
        id_usuario=session["user_id"], estado="active"
    ).first()
    has_access = pedido is not None or (suscripcion and suscripcion.is_active)

    if not has_access:
        flash("You must buy this tour or have an active subscription.", "error")
        return redirect(url_for("web.detalle_tour", tour_id=tour_id))

    tour = db.get_or_404(Tour, tour_id)

    pois_data = [{"nombre": p.nombre, "lat": p.lat, "lng": p.lng} for p in tour.puntos]
    itinerary_data = [
        {
            "place": i.get("place", ""),
            "time": i.get("time", ""),
            "desc": i.get("desc", ""),
            "day": i.get("day", 1),
        }
        for i in tour.itinerary
    ]
    audios_data = [{"titulo": a.titulo, "url": a.archivo_url} for a in tour.audios]

    return render_template(
        "my_tour.html",
        tour=tour,
        pois_data=pois_data,
        itinerary_data=itinerary_data,
        audios_data=audios_data,
    )


@web_bp.route("/claim-tour/<int:tour_id>", methods=["POST"])
def claim_tour(tour_id):
    if not session.get("user_id"):
        return redirect(url_for("web.login"))

    sub = Suscripcion.query.filter_by(
        id_usuario=session["user_id"], estado="active"
    ).first()
    if not sub or not sub.is_active:
        flash("You need an active subscription to claim this tour.", "error")
        return redirect(url_for("web.detalle_tour", tour_id=tour_id))

    existing = Pedido.query.filter_by(
        id_usuario=session["user_id"], id_tour=tour_id
    ).first()
    if not existing:
        pedido = Pedido(
            id_usuario=session["user_id"],
            id_tour=tour_id,
            monto=0,
            metodo_pago="subscription",
            estado="paid",
        )
        db.session.add(pedido)
        db.session.commit()
        flash("Tour added to your library!", "success")

    return redirect(url_for("web.my_tour", tour_id=tour_id))


@web_bp.route("/about")
def about():
    return render_template("about.html")


@web_bp.route("/free-guide")
def free_guide():
    return render_template("free_guide.html")


@web_bp.route("/download-guide")
def download_guide():
    html_content = """
    <html>
    <head>
        <style>
            body { font-family: Helvetica, Arial, sans-serif; color: #333; line-height: 1.6; }
            h1 { color: #0c2a4d; border-bottom: 2px solid #fedd00; padding-bottom: 10px; }
            h2 { color: #c05621; margin-top: 30px; }
            ul { margin-bottom: 20px; }
            li { margin-bottom: 10px; }
        </style>
    </head>
    <body>
        <h1>LatamXP: The Ultimate Latin America Survival Guide</h1>
        <p>Welcome to Latin America! This guide contains everything you need to know for a safe and enjoyable trip across the continent.</p>
        
        <h2>1. Connectivity: SIM Cards & Internet</h2>
        <ul>
            <li><strong>Buying SIM Cards:</strong> Every country has its own providers (Claro, Movistar, Entel, etc.). You will need your passport to register a SIM card.</li>
            <li><strong>eSIM is King:</strong> If your phone supports eSIM, use apps like Airalo or Holafly. It's often cheaper and saves you from hunting down physical stores in every new country.</li>
            <li><strong>Wi-Fi:</strong> Widely available in cafes and hotels, but security can be an issue. Use a VPN for sensitive data.</li>
        </ul>

        <h2>2. Getting Around: Transport</h2>
        <ul>
            <li><strong>Apps:</strong> Uber and Cabify are available in most major cities. For public transport, use Google Maps or Moovit.</li>
            <li><strong>Local Cards:</strong> Most cities require a rechargeable card for buses and metros (e.g., SUBE in Buenos Aires, Bip! in Santiago).</li>
            <li><strong>Air Travel:</strong> Budget airlines like LATAM, Avianca, and Sky are great for crossing long distances quickly.</li>
        </ul>

        <h2>3. Safety & Neighborhoods</h2>
        <ul>
            <li><strong>General Rule:</strong> Don't flash expensive phones or jewelry. Keep your bag in front of you in crowded areas.</li>
            <li><strong>At Night:</strong> Stick to well-lit, busy areas. Avoid walking alone in empty streets or parks.</li>
            <li><strong>Research:</strong> Always check which neighborhoods are safe in each city you visit. Tourist areas are generally safe during the day.</li>
        </ul>

        <h2>4. Basic Spanish & Slang</h2>
        <ul>
            <li><strong>Hola / Adiós:</strong> Hello / Goodbye</li>
            <li><strong>Por favor / Gracias:</strong> Please / Thank you</li>
            <li><strong>¿Cuánto cuesta?:</strong> How much does it cost?</li>
            <li><strong>La cuenta, por favor:</strong> The bill, please</li>
            <li><strong>¿Dónde está el baño?:</strong> Where is the bathroom?</li>
            <li><strong>No entiendo:</strong> I don't understand</li>
        </ul>

        <h2>5. Tipping & Local Food</h2>
        <ul>
            <li><strong>Restaurants:</strong> A 10% tip is standard in many countries (Argentina, Chile, Mexico). Check if it's already included.</li>
            <li><strong>Food to try:</strong> Asado (Argentina), Tacos (Mexico), Ceviche (Peru), Arepas (Colombia/Venezuela).</li>
        </ul>
        <br>
        <p><em>Enjoy your trip! - LatamXP Team</em></p>
    </body>
    </html>
    """

    pdf_buffer = io.BytesIO()
    pisa_status = pisa.CreatePDF(io.StringIO(html_content), dest=pdf_buffer)

    if pisa_status.err:
        flash("Error generating PDF.", "error")
        return redirect(url_for("web.free_guide"))

    pdf_buffer.seek(0)

    return send_file(
        pdf_buffer,
        mimetype="application/pdf",
        as_attachment=True,
        download_name="LatamXP_Latin_America_Guide.pdf",
    )


@web_bp.route("/blog")
def blog():
    posts = BlogPost.query.all()
    return render_template("blog.html", posts=posts)


@web_bp.route("/blog/<int:post_id>")
def blog_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    return render_template("blog_post.html", post=post)


@web_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = Usuario.query.filter_by(email=request.form.get("email")).first()
        if user and user.check_password(request.form.get("password")):
            session["user_id"] = user.id_usuario
            session["user_name"] = user.nombre
            return redirect(url_for("web.dashboard"))
        flash("Invalid credentials", "error")
    return render_template("login.html")


@web_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        schema = RegisterSchema()
        try:
            data = schema.load(request.form)
        except ValidationError as err:
            for field, messages in err.messages.items():
                for msg in messages:
                    flash(msg, "error")
            return redirect(url_for("web.registro"))
        email = data.get("email")
        if Usuario.query.filter_by(email=email).first():
            flash("Email is already registered.", "error")
            return redirect(url_for("web.registro"))
        user = Usuario(
            nombre=data.get("nombre"),
            email=email,
            idioma_preferido=data.get("idioma", "es"),
        )
        user.set_password(data.get("password"))
        db.session.add(user)
        db.session.commit()
        session["user_id"] = user.id_usuario
        session["user_name"] = user.nombre
        return redirect(url_for("web.dashboard"))
    return render_template("registro.html")


@web_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("web.home"))


@web_bp.route("/cancel-subscription", methods=["POST"])
def cancel_subscription():
    if not session.get("user_id"):
        return redirect(url_for("web.login"))

    suscripcion = Suscripcion.query.filter_by(
        id_usuario=session["user_id"], estado="active"
    ).first()
    if suscripcion:
        suscripcion.estado = "cancelled"
        db.session.commit()
        flash(
            "Subscription cancelled. You will keep access until the end of your billing period.",
            "success",
        )

    return redirect(url_for("web.dashboard"))


@web_bp.route("/dashboard")
def dashboard():
    if not session.get("user_id"):
        return redirect(url_for("web.login"))
    user = db.get_or_404(Usuario, session["user_id"])
    pedidos = user.get_pedidos_activos()

    descargas = DescargaOffline.query.filter_by(id_usuario=user.id_usuario).all()
    downloaded_tour_ids = {d.id_tour for d in descargas}

    valoraciones = Valoracion.query.filter_by(id_usuario=user.id_usuario).all()
    reviewed_tour_ids = {v.id_tour for v in valoraciones}

    suscripcion = (
        Suscripcion.query.filter_by(id_usuario=user.id_usuario, estado="active")
        .order_by(Suscripcion.fecha_fin.desc())
        .first()
    )

    if suscripcion and suscripcion.is_active:
        days_left = (suscripcion.fecha_fin - datetime.utcnow()).days
        if days_left <= 3:
            flash(
                f"Your subscription expires in {days_left} days! Please renew to keep access.",
                "warning",
            )

    return render_template(
        "dashboard.html",
        pedidos=pedidos,
        downloaded_tour_ids=downloaded_tour_ids,
        reviewed_tour_ids=reviewed_tour_ids,
        suscripcion=suscripcion,
    )


@web_bp.route("/delete-download/<int:tour_id>")
def delete_download(tour_id):
    if not session.get("user_id"):
        return redirect(url_for("web.login"))
    descarga = DescargaOffline.query.filter_by(
        id_usuario=session["user_id"], id_tour=tour_id
    ).first()
    if descarga:
        db.session.delete(descarga)
        db.session.commit()
        flash("Download removed successfully to free up space.", "success")
    return redirect(url_for("web.dashboard"))


@web_bp.route("/add-review/<int:tour_id>", methods=["POST"])
def add_review(tour_id):
    if not session.get("user_id"):
        return redirect(url_for("web.login"))
    puntuacion = int(request.form.get("puntuacion", 5))
    comentario = request.form.get("comentario", "")
    existing = Valoracion.query.filter_by(
        id_usuario=session["user_id"], id_tour=tour_id
    ).first()
    if existing:
        existing.puntuacion = puntuacion
        existing.comentario = comentario
    else:
        nueva = Valoracion(
            id_usuario=session["user_id"],
            id_tour=tour_id,
            puntuacion=puntuacion,
            comentario=comentario,
        )
        db.session.add(nueva)
    db.session.commit()
    flash("Review submitted successfully! Thank you.", "success")
    return redirect(url_for("web.dashboard"))


@web_bp.route("/download/<int:tour_id>")
def download_tour(tour_id):
    if not session.get("user_id"):
        return redirect(url_for("web.login"))

    tour = db.get_or_404(Tour, tour_id)
    audios = tour.audios

    if not audios:
        flash("No audio files available for this tour.", "error")
        return redirect(url_for("web.dashboard"))

    memory_file = io.BytesIO()
    with zipfile.ZipFile(memory_file, "w", zipfile.ZIP_DEFLATED) as zf:
        audio_files = {}
        for audio in audios:
            try:
                response = requests.get(audio.archivo_url, timeout=10)
                if response.status_code == 200:
                    filename = (
                        f"audio/{audio.orden:02d}_{audio.titulo.replace(' ', '_')}.mp3"
                    )
                    zf.writestr(filename, response.content)
                    audio_files[audio.titulo] = filename
            except Exception as e:
                print(f"Failed to download {audio.archivo_url}: {e}")

        html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{tour.titulo} - Offline Guide</title>
            <style>
                body {{ font-family: system-ui, -apple-system, sans-serif; background: #f4f4f4; color: #333; margin: 0; padding: 20px; }}
                .container {{ max-width: 800px; margin: 0 auto; background: #fff; padding: 30px; border-radius: 15px; box-shadow: 0 5px 15px rgba(0,0,0,0.1); }}
                h1 {{ color: #0c2a4d; border-bottom: 3px solid #fedd00; padding-bottom: 10px; }}
                .day {{ margin-top: 30px; font-size: 1.5rem; color: #c05621; font-weight: bold; border-left: 5px solid #fedd00; padding-left: 10px; }}
                .step {{ background: #f8f9fa; padding: 15px; margin-bottom: 15px; border-radius: 10px; border-left: 4px solid #74acdf; }}
                .step h3 {{ margin: 0 0 5px 0; color: #0c2a4d; }}
                .step p {{ margin: 0; color: #666; font-size: 0.9rem; }}
                .time {{ font-weight: bold; color: #c05621; font-size: 0.85rem; }}
                .audio-section {{ margin-top: 40px; background: #0c2a4d; padding: 20px; border-radius: 10px; color: #fff; }}
                audio {{ width: 100%; margin-top: 10px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>{tour.titulo}</h1>
                <p style="color: #666;">{tour.city}, {tour.country}</p>
                <p>{tour.descripcion}</p>
        """

        days = sorted(list(set([item.get("day", 1) for item in tour.itinerary])))
        for day in days:
            html_content += f'<div class="day">Day {day}</div>'
            for item in tour.itinerary:
                if item.get("day", 1) == day:
                    html_content += f"""
                    <div class="step">
                        <span class="time">{item.get('time', '')}</span>
                        <h3>{item.get('place', '')}</h3>
                        <p>{item.get('desc', '')}</p>
                    </div>
                    """

        html_content += '<div class="audio-section"><h3>Audio Tracks</h3>'
        for audio in audios:
            if audio.titulo in audio_files:
                html_content += f"""
                <div style="margin-bottom: 15px;">
                    <strong>{audio.titulo}</strong>
                    <audio controls>
                        <source src="{audio_files[audio.titulo]}" type="audio/mpeg">
                    </audio>
                </div>
                """
        html_content += "</div></div></body></html>"

        zf.writestr("index.html", html_content)
        zf.writestr(
            "README.txt",
            "Extract this folder and open 'index.html' in your browser to use the guide offline. All audio is stored in the 'audio' folder.",
        )

    memory_file.seek(0)

    existing = DescargaOffline.query.filter_by(
        id_usuario=session["user_id"], id_tour=tour_id
    ).first()
    if not existing:
        descarga = DescargaOffline(id_usuario=session["user_id"], id_tour=tour_id)
        db.session.add(descarga)
        db.session.commit()

    flash("Offline package downloaded! Unzip and open 'index.html'.", "success")
    return send_file(
        memory_file,
        mimetype="application/zip",
        as_attachment=True,
        download_name=f"{tour.titulo}_Offline_Guide.zip",
    )


@web_bp.route("/add-to-cart/<tour_id>")
def add_to_cart(tour_id):
    if "cart" not in session:
        session["cart"] = []

    if tour_id == "subscription":
        item_id = "subscription"
    else:
        try:
            item_id = int(tour_id)
        except ValueError:
            return redirect(url_for("web.home"))

    if item_id not in session["cart"]:
        session["cart"].append(item_id)
        session.modified = True
        flash("Item added to your cart!", "success")
    return redirect(request.referrer or url_for("web.home"))


@web_bp.route("/remove-from-cart/<item_id>")
def remove_from_cart(item_id):
    if "cart" not in session:
        return redirect(url_for("web.checkout"))

    if item_id == "subscription":
        if "subscription" in session["cart"]:
            session["cart"].remove("subscription")
    else:
        try:
            tour_id = int(item_id)
            if tour_id in session["cart"]:
                session["cart"].remove(tour_id)
        except ValueError:
            pass

    session.modified = True
    return redirect(url_for("web.checkout"))


@web_bp.route("/checkout")
def checkout():
    cart_items = session.get("cart", [])
    if not cart_items:
        flash("Your cart is empty.", "error")
        return redirect(url_for("web.home"))

    tour_ids = [item for item in cart_items if isinstance(item, int)]
    has_subscription = "subscription" in cart_items

    tours = Tour.query.filter(Tour.id_tour.in_(tour_ids)).all() if tour_ids else []
    total = sum(t.precio_float for t in tours)

    if has_subscription:
        total += 25.00

    if len(tours) >= 3:
        total = total * 0.8

    return render_template(
        "checkout.html",
        tours=tours,
        has_subscription=has_subscription,
        total=total,
        count=len(tours) + (1 if has_subscription else 0),
    )


@web_bp.route("/process-payment", methods=["POST"])
def process_payment():
    if not session.get("user_id"):
        flash("Please log in to complete your purchase.", "error")
        return redirect(url_for("web.login"))

    cart_items = session.get("cart", [])
    if not cart_items:
        return redirect(url_for("web.home"))

    tour_ids = [item for item in cart_items if isinstance(item, int)]
    has_subscription = "subscription" in cart_items

    tours = Tour.query.filter(Tour.id_tour.in_(tour_ids)).all() if tour_ids else []
    payment_method = request.form.get("payment_method", "MercadoPago")

    for tour in tours:
        pedido = Pedido(
            id_usuario=session["user_id"],
            id_tour=tour.id_tour,
            monto=tour.precio,
            metodo_pago=payment_method,
            estado="paid",
        )
        db.session.add(pedido)

    if has_subscription:
        existing = Suscripcion.query.filter_by(
            id_usuario=session["user_id"], estado="active"
        ).first()
        if not existing or not existing.is_active:
            nueva_sub = Suscripcion(
                id_usuario=session["user_id"],
                fecha_fin=datetime.utcnow() + timedelta(days=30),
                monto=25.00,
            )
            db.session.add(nueva_sub)

    db.session.commit()
    session.pop("cart", None)

    flash("Payment successful! Enjoy your tours.", "success")
    return redirect(url_for("web.dashboard"))


@web_bp.route("/health")
def health():
    return {"status": "ok", "message": "Server is running perfectly!"}, 200
