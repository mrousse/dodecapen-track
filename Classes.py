# PI 2022/2023 - Manon ROUSSE
## Declaration of point, Side, dodecehedron and stylus classes

## Import
import numpy as np
from math import *
from matplotlib import cm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import *

# Turn a vector into an unitary vector
def mk_uni(vect):
    norm = sqrt(vect[0]**2 + vect[1]**2 + vect[2]**2)
    uni = [vect[0]/norm, vect[1]/norm, vect[2]/norm]
    return uni

# Display a little space marker
def space(ax):
    # X-axis
    ax.plot3D(np.array([0, 1]), np.array([0, 0]), np.array([0, 0]), color='red')
    # Y-axis
    ax.plot3D(np.array([0, 0]), np.array([0, 1]), np.array([0, 0]), color='blue')
    # Z-axis
    ax.plot3D(np.array([0, 0]), np.array([0, 0]), np.array([0, 1]), color='green')

    return


## Point declaration
class Point :

    # Attributes with type(coord) = list/array
    def __init__(self, coord):
        self.x = float(coord[0])
        self.y = float(coord[1])
        self.z = float(coord[2])

    # Methods

    # Getter
    def get_coord(self): 
        return [self.x, self.y, self.z]

    # Display a single point without axes declaration neither plt.show() but with color and marker options
    def disp_point(self, ax = plt.axes(projection='3d'), color = None, mark = 'o'): 
        ax.scatter(self.x, self.y, self.z, c=color, marker=mark)
        return

    # Translate a single point
    def transl(self, trans_vect):
        self.x = self.x + trans_vect[0]
        self.y = self.y + trans_vect[1]
        self.z = self.z + trans_vect[2]
        return

    # Rotate a single point around the axis represented by any vector by an angle in radian
    # def rot(self, rot_axe, angle):
    #     uni_axe = mk_uni(rot_axe)
    #     rot_matrix = np.array([[np.cos(angle) + uni_axe[0]**2 * (1 - np.cos(angle)),
    #                             uni_axe[0] * uni_axe[1] * (1 - np.cos(angle)) - uni_axe[2] * np.sin(angle),
    #                             uni_axe[0] * uni_axe[2] * (1 - np.cos(angle)) + uni_axe[1] * np.sin(angle)],
    #                            [uni_axe[1] * uni_axe[0] * (1 - np.cos(angle)) + uni_axe[2] * np.sin(angle),
    #                             np.cos(angle) + uni_axe[1]**2 * (1 - np.cos(angle)),
    #                             uni_axe[1] * uni_axe[2] * (1 - np.cos(angle)) - uni_axe[0] * np.sin(angle)],
    #                            [uni_axe[2] * uni_axe[0] * (1 - np.cos(angle)) - uni_axe[1] * np.sin(angle),
    #                             uni_axe[2] * uni_axe[1] * (1 - np.cos(angle)) + uni_axe[0] * np.sin(angle),
    #                             np.cos(angle) + uni_axe[2]**2 * (1 - np.cos(angle))]])
    #     coord = np.array([self.x, self.y, self.z])
    #     rotated_coord = np.dot(rot_matrix, coord)
    #     [self.x, self.y, self.z] = rotated_coord
    #     return

    # Rotate a single point by the given rotation matrix
    def rot(self, rot_mat):
        [self.x, self.y, self.z] = rot_mat @ self.get_coord()
        return

class Side :

    # Attributes 
    def __init__(self, vertexes):
        self.vertexes = vertexes  # must be list[Point]
        self.N = len(vertexes)

    # Methods

    # Display the side's edges 
    def disp_side(self, ax, color=None):
        # Store the coordinates of each points in the broken line
        X = np.zeros(len(self.vertexes)+1)
        Y = np.zeros(len(self.vertexes)+1)
        Z = np.zeros(len(self.vertexes)+1)

        for i in range(len(self.vertexes)+1):
            [X[i], Y[i], Z[i]] = self.vertexes[i-1].get_coord()
        ax.plot3D(X, Y, Z, color=color)

        return

