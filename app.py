from flask import Flask, render_template

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route for about page
@app.route('/about.html')
def about():
    return render_template('about.html')

# Route for courses page
@app.route('/courses.html')
def courses():
    return render_template('courses.html')

# Route for appointment page
@app.route('/appointment.html')
def appointment():
    return render_template('appointment.html')

# Route for team page
@app.route('/team.html')
def team():
    return render_template('team.html')

# Route for testimonial page
@app.route('/testimonial.html')
def testimonial():
    return render_template('testimonial.html')

# Route for contact page
@app.route('/contact.html')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)