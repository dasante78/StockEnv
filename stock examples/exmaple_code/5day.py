#Keras model to use the last 5 days to predict close of next day
import keras
import numpy as np
from stocktrainer import Env
from keras.models import Sequential
from keras.layers import Dropout ,BatchNormalization, LSTM, Dense, GaussianDropout

#crete LSTM model
def create_model():
    model = Sequential()
    model.add(BatchNormalization(input_shape=(5, 6)))
    model.add(LSTM(512, return_sequences=True, activation='relu'))
    model.add(LSTM(1024, activation='relu'))
    model.add(Dropout(0.2))
    model.add(Dense(2048, activation='relu'))
    model.add(GaussianDropout(0.2))
    model.add(Dropout(0.4))
    model.add(Dense(1024, activation='relu'))
    model.add(Dense(512, activation='relu'))
    model.add(Dense(256, activation='relu'))
    model.add(Dense(512, activation='relu'))
    model.add(Dense(1, activation='relu'))

    model.compile(loss='mse', optimizer='adam')

    return model
            
def main():
    #create standard enviorment
    enviorment = Env("Standard", "AAPL")
    #get train ,test data to specifications, seed for constistency
    trainx,testx,trainy, testy = enviorment.train_test(test_percent= .30, shuffle = True, start_date='2003-01-01', end_date='now', agent_memory=5, seed=42)
    model = create_model()

    #fit model
    model.fit(trainx, trainy, epochs=10, batch_size=128, verbose=2)

    model.save('try1')

    #evaluate model
    model.evaluate(testx,testy )
    #use model to predict
    model.predict(testx)





if __name__ == '__main__':
    main()
