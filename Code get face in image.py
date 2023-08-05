#Import required libraries:
import os
import face_recognition
from PIL import Image

#Set the constants:
FACES_DIR = "Captured"  # Directory containing the images with faces
SIZE = (200, 200)       # Size to which the cropped faces will be resized

#Check if the "Cropped" directory exists within the "Captured" directory. If not, create it:
if not os.path.exists(os.path.join(FACES_DIR, "Cropped")):
    os.mkdir(os.path.join(FACES_DIR, "Cropped"))

#Initialize the  variable, which will be used to create filenames for the cropped images:file_index
file_index = 1

#Loop through all the files in the "Captured" directory:
for filename in os.listdir(FACES_DIR):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Load the image using face_recognition library
        image = face_recognition.load_image_file(os.path.join(FACES_DIR, filename))
        
        # Find face locations in the image using face_recognition library
        face_locations = face_recognition.face_locations(image)

#For each face found in the image, crop the face, resize it to the specified size, and save it:
        for face_location in face_locations:
            top, right, bottom, left = face_location
            square = (left, top, right, bottom)
            
            # Crop the face using PIL (Python Imaging Library)
            face_image = Image.fromarray(image).crop(square)
            
            # Resize the cropped face to the specified size
            face_image = face_image.resize(SIZE)
            
            # Create a new filename for the cropped image
            cropped_filename = f"biplab.{file_index}.jpg"
            cropped_filepath = os.path.join(FACES_DIR, "Cropped", cropped_filename)
            
            # Save the cropped face to the "Cropped" directory
            face_image.save(cropped_filepath)
            
            # Print the path where the cropped image is saved
            print(f"Saved cropped image to {cropped_filepath}")
            
            # Increment the file_index for the next cropped image
            file_index += 1
