from run import app
from app.extensions import db
from models import Tour, Usuario, BlogPost, PuntoInteres, Valoracion, AudioTrack
from werkzeug.security import generate_password_hash
from datetime import datetime

with app.app_context():
    db.drop_all()
    db.create_all()

    test_user = Usuario(
        nombre="Denis Miroshnichenko",
        email="test@test.com",
        password_hash=generate_password_hash("12345"),
    )
    db.session.add(test_user)
    db.session.flush()

    data = [
        {
            "c": "Argentina",
            "f": "ar",
            "city": "Buenos Aires",
            "desc": "The vibrant capital of Argentina, known for its European-style architecture, tango, and passionate culture.",
            "img": "photo-1589909202802-8f4aadce1849",
            "t": "City Center & History",
            "cat": "history",
            "coords": "-34.6037,-58.3816",
            "pois": [
                {
                    "n": "Plaza de Mayo",
                    "lat": -34.6082,
                    "lng": -58.3712,
                    "d": "The historic main square.",
                },
                {
                    "n": "Casa Rosada",
                    "lat": -34.6083,
                    "lng": -58.3702,
                    "d": "The presidential palace.",
                },
            ],
        },
        {
            "c": "Brazil",
            "f": "br",
            "city": "Rio de Janeiro",
            "desc": "Famous for its Copacabana beaches, the giant Christ the Redeemer statue, and vibrant Carnival.",
            "img": "photo-1483729558449-99ef09a8c325",
            "t": "Rio Highlights & Beaches",
            "cat": "nature",
            "coords": "-22.9519,-43.2105",
            "pois": [
                {
                    "n": "Christ the Redeemer",
                    "lat": -22.9519,
                    "lng": -43.2105,
                    "d": "Iconic statue on Corcovado.",
                },
                {
                    "n": "Copacabana",
                    "lat": -22.9711,
                    "lng": -43.1822,
                    "d": "Famous beach.",
                },
            ],
        },
        {
            "c": "Mexico",
            "f": "mx",
            "city": "Mexico City",
            "desc": "A high-altitude metropolis with a rich Aztec history, colonial architecture, and incredible food.",
            "img": "photo-1518659526054-190340b32735",
            "t": "Aztec History & Zocalo",
            "cat": "history",
            "coords": "19.4326,-99.1332",
            "pois": [
                {"n": "Zocalo", "lat": 19.4326, "lng": -99.1332, "d": "Main square."},
                {
                    "n": "Templo Mayor",
                    "lat": 19.4352,
                    "lng": -99.1315,
                    "d": "Ancient Aztec temple ruins.",
                },
            ],
        },
        {
            "c": "Colombia",
            "f": "co",
            "city": "Bogota",
            "desc": "Colombia's sprawling high-altitude capital, known for its vibrant street art and gold museums.",
            "img": "photo-1568843582128-850f15f5b86a",
            "t": "Street Art & Gold",
            "cat": "culture",
            "coords": "4.7110,-74.0721",
            "pois": [
                {
                    "n": "Gold Museum",
                    "lat": 4.6016,
                    "lng": -74.0721,
                    "d": "Huge collection of gold artifacts.",
                },
                {
                    "n": "La Candelaria",
                    "lat": 4.5964,
                    "lng": -74.0731,
                    "d": "Historic neighborhood.",
                },
            ],
        },
        {
            "c": "Peru",
            "f": "pe",
            "city": "Lima",
            "desc": "Peru's coastal capital, renowned for its top-tier culinary scene and colonial center.",
            "img": "photo-1531968455001-5c5272a41129",
            "t": "Culinary Experience",
            "cat": "food",
            "coords": "-12.0464,-77.0428",
            "pois": [
                {
                    "n": "Plaza Mayor",
                    "lat": -12.0464,
                    "lng": -77.0428,
                    "d": "Historic center square.",
                }
            ],
        },
        {
            "c": "Chile",
            "f": "cl",
            "city": "Santiago",
            "desc": "Chile's capital, nestled in a valley surrounded by the snow-capped Andes mountains.",
            "img": "photo-1534351590666-13e3e96c5017",
            "t": "Andes & City Views",
            "cat": "nature",
            "coords": "-33.4489,-70.6693",
            "pois": [
                {
                    "n": "San Cristobal Hill",
                    "lat": -33.4253,
                    "lng": -70.6342,
                    "d": "Best views of the city.",
                }
            ],
        },
        {
            "c": "Ecuador",
            "f": "ec",
            "city": "Quito",
            "desc": "Standing at 2,850m, it's the highest official capital city in the world.",
            "img": "photo-1591824438708-ce405f36ba3d",
            "t": "Colonial Quito",
            "cat": "history",
            "coords": "-0.1807,-78.4678",
            "pois": [
                {
                    "n": "Basilica del Voto Nacional",
                    "lat": -0.2147,
                    "lng": -78.5072,
                    "d": "Gothic cathedral.",
                }
            ],
        },
        {
            "c": "Bolivia",
            "f": "bo",
            "city": "La Paz",
            "desc": "The highest capital in the world, famous for its Witches' Market and cable car system.",
            "img": "photo-1594824476967-48c8b964273f",
            "t": "La Paz & Moon Valley",
            "cat": "nature",
            "coords": "-16.4897,-68.1193",
            "pois": [
                {
                    "n": "Moon Valley",
                    "lat": -16.5666,
                    "lng": -68.0833,
                    "d": "Surreal rock formations.",
                }
            ],
        },
        {
            "c": "Uruguay",
            "f": "uy",
            "city": "Montevideo",
            "desc": "A relaxed, elegant capital with a beautiful promenade and a rich literary history.",
            "img": "photo-1568824678382-673ae3a9525a",
            "t": "Old Town & Rambla",
            "cat": "culture",
            "coords": "-34.9011,-56.1645",
            "pois": [
                {
                    "n": "Plaza Independencia",
                    "lat": -34.9058,
                    "lng": -56.1991,
                    "d": "Main square.",
                }
            ],
        },
        {
            "c": "Paraguay",
            "f": "py",
            "city": "Asuncion",
            "desc": "One of South America's oldest cities, known for its mix of colonial and modern architecture.",
            "img": "photo-1612294037637-ec328d0e075e",
            "t": "Asuncion History",
            "cat": "history",
            "coords": "-25.2637,-57.5759",
            "pois": [
                {
                    "n": "Palacio de Lopez",
                    "lat": -25.2772,
                    "lng": -57.6372,
                    "d": "Government palace.",
                }
            ],
        },
        {
            "c": "Venezuela",
            "f": "ve",
            "city": "Caracas",
            "desc": "Nestled in a valley, surrounded by the Avila mountain, offering stunning views.",
            "img": "photo-1589554282354-9dcf1c199195",
            "t": "Avila Mountain Tour",
            "cat": "nature",
            "coords": "10.4806,-66.9036",
            "pois": [
                {
                    "n": "El Avila National Park",
                    "lat": 10.5453,
                    "lng": -66.8736,
                    "d": "Mountain park.",
                }
            ],
        },
        {
            "c": "Costa Rica",
            "f": "cr",
            "city": "San Jose",
            "desc": "The bustling capital, a great base for exploring the country's famous rainforests.",
            "img": "photo-1596386461350-326ccb383e9f",
            "t": "City & Coffee Tour",
            "cat": "food",
            "coords": "9.9281,-84.0907",
            "pois": [
                {
                    "n": "National Theatre",
                    "lat": 9.9333,
                    "lng": -84.0764,
                    "d": "Historic theatre.",
                }
            ],
        },
        {
            "c": "Panama",
            "f": "pa",
            "city": "Panama City",
            "desc": "A modern skyline juxtaposed with the historic Casco Viejo district.",
            "img": "photo-1582827441963-53690b1dd1c9",
            "t": "Panama Canal & Old Town",
            "cat": "history",
            "coords": "8.9824,-79.5199",
            "pois": [
                {
                    "n": "Panama Canal",
                    "lat": 9.0800,
                    "lng": -79.6800,
                    "d": "Engineering marvel.",
                }
            ],
        },
        {
            "c": "Cuba",
            "f": "cu",
            "city": "Havana",
            "desc": "Famous for its stunning colonial architecture, classic cars, and vibrant music.",
            "img": "photo-1500759285222-a95626b934cb",
            "t": "Classic Havana",
            "cat": "culture",
            "coords": "23.1136,-82.3666",
            "pois": [
                {
                    "n": "Old Havana",
                    "lat": 23.1367,
                    "lng": -82.3589,
                    "d": "Colonial center.",
                }
            ],
        },
        {
            "c": "Guatemala",
            "f": "gt",
            "city": "Guatemala City",
            "desc": "The largest city in Central America, blending modern life with ancient Mayan roots.",
            "img": "photo-1518638150340-f706e86654de",
            "t": "Mayan Heritage",
            "cat": "history",
            "coords": "14.6349,-90.5069",
            "pois": [
                {
                    "n": "National Palace",
                    "lat": 14.6419,
                    "lng": -90.5128,
                    "d": "Historic building.",
                }
            ],
        },
    ]

    for d in data:
        t = Tour(
            titulo=d["t"],
            descripcion="Experience the best of this beautiful destination with an immersive audio tour.",
            precio=9.99,
            duracion_minutos=90,
            categoria=d["cat"],
            portada_url=f"https://images.unsplash.com/{d['img']}?w=800",
            country=d["c"],
            city=d["city"],
            city_description=d["desc"],
            flag_url=f"https://flagcdn.com/w320/{d['f']}.png",
            distance_km=5.5,
            neighborhoods=f"{d['city']} Center, Old Town",
            map_coords=d["coords"],
            itinerary=[
                {
                    "day": 1,
                    "time": "10:00",
                    "place": d["pois"][0]["n"],
                    "desc": "Meeting point and introduction.",
                },
                {
                    "day": 1,
                    "time": "12:00",
                    "place": (
                        d["pois"][1]["n"] if len(d["pois"]) > 1 else d["pois"][0]["n"]
                    ),
                    "desc": "Exploring the main sights.",
                },
                {
                    "day": 2,
                    "time": "09:00",
                    "place": d["pois"][0]["n"],
                    "desc": "Second day activities.",
                },
            ],
            banners=[f"https://images.unsplash.com/{d['img']}?w=800"],
        )
        db.session.add(t)
        db.session.flush()
        a1 = AudioTrack(
            id_tour=t.id_tour,
            orden=1,
            titulo="Introduction",
            duracion_segundos=120,
            archivo_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
        )
        a2 = AudioTrack(
            id_tour=t.id_tour,
            orden=2,
            titulo="Main History",
            duracion_segundos=180,
            archivo_url="https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
        )
        db.session.add_all([a1, a2])

        for poi in d["pois"]:
            p = PuntoInteres(
                id_tour=t.id_tour,
                lat=poi["lat"],
                lng=poi["lng"],
                nombre=poi["n"],
                descripcion=poi["d"],
            )
            db.session.add(p)

        v = Valoracion(
            id_usuario=test_user.id_usuario,
            id_tour=t.id_tour,
            puntuacion=5,
            comentario="Amazing experience! Highly recommend.",
        )
        db.session.add(v)

    post1 = BlogPost(
        title="Top 10 Hidden Gems in Buenos Aires",
        content="Secret spots you must visit in the vibrant capital of Argentina.",
        image_url="https://images.unsplash.com/photo-1589909202802-8f4aadce1849?w=600",
        date=datetime.now(),
    )
    post2 = BlogPost(
        title="Guide to Rio's Best Beaches",
        content="From Copacabana to Ipanema: where to go and what to avoid.",
        image_url="https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=600",
        date=datetime.now(),
    )
    db.session.add_all([post1, post2])

    db.session.commit()
    print("✅ DB ready. User: test@test.com / 12345")
