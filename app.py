# Importing essential libraries
from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the Random Forest CLassifier model
filename = 'first-innings-score-lr-model.pkl'
regressor = pickle.load(open(filename, 'rb'))

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    temp_array = list()
    temp_array1=list()

    if request.method == 'POST':
        batting_team = request.form['batting-team']
        if batting_team == 'Chennai Super Kings':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
        elif batting_team == 'Delhi Daredevils':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
        elif batting_team == 'Kings XI Punjab':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
        elif batting_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
        elif batting_team == 'Mumbai Indians':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
        elif batting_team == 'Rajasthan Royals':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
        elif batting_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
        elif batting_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

        bowling_team = request.form['bowling-team']
        if bowling_team == 'Chennai Super Kings':
            temp_array = temp_array + [1, 0, 0, 0, 0, 0, 0, 0]
        elif bowling_team == 'Delhi Daredevils':
            temp_array = temp_array + [0, 1, 0, 0, 0, 0, 0, 0]
        elif bowling_team == 'Kings XI Punjab':
            temp_array = temp_array + [0, 0, 1, 0, 0, 0, 0, 0]
        elif bowling_team == 'Kolkata Knight Riders':
            temp_array = temp_array + [0, 0, 0, 1, 0, 0, 0, 0]
        elif bowling_team == 'Mumbai Indians':
            temp_array = temp_array + [0, 0, 0, 0, 1, 0, 0, 0]
        elif bowling_team == 'Rajasthan Royals':
            temp_array = temp_array + [0, 0, 0, 0, 0, 1, 0, 0]
        elif bowling_team == 'Royal Challengers Bangalore':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 1, 0]
        elif bowling_team == 'Sunrisers Hyderabad':
            temp_array = temp_array + [0, 0, 0, 0, 0, 0, 0, 1]

        try:   
            venue = request.form['venue']
            if venue == 'M Chinnaswamy Stadiums':
                temp_array = temp_array + [1, 0, 0, 0, 0,
                                       0, 0, 0, 0, 0,
                                       0, 0, 0, 0, 0,
                                       0, 0, 0, 0, 0,
                                       0, 0, 0, 0, 0,
                                       0, 0, 0, 0, 0, 0]
            elif venue == 'Feroz Shah Kotla':
                temp_array = temp_array + [0, 1, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == 'Eden Gardens':
                temp_array = temp_array + [0, 0, 1, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == ' Wankhede Stadium':
                temp_array = temp_array + [0, 0, 0, 1, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == 'MA Chidambaram Stadium, Chepauk':
                temp_array = temp_array + [0, 0, 0, 0, 1,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == 'Rajiv Gandhi International Stadium, Uppal':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        1, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == 'Punjab Cricket Association Stadium, Mohali':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 1, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == 'Sawai Mansingh Stadium ':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 1, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == 'Dr DY Patil Sports Academy':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 1, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == 'Subrata Roy Sahara Stadium':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 1,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == 'Maharashtra Cricket Association Stadium':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        1, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == ' Kingsmead':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 1, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == 'Sardar Patel Stadium, Motera':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 1, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == ' Brabourne Stadium':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 1, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == 'SuperSport Park':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 1,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]


            elif venue == 'OUTsurance Oval':
                temp_array = temp_array + [
                    0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0,
                    0, 0, 0, 0, 0,
                    1, 0, 0, 0, 0,
                    0, 0, 0, 0, 0,
                    0, 0, 0, 0, 1, 0]                              

            elif venue == 'Punjab Cricket Association IS Bindra Stadium, Mohali':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 1, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == 'Himachal Pradesh Cricket Association Stadium':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 1, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == ' Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 1, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == 'New Wanderers Stadium':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 1,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == "St George's Park":
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        1, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == ' Dubai International Cricket Stadium':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 1, 0, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == 'Barabati Stadium':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 1, 0, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == ' JSCA International Stadium Complex':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 1, 0,
                                        0, 0, 0, 0, 0, 0]

            elif venue == ' Sheikh Zayed Stadium':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 1,
                                        0, 0, 0, 0, 0, 0]

            elif venue == 'Sharjah Cricket Stadium':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        1, 0, 0, 0, 0, 0]

            elif venue == ' Shaheed Veer Narayan Singh International Stadium':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 1, 0, 0, 0, 0]

            elif venue == ' Newlands':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 1, 0, 0, 0]

            elif venue == 'Holkar Cricket Stadium':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 1, 0, 0]

            elif venue == ' Buffalo Park':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 1, 0]
        

            elif venue == ' De Beers Diamond Oval':
                temp_array = temp_array + [0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0,
                                        0, 0, 0, 0, 0, 1]
        except:
            return render_template('resultError.html', result="INPUT")
        
        try:
            overs = float(request.form['overs'])
        except:
            return render_template('resultError.html',result="INVALID OVERS FIELD.")
        try:
            runs = int(request.form['runs'])
        except:
            return render_template('resultError.html',result=" INVALID RUNS FIELD.")
            
        try:
            wickets = int(request.form['wickets'])
        except:
            return render_template('resultError.html',result=" INVALID WICKETS FIELD.")
        try:
            runs_in_prev_5 = int(request.form['runs_in_prev_5'])
        except:
            return render_template('resultError.html',result="INVALID RUNS IN PREV 5 OVER FIELD.")
        try:
            wickets_in_prev_5 = int(request.form['wickets_in_prev_5'])
        except:
            return render_template('resultError.html',result="INVALID WICKETS IN PREV 5 OVER FIELD.")

        if(batting_team==bowling_team):
            return render_template('resultError.html',result="Batting Team & Bowling team Cannot Be The Same.")
        if(overs>20):
            return render_template('resultError.html',result="Overs Cannot be Greater Than 20.")
        if(wickets>9):
            return render_template('resultError.html',result="Match has Ended Already.")
        if(runs_in_prev_5>runs):
            return render_template('resultError.html',result="Runs In Previous Five Overs Cannot Be Greater Than Total Runs.")
        try:
            temp_array = temp_array + temp_array1+ [overs, runs, wickets, runs_in_prev_5, wickets_in_prev_5]
            # temp_array1=temp_array+temp_array1
            data = np.array([temp_array])
            my_prediction = int(regressor.predict(data)[0])
            return render_template('result.html', lower_limit = my_prediction-10, upper_limit = my_prediction+5)
        except:
            return render_template('resultError.html', result="The Provided Venue Is Not Currently In Use.")


if __name__ == '__main__':
    app.run(debug=True)
