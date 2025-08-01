#import the necessary modules from Flask
from flask import Flask, render_template, request

#  create an instance of the Flask application
app = Flask(__name__)

# The main route - website

@app.route('/')
def home():
    return render_template('home.html')

# Route to the projects section
@app.route('/projects')
def projects():
    return render_template('projects.html')

# route to the skills section

@app.route('/skills')
def skills():
    return render_template('skills.html')

#route to the about section

@app.route('/about')
def about():
    return render_template('about.html')

# route to the contact form  (GET – shows the form, POST – receives data).

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Printing a message to the console, simulating sending a message
        print(f"Odebrano wiadomość od {name} ({email}): {message}")

        # We pass data from the form to the template
        return render_template('contact.html', submitted=True, name=name)
    
     # For the GET method we return an empty form
    return render_template('contact.html', submitted=False)
   
# We only run the application if the file is run directly
if __name__ == '__main__':
    app.run(debug=True)


# Portfolio Flask App created by Sebastian Kajda (UCD Assignment - August 2025)

