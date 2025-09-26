import matplotlib.pyplot as plt
import numpy as np
#straight line
xpoints=np.array([1,8])
ypoints=np.array([3,10])
plt.plot(xpoints,ypoints)
plt.show()
#
plt.plot(xpoints,ypoints,'o')
plt.show()
xpoints1=np.array([1,2,3,4,5])
ypoints2=np.array([3,5,7,9,12])
plt.plot(xpoints1,ypoints2)
plt.show()
  #marker
plt.plot(ypoints,marker="o")
plt.show()
#simple line plot
x=np.array([0,6])
y=np.array([0,250])
plt.plot(x,y)
plt.show()