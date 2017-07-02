from flask import Flask, render_template, request
from textblob import TextBlob
from aylienapiclient import textapi

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	client = textapi.Client("691d60ef", "e84ff6dca64ad756bd7676e6aef7f989")
	words = request.form['text']
	number = request.form['count']
	sentiment = client.Sentiment({'text': words})
	summary = client.Summarize({'title': "Hello World",'text': words, 'sentences_number': int(number)})
	classifications = client.Classify({"text": words})
	return render_template('index.html',sentiment=sentiment['polarity'],summary=summary['sentences'],classification=classifications['categories'][0]['label'])

if __name__ == '__main__':
	app.run(debug = True)