from flask import Flask,render_template,request,jsonify
from functions import *
from flask_cors import CORS


app=Flask(__name__)
CORS(app)

@app.route('/')
def index():
        return jsonify(get_student_details() )



if __name__=='__main__':
    app.run(debug=True)
