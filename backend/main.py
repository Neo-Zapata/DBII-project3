from sequential_search import *
from image_processing import *
import os

cwd = os.getcwd() # current working directory
processed_images_path = cwd + "/backend/processed_dataset"
filename = "processed_images.json"

class some_class():
    total = 13175
    block_dictionary = {}
    def __init__(self):
        pass

    def PROCESS_IMAGES(self):
        clear_processed_processes_directory()
        self.total, self.block_dictionary = process_dataset()

    def RANGE_SEARCH(self, file_name, radius):
        if(len(self.block_dictionary) == 0):
            # print(len(self.block_dictionary))
            # try to load with what is in the files
            self.block_dictionary = load_block_dictionary(self.block_dictionary, self.total)
            # print(len(self.block_dictionary))
            if(len(self.block_dictionary) == 0):

                print("data has not been processed..")
                return 0
            else:
                info = range_search(file_name, radius, cwd, self.block_dictionary)
                for key in info:
                    # print(key)
                    print("(" + str(key[0]) + ", " + str(key[1]) + ")")
        else:
            info = range_search(file_name, radius, cwd, self.block_dictionary)
            for key in info:
                # print(key)
                print("(" + str(key[0]) + ", " + str(key[1]) + ")")
    
    def KNN_SEARCH(self, file_name, k):
        # print(len(self.block_dictionary))
        if(len(self.block_dictionary) == 0):
            # try to load with what is in the files
            # print(len(self.block_dictionary))
            self.block_dictionary = load_block_dictionary(self.block_dictionary, self.total)
            # print(len(self.block_dictionary))
            if(len(self.block_dictionary) == 0):
                print("data has not been processed..")
                return 0
            else:
                info = knn_search(file_name, k, cwd, self.block_dictionary)
                counter = 0
                for key in info:
                    # print(key)
                    print(str(counter) + ") -> (" + str(key[0]) + ", " + str(key[1]) + ")")
                    counter += 1
        else:
            info = knn_search(file_name, k, cwd, self.block_dictionary)
            counter = 0
            for key in info:
                # print(key)
                print(str(counter) + ") -> (" + str(key[0]) + ", " + str(key[1]) + ")")
                counter += 1


# filename is provided
#  radius is provided
# cwd must be calculated before
# total must be calculated in init, is the number of encodings we have
# encodings is a list (example) with a relative order with the indexes
# paths is a list with a relative order with the indexes
#   it means that for index 0, encodings have an code, and paths have the name of that code in specific
# all of that calculated in init