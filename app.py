from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        pattern = request.form.get("pattern")
        string = request.form.get("string")
        matched = re.findall(pattern, string)
        return render_template("results.html", matched=matched)
    return render_template("index.html")

@app.route("/validator",methods = ["GET","POST"])
def validate():
    if request.method == "POST":
        mail = request.form.get("mail")
        if re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", mail):
            result = "Valid email address : " + mail
        else:
            result = "Invalid email address"

        return render_template("validation.html", result=result)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=5000)
