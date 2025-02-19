import streamlit as st
import os
import subprocess
import shutil
from werkzeug.utils import secure_filename

# Set custom theme colors
st.markdown(
    """
    <style>
    body {
        background-color: #2E3B4E;
        color: #EAECEE;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
    }
    .stFileUploader {
        background-color: #1F2A38;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True
)

uploads_dir = "uploads"
os.makedirs(uploads_dir, exist_ok=True)

st.title("Vehicle Detection WebApp - YOLO")

# Video Upload Section
st.header("Upload a Video")
uploaded_video = st.file_uploader("Choose a video", type=["mp4", "avi", "mov", "mkv"])

if uploaded_video is not None:
    video_filename = secure_filename(uploaded_video.name)
    video_path = os.path.join(uploads_dir, video_filename)
    with open(video_path, "wb") as f:
        f.write(uploaded_video.getbuffer())
    
    st.success(f"Uploaded {video_filename}")
    
    if st.button("Run Video Detection"):
        subprocess.run(['python', 'detect.py', '--source', video_path], shell=True)
        
        src_video_path = os.path.join('results', video_filename)
        dst_video_path = os.path.join('static', video_filename)
        shutil.copy(src_video_path, dst_video_path)
        
        st.video(dst_video_path)
        st.download_button("Download Processed Video", src_video_path)

# Image Upload Section
st.header("Upload an Image")
uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image_filename = secure_filename(uploaded_image.name)
    image_path = os.path.join(uploads_dir, image_filename)
    with open(image_path, "wb") as f:
        f.write(uploaded_image.getbuffer())
    
    st.success(f"Uploaded {image_filename}")
    st.image(image_path, caption="Uploaded Image", use_column_width=True)
    
    if st.button("Run Image Detection"):
        subprocess.run(['python', 'detect.py', '--source', image_path], shell=True)
        
        src_image_path = os.path.join('results', image_filename)
        dst_image_path = os.path.join('static', image_filename)
        shutil.copy(src_image_path, dst_image_path)
        
        st.image(dst_image_path, caption="Processed Image", use_column_width=True)
        st.download_button("Download Processed Image", src_image_path)
