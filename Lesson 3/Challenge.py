from PIL import Image, ImageDraw, ImageFont

# Create a new image with white background
width, height = 400, 200
image = Image.new('RGB', (width, height), color='white')

# Initialize ImageDraw object to add text to the image
draw = ImageDraw.Draw(image)

# Set the font and size (make sure you have a valid font on your system)
font = ImageFont.load_default()  # Using default font
text = "Hello, Pillow!"

# Calculate the text size and position using textbbox (bounding box)
bbox = draw.textbbox((0, 0), text, font=font)  # Get the bounding box of the text
text_width = bbox[2] - bbox[0]  # Width is the difference between right and left
text_height = bbox[3] - bbox[1]  # Height is the difference between top and bottom

# Calculate the position to center the text
position = ((width - text_width) // 2, (height - text_height) // 2)

# Add the text to the image
draw.text(position, text, fill="black", font=font)

# Save the image as a PNG file
image.save('generated_image.png')

# Display the image (optional)
image.show()



"""
When you run the above code, it will:

Create an image of size 400x200 pixels with a white background.
Draw the text "Hello, Pillow!" in the center of the image using the default font.
Save the image as generated_image.png in your working directory.
Optionally, the image will be opened using your default image viewer.
Customize:
You can change the text and background color to your preference.
If you have a specific font file (like .ttf), you can load it by specifying the path with ImageFont.truetype('path_to_font.ttf', size) instead of using ImageFont.load_default().

"""