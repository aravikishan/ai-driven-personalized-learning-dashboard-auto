# AI-Driven Personalized Learning Dashboard

## Overview
The AI-Driven Personalized Learning Dashboard is an innovative platform designed to enhance the educational experience through personalized learning paths. By leveraging user data and preferences, this application provides tailored course recommendations and tracks individual progress. It is ideal for educational institutions, online course providers, and individual learners seeking a customized learning journey. The dashboard integrates seamlessly with existing educational content and offers a user-friendly interface for both students and educators.

## Features
- **User Management**: Create and manage user profiles with personalized preferences.
- **Course Catalog**: Browse and manage a comprehensive list of available courses.
- **Progress Tracking**: Monitor individual course completion rates and last accessed times.
- **Personalized Recommendations**: Receive tailored course suggestions based on user preferences and progress.
- **Interactive Dashboard**: Access a central hub for managing learning activities and viewing analytics.
- **Responsive Design**: Enjoy a seamless experience across devices with a mobile-friendly interface.
- **Settings Management**: Customize application and account settings for a personalized experience.

## Tech Stack
| Component      | Technology   |
|----------------|--------------|
| Backend        | FastAPI      |
| Frontend       | HTML, CSS, JS|
| Database       | SQLite       |
| Templates      | Jinja2       |
| Server         | Uvicorn      |

## Architecture
The project is structured to separate concerns between the frontend and backend. The FastAPI backend serves API endpoints and renders HTML templates using Jinja2. Static files such as CSS and JavaScript are served to enhance the user interface. The SQLite database stores user, course, and progress data.

```plaintext
+------------------+
| FastAPI Backend  |
+------------------+
|  - API Endpoints |
|  - Database      |
+------------------+
        |
        v
+------------------+
| Frontend         |
+------------------+
|  - HTML Templates|
|  - Static Files  |
+------------------+
```

## Getting Started

### Prerequisites
- Python 3.11+
- pip (Python package installer)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-driven-personalized-learning-dashboard.git
   cd ai-driven-personalized-learning-dashboard
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up the database:
   - The database is automatically set up when you first run the application.

### Running the Application
1. Start the FastAPI server:
   ```bash
   uvicorn app:app --reload
   ```
2. Open your web browser and visit `http://localhost:8000` to access the dashboard.

## API Endpoints
| Method | Path                              | Description                                  |
|--------|-----------------------------------|----------------------------------------------|
| GET    | /api/users/{user_id}/recommendations | Get personalized course recommendations for a user. |
| GET    | /api/courses                      | Retrieve a list of all available courses.    |
| POST   | /api/users                        | Create a new user profile.                   |
| GET    | /api/users/{user_id}/progress     | Get progress details for a specific user.    |

## Project Structure
```
.
├── app.py                  # Main application file with API and HTML endpoints
├── Dockerfile              # Docker configuration file
├── requirements.txt        # List of Python dependencies
├── start.sh                # Script to start the application in a container
├── static/                 # Directory for static files
│   ├── css/
│   │   └── style.css      # Main stylesheet
│   └── js/
│       └── main.js        # Main JavaScript file
└── templates/              # Directory for HTML templates
    ├── analytics.html     # Analytics page template
    ├── courses.html       # Courses page template
    ├── dashboard.html     # Dashboard page template
    ├── profile.html       # Profile page template
    └── settings.html      # Settings page template
```

## Screenshots
*Screenshots of the application interface will be added here.*

## Docker Deployment
1. Build the Docker image:
   ```bash
   docker build -t ai-learning-dashboard .
   ```
2. Run the Docker container:
   ```bash
   docker run -p 8000:8000 ai-learning-dashboard
   ```

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes. Ensure that your code follows the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License.

---
Built with Python and FastAPI.