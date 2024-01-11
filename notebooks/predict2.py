import pickle
import pandas as pd
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

output_file = 'model_rfc.bin'

with open(output_file, 'rb') as f_in:
    rf_model = pickle.load(f_in)

def predict(player):
    player_row_df = pd.DataFrame([player])
    soft_prediction_for_player = rf_model.predict_proba(player_row_df)[0,1]
    hard_prediction_for_player = soft_prediction_for_player >= 0.5

    result = {
        'Probability of NBA player entering the Hall of Fame': soft_prediction_for_player,
        'Will player enter into Hall of Fame soon?': bool(hard_prediction_for_player)
    }

    return result

@app.route('/predict', methods=['GET', 'POST'])
def make_prediction():
    if request.method == 'POST':
        try:
            # Extract data from form and convert to appropriate types
            player = {
                "league": int(request.form['league']),
                "games": int(request.form['games']),
                "minutes": int(request.form['minutes']),
                "pts": int(request.form['pts']),
                "offReb": int(request.form['offReb']),
                "defReb": int(request.form['defReb']),
                "reb": int(request.form['reb']),
                "asts": int(request.form['asts']),
                "stl": int(request.form['stl']),
                "blk": int(request.form['blk']),
                "turnover": int(request.form['turnover']),
                "pf": int(request.form['pf']),
                "fga": int(request.form['fga']),
                "fgm": int(request.form['fgm']),
                "fta": int(request.form['fta']),
                "ftm": int(request.form['ftm']),
                "tpa": int(request.form['tpa']),
                "tpm": int(request.form['tpm']),
                "totalSeasons": int(request.form['totalSeasons']),
                "firstSeason": int(request.form['firstSeason']),
                "lastSeason": int(request.form['lastSeason']),
                "careerEnded": int(request.form['careerEnded']),
                "yrsRetired2004": int(request.form['yrsRetired2004']),
                "Points_Per_Game": float(request.form['Points_Per_Game']),
                "Assists_Per_Game": float(request.form['Assists_Per_Game']),
                "Rebounds_Per_Game": float(request.form['Rebounds_Per_Game']),
                "Blocks_Per_Game": float(request.form['Blocks_Per_Game']),
                "Steals_Per_Game": float(request.form['Steals_Per_Game']),
                "Minutes_Per_Game": float(request.form['Minutes_Per_Game']),
                "Career_Length_Years": int(request.form['Career_Length_Years']),
                "Field_Goal_Percentage": float(request.form['Field_Goal_Percentage']),
                "Free_Throw_Percentage": float(request.form['Free_Throw_Percentage']),
                "Center Position": 'Center Position' in request.form,
                "Forward Position": 'Forward Position' in request.form,
                "Guard Position": 'Guard Position' in request.form
            }
            result = predict(player)
            return result
        except Exception as e:
            return jsonify({'error': str(e)})
    return '''
            <form method="post">
                League: <input type="text" name="league" value="1"><br>
                Games: <input type="text" name="games" value="964"><br>
                Minutes: <input type="text" name="minutes" value="35875"><br>
                Points: <input type="text" name="pts" value="14437"><br>
                Offensive Rebounds: <input type="text" name="offReb" value="744"><br>
                Defensive Rebounds: <input type="text" name="defReb" value="1827"><br>
                Total Rebounds: <input type="text" name="reb" value="14464"><br>
                Assists: <input type="text" name="asts" value="2575"><br>
                Steals: <input type="text" name="stl" value="125"><br>
                Blocks: <input type="text" name="blk" value="553"><br>
                Turnovers: <input type="text" name="turnover" value="0"><br>
                Personal Fouls: <input type="text" name="pf" value="2624"><br>
                Field Goals Attempted: <input type="text" name="fga" value="13105"><br>
                Field Goals Made: <input type="text" name="fgm" value="5521"><br>
                Free Throws Attempted: <input type="text" name="fta" value="5089"><br>
                Free Throws Made: <input type="text" name="ftm" value="3395"><br>
                Three-Point Attempts: <input type="text" name="tpa" value="0"><br>
                Three-Point Made: <input type="text" name="tpm" value="0"><br>
                Total Seasons: <input type="text" name="totalSeasons" value="14"><br>
                First Season: <input type="text" name="firstSeason" value="1963"><br>
                Last Season: <input type="text" name="lastSeason" value="1976"><br>
                Career Ended: <input type="text" name="careerEnded" value="1"><br>
                Years Retired (as of 2004): <input type="text" name="yrsRetired2004" value="28"><br>
                Points Per Game: <input type="text" name="Points_Per_Game" value="14.976141"><br>
                Assists Per Game: <input type="text" name="Assists_Per_Game" value="2.671162"><br>
                Rebounds Per Game: <input type="text" name="Rebounds_Per_Game" value="15.004149"><br>
                Blocks Per Game: <input type="text" name="Blocks_Per_Game" value="0.573651"><br>
                Steals Per Game: <input type="text" name="Steals_Per_Game" value="0.129668"><br>
                Minutes Per Game: <input type="text" name="Minutes_Per_Game" value="37.21473"><br>
                Career Length (Years): <input type="text" name="Career_Length_Years" value="13"><br>
                Field Goal Percentage: <input type="text" name="Field_Goal_Percentage" value="0.42129"><br>
                Free Throw Percentage: <input type="text" name="Free_Throw_Percentage" value="0.667125"><br>
                Position (check all that apply):<br>
                Center: <input type="checkbox" name="Center Position" checked><br>
                Forward: <input type="checkbox" name="Forward Position"><br>
                Guard: <input type="checkbox" name="Guard Position"><br>
                <input type="submit" value="Submit">
            </form>
    '''


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)



"""
import pickle
import pandas as pd
from flask import Flask, request, render_template_string, jsonify

app = Flask(__name__)

output_file = 'model_rfc.bin'

with open(output_file, 'rb') as f_in:
    rf_model = pickle.load(f_in)

def predict():
    player = request.get_json()

    player_row_df = pd.DataFrame([player])
    soft_prediction_for_player = rf_model.predict_proba(player_row_df)[0,1]
    hard_prediction_for_player = soft_prediction_for_player >= 0.5

    result = {
        'Probability of NBA player entering the Hall of Fame': soft_prediction_for_player,
        'Will player enter into Hall of Fame soon?': hard_prediction_for_player
    }

    return jsonify(result)


@app.route('/name', methods=['GET', 'POST'])
def average():
    if request.method == 'POST':
        try:
            predict()
            value1 = float(request.form['value1'])
            value2 = float(request.form['value2'])
            value3 = float(request.form['value3'])
            average = (value1 + value2 + value3) / 3
            return f"The average is {average}"
        except ValueError:
            return "Please enter valid numbers."
    return '''
        <form method="post">
            Value 1: <input type="text" name="value1"><br>
            Value 2: <input type="text" name="value2"><br>
            Value 3: <input type="text" name="value3"><br>
            <input type="submit" value="Calculate Average">
        </form>
    '''

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)


"""
