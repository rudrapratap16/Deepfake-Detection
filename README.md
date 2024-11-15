# Deepfake Detection using InceptionResNetV2

## Overview

This project implements a deep learning model to detect **deepfake images** using a pre-trained **InceptionResNetV2** model. The model classifies images as either **real** or **fake** based on their authenticity. We leverage **transfer learning** to adapt the pre-trained model for our specific task of distinguishing manipulated media from authentic images.

### Objective

The goal of this project is to build a reliable model capable of detecting deepfake images, which can be useful for applications involving content verification and combating the spread of misinformation.

## Requirements

To run this project, you need to install the following dependencies:

- Python 3.6+
- TensorFlow 2.x
- Keras
- Numpy
- Matplotlib
- classification-models

You can install the required packages using `pip`:

```bash
pip install tensorflow numpy matplotlib classification-models
