import pandas as pd
from sklearn.ensemble import RandomForestClassifier

Datos ejemplo

data = {
'time_on_platform': [5, 15, 7, 20],
'clicks': [2, 10, 3, 15],
'visits': [1, 5, 2, 7],
'converted': [0, 1, 0, 1]
}

df = pd.DataFrame(data)

X = df[['time_on_platform', 'clicks', 'visits']]
y = df['converted']

model = RandomForestClassifier()
model.fit(X, y)

print("Modelo entrenado correctamente")
