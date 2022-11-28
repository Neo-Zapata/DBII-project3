
import time
import os
import numpy
import face_recognition
from queue import PriorityQueue 

def rangeSearchInd(file_name, radius, cwd, block_dictionary,idx,vectors):
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
            qmin = []
            qmax = []
            for d in new_face_encoding:
                qmin.append(d - r)
                qmax.append(d + r)
            q = qmin + qmax
            print("searching...")
            time1 = time.time()
            rangeValues = [n for n in idx.intersection(q)]
            result = []
            for path in rangeValues:
                dist = numpy.linalg.norm(numpy.asarray(
                    new_face_encoding)-numpy.asarray(vectors[path]))
                if dist < radius:
                    first = self.dict128VectorPhotos[str(tuple(self.vectors[path]))]
                    name = first.split('/')[1]
                    result.append((first, name, dist))
            result = sorted(result, key=lambda item: item[2])
            time2=time.time()
            for par in result:
                print(par[0], "\tname:", par[1], "\tdist:", par[2])
            print("Time in ms:", (end-start)*1000)
            return result
