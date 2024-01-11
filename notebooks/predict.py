import pickle
import pandas as pd

output_file = 'model_rfc.bin'

with open(output_file, 'rb') as f_in:
    rf_model = pickle.load(f_in)

player1 = {
    'league': 1,
    'games': 964,
    'minutes': 35875,
    'pts': 14437,
    'offReb': 744,
    'defReb': 1827,
    'reb': 14464,
    'asts': 2575,
    'stl': 125,
    'blk': 553,
    'turnover': 0,
    'pf': 2624,
    'fga': 13105,
    'fgm': 5521,
    'fta': 5089,
    'ftm': 3395,
    'tpa': 0,
    'tpm': 0,
    'totalSeasons': 14,
    'firstSeason': 1963,
    'lastSeason': 1976,
    'careerEnded': 1,
    'yrsRetired2004': 28,
    'Points_Per_Game': 14.976141,
    'Assists_Per_Game': 2.671162,
    'Rebounds_Per_Game': 15.004149,
    'Blocks_Per_Game': 0.573651,
    'Steals_Per_Game': 0.129668,
    'Minutes_Per_Game': 37.21473,
    'Career_Length_Years': 13,
    'Field_Goal_Percentage': 0.42129,
    'Free_Throw_Percentage': 0.667125,
    'Center Position': True,
    'Forward Position': False,
    'Guard Position': False
}

def predict(player):
    player_row_df = pd.DataFrame([player])
    soft_prediction_for_player = rf_model.predict_proba(player_row_df)[0,1]
    return soft_prediction_for_player

prediction = predict(player1)
print(f'\nProbability of NBA player entering the Hall of Fame:\n{prediction}')

for key, value in player1.items():
    print(f"{key}: {type(value)}")