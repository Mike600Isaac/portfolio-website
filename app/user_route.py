from flask import render_template, request, flash, redirect, url_for
from app import app


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        # For now we just print (later you can send email)
        print("New Contact Message")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)

        flash("Your message has been sent successfully!", "success")
        return redirect(url_for("contact"))

    return render_template("contact.html")
