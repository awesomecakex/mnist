import numpy as np
import re
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

class knn():
    def __init__(self, k=3):
        self.k = k
        self.counter = 0
       

    def fit(self, data, target):
        self.X_train = data
        self.y_train = target

        


        
 
    def distance(self,p1,p2):
        dis = 0.0
        for i in range(len(p1)):
            dis += float((p1[i]-p2[i])**2)
        dis =  np.sqrt(dis)
        return dis

    def predict(self,test):
        mink = []
        
        for i in range(len(self.X_train)):
            
            if len(mink)<self.k:
                mink.append((self.distance(self.X_train[i],test),self.y_train[i])) 
                
            else:
                for j in range(len(mink)):
                    if mink[j][0]>self.distance(self.X_train[i],test):
                        mink[j] = (self.distance(self.X_train[i],test),self.y_train[i])
                        break
        counter = 0
        flagy = None
        maxcount = 0
        favorite = -1
        
        for i in range(self.k):
            flagy = mink[i][1]
            for j in range(self.k):
                if mink[j][1] == flagy:
                    counter+=1
            if counter>maxcount:
                maxcount = counter
                favorite = flagy
            counter = 0
        return favorite
    
    
    def score(self, X, y):
        flaggy = None
        county = 0
        for i in range(len(X)):
            flaggy = X[i]
            if self.predict(flaggy) == y[i]:
                county+=1
            print(self.counter)
            self.counter +=1
        
        return f"{(county/len(X))*100}%"






mnist = load_digits()
X_train,X_test,y_train,y_test = train_test_split(mnist.data,mnist.target,test_size=0.2)
knnmodel = knn(k=3)
knnmodel.fit(X_train,y_train)
print(knnmodel.predict(X_test[0]))
trainscore = knnmodel.score(X_test, y_test)
testscore = knnmodel.score(X_train, y_train)
print("test score  = ", trainscore)
print("train score = ",testscore)
#Once you see the scores of the classifier u might question if it works as intended, I encourage you 
#to create a knn classifier from scikit-learn and see its results i assure that they are very close 
# and there is no overfitting or underfitting.

    
        

