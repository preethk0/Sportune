# -*- coding: utf-8 -*-
"""Model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1StmP2btiXfDvYtXDGqBvleYhESA0_tSd
"""

from google.colab import drive
drive.mount('/content/drive')

import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

filepath = "/content/drive/My Drive/Data Analysis Teams/Contract Pricing/Datasets/MAIN Dataset/player_numeric_data.csv"
data = np.genfromtxt(filepath, delimiter=',', dtype='float64')

scaler = MinMaxScaler(feature_range=[0, 1])
data_rescaled = scaler.fit_transform(data[1:, 0:34])

#Fitting the PCA algorithm with our Data
pca = PCA().fit(data_rescaled)
#Plotting the Cumulative Summation of the Explained Variance
plt.figure()
plot = plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Number of Components')
plt.ylabel('Variance (%)') #for each component
plt.title('Salary Dataset Explained Variance')
plt.show()

import pickle
pickle.dump(pca, open('/content/drive/My Drive/Data Analysis Teams/Contract Pricing/pca.sav', 'wb'))

xvalues = plot[0].get_xdata()
yvalues = plot[0].get_ydata()
i = 0
while yvalues[i] <= .99:
  i += 1
  
i

"""PCA with 20 components seems best (preserves 99% of variance)"""

pca = PCA(n_components=20)
dataset = pca.fit_transform(data_rescaled)

#create model
from sklearn.linear_model import LinearRegression

model = LinearRegression()

filepath = "/content/drive/My Drive/Data Analysis Teams/Contract Pricing/Datasets/MAIN Dataset/only_salaries.csv"
salaries = np.genfromtxt(filepath, delimiter=',', dtype='float64')[1:]

pd.DataFrame(salaries).isna()

model.fit(dataset, salaries)

r_sq = model.score(dataset, salaries)
r_sq

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree=3)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(dataset, salaries, test_size=0.2)

x_train = poly.fit_transform(x_train)
x_test = poly.fit_transform(x_test)

model = LinearRegression()
model.fit(x_train, y_train)

r_sq = model.score(x_train, y_train)
r_sq

y_pred = model.predict(x_test)
y_pred

y_test

from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred)

nba_data = pd.read_csv("/content/drive/My Drive/Data Analysis Teams/Contract Pricing/Datasets/MAIN Dataset/nba_players_independent.csv")
x = pca.fit_transform(nba_data.drop(columns = ['Player', 'Tm', 'Unnamed: 0']))
y = salaries
def build_model (x, y):
  poly = PolynomialFeatures(degree=3)
  x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
  x_train = poly.fit_transform(x_train)
  x_test = poly.fit_transform(x_test)
  model = LinearRegression()
  model.fit(x_train, y_train)
  print(x_test.shape)
  print(model.predict(x_test))
  print(model.score(x_train, y_train))
  return model

model = build_model (x, y)
def predict_salary (model, x):
  return model.predict(x)

import pickle
pickle.dump(model, open('/content/drive/My Drive/Data Analysis Teams/Contract Pricing/model.sav', 'wb'))

def predict_nba (model, name, year = None):
  poly = PolynomialFeatures(degree=3)
  rows = nba_data.loc[nba_data['Player'] == name]
  rows.drop(columns = ['Player', 'Tm', 'Unnamed: 0'], inplace = True)
  year = max (rows['season_start']) if year == None else year
  row = rows.loc[rows['season_start'] == year]
  row = row.head(1)
  vals = row.values
  vals = pca.transform(vals)
  vals = poly.fit_transform(vals)
  vals = np.reshape(a=vals, newshape= (1, -1))
  print(row.values)
  return predict_salary(model, vals)[0]

predict_nba(model, 'Seth Curry', 2017)

def predict_from_stats (model, stats):
  poly = PolynomialFeatures(degree=3)
  vals = [stats]
  vals = pca.transform(vals)
  vals = poly.fit_transform(vals)
  vals = np.reshape(a=vals, newshape= (1, -1))
  return predict_salary(model, vals)[0]

loaded_model = pickle.load(open('/content/drive/My Drive/Data Analysis Teams/Contract Pricing/model.sav', 'rb'))
model.score(x_test, y_test)

predict_nba (loaded_model, 'Kevin Durant')

predict_nba(loaded_model, 'Terry Rozier')

predict_nba(loaded_model, 'Karl-Anthony Towns', 2017)

predict_nba(loaded_model, 'Chandler Parsons', 2016)

predict_nba(loaded_model, 'Luol Deng', 2016)

predict_from_stats(loaded_model, row.values[0])

predict_nba(loaded_model, 'LeBron James', 20)