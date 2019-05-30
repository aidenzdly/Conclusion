import tensorflow as tf
from tensorflow.python.keras import backend as K
from tensorflow.python.keras.models import load_model

model = load_model(r"h5Model/retrain_model.h5")


tf.saved_model.simple_save(
    K.get_session(),
    "pb",  # 保存模型路径
    inputs={'input_image': model.input},
    outputs={t.name:t for t in model.outputs})