from flask import Flask,render_template,request
from flask_cors import cross_origin
import numpy as np 

app=Flask(__name__)

#loading the model
import pickle
model=pickle.load(open(r'C:\Users\sagar\OneDrive\Desktop\crop\RandomForest.pkl','rb'))
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['GET','POST'])
@cross_origin()
def predict():
    if predict.method=='POST':
        nmeasure=int(request.form['n'])
        pmeasure=int(request.form['p'])
        kmeasure=int(request.form['k'])
        tempmeasure=int(request.form['temp'])
        humimeasure=int(request.form['humi'])
        phmeasure=int(request.form['ph'])
        rainmeasure=int(request.form['rain'])
        yhat.model.predict([[nmeasure,pmeasure,kmeasure,tempmeasure,humimeasure,phmeasure,rainmeasure]])
        return render_template('output.html',prediction=yhat[0])

if __name__=='__main__':
    app.run(debug=True)
