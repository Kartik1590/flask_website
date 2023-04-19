from flask import Flask,render_template,jsonify
from database import load_db
app=Flask(__name__)
#route is a part of url after rendering a website
Jobs=load_db()
@app.route('/')#empty route or homepage
def hello_world():
  return render_template('home.html',job=Jobs,Company_name='Honey')
@app.route('/api/jobs')
def jason():
  return jsonify(Jobs)
if __name__ =='__main__':
    app.run(host='0.0.0.0',debug=True) #if we dont put this then we have to use flask bash command that will be find on flask website

