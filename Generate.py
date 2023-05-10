# PI 2022/2023 - Manon ROUSSE
# Generate random data - Testing and demo purpose
import random as rd
import time
import numpy as np
import math as mt
from Classes import mk_uni

def rd_generate(SD, Q):
    while True :
        delay_time = rd.gauss(0.33, 0.06)

        # Generate random transation
        rd_transl_vect = np.array([rd.randrange(-5, 5), rd.randrange(-5, 5), rd.randrange(-5, 5)])

        # Generate random rotation
        rd_rot_axe = mk_uni( np.array([rd.randrange(-3, 3), rd.randrange(-3, 3), rd.randrange(-3, 3)]) )
        rd_angle = 2* mt.pi * rd.random()
        rd_rot_mat = rot_matrix = np.array([[np.cos(rd_angle) + rd_rot_axe[0]**2 * (1 - np.cos(rd_angle)),
        rd_rot_axe[0] * rd_rot_axe[1] * (1 - np.cos(rd_angle)) - rd_rot_axe[2] * np.sin(rd_angle),
        rd_rot_axe[0] * rd_rot_axe[2] * (1 - np.cos(rd_angle)) + rd_rot_axe[1] * np.sin(rd_angle)],
        [rd_rot_axe[1] * rd_rot_axe[0] * (1 - np.cos(rd_angle)) + rd_rot_axe[2] * np.sin(rd_angle),
        np.cos(rd_angle) + rd_rot_axe[1]**2 * (1 - np.cos(rd_angle)),
        rd_rot_axe[1] * rd_rot_axe[2] * (1 - np.cos(rd_angle)) - rd_rot_axe[0] * np.sin(rd_angle)],
        [rd_rot_axe[2] * rd_rot_axe[0] * (1 - np.cos(rd_angle)) - rd_rot_axe[1] * np.sin(rd_angle),
        rd_rot_axe[2] * rd_rot_axe[1] * (1 - np.cos(rd_angle)) + rd_rot_axe[0] * np.sin(rd_angle),
        np.cos(rd_angle) + rd_rot_axe[2]**2 * (1 - np.cos(rd_angle))]])

        Q.put((rd_transl_vect, rd_rot_mat))

        time.sleep(delay_time)

def def_generate(SD, Q):
    start_time = time.time()
    n = 0
    while True:
        if (time.time() - start_time > 2) & (time.time() - start_time < 5) :
            if n == 0:
                rd_transl_vect = np.array([[5, 0, 0]])
                rd_rot_mat = np.eye(3)
                Q.put((rd_transl_vect, rd_rot_mat))
                start_time = time.time()                
                print("t1")
                n += 1

            elif n == 1 :
                rd_transl_vect = np.array([[0, 0, 0]])
                # rd_rot_mat = np.eye(3)
                rd_rot_mat = np.array([[ 0., 0., -1.],
                                        [ 0. , 1.,  0.],
                                        [1.,  0., 0. ]])
                Q.put((rd_transl_vect, rd_rot_mat))
                start_time = time.time()                
                print("t2")
                n += 1

            elif n == 2 :
                rd_transl_vect = np.array([[0, 0, 5]])
                rd_rot_mat = np.eye(3)
                Q.put((rd_transl_vect, rd_rot_mat))
                start_time = time.time()                
                print("t3")
                n += 1

        else :
            rd_transl_vect = np.array([0, 0, 0])
            rd_rot_mat = np.eye(3)
            Q.put((rd_transl_vect, rd_rot_mat))
            time.sleep(0.1)

    

    

    