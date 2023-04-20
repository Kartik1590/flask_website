from flask import Flask,render_template,jsonify
from database import load_db
import json
app=Flask(__name__)
#route is a part of url after rendering a website
Jobs=load_db()
# Jobs=[
#   {
#     'id':1,
#     'title':'Data Analyst',
#     'location':'Benguluru',
#     'salary':'Rs. 15,00,000'
#   },
#    {
#     'id':2,
#     'title':'Data Scientist',
#     'location':'Delhi',
#     'salary':'Rs. 15,00,000'
#   },
#    {
#     'id':3,
#     'title':'Web Developer',
#     'location':'SanFransisco',
#     'salary':'Rs. 15,000,000'
#   }
# ]
@app.route('/')#empty route or homepage
def hello_world():
  return render_template('home.html',job=Jobs,Company_name='Honey')
@app.route('/api/jobs')
def jason():
  
  return jsonify(Jobs)
if __name__ =='__main__':
    app.run(host='0.0.0.0',debug=True) #if we dont put this then we have to use flask bash command that will be find on flask website

