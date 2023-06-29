from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/certifications')
def certifications():
    return render_template('certifications.html')

@app.route('/guides')
def guides():
    return render_template('guides.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/subscriptions')
def subscriptions():
    return render_template('subscriptions.html')

@app.route('/resources/case_study')
def case_study():
    return render_template('case_study.html')

@app.route('/resources/energy_efficiency')
def energy_efficiency():
    return render_template('energy_efficiency.html')

@app.route('/resources/carbon_footprint', methods=['GET', 'POST'])
def carbon_footprint():
    if request.method == 'POST':
        # This function handles POST requests for /resources/carbon_footprint
        # Here you would typically process the form data and calculate the carbon footprint.
        print(request.form)
        return render_template('carbon_footprint.html', result='Carbon footprint calculation goes here.')
    else:
        # This function handles GET requests for /resources/carbon_footprint
        return render_template('carbon_footprint.html')

if __name__ == '__main__':
    app.run(debug=True)
