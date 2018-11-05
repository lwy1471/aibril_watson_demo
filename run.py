from flask import Flask, render_template

app = Flask(__name__)

@app.route('/apis/')
def hello():
	return render_template('apis.html')

@app.route('/apis/assistant_old')
def assistant():
    return render_template('assistant.html')

@app.route('/apis/assistant')
def assistant_test():
    return render_template('assistant_test.html')

	
if __name__ == '__main__':
	app.run(debug=True)