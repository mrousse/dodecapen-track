# dodecapen-track

# Software for camera-based 6 degrees of freedom tracking
<p>Project provided by InSimo to 3 student in Master 1 in engineering school (fr. 2e année d'école d'ingé) 
<p>Purpose : tracking the movement of one DodecaPen or more 
<p>Equipment : a camera OAK-D by Luxonis and some DodecaPen with AprilTags from 21h7 Circle family 

We have to warn you : the project is not finished (and will not be). The detection of AprilTags failed (apparently due to depthAI and its detection function which might not be available for RCV2 any longer).
For what we know, the rest seems okay.

## Table of content 
- Dependencies and utilisation
- Usage
- Contributing
- License and contact

## Dependencies and utilisation
  We runned on python3. You will need the following packages :
  - Main and SDManager :
    - multiprocessing
  - Animation and Classes:
    - matplotlib
    - numpy
    - mpl_toolkits
    - math
  - DataMngt :
    - numpy
  - Generate :
    - random
    - time
    - math
    - numpy
  - ImageProc : 
    - cv2
    - depthai (must be change)
    - time
    - numpy
    - sys
    - pathlib
<\p> You only need the given files in the same folder and then you can run the main. Seems obvious but if you use ImageProc, you need to plug the camera.

## Usage
  This project was conceived to supply an external software with the deplacement of the DodecaPen
  based on its detection by the camera via its AprilTags. To test it we also provided a simple display 
  function and two generators of movement data (random and determined) to compensate for the lack of results from ImageProc.
  <\p>You can use it as a starting point to achieve the initial problem or only to use the given classes and functions for your own project.
    
## Contributing
  If you need any informations about this project, I would be pleased to answer you.

  I juste have to precise that this was from a scholar project which is over now.

  Despite this, we thought about the modifications to be made :
    - Find another AprilTags' detection 
    - Adjust the code to take into consideration several DodecaPen
    - Implement the initialisation phase
    - Optimize and clarify this version
    - Work on the interface (aesthetics and functionalities)
    - Analyze the performances and parameters 
      
## License and contact
  This project is completely open source as long as you credit us.

  As I said, we were three students working on this project : Clément CAPDEVILLE, Amandine DE RAGO and Manon ROUSSE (me). 
  You can contact me at manon.rousse@orange.fr


  
