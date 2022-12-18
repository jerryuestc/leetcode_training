import numpy as np

a = np.zeros((3, 3))
poz_tuple = np.where(a[0, :] == 0)
print(poz_tuple)