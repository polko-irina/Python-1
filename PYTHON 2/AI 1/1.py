import pandas
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, precision_score, accuracy_score

data = pandas.read_csv("PYTHON 2/AI 1/wine.csv")
print(data.head())

X = data.drop(columns="quality")
y = data["quality"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

clf = KNeighborsClassifier()
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
# ConfusionMatrixDisplay.from_estimator(clf, X_test, y_test)
# plt.show()

# print(precision_score(y_test, y_pred, pos_label="good"))

ks = range(1, 31, 2)
accuracy_scores = []
for k in ks:
    clf = KNeighborsClassifier(n_neighbors=k)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    accuracy_scores.append(accuracy_score(y_test, y_pred))
plt.plot(ks, accuracy_scores)
plt.show()
