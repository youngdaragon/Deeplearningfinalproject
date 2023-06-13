import cv2
import os
import matplotlib.pyplot as plt
import numpy as np

# img=cv2.imread('C:/vscode/python/trainall/bird (1).jpg')

# plt.subplot(3,3,1)
# plt.imshow(img[0:40,0:40])
# plt.subplot(3,3,2)
# plt.imshow(img[0:40,44:84])
# plt.subplot(3,3,3)
# plt.imshow(img[0:40,88:128])
# plt.subplot(3,3,4)
# plt.imshow(img[44:84,0:40])
# plt.subplot(3,3,5)
# plt.imshow(img[44:84,44:84])
# plt.subplot(3,3,6)
# plt.imshow(img[44:84,88:128])
# plt.subplot(3,3,7)
# plt.imshow(img[88:128,0:40])
# plt.subplot(3,3,8)
# plt.imshow(img[88:128,44:84])
# plt.subplot(3,3,9)
# plt.imshow(img[88:128,88:128])
# plt.show()

# def img_division(img_name):
#     path_name='C:/vscode/python/trainall/'+img_name
#     img=cv2.imread(path_name)
#     resized_img = cv2.resize(img, (128, 128))

#     # 확장자 제거
#     file_name_without_extension = os.path.splitext(img_name)[0]

#     # 파일 이름 추출
#     only_image_name = os.path.basename(file_name_without_extension)

#     img1=resized_img[0:40,0:40]
#     cv2.imwrite('C:/vscode/python/train/'+only_image_name+"_1.jpg", img1)
#     img2=resized_img[0:40,44:84]
#     cv2.imwrite('C:/vscode/python/train/'+only_image_name+"_2.jpg", img2)
#     img3=resized_img[0:40,88:128]
#     cv2.imwrite('C:/vscode/python/train/'+only_image_name+"_3.jpg", img3)
#     img4=resized_img[44:84,0:40]
#     cv2.imwrite('C:/vscode/python/train/'+only_image_name+"_4.jpg", img4)
#     img5=resized_img[44:84,44:84]
#     cv2.imwrite('C:/vscode/python/train/'+only_image_name+"_5.jpg", img5)
#     img6=resized_img[44:84,88:128]
#     cv2.imwrite('C:/vscode/python/train/'+only_image_name+"_6.jpg", img6)
#     img7=resized_img[88:128,0:40]
#     cv2.imwrite('C:/vscode/python/train/'+only_image_name+"_7.jpg", img7)
#     img8=resized_img[88:128,44:84]
#     cv2.imwrite('C:/vscode/python/train/'+only_image_name+"_8.jpg", img8)
#     img9=resized_img[88:128,88:128]
#     cv2.imwrite('C:/vscode/python/train/'+only_image_name+"_9.jpg", img9)

#     return True



folder_path='C:/vscode/python/testall'

fileNameList=os.listdir(folder_path)
fileNameList.sort()
for file_name in fileNameList:
    new_file_name1 = file_name.replace(")", "")
    file_name1=folder_path+"/"+file_name
    new_file_name=folder_path+"/"+new_file_name1
    # 파일 이름 변경
    os.rename(file_name1, new_file_name)

# folder_path='C:/vscode/python/trainall'

# fileNameList=os.listdir(folder_path)
# fileNameList.sort()
# for file_name in fileNameList:
#     success=img_division(file_name)
