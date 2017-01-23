import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs, make_circles
from keras.utils import np_utils

from keras.models import Sequential
from keras.layers import Dense, Activation

X, y = make_blobs(n_samples=1000,
                  centers=[[0.1, 0.1],[0.9, 0.9]],
                  cluster_std=0.3,
                  n_features=2)

y = np_utils.to_categorical(y)

#plt.scatter(X[:,0], X[:,1], c=y[:,0], alpha=0.4)
#plt.show()

model=Sequential()
model.add(Dense(2, input_dim=2))
model.add(Activation('sigmoid'))
model.summary()

from keras.optimizers import SGD

model.compile(loss='categorical_crossentropy',optimizer=SGD(lr=0.04), metrics=['accuracy'])
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y)
model.fit(X_train, y_train, nb_epoch=20, batch_size=16)
result = model.evaluate(X_test, y_test)
print 'Test set loss: ', result[0]
print 'Test set accuracy: ', result[1]


def plot_decision_boundary(model, X, y):
    X_max = X.max(axis=0)
    X_min = X.min(axis=0)
    xticks = np.linspace(X_min[0], X_max[0], 100)
    yticks = np.linspace(X_min[1], X_max[1], 100)
    xx, yy = np.meshgrid(xticks, yticks)
    ZZ = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = ZZ[:,0] >= 0.5
    Z = Z.reshape(xx.shape)
    fig, ax = plt.subplots()
    ax = plt.gca()
    ax.contourf(xx, yy, Z, cmap=plt.cm.bwr, alpha=0.2)
    ax.scatter(X[:,0], X[:,1], c=y[:,0], alpha=0.4)

plot_decision_boundary(model, X, y)
plt.show()
