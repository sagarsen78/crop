from flask import Flask, render_template,request
import pickle
import numpy as np

model1=pickle.load(open('RandomForest.pkl','rb'))

app=Flask(__name__)

@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict',methods=['POST'])
def home():

    nmeasure = int(request.form['n'])
    pmeasure = int(request.form['p'])
    kmeasure = int(request.form['k'])
    tempmeasure = int(request.form['temp'])
    humimeasure = int(request.form['humi'])
    phmeasure = int(request.form['ph'])
    rainmeasure = int(request.form['rain'])


    arr=np.array([[nmeasure,pmeasure,kmeasure,tempmeasure,humimeasure,phmeasure,rainmeasure]])
    pred=model1.predict(arr)

if __name__=='__main__':
    app.run(debug=True)