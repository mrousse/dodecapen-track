#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 14:07:37 2022

@author: amandine
"""

#!/usr/bin/env python3

import cv2
import depthai as dai
import time
import numpy as np
import sys
from pathlib import Path



def Image_Processing(Shared_Data, Q):
    # Create pipeline
    pipeline = dai.Pipeline()
    
    # Define sources and outputs
    camRgb = pipeline.create(dai.node.ColorCamera)
    aprilTag = pipeline.create(dai.node.AprilTag)
    manip = pipeline.create(dai.node.ImageManip)
    
    xoutAprilTag = pipeline.create(dai.node.XLinkOut)
    xoutAprilTagImage = pipeline.create(dai.node.XLinkOut)
    
    xoutAprilTag.setStreamName("aprilTagData")
    xoutAprilTagImage.setStreamName("aprilTagImage")
    
    # Properties
    camRgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
    camRgb.setBoardSocket(dai.CameraBoardSocket.RGB)
    
    manip.initialConfig.setResize(480, 270)
    manip.initialConfig.setFrameType(dai.ImgFrame.Type.GRAY8)
    
    aprilTag.initialConfig.setFamily(dai.AprilTagConfig.Family.TAG_CIR21H7)
    
    # Linking
    aprilTag.passthroughInputImage.link(xoutAprilTagImage.input)
    camRgb.video.link(manip.inputImage)
    manip.out.link(aprilTag.inputImage)
    aprilTag.out.link(xoutAprilTag.input)
    # always take the latest frame as apriltag detections are slow
    aprilTag.inputImage.setBlocking(False)
    aprilTag.inputImage.setQueueSize(1)
    
    # Connect to device and start pipeline
    with dai.Device(pipeline) as device:
    
        # Output queue will be used to get the mono frames from the outputs defined above
        manipQueue = device.getOutputQueue("aprilTagImage", 8, False)
        aprilTagQueue = device.getOutputQueue("aprilTagData", 8, False)
    #    calibData = device.readCalibration()
    #    intrinsics = calibData.getCameraIntrinsics(dai.CameraBoardSocket.RIGHT)
    #    print('Right mono camera focal length in pixels:', intrinsics[0][0])
    #    intrinsics = calibData.getCameraIntrinsics(dai.CameraBoardSocket.LEFT)
    #    print('Left mono camera focal length in pixels:', intrinsics[0][0])
    
        calibFile = str((Path(__file__).parent / Path(f"calib_{device.getMxId()}.json")).resolve().absolute())
        if len(sys.argv) > 1:
            calibFile = sys.argv[1]
    
        calibData = device.readCalibration()
        calibData.eepromToJsonFile(calibFile)
        
        M_left = np.array(calibData.getCameraIntrinsics(dai.CameraBoardSocket.RGB, 480, 270))
    #    print("LEFT Camera resized intrinsics...  480 x 270")
    #    print(M_left)
    
    
        M_right = np.array(calibData.getCameraIntrinsics(dai.CameraBoardSocket.RIGHT, 480, 270))
    #    print("RIGHT Camera resized intrinsics... 480 x 270")
    #    print(M_right)
    #    
        D_left = np.array(calibData.getDistortionCoefficients(dai.CameraBoardSocket.RGB))
    #    print("LEFT Distortion Coefficients...")
    #    print(D_left)
    #    
        
        color = (0, 255, 0)
    
        startTime = time.monotonic()
        counter = 0
        fps = 0
        i=0
        numero_tag=[]
        sup_droit_x=[]
        sup_droit_y=[]
        sup_gauche_x=[]
        sup_gauche_y=[]
        inf_droit_x=[]
        inf_droit_y=[]
        inf_gauche_x=[]
        inf_gauche_y=[]
    
        
        while(True):
            Rotation = np.eye(3)
            Translation = np.zeros(3)
            inFrame = manipQueue.get()
    
            counter+=1
            current_time = time.monotonic()
            if (current_time - startTime) > 1 :
                fps = counter / (current_time - startTime)
                counter = 0
                startTime = current_time
    
            monoFrame = inFrame.getFrame()
            frame = cv2.cvtColor(monoFrame, cv2.COLOR_GRAY2BGR)
    
            aprilTagData = aprilTagQueue.get().aprilTags
            for aprilTag in aprilTagData:
                topLeft = aprilTag.topLeft
                topRight = aprilTag.topRight
                bottomRight = aprilTag.bottomRight
                bottomLeft = aprilTag.bottomLeft
    
                center = (int((topLeft.x + bottomRight.x) / 2), int((topLeft.y + bottomRight.y) / 2))
    
                cv2.line(frame, (int(topLeft.x), int(topLeft.y)), (int(topRight.x), int(topRight.y)), color, 2, cv2.LINE_AA, 0)
                cv2.line(frame, (int(topRight.x), int(topRight.y)), (int(bottomRight.x), int(bottomRight.y)), color, 2, cv2.LINE_AA, 0)
                cv2.line(frame, (int(bottomRight.x), int(bottomRight.y)), (int(bottomLeft.x), int(bottomLeft.y)), color, 2, cv2.LINE_AA, 0)
                cv2.line(frame, (int(bottomLeft.x), int(bottomLeft.y)), (int(topLeft.x), int(topLeft.y)), color, 2, cv2.LINE_AA, 0)
    
                idStr = "ID: " + str(aprilTag.id)
                cv2.putText(frame, idStr, center, cv2.FONT_HERSHEY_TRIPLEX, 0.5, color)
                
    #            print("ID: ", str(aprilTag.id))
    #            print("top left : ",topLeft.x, ",", topLeft.y,"top right : ",topRight.x, ",", topRight.y,"bottom left : ",bottomLeft.x, ",", bottomLeft,"bottom right : ",bottomRight.x, ",", bottomRight.y)
    #            print("centre : ", center[0], ",", center[1])
                sup_gauche_x.append(topLeft.x)
                sup_gauche_y.append(topLeft.y)
                sup_droit_x.append(topRight.x)
                sup_droit_y.append(topRight.y)
                inf_gauche_x.append(bottomLeft.x)
                inf_gauche_y.append(bottomLeft.y)
                inf_droit_x.append(bottomRight.x)
                inf_droit_y.append(bottomRight.y)
                numero_tag.append(str(aprilTag.id))
                
                if i>1 :
                    del(sup_gauche_x[0])
                    del(sup_gauche_y[0])
                    del(sup_droit_x[0])
                    del(sup_droit_y[0])
                    del(inf_gauche_x[0])
                    del(inf_gauche_y[0])
                    del(inf_droit_x[0])
                    del(inf_droit_y[0])
                    del(numero_tag[0])
                #print(numero_tag,sup_gauche_x,sup_gauche_y,sup_droit_x,sup_droit_y,inf_gauche_x,inf_gauche_y,inf_droit_x,inf_droit_y)
                
                
        
                objectPoints=np.array([[-1,1,1], [1,1,1], [-1,-1,1], [1,-1,1]],dtype=np.float32)
               
                imagePoints0=np.array([[sup_gauche_x[0],sup_gauche_y[0]], [sup_droit_x[0],sup_droit_y[0]], [inf_gauche_x[0],inf_gauche_y[0]], [inf_droit_x[0],inf_droit_y[0]]],dtype=np.float32)
                
                [retval0, rvecs0, tvecs0] = cv2.solveP3P(objectPoints, imagePoints0, np.array(M_left), np.array(D_left),cv2.SOLVEPNP_P3P)
                if i>0:
                    imagePoints1=np.array([[sup_gauche_x[1],sup_gauche_y[1]], [sup_droit_x[1],sup_droit_y[1]], [inf_gauche_x[1],inf_gauche_y[1]], [inf_droit_x[1],inf_droit_y[1]]],dtype=np.float32)
                    [retval1, rvecs1, tvecs1] = cv2.solveP3P(objectPoints, imagePoints1, np.array(M_left), np.array(D_left),cv2.SOLVEPNP_P3P)
                    mat1=cv2.Rodrigues(rvecs1[0])
                    # print("mat=",mat1[0])
                    # print("tvecs=",tvecs1[0])
                
                
                mat0=cv2.Rodrigues(rvecs0[0])
               
                
                #print("roulette",i)
                #print("rvecs=",rvecs0[0])
                # print("mat=",mat0[0])
                # print("tvecs=",tvecs0[0])
                if i>0:
                
                    
                    if numero_tag[0]==numero_tag[1]:
                        Translation=tvecs1[0]-tvecs0[0]
                        Rotation=mat1[0]@(np.linalg.inv(mat0[0]))
                        # print("T=",Translation)
                        # print("R=",Rotation)
                
                    else :
                        
                        print("changement de tag : problème")
                else :
                    Translation=tvecs0[0]
                    Rotation=mat0[0]
                    print("T=",Translation)
                    print("R=",Rotation)
                    
    
                
                
                 
                Q.put((Translation.transpose(), Rotation))  
                i+=1
                
                
                
                
                
                
            cv2.putText(frame, "Fps: {:.2f}".format(fps), (2, frame.shape[0] - 4), cv2.FONT_HERSHEY_TRIPLEX, 0.4, (255,255,255))
    
            cv2.imshow("April tag frame", frame)
    
            if cv2.waitKey(1) == ord('q'):
                break

    return