class Dodecahedron :

    # Attributes
    def __init__(self):
        # Geometry of the dodecahedron
        self.p1 = Point([0.0, 0.6, 1.67])
        self.p2 = Point([1., 1., 1.])
        self.p3 = Point([1.67, 0.0, 0.6])
        self.p4 = Point([1., -1., 1.])
        self.p5 = Point([0.0, -0.6, 1.67])
        self.p6 = Point([-1., 1., 1.])
        self.p7 = Point([-1.67, 0.0, 0.6])
        self.p8 = Point([-1., -1., 1.])
        self.p9 = Point([-0.6, -1.67, 0.0])
        self.p10 = Point([0.6, -1.67, 0.0])
        self.p11 = Point([1., -1., -1.])
        self.p12 = Point([1.67, 0.0, -0.6])
        self.p13 = Point([1., 1., -1.])
        self.p14 = Point([0.6, 1.67, 0.0])
        self.p15 = Point([-0.6, 1.67, 0.0])
        self.p16 = Point([-1., 1., -1.])
        self.p17 = Point([-1.67, 0.0, -0.6])
        self.p18 = Point([-1., -1., -1.])
        self.p19 = Point([0.0, -0.6, -1.67])
        self.p20 = Point([0.0, 0.6, -1.67])
        
        # All apexes of the dodecahedron
        self.points = [self.p1,  self.p2,  self.p3,  self.p4,  self.p5,  self.p6,  self.p7,  self.p8,  self.p9,  self.p10,  self.p11,  self.p12,  self.p13,  self.p14,  self.p15,  self.p16,  self.p17,  self.p18,  self.p19,  self.p20]

        # Apexes of each side
        self.f1 = Side([self.points[3],  self.points[2],  self.points[1],  self.points[0],  self.points[4]])
        self.f2 = Side([self.points[7],  self.points[4],  self.points[0],  self.points[5],  self.points[6]])
        self.f3 = Side([self.points[7],  self.points[4],  self.points[3],  self.points[9],  self.points[8]])
        self.f4 = Side([self.points[11],  self.points[10],  self.points[9],  self.points[3],  self.points[2]])
        self.f5 = Side([self.points[13],  self.points[12],  self.points[11],  self.points[2],  self.points[1]])
        self.f6 = Side([self.points[0],  self.points[1],  self.points[13],  self.points[14],  self.points[5]])
        self.f7 = Side([self.points[5],  self.points[6],  self.points[16],  self.points[15],  self.points[14]])
        self.f8 = Side([self.points[7],  self.points[8],  self.points[17],  self.points[16],  self.points[6]])
        self.f9 = Side([self.points[8],  self.points[9],  self.points[10],  self.points[18],  self.points[17]])
        self.f10 = Side([self.points[18],  self.points[10],  self.points[11],  self.points[12],  self.points[19]])
        self.f11 = Side([self.points[15],  self.points[19],  self.points[12],  self.points[13],  self.points[14]])
        self.f12 = Side([self.points[17],  self.points[18],  self.points[19],  self.points[15],  self.points[16]])

        # All sides of the dodecahedron
        self.area = [self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7, self.f8, self.f9, self.f10, self.f11, self.f12]

        # Associate an AprilTag to each side by its name
        self.tags = ["" for i in range(12)]
        # Coordinates of the center of each tag
        self.tags_ctr = [Point([0.734, 0.0, 1.188]),
                         Point([-0.734, 0.0, 1.188]),
                         Point([0.0, -1.188, 0.734]),
                         Point([1.188, -0.734, 0.0]),
                         Point([1.188, 0.734, 0.0]),
                         Point([0.0, 1.188, 0.734]),
                         Point([-1.188, 0.734, 0.0]),
                         Point([-1.188, -0.734, 0.0]),
                         Point([0.0, -1.188, -0.734]),
                         Point([0.734, 0.0, -1.188]),
                         Point([0.0, 1.188, -0.734]),
                         Point([-0.734, 0.0, -1.188])]

        # Stylus features
        self.center = Point([0, 0, 0])

        # The handle will be put on the 12th side
        self.tip = Point([-5.724, 0.0, -9.264])
    

    # Methods

    # Display the apexes of the figure, the option allow to display the center too
    def disp_dodeca_apexes(self, ax, center = False):
        for i in range(20): 
            self.points[i].disp_point(ax)
        
        if(center):
            self.center.disp_point(ax, mark='x')

        return

    # Display the edges of the figure, the options allow to display the center and the tags too
    def disp_dodeca_edges(self, ax, center = False, tag=False, color=None):
        for j in range(12):
            self.area[j].disp_side(ax, color=color)

        if(center):
            self.center.disp_point(ax, mark='x')

        if(tag):
            for i in range(12):
                ax.text(self.tags_ctr[0].get_coord()[0], self.tags_ctr[0].get_coord()[1], self.tags_ctr[0].get_coord()[2], self.tags[i])

        return

    # Display a side and its center, the option allow to display the tag too
    def disp_tag_ctr(self, n, ax, tag=False):
        self.area[n-1].disp_side(ax)
        self.tags_ctr[n-1].disp_point(ax, mark='x')
        
        if(tag):
            for i in range(12):
                ax.text(self.tags_ctr[0].get_coord()[0], self.tags_ctr[0].get_coord()[1], self.tags_ctr[0].get_coord()[2], self.tags[i])

        return

    # Display the handle and tip of the stylus
    def disp_handle(self, ax):
        X = np.array([self.tags_ctr[11].get_coord()[0], self.tip.get_coord()[0]])
        Y = np.array([self.tags_ctr[11].get_coord()[1], self.tip.get_coord()[1]])
        Z = np.array([self.tags_ctr[11].get_coord()[2], self.tip.get_coord()[2]])
        ax.plot3D(X, Y, Z, color='gray')
        
        return
    
    # Rotate the entire figure around an axis by an radian angle
    def rot_dodeca(self, rot_mat):
        self.center.rot(rot_mat)
        self.tip.rot(rot_mat)
        for i in range(12):
            self.tags_ctr[i].rot(rot_mat)
        for i in range(20):
            self.points[i].rot(rot_mat)
        return

    # Translate the entire figure by a given vector
    def transl_dodeca(self, transl_vect):
        self.center.transl(transl_vect)
        self.tip.transl(transl_vect)
        for i in range(12):
            self.tags_ctr[i].transl(transl_vect)
        for i in range(20):
            self.points[i].transl(transl_vect)
        return

