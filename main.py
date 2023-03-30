from pickle import TRUE
from flask import Flask
app=Flask(__name__)
@app.route('/')
def welcome():
    return "welcome to flask satya"

if __name__=='__main__':
    app.run(debug=TRUE,)
