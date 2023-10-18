# -*- coding: utf-8 -*-
"""Titanic survival prediction-Task1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LgW0QUp4JB9x7H8KPxmaykqAUeS_ekg8
"""

import pandas as pd

titanic= pd.read_csv('train.csv')

titanic.shape

test = pd.read_csv('test.csv')
test.shape

titanic.head()

titanic.info()

ports = pd.get_dummies(titanic.Embarked,prefix = 'Embarked')
ports.head()

titanic = titanic.join(ports)
titanic.drop(['Embarked'],axis = 1,inplace = True)

titanic.head()

titanic.Sex = titanic.Sex.map({'male':0, 'female':1})

y = titanic.Survived.copy()
x = titanic.drop(['Survived'], axis = 1)

x.drop(['Cabin','Ticket','Name','PassengerId'], axis = 1, inplace = True)

x.info()

x.isnull().values.any()

x[pd.isnull(x).any(axis = 1)]

x.Age.fillna(x.Age.mean(),inplace = True)

x.isnull().values.any()

from sklearn.model_selection import train_test_split
x_train,x_valid,y_train,y_valid = train_test_split(x,y, test_size = 0.2, random_state = 7)

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()

model.fit(x_train,y_train)

model.score(x_train,y_train)

model.score(x_valid,y_valid)