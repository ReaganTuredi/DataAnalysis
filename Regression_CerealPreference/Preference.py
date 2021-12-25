import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
#importing data
cereal=pd.read_excel('cereal.xlsx',skiprows=[1],usecols=[0,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
ratings=cereal['rating']
cereal_max=(cereal['name'].max(),cereal['rating'].max())
cereal_min=(cereal['name'].min(),cereal['rating'].min())
cereal_median=(ratings.median())
cereal_mean=(ratings.mean())
print('The max ratings is',cereal_max,'The min rating is',cereal_min,'The median rating is',cereal_median,'The mean rating is',cereal_mean)
sns.distplot(ratings).set(xlabel='ratings',ylabel='frequency',title='Distribution of cereal ratings')


#Dropping bad rows 
bad_rows=[]
for index, row in cereal.iterrows():
    for i in row:
        if i==-1:
            bad_rows.append(index)
bad_rows
cereal.drop(index=[4,20,57])

#Plot + heatmap
correlation=cereal.corr(method='pearson')
plt.figure(figsize=(20,5))
sns.heatmap(correlation,annot=True)


b, t = plt.ylim()
b += 0.5 
t -= 0.5
plt.ylim(b, t)
plt.show()

#creating the model 
fiber=cereal['fiber']
x=ratings
y=fiber
parameters=np.polyfit(x,y,1)
poly_function = np.poly1d(parameters)
y_predict=poly_function(x)
plt.scatter(x,y)
plt.plot(x,y_predict,color='r')
plt.xlabel('ratings')
plt.ylabel('fiber')
plt.title('Ratings vs. Fiber')
print('the respective slope and intercepts are',parameters)

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
x1=cereal['rating']
x1=x1.values.reshape(-1,1)

X_train = x1[:-20]
X_test = x1[-20:]

y_train = y[:-20]
y_test = y[-20:]

regr = linear_model.LinearRegression()

regr.fit(X_train, y_train)

y_predict = regr.predict(X_test)

print('Coefficients: \n', regr.coef_)

print('Mean squared error: %.2f'
      % mean_squared_error(y_test, y_predict))

print('Coefficient of determination: %.2f'
      % r2_score(y_test,y_predict))


plt.scatter(X_test, y_test,  color='black')
plt.plot(X_test, y_predict, color='blue', linewidth=2,label='regression line')
plt.xlabel('ratings')
plt.ylabel('fiber')
plt.title('Ratings vs. Fiber with linreg line')
plt.legend()
plt.show()


