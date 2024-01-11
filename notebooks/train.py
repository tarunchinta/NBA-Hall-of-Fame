import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

import pickle

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error,mean_absolute_error,r2_score, accuracy_score, classification_report

from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
import xgboost as xgb

#READING DATA

#What Does it Take for an NBA player to get into the NBA Hall of Fame?

file_path = '../data/Hall-of-fame-train.csv'

df = pd.read_csv(file_path)

#Feature Engineering

"""
Let's create features by dividing features such as points by the number of games the player played. 
The intuition is that capturing the average proportion of points per game would be useful in gauging the ability of a player.
"""

df['Points_Per_Game'] = df['pts'] / df['games']
df['Assists_Per_Game'] = df['asts'] / df['games']
df['Rebounds_Per_Game'] = df['reb'] / df['games']
df['Blocks_Per_Game'] = df['blk'] / df['games']
df['Steals_Per_Game'] = df['stl'] / df['games']
df['Minutes_Per_Game'] = df['minutes'] / df['games']
df['Career_Length_Years'] = df['lastSeason'] - df['firstSeason']

"""
Let's also create Field Goal Percentage and Free Throw Percentage which would be the field goals made divided by the field goals attempted.
"""

df['Field_Goal_Percentage'] = (df['fgm'] / df['fga']).fillna(0)
df['Free_Throw_Percentage'] = (df['ftm'] / df['fta']).fillna(0)


#print(df.columns)
#print(df.head())
#print(df['league'].unique())

# N = National Basketball Association (NBA); A = American Basketball Association (ABA)
# Convert string to integers

df['league'] = np.where(df['league'] == 'N', 1, 0)
df['league'] = df['league'].astype(int)

# Create dummy variables for each unique value in 'Position'
dummies = pd.get_dummies(df['Position'])
df = pd.concat([df, dummies], axis=1)

# Rename column 'C' to 'Center'
df.rename(columns={'C': 'Center Position', 'F': 'Forward Position', 'G': 'Guard Position'}, inplace=True)
df.drop(['Position'], axis=1, inplace=True)

#Split Training and Testing Data

#20% for testing
y = df['class']
X = df.drop('class',axis = 1)

X_train, X_test, y_train, y_test = train_test_split(X,y, 
                                                    test_size = 0.2, 
                                                    random_state = 123
                                                   )

#Trying various models

#Decision Tree

#Random Forest

# Step 2: Instantiate the RandomForestClassifier
rf_model = RandomForestClassifier(random_state=123)

# Step 3: Fit the model to the training data
rf_model.fit(X_train, y_train)

# Step 4: Make predictions on the test data
y_pred = rf_model.predict(X_test)

# Step 5: Evaluate the model's performance
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Classification Report:\n", report)

#Pickling the model

output_file = 'model_rfc.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump(rf_model, f_out)

