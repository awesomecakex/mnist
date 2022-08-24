import numpy as np
import re
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
 
class knn():
    def __init__(self, k=3):
        self.k = k
        self.counter = 0
       

    def fit(self, data, target):
        self.X = data
        self.Y = target
    

    
    def distance(self,p1,p2):
        dis = 0.0
        for i in range(len(p1)):
            dis += float((p1[i]-p2[i])**2)
        dis =  np.sqrt(dis)
        return dis

    def predict(self,test):
        mink = []
        
        for i in range(len(self.X)):
            if len(mink)<self.k:
                mink.append((self.distance(self.X[i],test),self.Y[i])) 
                
            else:
                for j in range(len(mink)):
                    if mink[j][0]>self.distance(self.X[i],test):
                        mink[j] = (self.distance(self.X[i],test),self.Y[i])
                        break
            
        
        counter = 0
        flagy = None
        maxcount = 0
        favorite = -1
        
        for i in range(self.k):
            flagy = mink[i][1]
            for j in range(self.k):
                if mink[i][1] == flagy:
                    counter+=1
            if counter>maxcount:
                maxcount = counter
                favorite = flagy
            counter = 0
        return favorite
    

    def score(self):
        flaggy = None
        counter = 0
        for i in range(len(self.X)):
            flaggy = self.X[i]
            self.predict(flaggy)
            if self.predict(flaggy) == self.Y[i]:
                counter+=1
            print(self.counter)
            self.counter +=1
        
        return f"{(counter/len(self.X))*100}%"






mnist = load_digits()
knnmodel = knn(k=5)
knnmodel.fit(mnist.data,mnist.target)
print(knnmodel.predict(mnist.data[2]))
print(knnmodel.score())

            
            
    
        

