import numpy as np
import re
 
class knn():
    def __init__(self, k=3):
        self.k = k

    
    def distance(self,p1,p2):
        dis = 0.0
        for i in range(len(p1)):
            dis += float((p1[i]-p2[i])**2)
        dis =  np.sqrt(dis)
        return dis

    def predict(self,data,target,test):
        mink = []
        for i in range(len(data)):
            if len(mink)<self.k:
                mink.append((self.distance(data[i],test),target[i])) 
                
            else:
                for j in range(len(mink)):
                    if mink[j][0]>self.distance(data[i],test):
                        mink[j] = (self.distance(data[i],test),target[i])
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
            
                

            
            
    
        

