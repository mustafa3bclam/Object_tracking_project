# Object Tracking Project
![real_time_object_detection](https://github.com/user-attachments/assets/b4333505-3169-4205-94c3-6283a74d87b5)

This project demonstrates object tracking using OpenCV and Streamlit. It allows users to upload a video file and detects moving objects in the video using background subtraction.

## Features

- Real-time object detection in video files
- Background subtraction using MOG2
- Bounding boxes around detected objects
- Streamlit interface for easy video upload and display

## Requirements

- Python 3.x
- OpenCV
- Streamlit
- NumPy

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit app:
    ```sh
    streamlit run app.py
    ```

2. Upload a video file in the Streamlit interface.

3. The app will display the original video feed and the foreground mask with detected objects highlighted.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
