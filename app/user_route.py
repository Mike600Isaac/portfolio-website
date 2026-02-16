from flask import render_template, request, flash, redirect, url_for
from app import app,csrf
from app.form import ContactForm,AdminLoginForm
from app.models import db,Contact,Admin


@app.route("/")
def home():
    contact = ContactForm()
    return render_template("index.html", contact=contact)


@app.route("/contact/us/", methods=['GET', 'POST'])
@csrf.exempt
def contact():

    contact = ContactForm()

    if contact.validate_on_submit():

        name = contact.name.data
        email = contact.email.data
        message = contact.message.data
        contact_method = contact.contact_method.data
        phone = contact.phone.data

        cont = Contact(
            name=name,
            email=email,
            message=message,
            contact_method=contact_method,
            phone=phone
        )

        db.session.add(cont)
        db.session.commit()

        flash('Your message has been received. I will get back to you shortly.', 'success')

        return redirect(url_for("contact") + "#contact-me")

    if request.method == 'POST':
        flash('Please fill the form correctly.', 'danger')

    return render_template('index.html', contact=contact)


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():

    form = AdminLoginForm()

    if form.validate_on_submit():

        admin = Admin.query.filter_by(email=form.email.data).first()

        if admin and admin.password(form.password.data):
            flash("Login successful", "success")
            return redirect(url_for('admin_dashboard'))

        flash("Invalid email or password", "danger")

    return render_template("admin_login.html", form=form)


