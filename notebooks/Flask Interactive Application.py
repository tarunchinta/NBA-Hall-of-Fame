import pickle
import pandas as pd
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

output_file = 'model_rfc.bin'
 
with open(output_file, 'rb') as f_in:
    rf_model = pickle.load(f_in)

def predict(player):
    player_row_df = pd.DataFrame([player])
    soft_prediction_for_player = rf_model.predict_proba(player_row_df)[0,1]
    hard_prediction_for_player = soft_prediction_for_player >= 0.5

    result = f'Probability of NBA player entering the Hall of Fame: {soft_prediction_for_player}<br><br>Player will likely enter into Hall of Fame soon?: {bool(hard_prediction_for_player)}'
    
    return result

@app.route('/')
def home():
    return f'{app.template_folder}'
    #render_template('index.html')

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
                "totalSeasons": int(int(request.form['lastSeason'])-int(request.form['firstSeason'])+1),
                "firstSeason": int(request.form['firstSeason']),
                "lastSeason": int(request.form['lastSeason']),
                "careerEnded": int(request.form['careerEnded']),
                "yrsRetired2004": int(2004 - int(request.form['lastSeason'])),
                "Points_Per_Game": float(int(request.form['pts'])/int(request.form['games'])),
                "Assists_Per_Game": float(int(request.form['asts'])/int(request.form['games'])),
                "Rebounds_Per_Game": float((int(request.form['reb']))/int(request.form['games'])),
                "Blocks_Per_Game": float(int(request.form['blk'])/int(request.form['games'])),
                "Steals_Per_Game": float(int(request.form['stl'])/int(request.form['games'])),
                "Minutes_Per_Game": float(int(request.form['minutes'])/int(request.form['games'])),
                "Career_Length_Years": int(request.form['Career_Length_Years']),
                "Field_Goal_Percentage": float(int(request.form['fgm'])/int(request.form['fga'])),
                "Free_Throw_Percentage": float(int(request.form['ftm'])/int(request.form['fta'])),
                "Center Position": request.form.get('position') == 'Center',
                "Forward Position": request.form.get('position') == 'Forward',
                "Guard Position": request.form.get('position') == 'Guard',
            }
            result = predict(player)
 
            player_data = "<br>".join([f"{key}: {value}" for key, value in player.items()])

            combined_response = f"<h1>Prediction Result:</h1><br>{result}<br><br><h1>Player Data:</h1><br>{player_data}"
            return combined_response

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
                First Season: <input type="text" name="firstSeason" value="1963"><br>
                Last Season: <input type="text" name="lastSeason" value="1976"><br>
                Career Ended: <input type="text" name="careerEnded" value="1"><br>
                Career Length (Years): <input type="text" name="Career_Length_Years" value="13"><br>
                Position:<br>
                Center: <input type="radio" name="position" value="Center" checked><br>
                Forward: <input type="radio" name="position" value="Forward"><br>
                Guard: <input type="radio" name="position" value="Guard"><br>
                <input type="submit" value="Submit">
            </form>
    '''


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)
    
