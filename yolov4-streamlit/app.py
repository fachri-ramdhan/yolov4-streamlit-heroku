import streamlit as st
import numpy as np
import base64
from PIL import Image
from detection.object_detection import detect_object


def main():
    st.title("Deteksi kesehatan mata Sapi")
    img_array = upload_image_ui()

    if isinstance(img_array, np.ndarray):
        image = detect_object(img_array)
        st.image(image)

def upload_image_ui():
    uploaded_image = st.file_uploader("silahkan masukkan gambar disini", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        try:
            image = Image.open(uploaded_image)
        except Exception:
            st.error("Error: Invalid image")
        else:
            img_array = np.array(image)
            return img_array

if __name__ == '__main__':
    main()


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""

    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('sapi1.png')