
import os
import glob
import face_recognition
import numpy as np
import shutil

def is_image(file_name):
    image_extensions = ['png', 'jpg', 'jpeg', 'webp', 'avif']
    return file_name.split('.')[-1].lower() in image_extensions

def get_images_with_faces_in_selected_folder(path='./'):
    images_with_faces = []

    for index, entry in enumerate(glob.glob(path + '/*')):

        if not is_image(entry) or not os.path.isfile(entry):
            continue
        # this file is an image
        image = face_recognition.load_image_file(entry)

        if len(face_recognition.face_locations(image)) == 0:
            continue

        # in this image there are faces
        images_with_faces.append({"entry": entry, "image_binary": image})
    
    return images_with_faces

def stack_by_face(images):

    known_face_encodings = {}

    images_per_person = {}
    
    for index, image in enumerate(images):
        image_face_encoding = face_recognition.face_encodings(image["image_binary"])[0]
        matches = face_recognition.compare_faces(list(known_face_encodings.values()), image_face_encoding)
        if True in matches:
            first_match_index = matches.index(True)
            print(first_match_index, f"finded match")

            face_distances = face_recognition.face_distance(list(known_face_encodings.values()), image_face_encoding)

            if not len(face_distances) == 0:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    # Get the corresponding key for the best match
                    name = list(known_face_encodings.keys())[best_match_index]
                    images_per_person[name].append(image["entry"]) 
        else:
            known_face_encodings[f"person{index}"] = image_face_encoding
            images_per_person[f"person{index}"] = [image["entry"]]

    return images_per_person

def move_images_to_correct_folder(images_per_person, folder_path):
    for key, values in images_per_person.items():
        for value in values:
            destination_folder = os.path.join(folder_path, key)
            os.makedirs(destination_folder, exist_ok=True)
            shutil.copy(value, os.path.join(folder_path, key, value.split("/")[-1]))

def organize_images_by_face(path='./'):
    images = get_images_with_faces_in_selected_folder(path)
    images_per_person = stack_by_face(images)
    move_images_to_correct_folder(images_per_person, path)
    
if __name__ == '__main__':
    path = input("Enter the path of the folder you want to organize: ")
    organize_images_by_face(path)
