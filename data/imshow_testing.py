#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 24 20:43:07 2020

@author: simondonike
"""

"""
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


lincoln_df = pd.read_csv("linc_seg.csv",delimiter=";",index_col="index")
print(lincoln_df)

fig = plt.imshow(lincoln_df, cmap="gray")
fig.savefig("export.tiff")
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dpi = 100 # Arbitrary. The number of pixels in the image will always be identical
#data = pd.read_csv("linc_seg.csv",delimiter=";",index_col="index")
data = np.random.randint(0,255,size=(100,100))
print("Numpy array created")
data = pd.DataFrame(data)
print("Numpy converted to datafrae")

#data = np.random.random((10, 10))
height, width = np.array(data.shape, dtype=float) / dpi


fig = plt.figure(figsize=(width, height), dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('off')

ax.imshow(data, interpolation='none', cmap="gray")
fig.savefig('test_large.tif', dpi=dpi, edgecolor = "none")
print("DONE!")


