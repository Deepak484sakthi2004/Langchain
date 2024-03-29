from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import streamlit as st

def modelTumour():
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open("inputMRI.jpeg").convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    # print("Class:", class_name[2:], end="")
    # print("Confidence Score:", confidence_score)

def main():
    st.title("Tumour classifier using google's teachable machine")
    st.write("upload the MRI image for classifying for tumour or not tumour")

    upload_image = st.file_uploader("Drop the MRI here",type=['jpeg','png','jpg'])

    if upload_image is not None:

        image_file = Image.open(upload_file)
        st.image(image_file,"Uploaded Image",use_column_width = True)

        label , confidence_score = modelTumour(image_file)
        if(label == "1 Yes\n"):
            st.error("MRI scan has brain tumour")
        else:
            st.success("No brain tumour found in the mri")


if __name__ =="__main__":
    main()