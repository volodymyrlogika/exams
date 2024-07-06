import pandas as pd

df = pd.read_csv('StudentsPerformance .csv')

df.info()

# Середня оцінка з Математики
mean_math = df['math score'].mean()
print(mean_math)