from flask import Flask, jsonify, request, render_template

# create flask instance
app = Flask(__name__)


# HOME PAGE
@app.route("/")
def home():
    name = "Aakash"
    return render_template("index.html", name=name)


# ABOUT PAGE
@app.route("/about")
def about():
    return "This is a simple Flask web application."


# JSON DATA API
@app.route("/data")
def data():
    user_data = {"name": "John Doe", "age": 30, "city": "New York"}
    return jsonify(user_data)


# FORM USING POST METHOD (DATA NOT SHOWN IN URL)
# =================================================


# STEP 1: SHOW FORM (POST version)
@app.route("/form", methods=["GET"])
def show_form():
    return render_template("form.html")


# STEP 2: HANDLE FORM SUBMISSION (POST)
@app.route("/form", methods=["POST"])
def handle_form():
    name = request.form["username"]
    password = request.form["password"]
    return f"[POST] Hello, {name}. Your password is {password}"


# =================================================
# FORM USING GET METHOD (DATA SHOWN IN URL)
# =================================================


# STEP 3: SHOW GET FORM
@app.route("/form-get", methods=["GET"])
def show_get_form():
    return render_template("form_get.html")


# STEP 4: HANDLE GET REQUEST (DATA COMES FROM URL)
@app.route("/form-get-result", methods=["GET"])
def handle_get_form():
    name = request.args.get("username")
    password = request.args.get("password")

    return f"[GET] Hello, {name}. Your password is {password}"


# another method to handle both GET and POST in a single route
# @app.route("/forms", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         name = request.form["username"]
#         password = request.form["password"]
#         return f"Hello, {name} and your password is {password}!"
#     return render_template("form.html")

# RUN APP
if __name__ == "__main__":
    app.run(debug=True)
