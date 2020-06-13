from flask import Flask,render_template
import requests
app = Flask(__name__)

@app.route('/')
def all():
	url = "https://type.fit/api/quotes"
	res = requests.get(url)
	quote = res.json()
	return render_template('home.html',data=quote,l=len(quote))
if __name__ == '__main__':
	app.run()