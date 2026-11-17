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

    # =====================================================================
    # BUENOS AIRES — 5 routes
    # =====================================================================
    buenos_aires_routes = [
        {
            "c": "Argentina",
            "f": "ar",
            "city": "Buenos Aires",
            "desc": "The vibrant capital of Argentina, known for its European-style architecture, tango, passionate culture, and strong local food traditions.",
            "img": "photo-1589909202802-8f4aadce1849",
            "t": "La Boca & San Telmo: History, Language, Food",
            "cat": "history",
            "coords": "-34.6345,-58.3633",
            "descripcion": "Two souls of Buenos Aires: the colorful port district of La Boca and the aristocratic, melancholic San Telmo. We trace the city's story from its founding through immigration, tango, art, and local food. Tour led in English; Russian or Spanish on request.",
            "precio": 60.00,
            "duracion_minutos": 360,
            "distance_km": 6.0,
            "neighborhoods": "La Boca, San Telmo",
            "itinerary": [
                {
                    "day": 1,
                    "time": "09:30",
                    "place": "La Boca – Caminito",
                    "desc": "Meeting point and introduction. The history of the port, Genoese and Italian immigration, conventillos, and the colorful facades of Caminito.",
                },
                {
                    "day": 1,
                    "time": "11:00",
                    "place": "La Bombonera / Boca neighborhood",
                    "desc": "Football culture, street art, and photo stops in the heart of La Boca.",
                },
                {
                    "day": 1,
                    "time": "12:30",
                    "place": "Mercado de San Telmo",
                    "desc": "Walk to San Telmo and explore the market: antiques, local producers, snacks, and everyday porteno life.",
                },
                {
                    "day": 1,
                    "time": "14:00",
                    "place": "Plaza Dorrego",
                    "desc": "Tango history, street performers, and a lunch break in the historic square.",
                },
                {
                    "day": 1,
                    "time": "15:30",
                    "place": "San Telmo backstreets",
                    "desc": "Immigration stories, artists, hidden courtyards, and the bohemian side of San Telmo.",
                },
                {
                    "day": 1,
                    "time": "16:30",
                    "place": "Local food stop: empanadas & mate",
                    "desc": "A local tasting and wrap-up of the route.",
                },
            ],
            "pois": [
                {
                    "n": "Caminito",
                    "lat": -34.6390,
                    "lng": -58.3630,
                    "d": "The most colorful street of La Boca.",
                },
                {
                    "n": "La Bombonera",
                    "lat": -34.6356,
                    "lng": -58.3647,
                    "d": "Boca Juniors stadium and football culture.",
                },
                {
                    "n": "Mercado de San Telmo",
                    "lat": -34.6190,
                    "lng": -58.3730,
                    "d": "Historic market with local food and antiques.",
                },
                {
                    "n": "Plaza Dorrego",
                    "lat": -34.6211,
                    "lng": -58.3732,
                    "d": "The heart of San Telmo and tango street life.",
                },
            ],
            "audio": [
                {
                    "titulo": "Introduction to La Boca",
                    "duracion_segundos": 150,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
                },
                {
                    "titulo": "Immigration and Caminito",
                    "duracion_segundos": 210,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
                },
                {
                    "titulo": "San Telmo and Tango",
                    "duracion_segundos": 180,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
                },
            ],
        },
        {
            "c": "Argentina",
            "f": "ar",
            "city": "Buenos Aires",
            "desc": "Elegant districts, historic cafes, cemeteries, parks, boutiques, and the European-facing side of Buenos Aires.",
            "img": "photo-1589909202802-8f4aadce1849",
            "t": "Palermo & Recoleta: Glamour, Customs & Legends",
            "cat": "culture",
            "coords": "-34.5875,-58.3930",
            "descripcion": "Recoleta, Palermo, and the city center: elegance that ages before your eyes. Continue discovering Buenos Aires—ambitious, wealthy, brilliant, and deeply European—through cemeteries, cafes, boutiques, parks, and legends.",
            "precio": 70.00,
            "duracion_minutos": 420,
            "distance_km": 8.0,
            "neighborhoods": "Recoleta, Palermo, City Center",
            "itinerary": [
                {
                    "day": 1,
                    "time": "10:00",
                    "place": "Recoleta Cemetery",
                    "desc": "Meeting and introduction. Mausoleums, Eva Peron's tomb, and the legends of Argentina's most famous cemetery.",
                },
                {
                    "day": 1,
                    "time": "11:30",
                    "place": "El Ateneo Grand Splendid",
                    "desc": "A beautiful theater converted into a bookstore; Recoleta architecture and cafe culture.",
                },
                {
                    "day": 1,
                    "time": "12:30",
                    "place": "Floralis Generica / Palermo parks",
                    "desc": "Photo stop and a walk through the park area.",
                },
                {
                    "day": 1,
                    "time": "13:30",
                    "place": "Palermo Soho",
                    "desc": "Lunch, boutiques, street art, local design, and the creative side of Palermo.",
                },
                {
                    "day": 1,
                    "time": "15:00",
                    "place": "MALBA / Palermo Chico",
                    "desc": "Art and elegant residential neighborhoods.",
                },
                {
                    "day": 1,
                    "time": "16:00",
                    "place": "Palermo Rose Garden",
                    "desc": "The Rosedal, city views, and a relaxed wrap-up of the route.",
                },
            ],
            "pois": [
                {
                    "n": "Recoleta Cemetery",
                    "lat": -34.5875,
                    "lng": -58.3930,
                    "d": "Historic cemetery with elaborate mausoleums.",
                },
                {
                    "n": "El Ateneo Grand Splendid",
                    "lat": -34.5959,
                    "lng": -58.3940,
                    "d": "Theater-turned-bookstore.",
                },
                {
                    "n": "Floralis Generica",
                    "lat": -34.5820,
                    "lng": -58.3930,
                    "d": "Iconic giant metal flower.",
                },
                {
                    "n": "Palermo Soho",
                    "lat": -34.5880,
                    "lng": -58.4300,
                    "d": "Trendy area with boutiques and street art.",
                },
                {
                    "n": "MALBA",
                    "lat": -34.5770,
                    "lng": -58.4030,
                    "d": "Museum of Latin American Art.",
                },
                {
                    "n": "Rosedal",
                    "lat": -34.5740,
                    "lng": -58.4180,
                    "d": "Rose garden in Palermo.",
                },
            ],
            "audio": [
                {
                    "titulo": "Recoleta and Its Legends",
                    "duracion_segundos": 180,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
                },
                {
                    "titulo": "Palermo and European Buenos Aires",
                    "duracion_segundos": 220,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
                },
                {
                    "titulo": "Art, Parks, and Local Life",
                    "duracion_segundos": 190,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
                },
            ],
        },
        {
            "c": "Argentina",
            "f": "ar",
            "city": "Buenos Aires",
            "desc": "A local food route through markets, cafes, empanadas, asado, mate, and Argentine sweets.",
            "img": "photo-1558030006-450675393462",
            "t": "Tastes of Buenos Aires: Local Food Tour",
            "cat": "food",
            "coords": "-34.6190,-58.3730",
            "descripcion": "Taste Buenos Aires through local spots rather than tourist restaurants: from asado and wine to coffee and empanadas. Breakfast, snack, and lunch are included.",
            "precio": 75.00,
            "duracion_minutos": 360,
            "distance_km": 4.5,
            "neighborhoods": "San Telmo, Palermo, Recoleta",
            "itinerary": [
                {
                    "day": 1,
                    "time": "09:00",
                    "place": "Local cafe – breakfast",
                    "desc": "Meeting point. Cafe con leche, medialunas, and an introduction to Buenos Aires food culture.",
                },
                {
                    "day": 1,
                    "time": "10:00",
                    "place": "San Telmo Market",
                    "desc": "Local producers, cheeses, spices, and market life.",
                },
                {
                    "day": 1,
                    "time": "11:30",
                    "place": "Empanada tasting",
                    "desc": "Different regional empanadas and the stories behind them.",
                },
                {
                    "day": 1,
                    "time": "13:00",
                    "place": "Asado lunch",
                    "desc": "A local grill: cuts of meat, chimichurri, and Malbec.",
                },
                {
                    "day": 1,
                    "time": "15:00",
                    "place": "Mate & alfajores stop",
                    "desc": "The mate ritual and traditional Argentine sweets.",
                },
                {
                    "day": 1,
                    "time": "16:00",
                    "place": "Heladeria / coffee",
                    "desc": "Argentine ice cream and coffee; final wrap-up.",
                },
            ],
            "pois": [
                {
                    "n": "Local cafe in San Telmo",
                    "lat": -34.6200,
                    "lng": -58.3730,
                    "d": "Traditional cafe breakfast.",
                },
                {
                    "n": "Mercado de San Telmo",
                    "lat": -34.6190,
                    "lng": -58.3730,
                    "d": "Local market and producers.",
                },
                {
                    "n": "Empanada spot",
                    "lat": -34.6180,
                    "lng": -58.3740,
                    "d": "Regional empanada tasting.",
                },
                {
                    "n": "Local asado restaurant",
                    "lat": -34.6200,
                    "lng": -58.3750,
                    "d": "Traditional Argentine grill.",
                },
                {
                    "n": "Mate and sweets stop",
                    "lat": -34.6210,
                    "lng": -58.3730,
                    "d": "Mate ritual and alfajores.",
                },
                {
                    "n": "Heladeria",
                    "lat": -34.6220,
                    "lng": -58.3740,
                    "d": "Argentine ice cream.",
                },
            ],
            "audio": [
                {
                    "titulo": "Buenos Aires Food Culture",
                    "duracion_segundos": 160,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
                },
                {
                    "titulo": "Empanadas and Asado",
                    "duracion_segundos": 230,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
                },
                {
                    "titulo": "Mate, Coffee, and Sweets",
                    "duracion_segundos": 170,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
                },
            ],
        },
        {
            "c": "Argentina",
            "f": "ar",
            "city": "Buenos Aires",
            "desc": "A 3-day package combining La Boca, San Telmo, Palermo, Recoleta, local food, and Tigre Delta.",
            "img": "photo-1589909202802-8f4aadce1849",
            "t": "All Buenos Aires + Tigre: 3-Day Package",
            "cat": "culture",
            "coords": "-34.6037,-58.3816",
            "descripcion": "The best choice if you have three free days and want to see the whole city without rushing. We combine three author routes—La Boca & San Telmo, Palermo & Recoleta, and the food tour—and add a Tigre Delta boat ride and a local train for a fuller understanding of Argentina. In Tigre: fruit market, lunch by the water, Sarmiento Museum, and the real rhythm of island life. Comfortable pace, stops at the best viewpoints and trusted local places. Group up to 6.",
            "precio": 165.00,
            "duracion_minutos": 4320,
            "distance_km": 45.0,
            "neighborhoods": "La Boca, San Telmo, Palermo, Recoleta, Tigre",
            "itinerary": [
                {
                    "day": 1,
                    "time": "09:30",
                    "place": "La Boca – Caminito",
                    "desc": "Meeting and introduction. Port history, immigration, conventillos, and colorful Caminito.",
                },
                {
                    "day": 1,
                    "time": "11:00",
                    "place": "La Bombonera / Boca neighborhood",
                    "desc": "Football culture, street art, and photo stops.",
                },
                {
                    "day": 1,
                    "time": "12:30",
                    "place": "Mercado de San Telmo",
                    "desc": "Market, antiques, local producers, and snacks.",
                },
                {
                    "day": 1,
                    "time": "14:00",
                    "place": "Plaza Dorrego",
                    "desc": "Tango history, street performers, and lunch break.",
                },
                {
                    "day": 1,
                    "time": "15:30",
                    "place": "San Telmo backstreets",
                    "desc": "Immigration stories, artists, and hidden courtyards.",
                },
                {
                    "day": 1,
                    "time": "16:30",
                    "place": "Empanadas & mate",
                    "desc": "Local tasting and wrap-up of day one.",
                },
                {
                    "day": 2,
                    "time": "10:00",
                    "place": "Recoleta Cemetery",
                    "desc": "Mausoleums, Eva Peron's tomb, and local legends.",
                },
                {
                    "day": 2,
                    "time": "11:30",
                    "place": "El Ateneo Grand Splendid",
                    "desc": "Theater-turned-bookstore and Recoleta architecture.",
                },
                {
                    "day": 2,
                    "time": "12:30",
                    "place": "Floralis Generica / Palermo parks",
                    "desc": "Photo stop and park walk.",
                },
                {
                    "day": 2,
                    "time": "13:30",
                    "place": "Palermo Soho",
                    "desc": "Lunch, boutiques, street art, and local design.",
                },
                {
                    "day": 2,
                    "time": "15:00",
                    "place": "MALBA / Palermo Chico",
                    "desc": "Art and elegant neighborhoods.",
                },
                {
                    "day": 2,
                    "time": "16:00",
                    "place": "Palermo Rose Garden",
                    "desc": "Rosedal and relaxed city views.",
                },
                {
                    "day": 3,
                    "time": "08:30",
                    "place": "Train to Tigre",
                    "desc": "Local train to Tigre and introduction to the delta region.",
                },
                {
                    "day": 3,
                    "time": "10:00",
                    "place": "Tigre Fruit Market",
                    "desc": "Local fruit market and riverfront atmosphere.",
                },
                {
                    "day": 3,
                    "time": "11:30",
                    "place": "Tigre Delta boat ride",
                    "desc": "Boat ride through the delta and island channels.",
                },
                {
                    "day": 3,
                    "time": "13:00",
                    "place": "Lunch by the water",
                    "desc": "Local lunch with river views.",
                },
                {
                    "day": 3,
                    "time": "15:00",
                    "place": "Sarmiento Museum",
                    "desc": "House-museum and the history of Domingo F. Sarmiento.",
                },
                {
                    "day": 3,
                    "time": "16:30",
                    "place": "Island life & mate",
                    "desc": "The rhythm of islanders, mate, and local stories.",
                },
                {
                    "day": 3,
                    "time": "18:00",
                    "place": "Return to Buenos Aires",
                    "desc": "Return and final wrap-up of the 3-day package.",
                },
            ],
            "pois": [
                {
                    "n": "Caminito",
                    "lat": -34.6390,
                    "lng": -58.3630,
                    "d": "Colorful La Boca street.",
                },
                {
                    "n": "La Bombonera",
                    "lat": -34.6356,
                    "lng": -58.3647,
                    "d": "Boca Juniors stadium.",
                },
                {
                    "n": "Mercado de San Telmo",
                    "lat": -34.6190,
                    "lng": -58.3730,
                    "d": "Historic market.",
                },
                {
                    "n": "Plaza Dorrego",
                    "lat": -34.6211,
                    "lng": -58.3732,
                    "d": "San Telmo square.",
                },
                {
                    "n": "Recoleta Cemetery",
                    "lat": -34.5875,
                    "lng": -58.3930,
                    "d": "Famous cemetery.",
                },
                {
                    "n": "El Ateneo Grand Splendid",
                    "lat": -34.5959,
                    "lng": -58.3940,
                    "d": "Bookstore in a former theater.",
                },
                {
                    "n": "Floralis Generica",
                    "lat": -34.5820,
                    "lng": -58.3930,
                    "d": "Metal flower sculpture.",
                },
                {
                    "n": "Palermo Soho",
                    "lat": -34.5880,
                    "lng": -58.4300,
                    "d": "Trendy Palermo area.",
                },
                {
                    "n": "MALBA",
                    "lat": -34.5770,
                    "lng": -58.4030,
                    "d": "Latin American art museum.",
                },
                {"n": "Rosedal", "lat": -34.5740, "lng": -58.4180, "d": "Rose garden."},
                {
                    "n": "Tigre Fruit Market",
                    "lat": -34.4260,
                    "lng": -58.5790,
                    "d": "Local fruit market in Tigre.",
                },
                {
                    "n": "Tigre Delta",
                    "lat": -34.4220,
                    "lng": -58.5740,
                    "d": "Delta boat ride.",
                },
                {
                    "n": "Sarmiento Museum",
                    "lat": -34.4160,
                    "lng": -58.5780,
                    "d": "Historic house-museum.",
                },
            ],
            "audio": [
                {
                    "titulo": "Day 1: La Boca and San Telmo",
                    "duracion_segundos": 240,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
                },
                {
                    "titulo": "Day 2: Recoleta and Palermo",
                    "duracion_segundos": 260,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
                },
                {
                    "titulo": "Day 3: Tigre and the Delta",
                    "duracion_segundos": 300,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
                },
                {
                    "titulo": "Local Food and Mate",
                    "duracion_segundos": 180,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-4.mp3",
                },
            ],
        },
        {
            "c": "Argentina",
            "f": "ar",
            "city": "Buenos Aires",
            "desc": "The historic core of Buenos Aires: Plaza de Mayo, Casa Rosada, the Cabildo, the Cathedral, the Obelisk, and Teatro Colon.",
            "img": "photo-1589909202802-8f4aadce1849",
            "t": "Buenos Aires City Center & History",
            "cat": "history",
            "coords": "-34.6037,-58.3816",
            "descripcion": "A compact introduction to Buenos Aires' historic core: Plaza de Mayo, Casa Rosada, the Cabildo, the Metropolitan Cathedral, the Obelisk, and Teatro Colon. Ideal for first-time visitors who want the essential history and architecture in one route.",
            "precio": 9.99,
            "duracion_minutos": 240,
            "distance_km": 5.0,
            "neighborhoods": "Monserrat, Plaza de Mayo, City Center",
            "itinerary": [
                {
                    "day": 1,
                    "time": "10:00",
                    "place": "Plaza de Mayo",
                    "desc": "Meeting point and introduction to the historic main square.",
                },
                {
                    "day": 1,
                    "time": "10:30",
                    "place": "Casa Rosada",
                    "desc": "The presidential palace and its political history.",
                },
                {
                    "day": 1,
                    "time": "11:00",
                    "place": "Cabildo",
                    "desc": "Colonial government building and the May Revolution.",
                },
                {
                    "day": 1,
                    "time": "11:30",
                    "place": "Metropolitan Cathedral",
                    "desc": "Buenos Aires' main Catholic church and its history.",
                },
                {
                    "day": 1,
                    "time": "12:30",
                    "place": "Obelisco",
                    "desc": "The city's iconic landmark and Avenida 9 de Julio.",
                },
                {
                    "day": 1,
                    "time": "13:00",
                    "place": "Teatro Colon",
                    "desc": "Exterior visit and the story of one of the world's great opera houses.",
                },
                {
                    "day": 1,
                    "time": "14:00",
                    "place": "Cafe / wrap-up",
                    "desc": "Optional cafe stop and final recommendations.",
                },
            ],
            "pois": [
                {
                    "n": "Plaza de Mayo",
                    "lat": -34.6083,
                    "lng": -58.3712,
                    "d": "The historic main square.",
                },
                {
                    "n": "Casa Rosada",
                    "lat": -34.6083,
                    "lng": -58.3702,
                    "d": "The presidential palace.",
                },
                {
                    "n": "Cabildo",
                    "lat": -34.6087,
                    "lng": -58.3735,
                    "d": "Colonial government building.",
                },
                {
                    "n": "Metropolitan Cathedral",
                    "lat": -34.6074,
                    "lng": -58.3733,
                    "d": "Main Catholic cathedral.",
                },
                {
                    "n": "Obelisco",
                    "lat": -34.6037,
                    "lng": -58.3816,
                    "d": "Iconic city landmark.",
                },
                {
                    "n": "Teatro Colon",
                    "lat": -34.6011,
                    "lng": -58.3830,
                    "d": "Famous opera house.",
                },
            ],
            "audio": [
                {
                    "titulo": "Introduction to Buenos Aires History",
                    "duracion_segundos": 140,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
                },
                {
                    "titulo": "Plaza de Mayo and Casa Rosada",
                    "duracion_segundos": 200,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
                },
                {
                    "titulo": "Obelisco and Teatro Colon",
                    "duracion_segundos": 180,
                    "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-3.mp3",
                },
            ],
        },
    ]

    # =====================================================================
    # OTHER CITIES
    # =====================================================================
    other_routes = [
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
                },
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
                },
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
                },
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
                },
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
                },
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
                },
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
                },
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
                },
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
                },
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
                },
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
                },
            ],
        },
    ]

    data = buenos_aires_routes + other_routes

    # =====================================================================
    # SEED LOOP
    # =====================================================================
    for d in data:
        portada = f"https://images.unsplash.com/{d['img']}?w=800"

        t = Tour(
            titulo=d["t"],
            descripcion=d.get(
                "descripcion",
                "Experience the best of this beautiful destination with an immersive audio tour.",
            ),
            precio=d.get("precio", 9.99),
            duracion_minutos=d.get("duracion_minutos", 90),
            categoria=d["cat"],
            portada_url=portada,
            country=d["c"],
            city=d["city"],
            city_description=d["desc"],
            flag_url=f"https://flagcdn.com/w320/{d['f']}.png",
            distance_km=d.get("distance_km", 5.5),
            neighborhoods=d.get("neighborhoods", f"{d['city']} Center, Old Town"),
            map_coords=d["coords"],
            itinerary=d.get("itinerary")
            or [
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
            banners=d.get("banners", [portada]),
        )
        db.session.add(t)
        db.session.flush()

        audio_tracks = d.get("audio") or [
            {
                "titulo": "Introduction",
                "duracion_segundos": 120,
                "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3",
            },
            {
                "titulo": "Main History",
                "duracion_segundos": 180,
                "archivo_url": "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-2.mp3",
            },
        ]

        for idx, a in enumerate(audio_tracks, start=1):
            db.session.add(
                AudioTrack(
                    id_tour=t.id_tour,
                    orden=idx,
                    titulo=a["titulo"],
                    duracion_segundos=a["duracion_segundos"],
                    archivo_url=a["archivo_url"],
                )
            )

        for poi in d.get("pois", []):
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

    # =====================================================================
    # BLOG POSTS
    # =====================================================================
    post1 = BlogPost(
        title="Top 10 Hidden Gems in Buenos Aires",
        content="""
        Buenos Aires is a city that rewards those who wander off the beaten path. While the Obelisco and Casa Rosada are must-sees, the true soul of the city lies in its hidden corners.

        Start with the 'Libreria El Ateneo Grand Splendid' in Recoleta, an opulent theater converted into a breathtaking bookstore. Then, head to the 'Barrio de Palermo' to find hidden 'Puertas Cerradas' (closed-door restaurants) where local chefs serve gourmet meals in intimate settings.

        Don't miss the 'Jardin Japones', a peaceful oasis amidst the concrete jungle. For tango lovers, avoid the tourist traps in San Telmo and instead visit 'La Catedral Club', an underground milonga that feels like a secret society.

        Finally, explore the street art in the hidden alleys of Barracas. The city reveals its magic when you get lost in its history.
        """,
        image_url="https://images.unsplash.com/photo-1589909202802-8f4aadce1849?w=600",
        date=datetime(2026, 11, 10),
    )

    post2 = BlogPost(
        title="Guide to Rio's Best Beaches",
        content="""
        Rio de Janeiro is synonymous with sun, sand, and samba. With over 70 beaches, choosing the right one can be overwhelming.

        Copacabana is the most famous, with its iconic black and white wave mosaic. It's vibrant but crowded. For a more upscale and safer experience, head to Ipanema or Leblon, where the locals hang out. The 'Posto 9' in Ipanema is legendary for its bohemian crowd.

        If you want to escape the city noise, try 'Prainha', a hidden gem located further south, surrounded by lush mountains. It's a favorite among surfers.

        Safety tip: Always bring only what you need. Leave your phone and expensive jewelry at the hotel. Instead, bring some cash for a refreshing 'Agua de Coco' (coconut water) from the local vendors. Embrace the 'Carioca' spirit and enjoy the sunset at Arpoador beach!
        """,
        image_url="https://images.unsplash.com/photo-1483729558449-99ef09a8c325?w=600",
        date=datetime(2026, 11, 12),
    )

    post3 = BlogPost(
        title="The Ultimate Guide to Argentine Asado",
        content="""
        An 'Asado' is not just a barbecue; it is a sacred ritual, a social event, and the backbone of Argentine cuisine.

        The secret lies in the fire. A true 'Asador' (grill master) uses wood or charcoal to create hot embers, never exposing the meat directly to the flame. The cuts you must try include 'Asado de Tira' (short ribs), 'Vacio' (flank steak), and 'Chorizo' (sausage).

        Before the meat, you'll be served 'Provoleta' (grilled provolone cheese) and 'Chimichurri' (a vibrant sauce made of parsley, garlic, vinegar, and oil).

        The golden rule of the Asado is patience. It takes hours to prepare, and it is meant to be enjoyed slowly with good wine (Malbec is the perfect pairing) and great conversation. Never rush an Asado; it is the ultimate expression of Argentine hospitality.
        """,
        image_url="https://images.unsplash.com/photo-1558030006-450675393462?w=600",
        date=datetime(2026, 11, 14),
    )

    db.session.add_all([post1, post2, post3])

    db.session.commit()
    print("✅ DB ready. User: test@test.com / 12345")
