# Django 3 Password Generator

A secure and customizable password generator web application built with Django 3.

## Features

- Generate strong, random passwords
- Choose password length and character sets
- Simple, user-friendly web interface
- Built with Django 3 for security and reliability

## Getting Started

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)
- Django 3.x

### Installation

1. **Clone the repository:**
   ```powershell
   git clone https://github.com/jubaer-bhuiyan/django3-password-generator.git
   cd django3-password-generator
   ```
2. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
3. **Run migrations:**
   ```powershell
   python manage.py migrate
   ```
4. **Start the development server:**
   ```powershell
   python manage.py runserver
   ```
5. **Open your browser:**
   Go to `http://127.0.0.1:8000/`

## Usage

- Select your desired password options (length, character types)
- Click "Generate" to receive a secure password

## Project Structure

```
manage.py
README.md
passwordGenarator/
    __init__.py
    asgi.py
    settings.py
    urls.py
    wsgi.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.