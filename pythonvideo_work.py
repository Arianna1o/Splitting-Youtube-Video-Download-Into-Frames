# importing the module
from pytube import YouTube

# importing the module
import cv2

# where to save
SAVE_PATH = "C:\\Users\\Naomi\\Documents\\Python Images" 

# link of the video to be downloaded
link="https://www.youtube.com/watch?v=dkRHmHx_aNA"

try:
	 #object creation using YouTube
	 #which was imported in the beginning
	yt = YouTube(link)
except:
	print("Connection Error") #to handle exception

# filters out all the files with "mp4" extension and downloading video to a specific folder

yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution')[-1].download(SAVE_PATH)
 
# reading the video for gray scale change
source = cv2.VideoCapture('C:\\Users\\Naomi\\Documents\\Python Images\\1 Minute of Cute Puppies Having A Playdate.mp4')
 
# running the loop
while True:
 
    # extracting the frames
    ret, img = source.read()
     
    # converting to gray-scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
    # displaying the video
    cv2.imshow("Live", gray)
 
    # exiting the loop
    key = cv2.waitKey(20)
    if key == ord("q"):
        break
     
 #closing the window
cv2.destroyAllWindows()
source.release()

# SPLITTING FRAMES OF A VIDEO
capture = cv2.VideoCapture('C:\\Users\\Naomi\\Documents\\Python Images\\1 Minute of Cute Puppies Having A Playdate.mp4')

frameNr = 0

while (True):
 
    success, frame = capture.read()
 
    if success:
        cv2.imwrite(f'C:\\Users\\Naomi\\Desktop\\Psychology\\Frames Output\\{frameNr}.jpg', frame)
 
    else:
        break
 
    frameNr = frameNr+1
 
capture.release()