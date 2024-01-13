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

    return {"probability": soft_prediction_for_player, "hall_of_fame_soon": hard_prediction_for_player}

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
                "Points_Per_Game": float(int(request.form['pts'])/int(request.form['games'])) if int(request.form['games']) != 0 else 0.0,
                "Assists_Per_Game": float(int(request.form['asts'])/int(request.form['games'])) if int(request.form['games']) != 0 else 0.0,
                "Rebounds_Per_Game": float((int(request.form['reb']))/int(request.form['games'])) if int(request.form['games']) != 0 else 0.0,
                "Blocks_Per_Game": float(int(request.form['blk'])/int(request.form['games'])) if int(request.form['games']) != 0 else 0.0,
                "Steals_Per_Game": float(int(request.form['stl'])/int(request.form['games'])) if int(request.form['games']) != 0 else 0.0,
                "Minutes_Per_Game": float(int(request.form['minutes'])/int(request.form['games'])) if int(request.form['games']) != 0 else 0.0,
                "Career_Length_Years": int(request.form['Career_Length_Years']),
                "Field_Goal_Percentage": float(int(request.form['fgm'])/int(request.form['fga'])) if int(request.form['fga']) != 0 else 0.0,
                "Free_Throw_Percentage": float(int(request.form['ftm'])/int(request.form['fta'])) if int(request.form['fta']) != 0 else 0.0,
                "Center Position": request.form.get('position') == 'Center',
                "Forward Position": request.form.get('position') == 'Forward',
                "Guard Position": request.form.get('position') == 'Guard',
            }
            result = predict(player)
 
            player_data = "<br>".join([f"{key}: {value}" for key, value in player.items()])

            #combined_response = f"<h1>Prediction Result:</h1><br>{result}<br><br><h1>Player Data:</h1><br>{player_data}"
            return render_template('prediction_result.html', result=result, player=player)


        except Exception as e:
            return jsonify({'error': str(e)})
        
    return render_template('predict.html')

@app.route('/contact')
def contact():
    try:
        return render_template('contact.html')
    except Exception as e:
            return jsonify({'error': str(e)})
            
@app.route('/')
def home():
    try:
        return render_template('index.html')
    except Exception as e:
            return jsonify({'error': str(e)})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)