class Stylus:

    # Attibutes
    def __init__(self):
        self.center = Point([0, 0, 0])
        self.tip = Point([0, 0, 10.89])

        self.direction = Side([Point([1, 0, 0]), self.center, Point([-1, 0, 0]), self.center, Point([0, 1, 0]), self.center, Point([0, -1, 0]), self.center, Point([0, 0, -1]), self.center])
        return

    # Methods 

    # Display the stylus
    def disp_styl(self, ax, tip = True):
        self.center.disp_point(ax, mark='x')
        if tip:
            self.tip.disp_point(ax, mark='x')
        self.direction.disp_side(ax)

        # Display the handle
        X = np.array([self.center.get_coord()[0], self.tip.get_coord()[0]])
        Y = np.array([self.center.get_coord()[1], self.tip.get_coord()[1]])
        Z = np.array([self.center.get_coord()[2], self.tip.get_coord()[2]])
        ax.plot3D(X, Y, Z, color='gray')

        return

    # Rotate the sylus
    def rot_styl(self, rot_mat):
        self.center.rot(rot_mat)
        self.tip.rot(rot_mat)

        # Rotate the direction
        for i in range(int(len(self.direction.vertexes)/2)):
            self.direction.vertexes[2*i].rot(rot_mat)

        return

    # Translate the stylus
    def transl_styl(self, transl_vect):
        self.center.transl(transl_vect)
        self.tip.transl(transl_vect)

        # translate the direction
        for i in range(int(len(self.direction.vertexes)/2)):
            self.direction.vertexes[2*i].transl(transl_vect)

        return

    # Initialize the stylus through the correspondence w/ a dodecahedron
    # Keep in mind that the direction permit us to see only the relative rotation
    def set_styl(self, D):
        # Calculate the translation between the centers of the current stylus and the initializer
        translation = [D.center.get_coord()[0] - self.center.get_coord()[0], D.center.get_coord()[1] - self.center.get_coord()[1], D.center.get_coord()[2] - self.center.get_coord()[2]]
        self.transl_styl(translation)

        # Set the direction and tip on the 12th face of D
        rot = [D.tip.get_coord()[0] + self.tip.get_coord()[0], D.tip.get_coord()[1] + self.tip.get_coord()[1], D.tip.get_coord()[2] + self.tip.get_coord()[2]]
        self.rot_styl(rot, pi)

        return