🎓 Grade Evaluator Web Application
This is a simple web application built with Flask that allows users to input a numerical grade and receive a corresponding letter grade (A+, A, A-, B+, etc.) or an "Invalid input" message if the grade is outside the 1-100 range. It features a clean, responsive user interface styled with CSS.

✨ Features
Grade Calculation: Converts numerical grades (1-100) into letter grades (A+ to F).

Input Validation: Checks for grades outside the valid range (1-100) and non-numerical inputs.

User-Friendly Interface: Simple form for grade submission.

Responsive Design: Styled with CSS for a visually appealing experience.

🚀 Technologies Used
Backend: Python (Flask)

Frontend: HTML, CSS

📁 Project Structure
The project is organized into a standard Flask application structure:

Grade/
├── grade.py          # Main Flask application logic
├── templates/
│   └── index.html    # HTML template for the web page
└── static/
    └── style.css     # CSS stylesheet for styling

⚙️ Setup and Installation
Follow these steps to get the Grade Evaluator running on your local machine.

Prerequisites
Python 3.x installed on your system. You can download it from python.org.

pip (Python package installer), which usually comes with Python.

Installation Steps
Clone the Repository (if applicable) or create the project structure:
If you've just pushed this to GitHub, you'd typically clone it. If you're setting it up from scratch, ensure you have the Grade folder with grade.py, templates/index.html, and static/style.css as described in the "Project Structure" section.

Navigate to the Project Directory:
Open your terminal or command prompt and change your current directory to the Grade folder:

cd C:\Users\HP\OneDrive\Desktop\PHYTON\Grade

(Adjust the path if your project is located elsewhere).

Install Flask:
It's recommended to use a virtual environment to manage dependencies.

Create a virtual environment (optional but recommended):

python -m venv venv

Activate the virtual environment:

On Windows:

.\venv\Scripts\activate

On macOS/Linux:

source venv/bin/activate

Install Flask:

pip install Flask

▶️ How to Run the Application
Ensure your virtual environment is activated (if you created one).

Run the Flask application from your project's root directory (Grade folder):

python grade.py

Access the application:
Open your web browser and go to:

http://127.0.0.1:5000/

The application will now be running and accessible in your browser.

To stop the server:
Go back to your terminal where the Flask server is running and press Ctrl + C.

📝 Usage
Open the application in your web browser.

Enter a numerical grade between 1 and 100 in the input field.

Click the "Check Grade" button.

The corresponding letter grade or an error message will be displayed below the form.

🤝 Contributing
Feel free to fork this repository, make improvements, and submit pull requests.

📄 License
This project is open source and available under the MIT License.