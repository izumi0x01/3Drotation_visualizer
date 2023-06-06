import matplotlib.pyplot as plt
import numpy as np

# ３軸表示するクラス
#　クォータニオンを行う関数

class SanJikuHyouji:
    
    fig = None

    
    def __init__(self):
        None

    def show(self):
        fig = plt.figure()
        axis = fig.add_subplot(111, projection='3d')
        axis.grid(True)

        Xvec, Yvec, Zvec = self.MakeSanjikuVec()

        axis.quiver(0,0,0,Xvec[0], Xvec[1], Xvec[2],
          color = "red", length = 1,
          arrow_length_ratio = 0.1)
        
        axis.quiver(0,0,0,Yvec[0], Yvec[1], Yvec[2],
          color = "green", length = 1,
          arrow_length_ratio = 0.1)
        
        axis.quiver(0,0,0,Zvec[0], Zvec[1], Zvec[2],
          color = "blue", length = 1,
          arrow_length_ratio = 0.1)

        axis.set_xlim(-2, 2)
        axis.set_ylim(-2, 2)
        axis.set_zlim(-2, 2)

        plt.show()

        return

    def MakeSanjikuVec(self, Theta = 0):
        Xvec = np.array([1, 0, 0])
        Yvec = np.array([0, 1, 0])
        Zvec = np.array([0, 0, 1])
        
        return (Xvec, Yvec, Zvec)

if __name__ == "__main__":
    sanJikuHyouji = SanJikuHyouji()
    sanJikuHyouji.show()