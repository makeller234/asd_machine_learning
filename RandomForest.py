from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import tree
import pandas as pd
import numpy as np
from flask import Flask
import os


app = Flask(__name__)
@app.route("/")
def ASDdeterminor():

    file = os.path.join("Autism_Data_Adult_Version-2.csv")
    asdDF = pd.read_csv(file)

    X = asdDF[["A1", "A2", "A3","A4","A5", "A6", "A7", "A8", "A9", "A10"]]
    y = asdDF["Class"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X_train, y_train)
    clf_score = clf.score(X_test, y_test)


    rf = RandomForestClassifier(n_estimators=200)
    rf = rf.fit(X_train, y_train)
    rf_train_score = rf.score(X_train, y_train)
    rf_test_score = rf.score(X_test, y_test)

    # print(f'Training Score: {rf_train_score}')
    # print(f'Testing Score: {rf_test_score}')

    importances = rf.feature_importances_
    sorted(zip(rf.feature_importances_, X), reverse=True)

    testing1 = input("I often notice small sounds when others do not ")
    testing2 = input("I usually concentrate mre on the whole picture, rather than the small details ")
    testing3 = input("I find it easy to do more than one thing at a time ")
    testing4 = input("If there is an interruption, I can switch back to what I was doing very quickly ")
    testing5 = input("I find it easy to read between the lines when someone is talking to me ")
    testing6 = input("I know how to tell if someone listening to me is getting bored ")
    testing7 = input("When I’m reading a story I find it difficult to work out the characters’ intentions ")
    testing8 = input("I like to collect information about categories of things (e.g. types of car, types of bird, types of train, and types of plant) ")
    testing9 = input("I find it easy to work out what someone is thinking or feeling just by looking at their face ")
    testing10 = input("I find it difficult to work out people’s intentions ")

    user_test = np.array([testing1, testing2, testing3, testing4, testing5, testing6, testing7, testing8, testing9, testing10])
    user_test = np.reshape(user_test, (-1,user_test.size))
    user_result = rf.predict(user_test)

    return(user_result[0])


if __name__ == "__main__":
    app.run(debug=True)