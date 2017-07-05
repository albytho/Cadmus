from flask import Flask, flash, render_template, request
from aylienapiclient import textapi
from logging import FileHandler, WARNING

app = Flask(__name__)

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	client = textapi.Client("691d60ef", "e84ff6dca64ad756bd7676e6aef7f989")
	words = request.form['text']
	number = request.form['count']
	sentiment = client.Sentiment({'text': str(words)})
	summary = client.Summarize({'title': "Hello World",'text': str(words), 'sentences_number': int(number)})
	classifications = client.Classify({"text": str(words)})
	return render_template('index.html',sentiment=sentiment['polarity'],summary=summary['sentences'],classification=classifications['categories'][0]['label'])

if __name__ == '__main__':
	app.debug = True
	app.run()