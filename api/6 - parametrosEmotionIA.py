import tensorflow as tf
from tensorflow import keras

# Carrega modelo EmotionIA
EmotionIA = keras.models.load_model('models/EmotionIA_mlp.h5')

# Exibir a quantidade de camadas/parametros
EmotionIA.summary()