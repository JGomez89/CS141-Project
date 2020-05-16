import numpy as np
from PIL import Image

img = Image.open('../images/plains.jpeg')
array = np.array(img)
print(array.shape)      # (170, 256, 3)
img = Image.fromarray(array)
img.save('../images/export/testrgb.jpeg')
