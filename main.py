from flask import Flask, render_template, request, send_file
from PIL import Image
import os

app = Flask(__name__)

# Predefined dimensions for various social media platforms
DIMENSIONS = {
    "facebook_post": (1200, 630),
    "instagram_post": (1080, 1080),
    "twitter_post": (1200, 675),
    "instagram_story": (1080, 1920),
    "whatsapp_status": (1080, 1920),
    "linkedin_post": (1200, 627),
}


def resize_image(input_path, output_path, new_width=None, new_height=None, platform=None):
    if platform:
        if platform not in DIMENSIONS:
            raise ValueError(f"Unsupported platform: {platform}. Choose from {list(DIMENSIONS.keys())}")
        new_width, new_height = DIMENSIONS[platform]
    elif new_width is None or new_height is None:
        raise ValueError("Custom dimensions (new_width and new_height) must be provided if no platform is selected.")

    with Image.open(input_path) as img:
        resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
        resized_img.save(output_path)


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Get the uploaded file
        file = request.files['image']
        if file.filename == '':
            return 'No selected file'

        # Save the file to a temporary location
        input_path = os.path.join('uploads', file.filename)
        file.save(input_path)

        # Get the user choice for resizing
        choice = request.form.get('resize_choice')

        output_path = os.path.join('outputs', f"resized_{file.filename}")

        if choice == 'platform':
            platform = request.form.get('platform')
            resize_image(input_path, output_path, platform=platform)
        elif choice == 'custom':
            new_width = int(request.form.get('width'))
            new_height = int(request.form.get('height'))
            resize_image(input_path, output_path, new_width=new_width, new_height=new_height)

        return send_file(output_path, as_attachment=True)

    return render_template('upload.html', platforms=list(DIMENSIONS.keys()))


if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    if not os.path.exists('outputs'):
        os.makedirs('outputs')
    app.run(debug=True)
