from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.label import Label

import os
import cv2

import numpy as np

dona = cv2.imread("assets/opend.png")
# Load the cascade

face_cascade = cv2.CascadeClassifier('assets/haarcascade_frontalface_default.xml')


# To capture video from webcam. 
#cap = cv2.VideoCapture("rick.mp4")

# To use a video file as input 
# cap = cv2.VideoCapture('filename.mp4')




cap = cv2.VideoCapture(0)

yeet = cv2.imread("assets/opend.png", cv2.IMREAD_UNCHANGED)





class Outer():
    def dank(self, a):
        print("yeet" + str(a))
        
        #cv2.imwrite("testerd.png", MyApp.capture.read())
        #cv2.imwrite("testerd.png", MyApp.update.frame)
        

    
        

class MyApp(App):
    
    def mooo(self, a):
        print("YOTE : " + str(a))
        print("mmm")
        #yeet = cv2.imread(MyApp.update.img)
        #cv2.imwrite("testerd.png", ifmmmg)
        print("dadadada")

    def build(self):
        self.icon = 'Logo.ico'
        
        def callback(self):
            #Outer.dank(self, self)
            MyApp.mooo(self, "ya")
            
            print('The button <%s> is being pressed' % self.text)
        self.img1=Image()
        self.bt1 = Button(text='PlaceHolder Button\n(Does Nothing ATM)', font_size=14)
        self.bt1.bind(on_press=callback)
        self.bt1.size_hint = 1, .25
        self.title = 'FaceEmoji V1'
        self.lbl = Label(text='FaceEmoji', font_size=14)
        self.lbl.size_hint = 1, .1

        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.img1)
        layout.add_widget(self.lbl)
        layout.add_widget(self.bt1)
        
        #opencv2 stuffs
        #self.capture = cv2.VideoCapture(0)
        #cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        
        #himg, img = self.capture.read()
        
        himg, img = cap.read()
        # Convert to grayscale
        #img = img = cv2.cvtColor(img, cv2.COLOR_)
        #box = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
        #fist = cv2.cvtColor(box, cv2.COLOR_BGRA2RGBA)
        gray = cv2.cvtColor(img, cv2.COLOR_RGBA2GRAY)
        #s_img = cv2.cvtColor(dona, cv2.COLOR_BGRA2GRAY)
        s_img = dona
        # Detect the faces
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        #hands = hand_cascade.detectMultiScale(gray, 1.1, 4)
        
        # Draw the rectangle around each face
        for (x, y, w, h) in faces:

            #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 255, 255), 3)
            
            #wid, hid, cid = s_img.shape
            #for i in range(0, wid):
            #    for j in range(0, hid):
            #        if s_img[i, j][3] != 0:
            #            img[y + i, x + j] = s_img[i, j]
            wid, hid, cid = s_img.shape
            x_offset=y_offset=50
            #xod, wod, hod = img.shape
            #img[y_offset:y_offset+s_img.shape[0], x_offset:x_offset+s_img.shape[1]] = s_img
            #alpha = dona[:,:,3] # Channel 3
            #result = np.dstack([s_img, alpha])
            dank = cv2.resize(s_img, (h, w))#, interpolation=cv2.INTER_CUBIC)
            #alpha = dank[:,:,3]
            dank = cv2.cvtColor(dank, cv2.COLOR_BGRA2BGR)
            #img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA)
            #img[y:y+hid, x:x+wid] = s_img
            
            #img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            img[y:y+h, x:x+w] = dank
            #img_BGRA[y:y+h, x:x+w] = dank
            

        #print(img)
        img = cv2.flip( img, 1 )
        frame = img
        #cv2.imshow("CV2 Image", frame)
        
        # display image from cam in opencv window
        # convert it to texture
        buf1 = cv2.flip(img, 0)
        buf = buf1.tostring()
        texture1 = Texture.create(size=(img.shape[1], img.shape[0]), colorfmt='bgr')
        texture1.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
        # display image from the texture
        
        self.img1.texture = texture1




    
    




    
    

    


if __name__ == '__main__':
    MyApp().run()
else:
    MyApp().stop()

while 1:
   pass