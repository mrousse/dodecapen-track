# PI 2022/2023 - Manon ROUSSE
# Set the data management
from multiprocessing import Lock
import numpy as np

def data_mngt(SD, Q):
    while True :
        cur_gen_data = Q.get()
        # print("mngt : ", cur_gen_data)

        # Modification only in this process to avoid every writing conflict
        if SD.get_read() == True :
            SD.update_transl_vect(np.zeros(3))
            SD.update_rot_mat(np.eye(3))
            # print("test read : ", SD.get_transl_vect())
        
        # If data not read, must not lose the previous transformation but add the new ones
        new_transl_vect = (SD.get_transl_vect()) + cur_gen_data[0][0]
        # print("somme transl : ", SD.get_transl_vect(), cur_gen_data[0][0], new_transl_vect)
        SD.update_transl_vect(new_transl_vect)
        new_rot_mat = (SD.get_rot_mat()) @ cur_gen_data[1]
        SD.update_rot_mat(new_rot_mat)
        SD.update_read(False)

    return