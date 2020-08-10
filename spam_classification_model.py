import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import svm
from sklearn.model_selection import train_test_split

df = pd.read_excel("Email_data.xlsx")

df = df[["Label", "Text"]]

X = df["Text"]
y = df["Label"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

cv = CountVectorizer()
features = cv.fit_transform(X_train)

pickle.dump(cv, open("transform.pkl", "wb"))

model = svm.SVC()
model.fit(features, y_train)

pickle.dump(model, open("spam_classification_model.pkl", "wb"))
