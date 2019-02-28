import numpy as np
from PIL import Image
im0 = Image.open("./0.jpg")
im0_rotate = im0.rotate(90)
# im0_rotate.show()
more_train = np.load("more_train.npy")
print(more_train.shape)