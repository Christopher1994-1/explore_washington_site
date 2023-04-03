from flask import Flask, render_template


app = Flask(__name__)




# route for the home page
@app.route('/')
def index():
    return render_template('index.html')


# route for the home page
@app.route('/about')
def about():
    return render_template('pages/about.html')



# route for the home page
@app.route('/portfolio')
def portfolio():
    return render_template('pages/portfolio.html')








if __name__ == "__main__":
    app.run(debug=True)