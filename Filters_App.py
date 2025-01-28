# LIBs

import io
import cv2
import numpy as np
from PIL import Image
import streamlit as st


# FILTERS FUNCTIONS

## GRAYSCALE
def white_black(image):
    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return gray_image

## pencil_sketch
def pencil_sketch(image):
    pen_gray_image, pen_colo_image  = cv2.pencilSketch(image)
    return pen_gray_image , pen_colo_image

## HSV
def hsv(image):
    hsv_image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    return hsv_image

## LAB
def lab(image):
    lab_image = cv2.cvtColor(image, cv2.COLOR_RGB2LAB)
    return lab_image

## XTZ
def xyz(image):
    xyz_image = cv2.cvtColor(image, cv2.COLOR_RGB2XYZ)
    return xyz_image

# BRIGHTNESS
def brightness(image, level):
    bri_img = cv2.convertScaleAbs(image, beta=level)
    return bri_img

# HDR
def hdr(image, sigma_s=10, sigma_r=0.1):
    hdr_img = cv2.detailEnhance(image, sigma_s=sigma_s, sigma_r=sigma_r)
    return hdr_img




# STREAMLIT UI

## TITLE
st.title("Filters Application")

## USER INPUT IMAGE
input_image = st.file_uploader("Please upload an image in one of the following formats: PNG, JPG, JPEG, or WEBP.", type=["png", "jpg", "jpeg", "webp"]) # Encoded Image
if input_image  is not None:
    
    input_image = Image.open(input_image) # Decoded Image
    input_image_array = np.array(input_image) # Convert Image to Numpy Array

    ### ORIGINAL VS FILTERED IMAGE

    original_image , filterd_image = st.columns(2)

    #### ORIGINAL IMAGE
    with original_image:
        st.header("Original Image")
        st.image(input_image_array, channels="RGB", use_container_width=True)

    #### CHOOSING FILTERED 
    fil = st.selectbox("Choose Filter :",["None","Black&White","Pencil_Sketch","HSV", "LAB", "XYZ", "Brightness","HDR"])

    color = "RGB"  # Defualt
    if fil == "None":
        new_image = input_image_array

    elif fil == "Black&White":
        new_image = white_black(input_image_array)
        color="GRAY"

    elif fil == "HSV":
        new_image = hsv(input_image_array)

    elif fil == "LAB":
        new_image = lab(input_image_array)

    elif fil == "XYZ":
        new_image = xyz(input_image_array)

    elif fil == "Pencil_Sketch":
        sch = st.selectbox("Do you want it :", ["Black & White Sketch", "Colored Sketch"])
        if sch == "Black & White Sketch":
            new_image, _ = pencil_sketch(input_image_array)
        else :
             _, new_image = pencil_sketch(input_image_array)

    elif fil == "Brightness":
        lev = st.slider("Choose brigthness level : ",-50,50,2)
        new_image = brightness(input_image_array, lev)

    else:
        sigma_s = st.slider("Choose spatial distance 'sigma_s'",1,50,10)
        sigma_r = st.slider("Choose contrast sensitivity 'sigma_s'",0.01,1.0,0.1,0.01)
        new_image = hdr(input_image_array, sigma_s=sigma_s, sigma_r=sigma_r)



    #### FILTERED IMAGE
    with st.spinner("Applying Choosen Filter..."):
        with filterd_image:
            st.header("Filtered Image")
            st.image(new_image,channels=color, use_container_width=True)



    ## SAVING FILTERED IMAGE
    pil_image = Image.fromarray(new_image)  # Convert numpy array to PIL image
    buf = io.BytesIO() # Create buffer 
    pil_image.save(buf, format="PNG") # Saving the image in the buffer
    byte_image = buf.getvalue() # Storing byte data into byte_image

    ## STREAMLIT DOWNLOAD BUTTON
    st.download_button(
            label="Download Filtered Image", 
            data=byte_image,
            file_name="filtered_image.png",
            mime="image/png"
                )
   
