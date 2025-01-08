import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load the trained model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model('model/deepfake_model.h5')

model = load_model()

# Preprocess image
def preprocess_image(image):
    img = image.resize((100, 100))  # Resize to match model input
    img_array = np.array(img) / 255.0  # Normalize to [0, 1]
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Streamlit App
st.title("Deepfake Detection App")
st.write("Upload an image to check if it's real or a deepfake.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    image = image.resize((100,100))
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess and predict
    st.write("Processing the image...")
    img_array = preprocess_image(image)
    prediction = model.predict(img_array)

    # Display result
    if prediction[0] > 0.5:
        st.success(f"The image is predicted to be **real** with a confidence of {prediction[0][0]*100:.2f}%")
    else:
        st.error(f"The image is predicted to be a **deepfake** with a confidence of {(1-prediction[0][0])*100:.2f}%")
