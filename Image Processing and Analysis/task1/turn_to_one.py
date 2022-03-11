import numpy as np
import matplotlib.pyplot as plt
from matplotlib import image

for i in range(5):
    ima = image.imread('{:}.jpg'.format(i))
    ima_G = ima.copy()
    ima_G[:, :, 1]= ima_G[:, :, 0]
    ima_G[:, :, 2]= ima_G[:, :, 0]
    
    plt.imsave('{:}.jpg'.format(i), ima_G)
