# 🎓 Grade Evaluator Web Application

A simple web application built with Flask that allows users to input a numerical grade and receive a corresponding letter grade (A+, A-, B+, etc.) or an "Invalid input" message if the grade is outside the 1-100 range. The app features a clean, responsive user interface styled with CSS.

---

## 🌐 Live Demo

**https://grade-evaluator.onrender.com 🚀**


---
## ✨ Features

* **Grade Calculation:** Converts numerical grades (1-100) into letter grades (A+ to F).
* **Input Validation:** Checks for grades outside the valid range (1-100) and non-numerical inputs.
* **User-Friendly Interface:** Simple form for grade submission.
* **Responsive Design:** Styled with CSS for a visually appealing experience.

## 🚀 Technologies Used

* **Backend:** Python (Flask)
* **Frontend:** HTML, CSS

## 📁 Project Structure

The project follows a standard Flask application layout:

```

Grade/
├── grade.py           \# Main Flask application logic
├── README.md          \# This documentation file
├── templates/
│   └── index.html     \# HTML template for the web page
└── static/
└── style.css      \# CSS stylesheet for styling

````

## ⚙️ Setup and Installation

Follow these steps to get the Grade Evaluator running on your local machine.

### Prerequisites

* **Python 3.x** installed. Download from [python.org](https://www.python.org/downloads/).
* **pip** package installer (usually included with Python).

### Installation Steps

1.  **Clone the repository (if applicable) or create the project structure** with the files as shown above.
2.  **Navigate to the project directory:**

    ```bash
    cd C:\Users\HP\OneDrive\Desktop\PHYTON\Grade
    ```
    (Adjust the path to your project location.)

3.  **(Optional but recommended) Create and activate a virtual environment:**
    * **Create virtual environment:**

        ```bash
        python -m venv venv
        ```
    * **Activate virtual environment:**
        * On Windows:

            ```bash
            .\venv\Scripts\activate
            ```
        * On macOS/Linux:

            ```bash
            source venv/bin/activate
            ```

## 📋 Requirements

Alternatively, you can create a `requirements.txt` file in your project root with the following content:

```text
Flask
````

Then install dependencies using:

```bash
pip install -r requirements.txt
```

## ▶️ How to Run the Application

1.  Ensure your virtual environment is activated (if you created one).

2.  Run the Flask application from the root directory (`Grade` folder):

    ```bash
    python grade.py
    ```

3.  Open your browser and go to:
    `http://127.0.0.1:5000/`

4.  To stop the server, press `Ctrl + C` in your terminal.

## 📝 Usage

1.  Open the application in your web browser.
2.  Enter a numerical grade between 1 and 100 in the input field.
3.  Click the "Check Grade" button.
4.  The corresponding letter grade or an error message will be displayed below the form.

## ❓ Troubleshooting

  * **"Flask app not found" or "ModuleNotFoundError: No module named 'flask'":**

      * Ensure Flask is installed by running:
        ```bash
        pip install Flask
        ```
      * If you are using a virtual environment, make sure it is activated before running `python grade.py`.

  * **"UnicodeEncodeError: 'charmap' codec can't encode..." when emojis appear:**

      * This is a common Windows console issue. To fix it, set the environment variable `PYTHONIOENCODING` to `utf-8`.
      * Search online for "set PYTHONIOENCODING Windows" for detailed instructions.

  * **"index.html not found" or "template not found":**

      * Verify your project structure. The `index.html` file must be inside a folder named `templates` which is located in the same directory as `grade.py`.

  * **Application doesn't load in browser (e.g., "This site can't be reached"):**

      * Ensure the Flask server is running in your terminal (`python grade.py` should be active and showing `Running on http://127.0.0.1:5000/`).
      * Check your firewall settings if you suspect port 5000 is blocked.

-----

## 📬 Contact

If you have any questions, issues, or suggestions, feel free to reach out. I'd love to hear from you\!

  * **GitHub Issues:** [Open an Issue](https://github.com/urjiiko1/GradeEvaluator/issues) 💬
  * **LinkedIn Profile:** [`Gemachis Tesfaye`](https://www.linkedin.com/in/gemachis-tesfaye-137196318) 👤
  * **Email:** `gemachistesfaye36@gmail.com` ✉️
  * **Telegram:** [`@urjiiko1`](https://t.me/urjiiko1) 📱

## 🤝 Contributing

Feel free to fork this repository, make improvements and submit pull requests. Your contributions are welcome\!

## 📅 Date of Completion

This project was completed on: August 1, 2025 🗓️

