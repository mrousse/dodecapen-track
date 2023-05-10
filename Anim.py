# PI 2022/2023 - Manon ROUSSE
# Set the animation process
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

# Function to update the object's position and the figure
def animate(SD, Q):
    n = 0 # use it to make a timeout in the while's condition in the debug process 
    l = 20

    ax = plt.axes(projection='3d')
    while True  :
        n += 1 
        ax.clear()

        # Read data
        transl_vect = SD.get_transl_vect()
        rot_mat = SD.get_rot_mat()
        SD.update_read(True)
        Q.put(([np.zeros(3)], np.eye(3)))

        # Move the object around
        SD.update_D(rot_mat, transl_vect)

        # Diplay the object in the new position
        SD.get_D().disp_dodeca_edges(ax)
        SD.get_D().disp_handle(ax)

        # Set the right POV (ie XZ-view, like in a mirror) and view frame
        ax.view_init(elev=0 , azim=-90)
        ax.set_xlim3d(-l, l)
        ax.set_ylim3d(-l, l)
        ax.set_zlim3d(-l, l)

        plt.pause(0.1) # To achieve the frame goal 


    return
