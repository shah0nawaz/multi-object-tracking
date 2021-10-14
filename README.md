# MOT: Multiple Object Trackig
An Mutiple Object Tracking Project

[![Mask RCNN on 4K Video](output/output.avi)]


This repository implements the opencv single object tracking class for multiple object tracking using python threading module on CPU. Because if you use single object tracking class of opencv sequentially without using threading module on CPU it will slow down the frame rate of the tracker and you cannot use it in real time. 
Besides, if you use multi object tracking class of opencv it does not give you the success score of every tracker. so you cannot interupte every object during tracking.


### 1. Installation

---

    git clone https://github.com/shah0nawaz/multi-object-tracking.git
    cd muti-object-tracking
    pip install -r requirements.txt

---

### 1. Running CVDV

    python main.py --video input/race.mp4 --tracker csrt

1.1 **Parameters:**

    --data_dir: Path of dataset directory

    --details_level: Levels of details you wannt to fetch
        . default: only class level information, or leave empty
        . all: for image level and object level information

    --im_size: Size of the images for [SQUARE IMAGES]

    --im_h: Height of the image for [NON-SQUARE IMAGES]
    --im_w: Width of the image for [NON-SQUARE IMAGES]





