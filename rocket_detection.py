import cv2
import os
import numpy as np

initialize = True
net = None
classes = ['dog']
COLORS = [(1, 190, 200), (255, 153, 255), (0, 0, 255)]

def get_output_layers(net):
  layer_names = net.getLayerNames()
  output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
  return output_layers


def draw_bbox(img, bbox, labels, confidence, colors=None, write_conf=False):
  global COLORS
  global classes

  for i, label in enumerate(labels):
    color = COLORS[classes.index(label)]
    if write_conf:
      label += ' ' + str(format(confidence[i] * 100, '.2f')) + '%'

    cv2.rectangle(img, (bbox[i][0],bbox[i][1]), (bbox[i][2],bbox[i][3]), color, 2)
    cv2.putText(img, label, (bbox[i][0],bbox[i][1]-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

  return img

def detect_common_objects(image, confidence=0.5, nms_thresh=0.3, model='yolov3', enable_gpu=False):
  Height, Width = image.shape[:2]
  scale = 0.00392

  global classes
  global initialize
  global net

  config_file_name = './yolov3-tiny.cfg'
  weights_file_name = './yolov3-tiny.weights'
  blob = cv2.dnn.blobFromImage(image, scale, (416,416), (0,0,0), True, crop=False)

  if initialize:
    classes = populate_class_labels()
    net = cv2.dnn.readNet(weights_file_name, config_file_name)
    initialize = False

  net.setInput(blob)

  outs = net.forward(get_output_layers(net))

  class_ids = []
  confidences = []
  boxes = []

  for out in outs:
    for detection in out:
      scores = detection[5:]
      class_id = np.argmax(scores)
      max_conf = scores[class_id]
      if max_conf > confidence:
        center_x = int(detection[0] * Width)
        center_y = int(detection[1] * Height)
        w = int(detection[2] * Width)
        h = int(detection[3] * Height)
        x = center_x - w / 2
        y = center_y - h / 2
        class_ids.append(class_id)
        confidences.append(float(max_conf))
        boxes.append([x, y, w, h])

  indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence, nms_thresh)

  bbox = []
  label = []
  conf = []

  for i in indices:
    i = i[0]
    box = boxes[i]
    x, y, w, h = box
    bbox.append([round(x), round(y), round(x+w), round(y+h)])
    label.append(str(classes[class_ids[i]]))
    conf.append(confidences[i])

  return bbox, label, conf