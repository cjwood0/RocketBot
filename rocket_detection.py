import cv2
import os
import numpy as np

initialize = True
net = None

def get_output_layers(net):
  layer_names = net.getLayerNames()
  output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
  return output_layers


def detect_common_objects(image, confidence=0.05, nms_thresh=0.05, model='yolov3', enable_gpu=False):
  Height, Width = image.shape[:2]
  scale = 0.00392

  global initialize
  global net

  blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

  if initialize:
    weights_file_name = './yolov3-tiny.weights'
    config_file_name = './yolov3-tiny.cfg'
    net = cv2.dnn.readNet(weights_file_name, config_file_name)
    initialize = False

  net.setInput(blob)

  outs = net.forward(get_output_layers(net))

  dogs = 0
  for out in outs:
    for detection in out:
      scores = detection[5:]
      class_id = np.argmax(scores)
      max_conf = scores[class_id]
      if max_conf > confidence:
        # TODO CHECK CLASS ID
        dogs += 1

  return dogs