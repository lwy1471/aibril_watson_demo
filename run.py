from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/apis/')
def hello():
	return render_template('apis.html')

@app.route('/apis/assistant_old')
def assistant_old():
    return render_template('assistant_test.html')

@app.route('/apis/assistant')
def assistant():
    return render_template('assistant.html')
    
@app.route('/apis/assistant/getService',methods=['GET','POST'])
def assistantGetService():
    if (request.method=='POST'):
        username = request.form['username']
        password = request.form['password']
        workspaceId = request.form['workspaceId']
        response = ["Username: ","password: ", "workspaceId: "]
        print("username: "+username+" password: "+password+" workspaceId: "+workspaceId)
        return "hi"
    else:
        return "bye"

if __name__ == '__main__':
	app.run(debug=True)