# MOT: Multiple Object Trackig
Mutiple Object Tracking Project

[![Watch the video](https://github.com/shah0nawaz/multi-object-tracking/blob/main/demo.mkv)


This repository implements the opencv single object tracking class for multiple object tracking using python threading module on CPU. Because if you use single object tracking class of opencv sequentially without using threading module on CPU it will slow down the frame rate of the tracker and you cannot use it in real time. 
Besides, if you use multi object tracking class of opencv it does not give you the success score of every tracker. so you cannot interupte every object during tracking.


### 1. Installation

---

    git clone https://github.com/shah0nawaz/multi-object-tracking.git
    cd muti-object-tracking
    pip install -r requirements.txt

---

### 1. Running MOT

    python main.py --video input/race.mp4 --tracker csrt





