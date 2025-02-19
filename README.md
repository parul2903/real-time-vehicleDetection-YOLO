# Vehicle Detection with YOLOv5

## Overview
This project detects different types of vehicles such as cars, trucks, and ambulances using **YOLOv5**. It includes a web application where users can upload an image or video, process it, and get the output with detected vehicles.

## Features
- **Real-time vehicle detection** using YOLOv5.
- **Supports images and videos** as input.
- **Web-based interface** built with Streamlit.
- **Downloadable processed results.**

## How to Use This Project

### Clone the Repository
```bash
git clone https://github.com/kkkumar2/Vehicle-detection-with-yolov5.git
cd Vehicle-detection-with-yolov5
```

### Install Dependencies
Make sure you have Python installed, then run:
```bash
pip install -r requirements.txt
```

### Run the Web Application
```bash
streamlit run app.py
```

## Web Application Interface

### Upload an Image or Video
The homepage allows you to upload either an **image** or a **video**.

#### Example:
https://github.com/parul2903/real-time-vehicleDetection-YOLO/issues/3#issue-2864320779

### Process and Download the Output
Once uploaded, click on the "Run Detection" button. When processing is complete, a **download button** will appear.

#### Example:
https://github.com/parul2903/real-time-vehicleDetection-YOLO/issues/2#issue-2864320137

### View the Processed Results
The final processed image or video will highlight detected vehicles.

#### Example:
https://github.com/parul2903/real-time-vehicleDetection-YOLO/issues/1#issue-2864319193

## Sample Video Output

https://user-images.githubusercontent.com/88458239/163666098-b9b7f67e-686c-4309-a055-67ea55f345ea.mp4

## YOLOv5 Model Details
This project uses the **YOLOv5 model** for object detection. The model is trained on a dataset containing different vehicle classes and is optimized for real-time inference.

## Folder Structure
```
Vehicle-detection-with-yolov5/
│── detect.py               # YOLOv5 detection script
│── app.py                  # Web application script
│── requirements.txt        # Required dependencies
│── uploads/                # Folder for uploaded files
│── results/                # Folder for processed results
│── static/                 # Folder for static files
│── readme_images/          # Images for README
```

## Future Improvements
- Improve model accuracy with fine-tuned training.
- Add support for additional vehicle types.
- Deploy the web app online.

## Contributing
Feel free to fork this repository and submit pull requests for improvements!

## License
This project is licensed under the MIT License.

---

🚀 **Happy Detecting!** 🚀
