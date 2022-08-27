import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold

mnist = load_digits()


class Knn:
    def __init__(self, k=3):
        self.k = k
        self.counter = 0
        self.dis = 0.0
        self.X = mnist.data
        self.y = mnist.target
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X, self.y, test_size=0.2)
        self.prediction = None

    def fit(self):
        self.X_train = self.X
        self.y_train = self.y

    def kfold(self, cv=5):
        kf = KFold(n_splits=cv)
        kf.get_n_splits(self.X)
        count = 0
        cvnum = 1
        cvarr = []
        for train_index, test_index in kf.split(self.X):
            self.fit(self.X[train_index], self.y[train_index])
            count += self.score(self.X[test_index], self.y[test_index])
            cvarr.append(f"score for validation portion {cvnum} : {self.score(self.X[test_index], self.y[test_index])}")
            cvnum += 1
        for i in range(len(cvarr)):
            print(cvarr[i])
        return count / cv

    def distance(self, p1, p2):
        self.dis = 0.0
        for i in range(len(p1)):
            self.dis += float((p1[i] - p2[i]) ** 2)
        self.dis = np.sqrt(self.dis)
        return self.dis

    def predict(self, test):
        mink = []
        for i in range(len(self.X_train)):
            if len(mink) < self.k:
                mink.append((self.distance(self.X_train[i], test), self.y_train[i]))
            else:
                for j in range(len(mink)):
                    if mink[j][0] > self.distance(self.X_train[i], test):
                        mink[j] = (self.distance(self.X_train[i], test), self.y_train[i])
                        break
        counter = 0
        flagy = None
        maxcount = 0
        favorite = -1

        for i in range(self.k):
            flagy = mink[i][1]
            for j in range(self.k):
                if mink[j][1] == flagy:
                    counter += 1
            if counter > maxcount:
                maxcount = counter
                favorite = flagy
            counter = 0
        return favorite

    def score(self):
        flaggy = None
        county = 0
        for i in range(len(self.X)):
            flaggy = self.X[i]
            if self.predict(flaggy) == self.y[i]:
                county += 1
            print(self.counter)
            self.counter += 1
        return (county / len(self.X)) * 100


# -------------------------------------
# Once you see the scores of the classifier u might question if it works as intended, I encourage you
# to create a knn classifier from scikit-learn and see its results i assure that they are very close
# and there is no overfitting or underfitting.
# -------------------------------------
# from sklearn.neighbors import KNeighborsClassifier

# knnmod = KNeighborsClassifier(n_neighbors=3)
# knnmod.fit(X_train,y_train)

# print("sklearn model", knnmod.predict(X_test[20].reshape(1,-1)))
