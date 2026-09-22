# LatamXP — Interactive Audio Tours Platform

LatamXP is a web platform designed for discovering Latin America through immersive audio tours. The system allows tourists to browse countries and cities, purchase audio tours, and access interactive maps and itineraries at their own pace.

## 🚀 Technologies Used
- **Backend:** Python 3, Flask
- **Database:** PostgreSQL, SQLAlchemy (ORM)
- **Database Migrations:** Flask-Migrate
- **Frontend:** HTML5, CSS3, Jinja2 Template Engine
- **Maps Integration:** Leaflet.js (OpenStreetMap)
- **Authentication:** Werkzeug Security (Password Hashing), Flask Sessions

## 🏗️ Architecture (MVC)
The project strictly follows the **Model-View-Controller** architecture:
- **Models:** Located in the `models/` folder (e.g., `usuario.py`, `tour.py`, `pedido.py`). Handles database structure and business logic.
- **Views:** Located in the `templates/` folder. Jinja2 HTML templates that render the user interface.
- **Controllers:** Located in `app.py` (routes) and `api/routes.py` (REST API endpoints). Handles user requests and communicates with models and views.

## 🔌 REST API
The system includes a functional API for external integrations:
- `GET /api/v1/tours` — Returns a JSON list of all active tours.
- `GET /api/v1/tours/<id>` — Returns detailed JSON data for a specific tour.
- `POST /api/v1/auth/login` — Accepts JSON credentials and returns an authentication token.

## ⚙️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/latamxp.git
   cd latamxp