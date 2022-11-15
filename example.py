from cmplot import cmplot
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LogisticRegression

# force binomial classification - class '0' or class 'not 0'
X, y = load_iris(return_X_y=True, as_frame=True)
y = y.map({0: 0, 1: 1, 2: 1})

# train on only one variable
clf = LogisticRegression(random_state=0).fit(
    X[['sepal width (cm)']], y)
y_pred = clf.predict(X[['sepal width (cm)']])


# create confusion matrix
cm = confusion_matrix(y, y_pred, labels=[0, 1])

# plot
cmplot(cm)
