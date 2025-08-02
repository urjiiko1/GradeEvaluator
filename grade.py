from flask import Flask, render_template, request
app=Flask(__name__)


def grade(grd):
    if grd > 100 or grd < 1:
        return "Invalid input ⚠️ Grade must be between 1 and 100"

    if grd >= 90:
        return "A+ (Excellent 🌟)"
    elif grd >= 85:
        return "A (Very Good ✅)"
    elif grd >= 80:
        return "A- (Good ✅)"
    elif grd >= 75:
        return "B+ (Above Average 👍)"
    elif grd >= 70:
        return "B (Average 🙂)"
    elif grd >= 65:
        return "B- (Satisfactory 🙂)"
    elif grd >= 60:
        return "C+ (Pass 👌)"
    elif grd >= 55:
        return "C (Pass 👌)"
    elif grd >= 50:
        return "C- (Just Passed ⚠️)"
    elif grd >= 40:
        return "D (Needs Improvement ⚠️)"
    else:
        return "F (Failed ❌)"

        message = "F⚡"
    

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        print("POST request received")
        try:
            user_grade = float(request.form["grade"])
            print(f"Received grade: {user_grade}")
            result = grade(user_grade)
        except (ValueError, KeyError):
            result = "❌ Please enter a valid number!"
    return render_template("index.html", result=result)

if __name__=="__main__":
    app.run(debug=True)        
