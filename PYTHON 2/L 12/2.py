import pandas

from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    f1_score,
    accuracy_score,
)
import matplotlib.pyplot as plt

data = pandas.read_csv("reviews.csv")
print(data)
X = data["label"]
y = data["product"]
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)
vec = CountVectorizer()
vec = TfidfVectorizer()
X_train = vec.fit_transform(X_train)
#print(X_train.shape)
X_test = vec.transform(X_test)
clf = LinearSVC()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
ConfusionMatrixDisplay.from_estimator(
    clf,
    X_test,
    y_test,
)
# plt.show()
# print(accuracy_score(y_test, y_pred))
df_coef = pandas.DataFrame(clf.coef_.T, columns=clf.classes_)
df_coef["label"] = vec.get_feature_names_out()
print(df_coef.sort_values("label", ascending=True).head(20))