# Glitters & Giggles - Children's Event Management

![Glitters & Giggles](https://img.shields.io/badge/Status-Active-success)
![Django](https://img.shields.io/badge/Django-4.2.25-blue)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple)

> Where Magic And Fun Comes To Life

Glitters & Giggles is a comprehensive children event management platform built with Django. We specialize in creating magical, educational, and inclusive experiences for children across Kampala, Wakiso, and Entebbe.

## ✨ Features

### 🎉 Event Services
- **Birthday Parties** - Magical celebrations with themed decorations and activities
- **Corporate Events** - Professional kids' corners for corporate functions
- **School Activities** - Educational workshops and field days
- **Cultural Events** - Traditional Ugandan celebrations and performances
- **STEM Workshops** - Science, Technology, Engineering, and Math activities
- **Inclusive Play** - Activities designed for children of all abilities

### 📸 Gallery & Blog
- **Photo Gallery** - Showcase of our beautiful events and happy children
- **Blog** - Tips, stories, and insights for parents and educators
- **Newsletter** - Stay updated with our latest events and offers

### 🛠️ Management Features
- **Booking System** - Easy online event booking and management
- **Contact Forms** - Multiple ways for clients to reach us
- **Admin Dashboard** - Complete event and content management
- **API Integration** - RESTful API for mobile apps and integrations

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- Django 4.2+
- PostgreSQL or SQLite (SQLite for development)
- Git

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/glitters-giggles.git
   cd glitters-giggles
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Setup the database**
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   ```

5. **Load initial data**
   ```bash
   python manage.py loaddata accounts/fixtures/users.json
   python manage.py loaddata services/fixtures/services.json
   python manage.py loaddata gallery/fixtures/gallery.json
   python manage.py loaddata blog/fixtures/blog.json
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   Open your browser and go to `http://localhost:8000`

## 📁 Project Structure

```
glitters-giggles/
├── accounts/           # User management and authentication
├── api/               # REST API endpoints
├── blog/              # Blog functionality
├── bookings/          # Event booking system
├── core/              # Main application logic
├── dashboard/         # Admin dashboard
├── gallery/           # Photo gallery
├── newsletter/        # Email newsletter system
├── services/          # Event services management
├── glittersgiggles/   # Django project settings
├── static/            # Static files (CSS, JS, images)
├── templates/         # HTML templates
├── requirements.txt   # Python dependencies
└── manage.py         # Django management script
```

## 🛠️ Technologies Used

- **Backend**: Django 4.2.25, Python 3.8+
- **Frontend**: Bootstrap 5.3, HTML5, CSS3, JavaScript
- **Database**: SQLite (development), PostgreSQL (production)
- **API**: Django REST Framework
- **Images**: Local static files + Unsplash integration
- **Email**: Django Email Backend with SMTP
- **Authentication**: Django Auth + JWT tokens

## 🎯 Key Features

### Event Management
- ✅ Online booking system
- ✅ Service categorization
- ✅ Price range display
- ✅ Event calendar integration
- ✅ Customer management

### Content Management
- ✅ Dynamic service pages
- ✅ Photo gallery with filtering
- ✅ Blog with rich content
- ✅ Newsletter subscription
- ✅ Contact forms

### User Experience
- ✅ Responsive design (mobile-first)
- ✅ Fast loading with optimized images
- ✅ Interactive animations
- ✅ Accessibility features
- ✅ Multi-language support ready

## 📧 Contact Information

**Glitters & Giggles**
- **Phone**: +256 748 123 888 / +256 775 785 911
- **Email**: doreenmatha.nakibugw@gmail.com
- **Locations**: Kampala, Wakiso & Entebbe
- **WhatsApp**: https://wa.me/256748123888
- **TikTok**: https://www.tiktok.com/@glitters.and.gigg

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues and enhancement requests.

### Development Setup
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

### Code Style
- Follow PEP 8 for Python code
- Use Bootstrap conventions for frontend
- Write descriptive commit messages
- Add tests for new features

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Unsplash** for high-quality stock images
- **Bootstrap** for the responsive frontend framework
- **Django** for the robust backend framework
- **Font Awesome** for beautiful icons

## 📞 Support

For technical support or questions about our services:
- Visit our website: [Glitters & Giggles](#)
- Email us: info@glittersgiggles.com
- Call us: +256 748 123 888

---

**Made with ❤️ for children everywhere**

*Glitters & Giggles - Where Magic And Fun Comes To Life*