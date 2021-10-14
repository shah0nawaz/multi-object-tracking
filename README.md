# MOT: Multiple Object Trackig
An Mutiple Object Tracking Project

[![Mask RCNN on 4K Video](output/output.avi)]


This repository implements the opencv single object tracking class for multiple object tracking using python threading module on CPU. Because if you use sigle object tracking class of opencv sequential without using threading module on CPU it will slow down the frame rate of the tracker and you cannot use it in real time. 
Besides, if you use multi object tracking class of opencv it does not give you the success score of every tracker. so you cannot interupte the every object during tracking.



