
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
import os
import cv2

new_model=load_model(os.path.join('models','legal_illegal.h5'))
img=cv2.imread('210034.jpg')
resize=tf.image.resize(img, (256,256))
yhatnew=new_model.predict(np.expand_dims(resize/255, 0))
print(yhatnew)
if yhatnew> 0.5:
    print('Congratulation! Your Bowling action is legal.......')
else:
    print('Alert! Your Bowling Action is illegal............')
    print(f'According to the ICC rules your angle is greater than 15{chr(176)}')