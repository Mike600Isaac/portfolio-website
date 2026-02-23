from flask import jsonify, render_template, request, flash, redirect, session, url_for
from wtforms import form
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

    form = ContactForm()

    if form.validate_on_submit():

        cont = Contact(
            name=form.name.data,
            email=form.email.data,
            message=form.message.data,
            contact_method=form.contact_method.data,
            phone=form.phone.data
        )

        db.session.add(cont)
        db.session.commit()

        flash('Your message has been received. I will get back to you shortly.', 'success')

        return redirect(url_for("contact") + "#contact-me")

    if request.method == 'POST':
        flash('Please fill the form correctly.', 'danger')

    return render_template('index.html', contact=form)

from flask import session, redirect, url_for, flash, render_template

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():

    form = AdminLoginForm()

    if form.validate_on_submit():
        admin = Admin.query.filter_by(email=form.email.data).first()
        if admin and admin.password == form.password.data:

            session['admin_logged_in'] = True
            session['admin_id'] = admin.id

            flash("Login successful", "success")
            return redirect(url_for('admin_dashboard'))

        flash("Invalid email or password", "danger")
    return render_template("admin_login.html", form=form)


@csrf.exempt
@app.route('/admin/contact/<int:id>/attend', methods=['POST'])
def mark_attended(id):

    contact = Contact.query.get_or_404(id)

    contact.contact_status = "attended"
    db.session.commit()

    return jsonify(success=True)


@app.route('/admin/dashboard')
def admin_dashboard():

    if not session.get('admin_logged_in'):
        flash("Please login first", "danger")
        return redirect(url_for('admin_login'))
    contacts = Contact.query.order_by(Contact.date_sent.desc()).all()

    return render_template('admin_dashboard.html', contacts=contacts)



@app.route('/admin/logout')
def admin_logout():
    session.clear()
    return redirect(url_for('admin_login'))

    

