import numpy as np
import matplotlib.pyplot as plt
a = np.loadtxt('sylv.txt')

fig = plt.figure()
plt.plot(a[:,0], a[:,1], label='ours')
plt.plot(a[:,0], (a[:,2]), label='IVT')
plt.plot(a[:,0], (a[:,3]), label='OAB')
plt.xlabel("Frames#")
plt.ylabel("Error")
plt.title('sylv')
plt.legend()
plt.show()
fig.savefig('sylv.jpg')