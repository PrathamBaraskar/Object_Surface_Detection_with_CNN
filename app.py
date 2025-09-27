import streamlit as st 
import numpy as np , cv2, os
from tensorflow.keras.models import load_model
from PIL import Image
import tensorflow as tf 

model = load_model(r"C:\Users\Pratham\Desktop\Artifiical intelligence\Deep learning\projects\scripts\models\baseline_cnn_net.h5")
classes = os.listdir(r"C:\Users\Pratham\Desktop\Artifiical intelligence\Deep learning\projects\NEU-DET\train")
classes.sort()

st.title('NEU surface Detection')
uploaded_file = st.file_uploader("Upload an image", type=['jpg','png','jpeg'])

if uploaded_file:
    img = Image.open(uploaded_file)
    img_resized = img.resize((128,128))
    img_array = np.array(img_resized)/255.0
    pred = np.argmax(model.predict(np.expand_dims(img_array,0)))

    st.image(img,caption=f"Prediction: {classes[pred]}", use_column_width = True)