import cv2

img = cv2.imread("poster.jpg")

rocket = img[120:360,400:500]

# #rocket = img[100:360,200:500]
# #img[0:260, 300:600] = rocket

img[0:240, 500:600] = rocket

# img[100:340, 0:100] = rocket


text_to_show = "I love coding at WhiteHatJr."
cv2.putText(img,  
           text_to_show,
           (20, 120),  
           fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
           fontScale=1.5,  
           color=(187,0,255)
           )

cv2.imshow("Output",img)

cv2.waitKey(0)