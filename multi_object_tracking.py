# USAGE
# python ThreadingNew.py --video 5.avi --tracker csrt

# update1, update2, update3, update4 are the four tracker functions which are executed in threads initialized and started in the 
# init function of the class


from imutils.video import VideoStream
from imutils.video import FPS
import argparse
import imutils
import time
import cv2
import numpy as np
import threading
from time import sleep

from threading import Thread
import cv2, time


class MULTI_OBJECT_TRACKER(object):
    def __init__(self, tracker_args):

        # all global variables are defined here

        self.tracker_1 = None
        self.tracker_2 = None
        self.tracker_3 = None
        self.tracker_4 = None

        self.tracker_1_success = False
        self.tracker_2_success = False
        self.tracker_3_success = False
        self.tracker_4_success = False

        self.tracker_2_box = []
        self.tracker_1_box = []
        self.tracker_3_box = []
        self.tracker_4_box = []

        self.fps = 0
        self.fps1 = 0
        self.fps2 = 0
        self.fps3 = 0
        self.fps4 = 0

        self.frame = None

        self.t1flag = True
        self.t2flag = True
        self.t3flag = True
        self.t4flag = True

        self.OPENCV_OBJECT_TRACKERS = OPENCV_OBJECT_TRACKERS = {
            "csrt": cv2.TrackerCSRT_create,
            "kcf": cv2.TrackerKCF_create,
            "boosting": cv2.TrackerBoosting_create,
            "mil": cv2.TrackerMIL_create,
            "tld": cv2.TrackerTLD_create,
            "medianflow": cv2.TrackerMedianFlow_create,
            "mosse": cv2.TrackerMOSSE_create}

        self.tracker_name = tracker_args['tracker']  # Tracker name
        self.capture = self.grab_video(tracker_args)  # Video capturing
        
        frame_width = int(self.capture.get(3))
        frame_height = int(self.capture.get(4))
        size = (frame_width, frame_height)
        
        self.result = cv2.VideoWriter('output/output.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         30, size)
        
        self.thread1 = Thread(target=self.update1, args=())  # making and starting thread1
        self.thread1.daemon = True
        self.thread1.start()

        self.thread2 = Thread(target=self.update2, args=())  # making and starting thread2
        self.thread2.daemon = True
        self.thread2.start()

        self.thread3 = Thread(target=self.update3, args=())  # making and starting thread3
        self.thread3.daemon = True
        self.thread3.start()

        self.thread4 = Thread(target=self.update4, args=())  # making and starting thread4
        self.thread4.daemon = True
        self.thread4.start()


    def grab_video(self,tracker_args):
        # if a video path was not supplied, grab the reference to the web cam
        if not tracker_args.get("video", False):
            print("[INFO] starting video stream....")
            vs = cv2.VideoCapture('rtsp://admin:admin123@192.168.1.108')
            time.sleep(5)
            #print(1)

        # otherwise, grab a reference to the video file
        else:
            vs = cv2.VideoCapture(tracker_args["video"])

        return vs

    def create_tracker(self):
        created_tracker = self.OPENCV_OBJECT_TRACKERS[self.tracker_name]()
        if self.tracker_name == "csrt":
            fs = cv2.FileStorage("params.json", cv2.FileStorage_READ)
            created_tracker.read(fs.root())

        return created_tracker



    def update2(self):
        # loop_time_start = time.time()
        loop_freq = self.capture.get(cv2.CAP_PROP_FPS)

        #self.Tracker2 = self.OPENCV_OBJECT_TRACKERS[self.tracker_name]()
        self.Tracker2 = self.create_tracker()
        while (1):
            loop_time_start = time.time()
            if self.capture.isOpened():
                if self.frame is None:
                    # print(1)

                    continue
                if self.tracker_2 is not None:

                    (self.tracker_2_success, self.tracker_2_box) = self.Tracker2.update(self.frame)
                    c = (time.time() - loop_time_start)
                    if c != 0:
                        self.fps2 = 1 / c  # check if the denominator of the is not zero
                        c = 0
                else:
                    self.tracker_2 = None
            self.t2flag = False

    def update1(self):

        loop_freq = self.capture.get(cv2.CAP_PROP_FPS)
        self.Tracker1 = self.create_tracker()
        while True:
            loop_time_start = time.time()
            if self.capture.isOpened():

                if self.frame is None:
                    continue
                if self.tracker_1 is not None:
                    (self.tracker_1_success, self.tracker_1_box) = self.Tracker1.update(self.frame)

                    c = (time.time() - loop_time_start)
                    if c != 0:  # check if the denominator of the is not zero
                        self.fps1 = 1 / c
                        c = 0


                else:
                    self.tracker_1 = None

            self.t1flag = False

    def update3(self):

        self.Tracker3 = self.create_tracker()
        while True:
            loop_time_start = time.time()

            if self.capture.isOpened():
                if self.frame is None:
                    continue
                if self.tracker_3 is not None:
                    (self.tracker_3_success, self.tracker_3_box) = self.Tracker3.update(self.frame)
                    c = (time.time() - loop_time_start)
                    if c != 0:
                        self.fps3 = 1 / c  # check if the denominator of the is not zero
                        c = 0

                else:
                    self.tracker_3 = None

            self.t3flag = False

    def update4(self):

        self.Tracker4 = self.create_tracker()
        while True:
            loop_time_start = time.time()
            if self.capture.isOpened():
                if self.frame is None:
                    continue
                if self.tracker_4 is not None:
                    print(1)
                    (self.tracker_4_success, self.tracker_4_box) = self.Tracker4.update(self.frame)
                    c = (time.time() - loop_time_start)
                    if c != 0:
                        self.fps4 = 1 / c  # check if the denominator of the is not zero
                        c = 0

                else:
                    self.tracker_4 = None

            self.t4flag = False

    def show_frame(self):
        loop_freq = self.capture.get(cv2.CAP_PROP_FPS)
        while True:
            loop_time_start = time.time()
            ret, self.frame = self.capture.read()
            # self.frame_read_time = time.time() - loop_time_start
            (H, W) = self.frame.shape[:2]

            while self.t1flag or self.t2flag or self.t3flag or self.t4flag:  # waiting for every thread output
                cv2.waitKey(1)

            self.t1flag = self.t2flag = self.t3flag = self.t4flag = True

            if self.tracker_1_success:
                (x, y, w, h) = [int(v) for v in self.tracker_1_box]
                cv2.rectangle(self.frame, (x, y), (x + w, y + h),
                              (0, 255, 255), 2)

            if self.tracker_2_success:
                (x, y, w, h) = [int(v) for v in self.tracker_2_box]
                cv2.rectangle(self.frame, (x, y), (x + w, y + h),
                              (0, 255, 0), 2)

            if self.tracker_3_success:
                (x, y, w, h) = [int(v) for v in self.tracker_3_box]
                cv2.rectangle(self.frame, (x, y), (x + w, y + h),
                              (0, 0, 255), 2)

            if self.tracker_4_success:
                (x, y, w, h) = [int(v) for v in self.tracker_4_box]
                cv2.rectangle(self.frame, (x, y), (x + w, y + h),
                              (255, 255, 0), 2)

            tracker_info = [
                ("Tracker W (W key to initiate then press space) Success", "Yes" if self.tracker_2_success else "No", (0, 255, 0)),
                ("Tracker E (E key to initiate then press space) Success", "Yes" if self.tracker_1_success else "No", (0, 255, 255)),
                ("Tracker R (R key to initiate then press space) Success", "Yes" if self.tracker_3_success else "No", (0, 0, 255)),
                ("Tracker T (T key to initiate then press space) Success", "Yes" if self.tracker_4_success else "No", (255, 255, 0))
            ]

            for (i, (k, v, (color_r, color_g, color_b))) in enumerate(tracker_info):
                text = "{}: {}".format(k, v)
                cv2.putText(self.frame, text, (10, ((i * 20) + 20)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (color_r, color_g, color_b), 2)
            info = [
                ("Video FPS", "{:.2f}".format(self.fps)),
                ("Tracker: ", '{:}'.format(tracker_args['tracker'])),
            ]

            for (i, (k, v)) in enumerate(info):
                text = "{}: {}".format(k, v)
                cv2.putText(self.frame, text, (10, H - ((i * 20) + 20)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            cv2.imshow('frame', self.frame)  # showing the result

            # print((time.time()-loop_time_start) - self.delay)
            self.key = cv2.waitKey(20)

            if self.key & 0xFF == ord('w'):
                self.tracker_2 = cv2.selectROI('frame', self.frame, fromCenter=False,
                                             showCrosshair=True)
                print(self.tracker_2)
                self.Tracker2 = self.create_tracker()
                #self.Tracker2 = self.create_tracker(tracker_args)
                self.Tracker2.init(self.frame, self.tracker_2)

            if self.key & 0xFF == ord('e'):
                self.tracker_1= cv2.selectROI('frame', self.frame, fromCenter=False,
                                             showCrosshair=True)
                self.Tracker1 = self.create_tracker()
                self.Tracker1.init(self.frame, self.tracker_1)
                
                # self.fps1 = FPS().start()
                print(self.tracker_1)

            if self.key & 0xFF == ord('r'):
                self.tracker_3 = cv2.selectROI('frame', self.frame, fromCenter=False,
                                             showCrosshair=True)
                #self.Tracker3 = self.OPENCV_OBJECT_TRACKERS[self.tracker_name]()
                self.Tracker3 = self.create_tracker()
                self.Tracker3.init(self.frame, self.tracker_3)

                print(self.tracker_3)

            if self.key & 0xFF == ord('t'):
                self.tracker_4 = cv2.selectROI('frame', self.frame, fromCenter=False,
                                             showCrosshair=True)
                self.Tracker4 = self.create_tracker()
                self.Tracker4.init(self.frame, self.tracker_4)

                print(self.tracker_4)

            if self.key == ord('q'):
                self.capture1.release()
                cv2.destroyAllWindows()
                exit(1)

            # Run loop maximum at video frequency
            time.sleep(max(0, (1 / loop_freq) - (time.time() - loop_time_start)))
            self.fps = 1 / (time.time() - loop_time_start)
            self.result.write(self.frame)
        self.result.release()
        


if __name__ == '__main__':

    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", type=str,
                help="path to input video file")
    ap.add_argument("-t", "--tracker", type=str, default="kcf",
                help="OpenCV object tracker type")
    ap.add_argument("-b", "--BBox", type=str, default=None,
                help="Enter BBox: Syntax (x, y, w, h)")
    tracker_args = vars(ap.parse_args())


    multi_object_tracker = MULTI_OBJECT_TRACKER(tracker_args)

    try:
        multi_object_tracker.show_frame()
    except AttributeError:
        pass
