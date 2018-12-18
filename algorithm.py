import pickle


pkl_filename = "pickle_model.pkl"
with open(pkl_filename, 'rb') as file:
    clf = pickle.load(file)

def predict(dataList):
    pulseList = dataList[0]
    temperatureList = dataList[1]
    result = 0.0
    for i in range(0,temperatureList.__len__()):
        temperature = temperatureList[i]
        pulse = pulseList[i]
        result+=decision(temperature, pulse)
    result=result/float(temperatureList.__len__())
    if result<0.5:
        return 0
    elif result>=0.5 and result<1:
        return 1
    elif result==1:
        return 2

def decision(temperature, pulse):
    return clf.predict([[temperature, pulse]])
