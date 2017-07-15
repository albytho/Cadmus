from flask import Flask, flash, render_template, request
from aylienapiclient import textapi
from logging import FileHandler, WARNING

app = Flask(__name__)

file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)

app.logger.addHandler(file_handler)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
	client = textapi.Client("691d60ef", "e84ff6dca64ad756bd7676e6aef7f989")
	words = request.form['text']
	number = request.form['count']
	words = words.replace( u'\u2018', "'").replace( u'\u2019', "'").replace( u'\u201c', '"').replace( u'\u201d', '"')
	sentiment = client.Sentiment({'text': words})
	summary = client.Summarize({'title': "Hello World",'text': words, 'sentences_number': number})
	classifications = client.Classify({"text": words})
	return render_template('index.html',sentiment=sentiment['polarity'],summary=summary['sentences'],classification=classifications['categories'][0]['label'])

if __name__ == '__main__':
	app.debug = True
	app.run()