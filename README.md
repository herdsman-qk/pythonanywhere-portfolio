# My Portfolio

**My Portfolio** is a personal portfolio website built with Django. It provides information about who I am, my skills, and showcases the projects I have worked on. The website is designed to give visitors an overview of my professional journey, along with detailed descriptions of each project, technologies used, and relevant links.

## Features

- **About Me**: A section that introduces who I am, my background, and my professional journey.
- **Projects Showcase**: A collection of my personal and professional projects, including descriptions, technologies used, and links to live projects or code repositories.
- **Contact Form**: A simple form that allows visitors to get in touch with me for potential opportunities or collaborations.
- **Responsive Design**: The website is designed to be responsive and works well across different devices, from desktops to mobile phones.
- **Admin Panel**: Easily manage and update portfolio content through Django's built-in admin panel.

## Installation

### Prerequisites

- **Python 3.x**: Make sure you have Python 3 installed. You can download it from [here](https://www.python.org/downloads/).
- **Django**: You need to have Django installed. You can install it via pip.
- **Database**: By default, the project uses SQLite. However, you can configure it to use other databases such as PostgreSQL or MySQL if needed.

### Getting Started

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/herdsman-qk/HerdsmanPortfolio.git
    cd HerdsmanPortfolio
    ```

2. **Migrate the Database**:
    Django uses migrations to manage database schema changes. Run the following commands to apply migrations:
    ```bash
    python manage.py migrate
    ```

3. **Create a Superuser** (optional, to access the Django admin):
    ```bash
    python manage.py createsuperuser
    ```

4. **Run the Development Server**:
    ```bash
    python manage.py runserver
    ```

   The server will start at `http://127.0.0.1:8000/`. Open this URL in your browser to view the portfolio.

## Usage

1. **Browse Portfolio**: Once the server is running, visit the homepage (`http://127.0.0.1:8000/`) to view the portfolio website.
2. **Admin Panel**: Access the Django admin panel at `http://127.0.0.1:8000/admin/` to manage and update the portfolio content. You will need to log in using the superuser account you created earlier.
3. **Update Content**: You can update sections such as the "About Me", "Projects", and "Contact Information" through the admin interface.
4. **Contact Form**: Visitors can use the contact form to send a message, which will be forwarded to the email address set up in the Django settings.

## Project Structure

The structure of the project is as follows:

- `myportfolio/`: The main project directory containing the settings, URL routing, and WSGI configuration.
    - `settings.py`: Django project settings.
    - `urls.py`: The URL routing configuration.
    - `wsgi.py`: WSGI configuration for deploying the app.
- `portfolio/`: The app containing the main logic for the portfolio website.
    - `models.py`: The database models for the portfolio's sections (e.g., About Me, Projects, etc.).
    - `views.py`: The views that render the HTML templates for each section.
    - `urls.py`: The URL routing for the portfolio app.
- `templates/`: HTML files for rendering the portfolio.
    - `base.html`: The base template for the portfolio website.
    - `main`
      - `index.html`: The main template.
- `static/`: Static files such as CSS, JavaScript, and images.

## Dependencies

This project uses the following libraries and packages:

- **Django**: The web framework used to build the portfolio.
- **Pillow**: Used for image handling (e.g., for project images).

You can find all the dependencies listed in `requirements.txt`.

## Testing

To run the tests:

1. **Unit Tests**: Django allows running unit tests using the following command:
    ```bash
    python manage.py test
    ```

## Contributing

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Create a new pull request.

## Acknowledgements

- **Django**: For providing a robust framework for web development.
- **Bootstrap**: For helping create a responsive and modern design.
- **FontAwesome**: For providing icons used in the portfolio.

## Contact

For any questions or feedback, feel free to contact me at [quinn.k.2500@gmail.com].

---

Thank you for visiting my portfolio! Feel free to explore my projects and connect with me.
