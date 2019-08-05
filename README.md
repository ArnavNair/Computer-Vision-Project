This project performs Computer Vision operations on real-time images, in this case, newspaper images.
It first performs OCR on a set of newspaper images, searching for a user-given keyword.
In pages containing this keyword, it performs Facial Recognition.
Finally, it compiles found images into a contact sheet to be ultimately displayed.

The images are first present in a zip file, which is handled using the in-built ZipFile module.
The OCR is performed using the pytesseract module, present in the kraken package.
The facial recognition is performed using the numpy module to convert to an acceptable form, and then the opencv module's Haar Cascade functions to detect the faces.
Finally, the images are compiled into a contact sheet using the Image module.

Note: Despite several attempts, the efficiency of the facial recognition itself remains quite low. Thus, it's unable to pick up all faces. This would be an area for possible fututre improvement.
