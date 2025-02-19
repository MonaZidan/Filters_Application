# Filters Application

This is a Streamlit-based web application that allows users to apply various filters to their images. The application supports multiple image formats and provides several filters including grayscale, pencil sketch, HSV, LAB, XYZ, brightness adjustment, and HDR.

## Features

- Upload images in PNG, JPG, JPEG, or WEBP formats.
- Apply different filters to the uploaded images:
  - Grayscale
  - Pencil Sketch (Black & White or Colored)
  - HSV
  - LAB
  - XYZ
  - Brightness Adjustment
  - HDR
- View the original and filtered images side by side.
- Download the filtered image.

## Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```sh
    cd Filters_Application
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```sh
    streamlit run Filters_App.py
    ```
2. Open your web browser and go to `http://localhost:8501`.
3. Upload an image and choose a filter to apply.
4. View the original and filtered images.
5. Download the filtered image using the download button.

