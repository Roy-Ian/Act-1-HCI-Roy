from flask import Flask, render_template, request, redirect, url_for, flash, session
from markupsafe import escape

app = Flask(__name__)
app.secret_key = "super-secret-key"  # Required for flash messages & sessions

# Fake user database (demo only)
users = {
    "rai@gmail.com": "PasswordNi"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    # Authentication
    if email in users and users[email] == password:
        session["user"] = email
        flash("Login successful!", "success")
        return redirect(url_for("dashboard"))
    else:
        flash("Invalid email or password.", "error")
        return redirect(url_for("home"))

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("home"))
    return render_template("dashboard.html", user=session["user"])


@app.route("/logout")
def logout():
    session.pop("user", None)
    flash("You have been logged out.", "info")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
