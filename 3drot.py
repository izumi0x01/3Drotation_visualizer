import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime
from scipy.spatial.transform import Rotation
import mpl_toolkits.mplot3d.axes3d as p3
import time
from matplotlib import animation

# ３軸表示するクラス
#　クォータニオンを行う関数

class SanJikuHyouji:

    def __init__(self):
        return

    def get_arrow(self,theta):
        x = 0
        y = 0
        z = 0
        u = 1 + 0.01 * theta
        v = 0
        w = 0
        return x,y,z,u,v,w
    

    def update(self,theta):
          self.quiver.remove()
          self.quiver = self.axis.quiver(*self.get_arrow(theta), color = "green", length = 1,arrow_length_ratio = 0.1)

    def show(self):
          
          self.fig = plt.figure()
          self.axis = self.fig.add_subplot(111, projection='3d')
          self.axis.grid(True)
          
          self.axis.set_xlim(-3, 3)
          self.axis.set_ylim(-3, 3)
          self.axis.set_zlim(-3, 3)

          self.quiver = self.axis.quiver(*self.get_arrow(0))

          N = 100
          animation.FuncAnimation(self.fig, self.update, N, interval=10000/N, blit=False)
          plt.show()
          return

if __name__ == "__main__":
    sanJikuHyouji = SanJikuHyouji()
    sanJikuHyouji.show()