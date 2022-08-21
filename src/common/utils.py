import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


class Dim2Data():
    color_map = ['red','green','blue']
    COLOR_RED = 0
    COLOR_GREAN  = 1
    
    def rand_data(self, num:int):
        self.data = np.random.randint(1,100, (3,num))
        self.colors = np.zeros(num)
        return self.data
    
    def rand_data_by_sum(self, num:int, coeff=(1,1)):
        data = self.rand_data(num)
        for i in  range(data.shape[1]):
            data[2,i] = coeff[0]*data[0,i] + coeff[1]*data[1,i]
        return data
        
    def set_colors(self, colors):
        self.colors = colors
    def set_color(self, id, color):
        self.colors[id] = color
    
    def draw_scatter(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_xlabel('X label')
        ax.set_ylabel('Y lable')
        ax.set_zlabel('Z label')
        ax.set_title("scatter image")   
             
        data = self.data 
        # for i in range(data.shape[1]):
        #     ax.scatter(data[0,i],data[1,i], data[2,i], c=self.colors[i])
        ax.scatter(data[0,:],data[1,:], data[2,:], c=self.colors)
        # plt.plot()
            
        plt.show()
        
        
if __name__ == '__main__':    
        d2data = Dim2Data()
        d2data.rand_data_by_sum(10)
        d2data.set_color(9, Dim2Data.COLOR_GREAN)
        d2data.draw_scatter()