from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/skills')
def skills():
    return render_template('skills.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        print(f"Odebrano wiadomość od {name} ({email}): {message}")
        return render_template('contact.html', submitted=True, name=name)
    return render_template('contact.html', submitted=False)
   

if __name__ == '__main__':
    app.run(debug=True)

