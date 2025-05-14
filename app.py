from flask import Flask, request, jsonify, render_template
from model import predict_category

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Serves your HTML template

@app.route('/predict', methods=['POST'])
def predict():
    text = request.form.get('article', '')

    if not text.strip():
        return render_template('index.html',prediction_text='Error: No text provided')

    category, confidence = predict_category(text)
    return render_template('index.html', prediction_text='Category : {}'.format(category))

if __name__ == '__main__':
    app.run(debug=True)
