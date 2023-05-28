from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
import os
import json
import cv2
#from flask_cors import CORS

app=Flask(__name__) 
#CORS(app)
new_model=load_model(os.path.join('models','legal_illegal.h5'))
#member api routes
def detect_bowling_hand_from_image(file):
    file.save('image.jpeg')
    image = cv2.imread('image.jpeg')

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a hand detection algorithm (replace this with your specific detection method)
    # For example, you can use Haar cascades or a machine learning-based approach like TensorFlow or YOLO.
    # Here, we'll use a placeholder method that simply detects if the hand is on the left or right side of the image.
    height, width, _ = image.shape
    left_side = gray[:, :width // 2]
    right_side = gray[:, width // 2:]

    if cv2.countNonZero(left_side) > cv2.countNonZero(right_side):
        return "Left-handed bowler"
    else:
        return "Right-handed bowler"


@app.route("/hand_detect", methods=['POST'])
def hand_detect():
    if 'image' not in request.files:
        return jsonify({'success': False, 'message': 'No image file uploaded'})
    file = request.files['image'] 
    print('image found') 
    try:
       hand = detect_bowling_hand_from_image(file)
       print("the bowler is", hand)
       tr="The Bowler is "+str(hand)
       return {'result': tr}
    except:
        return {'success': False, 'message': 'Invalid image'}

@app.route("/members")

def members():
    return{"members":["member1","member2","member3"]}
 
@app.route('/predict_img', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'success': False, 'message': 'No image file uploaded'})
    file = request.files['image']
    print('Yes here')
    file.save('image.jpg')
    try:
        img=cv2.imread('image.jpg')
        resize=tf.image.resize(img, (256,256))
        resize.numpy().astype(int)
        yhatnew=new_model.predict(np.expand_dims(resize/255, 0))
        print(yhatnew)
        if yhatnew==0.9:
            print()
            return {'result':'invalid image! please upload correct image'}
        if yhatnew > 0.5:
           print( 'Congratulation! Your Bowling action is legal.......')
           return {'result':'Congratulation! Your Bowling action is legal.......'}
        else:
           print('Alert! Your Bowling Action is illegal............'+f'According to the ICC rules your angle is greater than 15{chr(176)}')
           return {'result':'Alert! Your Bowling Action is illegal............'+f'According to the ICC rules your angle is greater than 15{chr(176)}'}
    except:
        return {'success': False, 'message': 'Invalid image'}

if __name__=="__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')