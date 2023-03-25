# create-color-bars-based-on-image# Image Color Bar Generator

This is a Python script that generates a color bar based on the dominant colors in an image. It uses k-means clustering to find the most common colors in the image, and then creates a bar chart with each color represented as a block.

## Dependencies

This script requires the following dependencies:

-   OpenCV
-   NumPy
-   Matplotlib
-   webcolors
-   colormath

You can install these dependencies using pip:

Copy code

`pip install opencv-python numpy matplotlib webcolors colormath` 

## Usage

1.  Place the script in a directory with your image files.
2.  Run the script using Python: `python main.py`
3.  The script will create an output directory if it does not already exist.
4.  For each image file, the script will generate a color bar and save it to the output directory with the same filename as the original image, but with '_bar' added before the file extension.

## Example

For example, if you have an image file named 'myimage.jpg', the script will generate a color bar and save it to 'output/myimage_bar.jpg'.
