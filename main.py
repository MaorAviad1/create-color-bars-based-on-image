import cv2
import numpy as np
import os
import matplotlib.pyplot as plt


def create_bar(height1, width2, color):
    bar1 = np.zeros((height1, width2, 3), np.uint8)
    bar1[:] = color
    red, green, blue = int(color[2]), int(color[1]), int(color[0])
    return bar1, (red, green, blue)


# Get list of image files in same folder as script
script_dir = os.path.dirname(os.path.realpath(__file__))
img_files = [f for f in os.listdir(script_dir) if f.endswith('.png') or f.endswith('.jpg')]

# Create output directory if it does not exist
output_dir = os.path.join(script_dir, 'output')
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for img_file in img_files:

    # Load image
    img_path = os.path.join(script_dir, img_file)
    img = cv2.imread(img_path)

    if img is None:
        print(f'Error: Failed to load image at {img_path}')
        continue

    # Perform k-means clustering
    height, width, _ = np.shape(img)
    data = np.reshape(img, (height * width, 3))
    data = np.float32(data)

    number_clusters = 5
    criteria = [cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0]
    flags = cv2.KMEANS_RANDOM_CENTERS
    compactness, labels, centers = cv2.kmeans(data, number_clusters, None, criteria, 10, flags)

    # Create bar chart for each cluster
    font = cv2.FONT_HERSHEY_SIMPLEX
    bars = []
    rgb_values = []

    for index, row in enumerate(centers):
        bar, rgb = create_bar(200, 200, row)
        bars.append(bar)
        rgb_values.append(rgb)

    img_bar = np.hstack(bars)

    for index, row in enumerate(rgb_values):
        image = cv2.putText(img_bar, f'{index + 1}. RGB: {row}', (5 + 200 * index, 200 - 10),
                            font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
        print(f'{index + 1}. RGB{row}')

    # Display and save output
    plt.figure(figsize=(12, 8))
    plt.subplot(121)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.title('Input Image')
    plt.axis('off')
    plt.subplot(122)
    plt.imshow(cv2.cvtColor(img_bar, cv2.COLOR_BGR2RGB))
    plt.title('Dominant Colors')
    plt.axis('off')
    out_file = os.path.splitext(img_file)[0] + '_bar.jpg'
    out_path = os.path.join(output_dir, out_file)
    plt.savefig(out_path)
    plt.show()