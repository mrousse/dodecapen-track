# PI 2022/2023 - Manon ROUSSE for Insimo
# Launch multithreading to :
#   Aquire images from an OAK-D by Luxonis, detect visibles AprilTags and calculate the translation and rotation between two positions -> generate
#   Manage the data flow -> data_mngt
#   Display the DodecaPen's movement in a 3D-animation -> anim
from Anim import *
from Generate import *
from DataMngt import *
from ImageProc import *
from SDManager import *
from multiprocessing import Process, Manager


if __name__ == '__main__':

    # My Managers
    manager = SD_manager()
    manager.start()
    current_SD = manager.SD()

    # Writer : generate & Reader : data_mngt
    Q = Queue()

    processes = []

    # Generating random transformation process
    generate = Process(target=def_generate, args=(current_SD, Q,))
    processes.append(generate)

    # Data aquisition and treatment process
    data = Process(target=data_mngt, args=(current_SD, Q,))
    processes.append(data)

    # Animation process
    anim = Process(target=animate, args=(current_SD, Q,))
    processes.append(anim)
    
    # Lauch processes
    for p in processes:
        p.start()
    # Wait for processes termination
    for p in processes:
        p.join()
        # p.join(timeout=10)

    print("Finally a run without any error !")
    manager.shutdown()
