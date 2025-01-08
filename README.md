# Deepfake Detection with Streamlit

This project provides a simple and user-friendly web application to detect whether an uploaded image is real or a deepfake. It uses a pretrained deep learning model (InceptionResNetV2) fine-tuned for binary classification, integrated into an interactive **Streamlit** app.

## Features
- **Upload Image**: Users can upload an image file (JPG, JPEG, or PNG) directly through the web interface.
- **Real-Time Predictions**: The app processes the image and predicts whether it is real or a deepfake.
- **Confidence Score**: Displays the model's confidence level for the prediction.

## Requirements

To run this app locally, you'll need the following:

- **Python 3.6+**
- **TensorFlow** (for running the deep learning model)
- **Streamlit** (for the web interface)
- **Pillow** (for image handling)

You can install all dependencies with:

```bash
pip install -r requirements.txt
```
## Installation and Setup

Follow these steps to set up the project on your local machine:

### 1. Clone the Repository
Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/your-username/deepfake-detection
cd deepfake-detection
```

### 2. Install Dependencies
Install the required libraries listed in the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 3. Save the Trained Model
Ensure the trained model file deepfake_model.h5 is placed in the model/ directory.

If you don’t have the trained model:

Train the model using your dataset (refer to the model training section in the repo).
Save the model using the following code:

```python
model.save('model/deepfake_model.h5')
```

### 4. Run the Streamlit App
Start the Streamlit app by running:

```bash
streamlit run app.py
```

After running this command, a local web server will start, and you'll see a URL (usually `http://localhost:8501`)
