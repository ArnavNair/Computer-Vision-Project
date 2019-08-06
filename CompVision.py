#PYTHON PROJECT

#Import statements
from zipfile import ZipFile
from PIL import Image, ImageDraw
from IPython.display import display
import pytesseract
import cv2 as cv
import numpy as np


#FACIAL DETECTION
#Function to perform Facial Recognition
def face_recog(img): 
    #Open the grey-scaled image as an n-dimensional array
    image = np.array(img)
    
    #Loading the face detection classifier
    face_cascade = cv.CascadeClassifier('readonly/haarcascade_frontalface_default.xml')
    
    #Return the facial recognition rectangles
    return face_cascade.detectMultiScale(image, scaleFactor = 1.3, minNeighbors = 5)
    
#CREATE AND PRINT THE CONTACT SHEET
#Function to create and print the contact sheet
def contact_sheet(img, faces):
    #Create the contact sheet
    contact = Image.new(img.mode, (500, 200))
    
    #Paste the faces onto the contact sheet
    for x, y, w, h in faces:
        #Obtain the face
        face = (img.crop((x, y, x + w, y + h))).resize((100, 100))
        
        #Paste the face onto the contact sheet
        x, y = 0, 0
        contact.paste(face, (x, y, face.width, face.height))
        if x + face.width == contact.width:
            x = 0
            y += face.height
        else:
            x += face.width
            
    #Print the contact sheet
    display(contact)
        
#NAVIGATE THE ZIP FILE TO OBTAIN ALL IMAGES
#Open the ZIP file
fl = 'images.zip'
z = ZipFile(fl)

#Extract the images
pages = []
for name in z.namelist():
    dic = {}
    dic['name'] = name
    dic['image'] = Image.open(z.extract(name))
    pages.append(dic)
    
z.close()
    
#ACCEPT THE SEARCH WORD
#Accept the search word from the user
key = input('Enter the word to be searched for in the pages:')

#EXTRACT THE TEXT, PERFORM OCR,OBTAIN THE FACES AND PRINT THE CONTACT SHEET
#Perform the comprehensive search
for page in pages:
    #Binarize the image
    img = page['image'].convert('L')

    for x in range(img.width):
        for y in range(img.height):
            if img.getpixel((x, y)) > 140:
                img.putpixel((x, y), 255)
            else:
                img.putpixel((x, y), 0)
                
    #Create a flag
    found = False
    
    #Perform OCR on the image and search for the key
    if key in pytesseract.image_to_string(img):
        #Set flag to True
        found = True
            
        #Print that the key has been found
        print('Results found in file {}'.format(page['name']))
            
        #Obtain the facial recognition boxes
        page['faces'] = face_recog(img)
    
    #Print the contact sheet if key has been found
    if found:
        #If no faces detected, print a message saying so
        if page['faces'].any() == None:
            print('But there were no faces in that file!')
        else:   
            contact_sheet(page['image'], page['faces'])
            