#importing dependencies
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
%matplotlib inline

#using pandas to read the database stored in the same folder
data = pd.read_csv('https;//query.data.world/s/z2i77f6nei7fiotnb63sbacfu6zlfw')

#viewing column heads
data.head()

#extracting data from the dataset and viewing it up close
a = data.iloc[3,:].values
#reshaping the extracted data into a reasonable size
a = a.reshape(28,28)
plt.imshow(a)

#preparing the data
#seperating labels and data values
df_x = data.iloc[:,1:]
df_y = data.iloc[:,0]

#creating test and train sizes/batches
x_train, x_test, y_train, y_test = train_test_split(df_x, df_y,test_size = 0.2, random_state = 4)
#check data
y_train.head()

#call the classifier
rf = RandomForestClassifier(n_estimators = 100)
#fit the model
rf.fit(x_train, y_train)
#prediction on the test data
pred = rf.predict(x_test)
print(pred)

#check prediction accuracy
s = y_test.values
#calculate the number of accurately predicted values
count =0
for i in range(len(pred)):
    if pred[i] == s[i]:
        count = count +1
print(count)

#total values that the prediction code was run on
print(len(pred))
#accuracy
count/len(pred)



