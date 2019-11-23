import pandas as pd

cars = pd.read_csv('cars.csv')

a = cars.iloc[0:5, 1:10:2]
b = cars[cars['Model'] == 'Mazda RX4']
c = cars.loc[cars['Model'] == 'Camaro Z28', ['cyl']]
d = cars.loc[[1, 28, 18], ['cyl', 'gear']]