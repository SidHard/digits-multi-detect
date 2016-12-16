import sys
import numpy
import caffe
from matplotlib import pyplot
import cv2
import datetime

WEIGHTS_FILE = 'model/model.caffemodel'
DEPLOY_FILE = 'model/deploy.prototxt'

caffe.set_mode_gpu()
net = caffe.Net(DEPLOY_FILE, WEIGHTS_FILE, caffe.TEST)
IMAGE_SIZE = net.blobs['data'].data.shape[1:]
print IMAGE_SIZE
# net.blobs['data'].reshape(1, 3, *IMAGE_SIZE)

idx = 0
total_loss = 0.0

image_list = 'fullpath.txt'

with open(image_list, 'r') as f:
    for line in f.readlines():
        img_orig = cv2.imread(line.strip())
        # print img_orig

        # img_orig = cv2.imread('6.jpg')
        start_time = datetime.datetime.now()
        img = cv2.resize(img_orig, (IMAGE_SIZE[2], IMAGE_SIZE[1]))
        img = numpy.transpose(img, [2, 0, 1])
        # img -= 127.0

        net.blobs['data'].data[...] = [img]

        output = net.forward()
        pose = output['bbox-list']
        m_color = [(0, 0, 255), (0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 0, 255)]
        for classes in range(len(pose)):
            pose_predict = pose[classes][0]
            process_time = datetime.datetime.now()-start_time
            print process_time
            img_orig = cv2.resize(img_orig, (IMAGE_SIZE[2], IMAGE_SIZE[1]))
            for idx in range(len(pose_predict)):
                pt1 = (pose_predict[idx][0], pose_predict[idx][1])
                pt2 = (pose_predict[idx][2], pose_predict[idx][3])
                if pt2[0] != 0:
                    color_class = classes%5
                    cv2.rectangle(img_orig, pt1, pt2, m_color[color_class], 2)
        cv2.imshow('1', img_orig)
        cv2.waitKey(1)

