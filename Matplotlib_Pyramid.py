import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def getTop(top,sides,height,p1,delta_h):
    # Recursive process for defining height from outer layer to the core.
    if sides - p1 == 1:
        top[sides-1,p1] = height
        return top    
    else:        
        for x in [p1,sides-1]:
            for y in range(p1,sides):
                top[x,y] = height    
        for x in range(p1,sides):
            for y in [p1,sides-1]:
                top[x,y] = height
        
        getTop(top,sides-1,height+delta_h,p1+1,delta_h)

def printPyramid(sides,height):
    # Set axes values
    half = sides//2 
    x1 = np.arange(-half,half+1,1)
    y1 = x1.copy()
    x_1, y_1 = np.meshgrid(x1,y1)
    x_2, y_2 = x_1.flatten(), y_1.flatten()
    
    # Define top (call function getTop()) and bottom values.
    p1 = 0
    top = y_1.copy()
    delta_h = height
    getTop(top,sides,height,p1,delta_h)
    top1 = top.flatten()
    bottom = np.zeros_like(top1)
    
    # Visualize 3D Pyramid 
    fig = plt.figure(figsize=(9,6))
    plot1 = fig.add_subplot(111, projection='3d')
    plot1.set_title(f'Pyramid sides = {sides}\nHeight = {height}')
    width = depth = 1

    plot1.bar3d(x_2,y_2,bottom,width,depth,top1,shade=True)
    return plt.show()

def main():
    # Start.
    print('\nWELCOME TO PYRAMID 3D')
    while True:
        try:
            sides = int(input('\nInput sides (sides=width=length) of your desired pyramid = '))
        except ValueError:
            print('\nInvalid input (integer only)!')
            continue
        else:
            if sides % 2 == 0:
                print('\nInput odd number only!')
                continue
            else:
                break
    while True:
        try:
            height = int(input('\nInput height difference of the pyramid = '))
        except ValueError:
            print('\nInvalid input (integer only)!')
            continue
        else:
            break
    # Print the result
    printPyramid(sides,height)

main()
