
import cv2 
def on_change(val):
              print(val)
              Alpha = val/100
              Beta = (1.0- Alpha)
              result = cv2.addWeighted(background_img, Alpha,foreground_img, Beta ,0.0);
              cv2.imshow('Blend',result)
       

background_img = cv2.imread("Path\\16391545485537.jpg")
foreground_img = cv2.imread("Path\.jpeg")
background_img = cv2.resize(background_img,(512,512))
foreground_img = cv2.resize(foreground_img,(512,512))
blended_img = cv2.addWeighted(background_img,0.9,foreground_img,0.3,0.0)

cv2.imshow("Ronaldo",blended_img)
#cv2.createTrackbar('slider','Blend', 0, 100, on_change)
          
cv2.waitKey(0)
cv2.destroyAllWindows()
