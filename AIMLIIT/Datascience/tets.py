import matplotlib.pyplot as plt
import numpy as np


#line CHarts
x = np.array([100,200,300,400,500])
y = np.random.randint(1,100,size=5)
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Line Chart Example")

plt.plot(x,y, marker='*', color='b', linestyle='--', linewidth=2, markersize=38)
plt.grid(True)
plt.xticks(x)
plt.show()