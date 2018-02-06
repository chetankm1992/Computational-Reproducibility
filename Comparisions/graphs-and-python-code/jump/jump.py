import numpy as np
import matplotlib.pyplot as plt
a = np.loadtxt('jump.txt')

fig = plt.figure()
plt.plot(a[:,0], a[:,1], label='ours')
plt.plot(a[:,0], (a[:,2]), label='OAB')
plt.xlabel("Frames#")
plt.ylabel("Error")
plt.title('jump')
plt.legend()
plt.show()
fig.savefig('jump.jpg')