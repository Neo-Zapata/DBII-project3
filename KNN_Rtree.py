from typing import Collection
import face_recognition
import numpy
import matplotlib.pyplot as plt
import random
import json
import linecache
import io
from rtree import index
import os
from os.path import join, dirname, realpath
from queue import PriorityQueue
from timeit import default_timer as timer
import time


path_data = "data.json"


def KNNSearchInd(file_name, K, cwd,block_dictionary,idx,vectors):
  image_path = cwd + '/backend/test_images/' + file_name
  if not os.path.exists(image_path):
        print("No path")
        return 0
  else:
        face = face_recognition.load_image_file(image_path)
        face_encoding = face_recognition.face_encodings(face) # calculating the image encoding
        if len(face_encoding) == 0:
            print("no face founnd")
            return 0
        else:
          new_face_encoding = tuple(face_encoding)
          result=[]
          time1=time.time()
          path = list(idx.nearest(coordinates=new_face_encoding, num_results=K))    
          for path in block_dictionary:
             first = numpy.array(list(map(float, block_dictionary[path].strip("()").split(', '))))
             name = first.split('/')[1]
             dist = numpy.linalg.norm(numpy.asarray(vectors[x])-numpy.asarray(new_face_encoding))
             print(new_face_encoding, "\tname:", name, "\tdist:", dist)
             result.append((first, name, dist))
          time2=time.time()   
          print("Time in ms:", (end-start)*1000)
          return result
