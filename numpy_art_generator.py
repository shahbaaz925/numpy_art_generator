import numpy as np
import matplotlib.pyplot as plt

# Define the size of the image
width, height = 400, 400

# Create an empty canvas (white image)
image = np.ones((height, width, 3), dtype=np.uint8) * 255

# Define the colors for the squares
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0)]

# Define the positions and sizes of the squares
squares = [(50, 50, 100, 100),  # (x, y, width, height)
           (200, 50, 100, 100),
           (50, 200, 100, 100),
           (200, 200, 100, 100)]

# Fill the canvas with colored squares
for i, (x, y, w, h) in enumerate(squares):
    color = colors[i % len(colors)]
    image[y:y+h, x:x+w] = color

# Display the image
plt.imshow(image)
plt.axis('off')
plt.show()
