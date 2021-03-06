import numpy as np
import matplotlib.pyplot as plt
a = np.loadtxt('woman.txt')

fig = plt.figure()
plt.plot(a[:,0], a[:,1], label='ours')
plt.plot(a[:,0], (a[:,2]), label='OAB')
plt.xlabel("Frames#")
plt.ylabel("Error")
plt.title('woman')
plt.legend()
plt.show()
fig.savefig('woman.jpg')