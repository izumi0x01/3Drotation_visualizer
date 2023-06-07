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

    def get_arrow(self,u = 1,v = 0,w = 0,theta = 0):
        targetVec = np.array([u,v,w])
        # axis = np.array([0, 1, 0])
        angle = np.pi*theta/180
        rotationVec = targetVec*angle
        print("θ: " + str(theta) + ", Vec: " + str(rotationVec))
        
        return rotationVec

    def update(self,theta):
          self.quiver.remove()
          self.quiver = self.axis.quiver(0,0,0,*self.get_arrow(1,0,0,theta), color = "green", length = 1,arrow_length_ratio = 0.1)


    def show(self):
          
          self.fig = plt.figure()
          self.axis = self.fig.add_subplot(111, projection='3d')
          self.axis.grid(True)
          
          self.axis.set_xlim(-3, 3)
          self.axis.set_ylim(-3, 3)
          self.axis.set_zlim(-3, 3)

          self.quiver = self.axis.quiver(0,0,0,*self.get_arrow())

          N = 100

          anim = animation.FuncAnimation(self.fig, self.update, N, interval=10000/N, blit=False)

          plt.show()
          return

if __name__ == "__main__":
    sanJikuHyouji = SanJikuHyouji()
    sanJikuHyouji.show()