from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras import utils


image_w = 28
image_h = 28
nb_classes = 10


def main():
    # MNIST 데이터 읽어 들이기
    (X_train, y_train), (X_test, y_test) = mnist.load_data()
    # 데이터 정규화
    X_train = X_train.reshape(X_train.shape[0], image_w * image_h).astype('float32')
    X_test = X_test.reshape(X_test.shape[0], image_w * image_h).astype('float32')
    X_train /= 255
    X_test /= 255
    y_train = utils.to_categorical(y_train, 10)
    y_test = utils.to_categorical(y_test, 10)
    # 모델 구축
    model = build_model()
    model.fit(X_train, y_train, batch_size=128, epochs=20, verbose=1, validation_data=(X_test, y_test))
    # 모델 저장
    model.save_weights('mnist.hdf5')
    # 모델 평가
    score = model.evaluate(X_test, y_test, verbose=0)
    print('score=', score)


def build_model():
    # MLP 모델 구축
    model = Sequential()
    model.add(Dense(512, input_shape=(784,)))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(512))
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    model.add(Dense(10))
    model.add(Activation('softmax'))
    model.compile(loss='categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])
    return model


if __name__ == '__main__':
    main()
