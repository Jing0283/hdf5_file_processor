import h5py
import numpy as np
from PIL import Image

hf = h5py.File("file name", 'r')

for key in hf.keys():
    print(key)  # Names of the root level object names in HDF5 file - can be groups or datasets.
    print(type(hf[key]))

n1 = np.array(hf["dataset name"][:])
print(n1)

print(n1.shape[0])
print(n1.ndim)
print(n1.size)


image_numpy = Image.fromarray(n1[0] * 255)
root = 'file location'
image_numpy.save(root + "\\"+"png name.png")

n1 = np.array(hf["dataset root"])

np.savetxt('file_root_name.txt', n1,fmt='%f',delimiter=',')


