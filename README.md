## 🧠 Class 1: API Basics + Real-World Context (Foundation) 
 
### 1. What is an API?

- **API = Application Programming Interface**
- A bridge that lets **two software systems talk to each other**
- Think of it like:
  - 🍽️ Restaurant menu → you order → kitchen responds
  - You don’t know _how_ food is cooked, just the result

### 2. Real-World API Examples

- **Google Maps API** → location, routes
- **Weather API** → temperature, forecast
- **Payment APIs (GPay, PhonePe, Stripe)** → transactions
- **Social Media APIs** → login, posts, analytics

### 3. Basic Communication Flow

```
Frontend (React / HTML)
        ↓ API Request
Backend (Flask / Node / Java)
        ↓ Query
Database (MySQL / MongoDB)
        ↑ Response
Backend
        ↑ JSON Response
Frontend
```

### 4. API-Driven Architecture (GPay Example)

- Mobile App (Frontend)
- Backend Services:
  - User Service
  - Payment Service
  - Notification Service

- APIs handle:
  - Authentication
  - Transaction processing
  - Bank communication

- **Microservices + REST APIs**

✅ Outcome:
Students understand _why APIs exist_ and _where they’re used_.

---

## 🧩 Class 2: Introduction to APIs & REST APIs

### 1. Introduction to APIs

- APIs expose **functions/data securely**
- Decouple frontend and backend

### 2. Types of APIs

| Type              | Example               |
| ----------------- | --------------------- |
| Open / Public API | Weather API           |
| Private API       | Internal company APIs |
| Partner API       | Payment gateways      |

### 3. Web API Concept

- Runs over **HTTP**
- Uses **URLs + HTTP methods**
- Returns **JSON / XML**

### 4. API Protocols

| Protocol | Description              |
| -------- | ------------------------ |
| SOAP     | XML-based, heavy, secure |
| REST     | Lightweight, HTTP-based  |
| GraphQL  | Client chooses data      |

👉 **REST is most widely used**

---

## 🌐 REST API (Core Concept)

### Principles of REST

1. Client–Server separation
2. Stateless requests
3. Resource-based URLs
4. Uses HTTP methods
5. Data usually in JSON

### HTTP Methods

| Method | Purpose            |
| ------ | ------------------ |
| GET    | Fetch data         |
| POST   | Create data        |
| PUT    | Update entire data |
| PATCH  | Partial update     |
| DELETE | Remove data        |

Example:

```
GET /users
POST /users
GET /users/1
DELETE /users/1
```

✅ Outcome:
Students can **read and understand APIs** confidently.

---

## 🧪 Class 3: Introduction to Flask (Backend Begins)

### What is Flask?

- Lightweight Python web framework
- Used for:
  - APIs
  - Microservices
  - Backend servers

---

### Basic Flask App (Improved Explanation)

```python
from flask import Flask

# Create Flask app instance
app = Flask(__name__)

# Base route
@app.route("/")
def home():
    return """
    <h1>Welcome to the Home Page</h1>
    <p>This is the main page of the Flask web application.</p>
    """

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
```

### Key Concepts Explained

- `Flask(__name__)` → identifies app location
- `@app.route("/")` → URL mapping
- `debug=True` → auto reload + error details

---

### Understanding Routes & Responses

```python
@app.route("/api/user")
def user():
    return {
        "id": 1,
        "name": "Lewis",
        "role": "Student"
    }
```

✔ Flask automatically converts dictionary → JSON
✔ This is a **REST API response**

✅ Outcome:
Students can **build and test APIs locally**

---

## 🎨 Class 4: Working with Templates in Flask (MAKE IT BETTER)

Now this is where Flask becomes **real web development**, not just APIs.

Perfect content 👍
Your structure is already good — it just needs **clarity, simplification, and smoother teaching flow**, especially around **GET vs POST**. I’ll rewrite **Class 4** in a **student-friendly, easy-to-understand way**, without overloading them.

---

# 🎨 Class 4: Working with Templates in Flask (Improved & Simplified)

> This class moves Flask from _just backend code_ to **real web development** with proper HTML pages.

---

## 🔧 1. Introduction to Flask Templates

### What are Templates?

- Templates are **HTML files** that Flask uses to render web pages
- They allow **dynamic content** (data coming from Python)
- Stored inside the **`templates/` folder**

---

### ❌ Returning HTML Directly (Not Recommended)

```python
@app.route("/")
def home():
    return "<h1>Hello World</h1>"
```

🔴 Problems:

- Messy for large HTML
- No styling
- Hard to maintain

---

### ✅ Using Templates (Best Practice)

```python
@app.route("/")
def home():
    return render_template("index.html")
```

✔ Clean
✔ Reusable
✔ Professional

---

## 🗂️ 2. Setting Up Template Structure

### Creating Templates Folder

```
project/
│── app.py
│── templates/
│     └── index.html
```

