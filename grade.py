from flask import Flask, render_template, request
app=Flask(__name__)


def grade(grd):
    if grd > 100 or grd < 1:
        return "Invalid input ⚠️ Grade must be between 1 and 100"

    if grd >= 90:
        message = "A+"
    elif grd >= 85:
        message = "A"
    elif grd >= 80:
        message = "A-"
    elif grd >= 75:
        message = "B+"
    elif grd >= 70:
        message = "B"
    elif grd >= 65:
        message = "B-"
    elif grd >= 60:
        message = "C+"
    elif grd >= 55:
        message = "C"
    elif grd >= 50:
        message = "C+"
    elif grd >= 40:
        message = "D"
    else:
        message = "F⚡"
    
    return message

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        print("POST request received")
        try:
            user_grade = int(request.form["grade"])
            print(f"Received grade: {user_grade}")
            result = grade(user_grade)
        except (ValueError, KeyError):
            result = "❌ Please enter a valid number!"
    return render_template("index.html", result=result)

if __name__=="__main__":
    app.run(debug=True)        
