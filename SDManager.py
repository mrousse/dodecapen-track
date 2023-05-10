# PI 2022/2023 - Manon ROUSSE
# Declaration of custom class to share data between processes and custom manager to handle it
from multiprocessing.managers import BaseManager
from multiprocessing import Queue, Lock
from Classes import *
import matplotlib.pyplot as plt

# Custom class
class SD :
    ## Attributes
    def __init__(self):
        self.D = Dodecahedron()

        # Writer : data_mngt & Reader : animate
        self.transl_vect = np.zeros(3)
        self.rot_mat = np.eye(3)

        # Reader : data_mngt & Writer : animate
        self.read = False

        return
    
    def get_D(self):
        return self.D
    
    def update_D(self, rot_mat, transl_vect): 
        self.D.rot_dodeca(rot_mat)
        self.D.transl_dodeca(transl_vect)
    
    def disp_D(self, ax):
        self.get_D().disp_dodeca_edges(ax)
        self.get_D().disp_handle(ax)
    
    def get_transl_vect(self):
        return self.transl_vect
    
    def update_transl_vect(self, new_transl):
        self.transl_vect = new_transl
    
    def get_rot_mat(self):
        return self.rot_mat
    
    def update_rot_mat(self, new_rot):
        self.rot_mat = new_rot
    
    def get_read(self):
        return self.read
    
    def update_read(self, new_read):
        self.read = new_read
    
    



# Custom manager
class SD_manager(BaseManager):
    pass

SD_manager.register('SD', SD)
