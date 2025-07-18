
                                                            #HOW  TO OPEN CEMERA IN PROGRAMMING 
# import cv2                                                    # LIBRARY OF FACE DETECTION 

# samran_cap = cv2.VideoCapture(1)          
#  #USING THIS FOR VIDEO CAPTURE OR ENABLE THE CEMERA OF LAPTOPS ETC  
#     #VIDEO.CAPTURE() FUNCTION CEMERA OF LAPTOPS 

# while True:                                          # we use while loops coz the cemera open every time we run 
#     ret, video_data = samran_cap.read()               # we use read() function to read the images that we recive 
#     cv2.imshow("live video", video_data)#we here make frame for images and give him a title to the frame 

#     if cv2.waitKey(10) == ord("a"):# here we use waitkey() for particlar time it run and if we wanna stop the video we press simple a  
#         break

# samran_cap.release() #then we use release method to release the video or data which they caputure 



import cv2   
face_capture = cv2.CascadeClassifier(r"C:\Users\pro5\Downloads\haarcascade_frontalface_default.xml")                                          

samran_cap = cv2.VideoCapture(1)          


while True:                                          
    ret, video_data = samran_cap.read()   
    #sam = cv2.cvtColor(video_data ,)  
    face = face_capture.detectMultiScale(
        video_data,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30 , 30),
        flags=cv2.CASCADE_SCALE_IMAGE

        
    )  
    for ( x , y , w , h) in face:
        cv2.rectangle(video_data,(x , y), (x+w , y+h), (0, 255, 0 ), 2) 

    cv2.imshow("live video", video_data)

    if cv2.waitKey(10) == ord("a"):
        break

samran_cap.release()
