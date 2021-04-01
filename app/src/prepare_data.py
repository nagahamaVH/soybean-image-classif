import numpy as np
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

test_size = 0.2
seed = 42

x_data = np.load('./data/soja_images_150_new.npy', allow_pickle=True)
y_data = np.load('./data/soja_labels_150_new.npy', allow_pickle=True)

x_data = x_data.astype(np.float32)

y_data_cat = to_categorical(y_data)
x_train, x_test, y_train, y_test = train_test_split(
    x_data, y_data_cat, test_size=test_size, random_state=seed)

with open('./data/x_train.npy', 'wb') as f:
    np.save(f, x_train)

with open('./data/x_test.npy', 'wb') as f:
    np.save(f, x_test)

with open('./data/y_train.npy', 'wb') as f:
    np.save(f, y_train)

with open('./data/y_test.npy', 'wb') as f:
    np.save(f, y_test)
