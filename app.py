from flask import Flask, render_template, request
from aylienapiclient import textapi

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	client = textapi.Client("691d60ef", "e84ff6dca64ad756bd7676e6aef7f989")
	link = request.form['words']
	number = request.form['count']
	sentiment = client.Sentiment({'url': link})
	summary = client.Summarize({'url': link, 'sentences_number': number})
	return render_template('index.html',sentiment=sentiment['polarity'],summary=summary['sentences'])

if __name__ == '__main__':
	app.run()