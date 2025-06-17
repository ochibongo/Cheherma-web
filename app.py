#imports
from flask import Flask, render_template, redirect, request, url_for,flash
from flask_sqlalchemy import SQLAlchemy
from flask_scss import Scss
from datetime import datetime


# Initialize Flask app
app = Flask(__name__)
app.secret_key = "super_secret_key"
Scss(app)  # Enable SCSS support


# Database configuration-sqlachemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


# Databse model-Defining the Task model (like a table)
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(100), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)
    completed = db.Column(db.Boolean, default=False)

    def __str__(self):
        return f"Task {self.id}"

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

class PartnerWithUs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    message = db.Column(db.Text, nullable=False)
    submitted_at = db.Column(db.DateTime, default=datetime.utcnow)

class Donation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    type = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)


# ---------- Routes ----------
# Home page with form & task list
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        current_task = request.form["content"]
        new_task = MyTask(content=current_task)
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error saving task: {e}"
    else:
        tasks = MyTask.query.order_by(MyTask.created.desc()).all()
        return render_template("index.html", tasks=tasks)

@app.route('/partnerships', methods=['GET', 'POST'])
def partnerships():
    if request.method == 'POST':
        # handle form submission here
        # e.g., save data or send email
        pass
    return render_template('partnerships.html')


@app.route('/volunteer', methods=['GET', 'POST'])
def volunteer():
    if request.method == 'POST':
        # Extract form data
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        country_code = request.form.get('country_code')
        country = request.form.get('country')
        partnership_type = request.form.get('type')
        message = request.form.get('message')

        # Group-specific fields
        group_size = request.form.get('group_size')  # May be None if not provided
        group_name = request.form.get('group_name')

        # ✅ Debug / print to console
        print("Volunteer Submission Received:")
        print(f"Name: {name}, Email: {email}, Phone: {country_code} {phone}")
        print(f"Country: {country}, Type: {partnership_type}")
        print(f"Group Size: {group_size}, Group Name: {group_name}")
        print(f"Message: {message}")

        # ✅ Flash a success message or redirect
        flash("Thank you for signing up to volunteer! We will be in touch soon.", "success")
        return redirect(url_for('volunteer'))

    return render_template('volunteer.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        other_name = request.form.get('other_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        country = request.form.get('country')
        subject = request.form.get('subject')
        message = request.form.get('message')

        print("New Contact Submission:")
        print(f"Name: {first_name} {other_name} {last_name}")
        print(f"Email: {email}, Phone: {phone}, Country: {country}")
        print(f"Subject: {subject}")
        print(f"Message: {message}")

        flash("Thank you for contacting us! We'll get back to you shortly.", "success")
        return redirect(url_for('contact'))

    return render_template('contact.html')


@app.route("/donate", methods=["GET", "POST"])
def donate():
    preselected_type = request.args.get("type", "")  # Get donation type from URL
    if request.method == "POST":
        # Handle donation submission
        pass
    return render_template("donate.html", preselected_type=preselected_type)
  
# Static pages routes
@app.route("/projects")
def project_list():
    return render_template("projects.html")

@app.route("/careers")
def careers():
    return render_template("careers.html")

@app.route("/water")
def water():
    return render_template("water.html")

@app.route("/women")
def women():
    return render_template("women.html")

@app.route('/medicalcamp', methods=['GET', 'POST'])
def medicalcamp():
    if request.method == 'POST':
        # handle form submission here
        # e.g., save data or send email
        pass
    return render_template('medicalcamp.html')

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/food")
def food():
    return render_template("food.html")

@app.route("/stories")
def stories():
    return render_template("stories.html")

@app.route("/whoweare")
def whoweare():
    return render_template("whoweare.html")

@app.route("/mission")
def mission():
    return render_template("mission.html")

@app.route('/team')
def team():
    flash("Team page is currently unavailable. Please check back soon.", "danger",)
    return redirect(url_for('index'))

@app.route("/getinvolved")
def getinvolved():
    return render_template("getinvolved.html")

@app.route("/advocacy")
def advocacy():
    return render_template("advocacy.html")

@app.route("/education")
def education():
    return render_template("education.html")

@app.route("/digitalhealth")
def digitalhealth():
    return render_template("digitalhealth.html")

@app.route("/ncds")
def ncds():
    return render_template("ncds.html")

@app.route("/ourstory")
def ourstory():
    return render_template("ourstory.html")

@app.route("/telemedicine")
def telemedicine():
    return render_template("telemedicine.html")

@app.route("/communitypharmacy")
def communitypharmacy():
    return render_template("communitypharmacy.html")


# Delete a task
@app.route("/delete/<int:id>")
def delete(id):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        return f"Error deleting task: {e}"
    
# Edit a task
@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    task = MyTask.query.get_or_404(id)
    if request.method == "POST":
        try:
            task.content = request.form["content"]
            db.session.commit()
            return redirect("/")
        except Exception as e:
            return f"Error: {e}"
    else:
        return render_template("edit.html", task=task)

# Run the app
if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Create tables if not already existing
    app.run(debug=True)



