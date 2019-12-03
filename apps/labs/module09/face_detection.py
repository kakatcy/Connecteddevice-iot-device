'''
Created on Nov 15, 2019

@author: cytang
'''
# -*- coding: UTF-8 -*-

"""
opencv实现人脸识别
参考：
1、https://github.com/opencv/opencv/tree/master/data/haarcascades
2、http://www.cnblogs.com/hanson1/p/7105265.html

"""
import cv2

# 待检测的图片路径
imagepath='nba2.jpg'
image = cv2.imread(imagepath)

#cv2.imshow("image",image)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


'''
# 获取人脸识别训练数据

对于人脸特征的一些描述，opencv在读取完数据后很据训练中的样品数据，
就可以感知读取到的图片上的特征，进而对图片进行人脸识别。
xml数据下载，
参考：https://github.com/opencv/opencv/tree/master/data/haarcascades
'''

face_cascade = cv2.CascadeClassifier('/Users/cytang/program/opencv-4.1.2/data/haarcascades/haarcascade_frontalface_default.xml')

# 探测人脸
# 根据训练的数据来对新图片进行识别的过程。
faces = face_cascade.detectMultiScale(
  gray,
  scaleFactor = 1.15,
  minNeighbors = 5,
  minSize = (5,5),
  flags = cv2.CASCADE_SCALE_IMAGE
)

# 我们可以随意的指定里面参数的值，来达到不同精度下的识别。返回值就是opencv对图片的探测结果的体现。

# 处理人脸探测的结果
print ("发现{0}个人脸!".format(len(faces)))
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
    # cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)

#show changeable image
cv2.namedWindow("image", cv2.WINDOW_NORMAL)
cv2.imshow("image",image)      
k = cv2.waitKey(0) & 0xFF
if k==27:
    cv2.destroyAllWindows()
elif k==ord('s'):
    #write to disk
    cv2.imwrite("NBA.png",image)
    cv2.destroyAllWindows()


