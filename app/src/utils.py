import matplotlib.pyplot as plt
import numpy as np

def plot_loss_acc(history):
    fig, axs = plt.subplots(1, 2, figsize=(12, 4))

    axs[0].plot(history.history['loss'])
    axs[0].plot(history.history['val_loss'])
    axs[0].set_ylabel('Loss')
    axs[0].set_xlabel('Epoch')
    axs[0].set_title('Loss')
    axs[0].legend(['Train', 'Val'], loc='upper right')

    axs[1].plot(history.history['accuracy'])
    axs[1].plot(history.history['val_accuracy'])
    axs[1].set_ylabel('Accuracy')
    axs[1].set_xlabel('Epoch')
    axs[1].set_title('Accuracy')
    axs[1].legend(['Train', 'Val'], loc='lower right')

def get_pred_class(model, x_test):
    pred = model.predict(x_test)
    pred_class = np.argmax(pred, axis=1)
    
    return pred_class

def sample_from_true_prediction_given_class(pred_class, y_class, n_images, class_value, seed):
    is_class = y_class == class_value
    is_true_class = y_class == pred_class

    idxs = np.where(is_class * is_true_class)[0]
    np.random.seed(seed)
    sampled_idxs = np.random.choice(idxs, n_images, replace=False)

    return sampled_idxs

def get_layer_index_by_name(model, layer_name):
    for idx, layer in enumerate(model.layers):
        if layer.name == layer_name:
            return idx
