import pickle


pkl_filename = "pickle_model.pkl"
with open(pkl_filename, 'rb') as file:
    clf = pickle.load(file)


def predict(temperature, pulse):
    return clf.predict([[temperature, pulse]])
