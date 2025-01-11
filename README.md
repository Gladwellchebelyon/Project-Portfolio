# Portfolio Project

A modern portfolio website built with Django, featuring a dynamic skills showcase and project gallery.

## Features

- Dynamic skills management with icons and proficiency levels
- Project showcase with images and details
- Responsive design
- Admin interface for content management
- Contact form

## Setup

1. Clone the repository:
```bash
git clone https://github.com/Gladwellchebelyon/portfolio.git
cd portfolio
```

2. Create and activate a virtual environment:
```bash
python -m venv GK
source GK/bin/activate  # On Windows: GK\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create environment variables:
```bash
cp .env.example .env
# Edit .env with your settings
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/admin to manage content.

## Environment Variables

Copy `.env.example` to `.env` and update the following variables:

- `SECRET_KEY`: Your Django secret key
- `DEBUG`: Set to False in production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `EMAIL_HOST_USER`: Your email for the contact form
- `EMAIL_HOST_PASSWORD`: Your email password

## Project Structure

- `portfolio_app/`: Main application directory
  - `static/`: Static files (CSS, JS, images)
  - `templates/`: HTML templates
  - `models.py`: Database models
  - `views.py`: View functions
  - `admin.py`: Admin interface configuration

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.