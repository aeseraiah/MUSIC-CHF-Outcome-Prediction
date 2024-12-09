from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dropout, Dense, Conv1D, Flatten, BatchNormalization, MaxPooling1D
from sklearn.ensemble import RandomForestClassifier

def simple_neural_net(xtrain):
    input_d = xtrain.shape[1]
    print(f'Input dimension: {input_d}')
    num_classes = 4

    model = Sequential([
        # Dense(512, activation='relu', input_dim=input_d), 
        Dense(128, activation='relu', input_dim=input_d), 
        Dropout(0.2),
        Dense(64, activation='relu'),
        Dropout(0.2),
        Dense(32, activation='relu'),
        Dense(num_classes, activation='softmax')
    ])

    return model


def cnn(X_train):
    num_classes = 4
    model = Sequential()
    # model.add(Conv1D(64,  kernel_size=3, activation='relu', kernel_initializer='he_uniform',padding = 'same', input_shape=(X_train.shape[1], X_train.shape[2])))
    model.add(Conv1D(128, 3, activation='relu', input_shape=(X_train.shape[1], X_train.shape[2])))
    # model.add(MaxPooling1D(pool_size=2))
    model.add(Dropout(0.20))
    model.add(Conv1D(64, 3, activation='relu'))
    model.add(Flatten())
    model.add(Dense(32, activation='relu'))
    model.add(Dense(num_classes,activation = 'softmax'))

    # model.add(Conv1D(64,  kernel_size=3, activation='relu', kernel_initializer='he_uniform',padding = 'same', input_shape=(X_train.shape[1], X_train.shape[2]))) 
    # model.add(BatchNormalization(axis = -1))
    # model.add(MaxPooling1D(pool_size=2))
    # model.add(Dropout(0.20))
    # model.add(Conv1D(64,  kernel_size=3, activation='relu', kernel_initializer='he_uniform',padding = 'same'))
    # model.add(BatchNormalization(axis=-1))
    # model.add(MaxPooling1D(pool_size=2))
    # model.add(Dropout(0.20))
    # model.add(Flatten())
    # model.add(Dropout(0.20))
    # model.add(Dense(32, activation = 'relu'))
    # model.add(Dense(16, activation = 'relu'))
    # model.add(Dense(num_classes,activation = 'softmax'))

    return model