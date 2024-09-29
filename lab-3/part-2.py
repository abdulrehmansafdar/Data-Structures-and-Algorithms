import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Train.csv')
symptoms = df.columns[:-1]
print(df.dtypes)
plt.figure(figsize=(20, 10))
for symptom in symptoms:
    plt.scatter(df[symptom], df['TYPE'], label=symptom)

plt.xlabel('Symptom')
plt.ylabel('Type')
plt.title('Scatter Plot of Symptoms vs Type')
plt.legend()

plt.show()