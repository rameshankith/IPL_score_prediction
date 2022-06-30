#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template
import pickle
import numpy as np

filename = "Batting-score-LassoReg-model.pkl"
regressor = pickle.load(open(filename,'rb'))

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    imput_array = list()
    if request.method == 'POST':
        batting_team = request.form['batting-team']
        
        if(batting_team=='Chennai Super Kings'):
            input_array=input_array + [1,0,0,0,0,0,0,0]
        elif(batting_team=='Delhi Capitals'):
            input_array=input_array + [0,1,0,0,0,0,0,0]
        elif(batting_team=='Kings XI Punjab'):
            input_array=input_array + [0,0,1,0,0,0,0,0]
        elif(batting_team=='Kolkata Knight Riders'):
            input_array=input_array + [0,0,0,1,0,0,0,0]
        elif(batting_team=='Mumbai Indians'):
            input_array=input_array + [0,0,0,0,1,0,0,0]
        elif(batting_team=='Rajasthan Royals'):
            input_array=input_array + [0,0,0,0,0,1,0,0]
        elif(batting_team=='Royal Challengers Banglore'):
            input_array=input_array + [0,0,0,0,0,0,1,0]
        elif(batting_team=='Sunrisers Hyderabad'):
            input_array=input_array + [0,0,0,0,0,0,0,1]
        
        
        bowling_team = request.form('bowling-team')
        
        if(bowling_team=='Chennai Super Kings'):
            input_array=input_array + [1,0,0,0,0,0,0,0]
        elif(bowling_team=='Delhi Capitals'):
            input_array=input_array + [0,1,0,0,0,0,0,0]
        elif(bowling_team=='Kings XI Punjab'):
            input_array=input_array + [0,0,1,0,0,0,0,0]
        elif(bowling_team=='Kolkata Knight Riders'):
            input_array=input_array + [0,0,0,1,0,0,0,0]
        elif(bowling_team=='Mumbai Indians'):
            input_array=input_array + [0,0,0,0,1,0,0,0]
        elif(bowling_team=='Rajasthan Royals'):
            input_array=input_array + [0,0,0,0,0,1,0,0]
        elif(bowling_team=='Royal Challengers Banglore'):
            input_array=input_array + [0,0,0,0,0,0,1,0]
        elif(bowling_team=='Sunrisers Hyderabad'):
            input_array=input_array + [0,0,0,0,0,0,0,1]
            
        venue = request.form('venue')
        
        if(venue=='Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium'):
            input_array=input_array + [1,0,0,0,0,0,0,0,0,0,0,0]
        elif(venue=='Dubai International Cricket Stadium'):
            input_array=input_array + [0,1,0,0,0,0,0,0,0,0,0,0]
        elif(venue=='Eden Gardens'):
            input_array=input_array + [0,0,1,0,0,0,0,0,0,0,0,0]
        elif(venue=='Feroz Shah Kotla'):
            input_array=input_array + [0,0,0,1,0,0,0,0,0,0,0,0]
        elif(venue=='Himachal Pradesh Cricket Association Stadium'):
            input_array=input_array + [0,0,0,0,1,0,0,0,0,0,0,0]
        elif(venue=='M Chinnaswamy Stadium'):
            input_array=input_array + [0,0,0,0,0,1,0,0,0,0,0,0]
        elif(venue=='MA Chidambaram Stadium, Chepauk'):
            input_array=input_array + [0,0,0,0,0,0,1,0,0,0,0,0]
        elif(venue=='Punjab Cricket Association Stadium, Mohali'):
            input_array=input_array + [0,0,0,0,0,0,0,1,0,0,0,0]
        elif(venue=='Sawai Mansingh Stadium'):
            input_array=input_array + [0,0,0,0,0,0,0,0,1,0,0,0]
        elif(venue=='Sharjah Cricket Stadium'):
            input_array=input_array + [0,0,0,0,0,0,0,0,0,1,0,0]
        elif(venue=='Sheikh Zayed Stadium'):
            input_array=input_array + [0,0,0,0,0,0,0,0,0,0,1,0]
        elif(venue=='Wankhede Stadium'):
            input_array=input_array + [0,0,0,0,0,0,0,0,0,0,0,1]
        
        
        overs = float(request.form['overs'])
        runs = int(request.form['runs'])
        wickets = int(request.form['wickets'])
        runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        
        input_array = input_array + [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
        
        features = np.array([input_array])
        prediction = int(regressor.predict(features)[0])
        
        return render_template('result.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5)
        
        
if __name__ == '__main__':
    app.run(debug=True)

