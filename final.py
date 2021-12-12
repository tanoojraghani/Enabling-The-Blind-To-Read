# import the following libraries 
# will convert the image to text string 
import pytesseract	 

# will connect webcam for near real-time detection
import cv2

# adds image processing capabilities 
from PIL import Image	 

# converts the text to speech 
#import pyttsx3	
from gtts import gTTS
import os	 

#(optional feature, can implement later)
#translates into the mentioned language 
from googletrans import Translator	 

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)  
i=0 #to save all the clicked images
while(True):
    ret, frame = cap.read()
    cv2.imshow("PRESS C TO CAPTURE",frame)
    key=cv2.waitKey(30)
    if key==ord('q'):
        break
    if key==ord('c'):
        #x=str(datetime.now())
        #print(x)
        #i+=1
        cv2.imshow("Image Captured",frame)
        cv2.imwrite('C:/Users/hdrah/OneDrive/desktop/py4e/image'+str(i)+'.png', frame)
        print("Wrote Image")
        
        break
# release the capture
cap.release()
cv2.destroyAllWindows()
# opening an image from the source path 
img = Image.open('image0.png')	 

# describes image format in the output 
print(img)						 
# path where the tesseract module is installed 
#pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = 'C:/Users/hdrah/AppData/Local/Tesseract-OCR/tesseract.exe'
# converts the image to result and saves it into result variable 
result = pytesseract.image_to_string(img) 
# write text in a text file and save it to source path 
with open('abc.txt',mode ='w') as file:	 
	file.write(result) 
	print(result) 
				

#p = Translator()					 
# translates the text into german language 
#k = p.translate(result,dest='german')	 
#print(k) 
##engine = pyttsx3.init() #runs only in english 

# an audio will be played which speaks the test if pyttsx3 recognizes it 
##engine.say(result)							 
##engine.runAndWait() 

# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed 
myobj = gTTS(text=result, lang='en', slow=False) 

# Saving the converted audio in a mp3 file named result 
myobj.save("result.mp3") 

# Playing the converted file 
os.system("result.mp3")
#print("Would you like to translate the given text?")