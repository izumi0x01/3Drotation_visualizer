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

    def show(self):
          
          self.fig = plt.figure()
          # self.axis = p3.Axes3D(self.fig)
          self.axis = self.fig.add_subplot(111, projection='3d')
          self.axis.grid(True)


          Xvec, Yvec, Zvec = self.UpdateSanjikuVec(0)

          # print("X:" + np.array2string(Xvec)+ "Y:" + np.array2string(Yvec)+ "Z:" + np.array2string(Zvec) )

          self.UpdateDrawVec(Xvec, "red")
          self.UpdateDrawVec(Yvec, "green")
          self.UpdateDrawVec(Zvec, "blue")
          
          # ベクトルの定義
          composite_vector = Xvec + Yvec + Zvec
          normalized_vector = composite_vector / np.linalg.norm(composite_vector)
          self.UpdateDrawVec(normalized_vector, "pink")

          self.axis.set_xlim(-2, 2)
          self.axis.set_ylim(-2, 2)
          self.axis.set_zlim(-2, 2)

          N = 100
          data = np.array(list(self.gen(N))).T
          line, = self.axis.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])
          ani = animation.FuncAnimation(self.fig, self.update, N, fargs=(data, line), interval=10000/N, blit=False)
          plt.show()

          return

    def gen(self, n):
        phi = 0
        while phi < 2*np.pi:
            yield np.array([np.cos(phi), np.sin(phi), phi])
            phi += 2*np.pi/n


    def update(self, num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    def UpdateDrawVec(self, vec, color):
        self.axis.quiver(0,0,0,vec[0], vec[1], vec[2],
        color = color, length = 1,
        arrow_length_ratio = 0.1)


    def UpdateSanjikuVec(self, Theta = 0):
        
        angle = Theta * np.pi / np.pi 

        Xvec = np.array([1, 0, 0])
        rotXvec = angle * Xvec
        rotation = Rotation.from_rotvec(rotXvec)
        rotation_matrix = rotation.as_matrix()
        newXvec = np.dot(rotation_matrix, Xvec)

        Yvec = np.array([0, 1, 0])
        newYvec = np.dot(rotation_matrix, Yvec)
        Zvec = np.array([0, 0, 1])
        newZvec = np.dot(rotation_matrix, Zvec)
        
        return (newXvec, newYvec, newZvec)

if __name__ == "__main__":
    sanJikuHyouji = SanJikuHyouji()
    sanJikuHyouji.show()