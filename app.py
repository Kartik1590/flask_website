from flask import Flask
app=Flask(__name__)
#route is a part of url after rendering a website
@app.route('/')#empty route or homepage
def hello_world():
  return 'Hello World!'
if __name__ =='__main__':
    app.run(host='0.0.0.0',debug=True) #if we dont put this then we have to use flask bash command that will be find on flask website

