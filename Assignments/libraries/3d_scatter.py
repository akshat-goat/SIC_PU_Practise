import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.random.rand(50)
y = np.random.rand(50)
z = np.random.rand(50)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(x, y, z, color='red')
ax.set_xlabel("Variable X")
ax.set_ylabel("Variable Y")
ax.set_zlabel("Variable Z")
ax.set_title("Distribution of Three Random Variables in 3D Space")
plt.show()
