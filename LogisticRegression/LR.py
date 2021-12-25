import pandas as pd
import matplotlib.pyplot as plt
from sklearn import metrics 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('Olympic.csv')
df= df.drop(columns=['Athletes'])
df=df.drop([18,28])

#Making the total ascending
df['Total']=df['Total'].astype(float)
df.sort_values(by=['Total'], inplace=True)
#just for viewing
df.hist()

# Sorting by most gold medals. If equal gold medals, then most silver. If equal gold and silver, then most bronze.
df['Gold']=df['Gold'].astype(float)
df['Silver']=df['Silver'].astype(float)
df['Bronze']=df['Bronze'].astype(float)
df.sort_values(['Gold','Silver','Bronze'], ascending=[False, False,False],inplace=True)

#Logistic Regression Implementation
game_list=np.arange(1896,2019,4)
game_list=np.delete(game_list,(3,9,10,19))
years=pd.DataFrame(game_list)

gold_in=df["Gold"]
gold_in = (gold_in > 37.0) 
gold_binary=pd.DataFrame(gold_in)
gold_binary=gold_binary.astype(int)

X_train, X_test, y_train, y_test = train_test_split(years, gold_binary, test_size=0.25)
print(X_test)
print(y_test)

logreg = LogisticRegression()
logreg.fit(X_train,y_train)
y_pred = logreg.predict(X_test)

