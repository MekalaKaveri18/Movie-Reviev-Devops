from flask import Flask, render_template, request

app = Flask(__name__)

reviews = []

@app.route('/')
def home():
    return render_template('index.html', reviews=reviews)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/add', methods=['POST'])
def add_review():
    movie = request.form['movie']
    review = request.form['review']
    rating = request.form['rating']
    reviews.append({'movie': movie, 'review': review, 'rating':rating})
    return render_template('index.html', reviews=reviews)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