📌 Flask automatically looks for HTML files inside `templates/`

---

## 🖼️ 3. Rendering HTML Using `render_template()`

### Linking Python Route to HTML

```python
@app.route("/")
def home():
    return render_template("index.html")
```

---

### Passing Data from Python → HTML

```python
@app.route("/")
def home():
    name = "Aakash"
    return render_template("index.html", name=name)
```

---

## 🧩 4. Jinja2 Templating Syntax (Very Easy)

### 📄 `index.html`

```html
<!doctype html>
<html>
  <head>
    <title>Flask Templates</title>
  </head>
  <body>
    <h1>Welcome to Flask App</h1>

    <!-- Variable -->
    <h3>Hello, {{ name }}</h3>

    <!-- Condition -->
    {% if name == "Aakash" %}
    <p>You are an admin user</p>
    {% else %}
    <p>You are a guest user</p>
    {% endif %}

    <!-- Loop -->
    {% for i in range(5) %}
    <p>Iteration {{ i }}</p>
    {% endfor %}
  </body>
</html>
```

### Key Rules

- `{{ }}` → variables
- `{% %}` → logic (if, for)
- Python logic inside HTML

---

## 🎯 Why Templates Are Important

- ❌ No hardcoded HTML in Python
- ✅ Logic → Python
- ✅ UI → HTML
- Uses **Jinja2 templating engine**

---

## 📁 Recommended Project Structure

```
project/
│── app.py
│
│── templates/
│     ├── index.html
│     └── form.html
│
│── static/
│     ├── css/
│     │     └── style.css
│     └── js/
│           └── script.js
```

---

Nice, this fits **perfectly** as a teaching flow 👍
I’ll explain it **exactly in your format**, clean, structured, and easy to revise.

---

## 🧠 Class 5 – Understanding REST API: Introduction to GET and POST

## 🔹 1. By default Flask uses **GET** method

- When you create a route in Flask **without specifying `methods`**, it automatically accepts **GET** requests.
- GET is mainly used to **fetch data** or **display pages**.

### Example:

```python
@app.route("/")
def home():
    return "Hello Flask"
```

➡️ This route works only with **GET**
➡️ Opened directly in the browser

---

## 🔹 2. What is a REST API?

**REST (Representational State Transfer)** is a way to build web services using HTTP methods.

### Common HTTP methods:

| Method | Purpose     |
| ------ | ----------- |
| GET    | Fetch data  |
| POST   | Send data   |
| PUT    | Update data |
| DELETE | Delete data |

In this class, we focus on **GET and POST**.

---

## 🔹 3. GET vs POST (Concept)

### ✅ GET Method

- Sends data through the **URL**
- Data is visible
- Used for **search, filters, reading data**

Example URL:

```
/login?username=admin&password=123
```

---

### ✅ POST Method

- Sends data through **request body**
- Data is hidden
- Used for **login, signup, sensitive data**

---

## 🔹 4. First Form: Using **Both GET and POST in One Route**

### Flask Code:

```python
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        name = request.form["username"]
        password = request.form["password"]
        return f"POST → Hello {name}"
    return render_template("form.html")
```

### Explanation:

- GET → shows the form
- POST → processes form data
- Single route handles both actions

---

## 🔹 5. Second Method: **Separating GET and POST Routes**

### Show Form (GET):

```python
@app.route("/form", methods=["GET"])
def show_form():
    return render_template("form.html")
```

### Handle Data (POST):

```python
@app.route("/form", methods=["POST"])
def handle_form():
    name = request.form["username"]
    return f"POST → Hello {name}"
```

### Why this method?

- Cleaner code
- Better readability
- Used in real projects

---

## 🔹 6. Third Method: Form Using **GET Only**

### Flask Code:

```python
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
```

### HTML Form:

```html
<form method="get" action="/form-get-result">
  <label>Username:</label>
  <input type="text" name="username" required />

  <br /><br />

  <label>Password:</label>
  <input type="text" name="password" required />

  <br /><br />

  <button type="submit">Submit (GET)</button>
</form>
```

### Output URL:

```
/search?username=Aakash
```

---

## 🔹 7. request.form vs request.args

| Feature       | request.form | request.args |
| ------------- | ------------ | ------------ |
| Method        | POST         | GET          |
| Data location | Request body | URL          |
| Secure        | ✅           | ❌           |

---

## 🔹 8. Summary (Exam Friendly)

- Flask uses **GET by default**
- GET is used to **fetch data**
- POST is used to **send data**
- Forms can use:
  1. GET + POST in same route
  2. Separate GET and POST routes
  3. GET-only route (data visible in URL)

- REST API works using HTTP methods


## Designing a RESTful Backend: Planning a Flask Application for User Management

1.understanding http method in flask
* understanding get, post, put, delete methods in flask
* downloading the postman tool for api testing
