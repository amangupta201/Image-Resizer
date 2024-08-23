# Image-Resizer
The Image Resizer is a web-based application built using Flask and Python's Pillow library. It allows users to upload images and resize them either to custom dimensions or to predefined sizes tailored for popular social media platforms such as Facebook, Instagram, Twitter, WhatsApp, and LinkedIn.

Features
Platform-Specific Resizing: Resize images to predefined dimensions optimized for various social media platforms, including: 

Facebook Post (1200x630)

Instagram Post (1080x1080)

Twitter Post (1200x675)

Instagram Story (1080x1920)

WhatsApp Status (1080x1920)

LinkedIn Post (1200x627)

Custom Resizing: Option to manually specify the width and height for custom resizing.

File Upload: Users can upload their images through a simple web interface.

Download Resized Image: After resizing, the user can download the resized image directly from the browser.

Installation

To run this project locally, follow these steps:

Clone the repository:

git clone https://github.com/amangupta201/Image-Resizer.git

cd Image-Resizer

Create a virtual environment and activate it:


python -m venv venv

source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required packages:


pip install -r requirements.txt

Run the Flask app:

python app.py

Open your web browser and navigate to:

http://127.0.0.1:5000/

Usage

Upload an Image:

Navigate to the app's homepage.

Click the "Choose File" button to upload an image from your device.

Choose Resizing Option:

Platform-Specific Resizing: Select a social media platform from the dropdown to automatically resize the image to the platform's recommended dimensions.

Custom Resizing: Select the "Custom" option and enter the desired width and height.

Download the Resized Image:

Click the "Submit" button.

After processing, the resized image will be available for download.
