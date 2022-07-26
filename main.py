import numpy as np
import matplotlib.pyplot as plt

from take_picture import take_picture

frame = take_picture()

imgplot = plt.imshow(frame)
plt.show()

# Now run facial recognition :)