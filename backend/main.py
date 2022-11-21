import face_recognition
# import numpy
# from os import listdir
import shutil
import os
# from os.path import isfile, join
import json

cwd = os.getcwd() # current working directory
processed_images_path = cwd + "/backend/processed_dataset"
filename = "processed_images.json"
BLOCK_SIZE = 15000 # documents, this number was arbitrary selected in order not to saturate the processing of images
path_to_clean_1 = processed_images_path

def process_dataset():

    if not os.path.exists(processed_images_path): # of the path for the processed imaged folder do not exist, create it
        os.makedirs(processed_images_path)

    counter = 0
    block_dictionary = {}
    # aux_list = [] # this is used to load each dictionary in an entry of the list, to append each entry in one line of the file, by iterating over this list
    dataset_directory_path = cwd + "/backend/dataset" # path for the data file
    dataset_subdirectories_list = os.listdir(dataset_directory_path) # path for the subdirectories in the data file

    for subdirectory in dataset_subdirectories_list: # list of all subdirectories names
        # print(subdirectory) # name of the las sub subdirectories
        subdirectory_path = dataset_directory_path + "/" + subdirectory
        for image in os.listdir(subdirectory_path): # search in all subdirectories # in most of them there are only 1
            image_path = subdirectory_path + "/" + image
            face = face_recognition.load_image_file(image_path)
            face_encoding = face_recognition.face_encodings(face) # calculating the image encoding
            
            if len(face_encoding) != 0:
                new_face_encoding = str(tuple(face_encoding[0]))
                if new_face_encoding not in block_dictionary:
                    block_dictionary[new_face_encoding] = image_path
                    print(counter)
                    counter += 1
                    # if counter > 250:
                    #     load_to_memory(block_dictionary)
                    #     return
                # aux_list.append(block_dictionary)
                # block_dictionary.clear()
            else: # some debugging
                print("image found twice: " + str(image_path))
        load_to_memory(block_dictionary)


def load_to_memory(block_dictionary):
    try:
        path = processed_images_path + '/' + filename
        with open(path, 'w', encoding="utf-8") as file: # append mode
            print("data is: [face_encoding] -> face_image_path")
            print("loading data into new directory file...")
            file.write(json.dumps(block_dictionary, ensure_ascii=False))
            print("data successfully uploaded")
            # for item in aux_list:
            #     file.write(json.dumps(item))
            #     file.write("\n")
            #     counter += 1
            #     if counter == 1000:
            #         print(counter)
            #         counter = 0
            #     # current_block_size++
            file.close()
    except IOError:
        print("Problem reading: " + str(processed_images_path) + " path.")
        return 0

def clear_processed_processes_directory():
    if os.path.exists(path_to_clean_1):
        # clean_dir_1 = []
        # if len(os.listdir(path_to_clean_1)) != 0:
        #     clean_dir_1 = os.listdir(path_to_clean_1) # archivos de imagenes procesadas
        # if len(clean_dir_1) != 0:
        #     for file in clean_dir_1:
                # os.remove(path_to_clean_1 + "/" + file)
        # os.remove(path_to_clean_1)
        shutil.rmtree(path_to_clean_1)
    else:
        print("files not found")


clear_processed_processes_directory()
process_dataset()