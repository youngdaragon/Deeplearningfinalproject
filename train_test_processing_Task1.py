import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
import random
import csv

def select_random_files(folder_path, num_files):
    file_list = os.listdir(folder_path)
    random_files = random.sample(file_list, num_files)
    return random_files

def img_division(img_name,img_name2):

    path_name='C:/vscode/python/testall/'+img_name
    path_name2='C:/vscode/python/testall/'+img_name2
    img_a=cv2.imread(path_name)
    img_b=cv2.imread(path_name2)
    resized_img = cv2.resize(img_a, (128, 128))
    resized_img2 = cv2.resize(img_b, (128, 128))

    # 확장자 제거
    file_name_without_extension = os.path.splitext(img_name)[0]
    file_name_without_extension2 = os.path.splitext(img_name2)[0]
    # 파일 이름 추출
    only_image_name = os.path.basename(file_name_without_extension)
    only_image_name2 = os.path.basename(file_name_without_extension2)


    if file_name_without_extension.startswith("bird"):
        label = 'bird'
    elif file_name_without_extension.startswith("dog"):
        label = 'dog'
    else:
        label = 'none'
    

    if file_name_without_extension2.startswith("bird"):
        label2 = 'bird'
    elif file_name_without_extension2.startswith("dog"):
        label2 = 'dog'
    else:
        label2 = 'none'

    
    img1=resized_img[0:40,0:40]

    img2=resized_img[0:40,44:84]

    img3=resized_img[0:40,88:128]

    img4=resized_img[44:84,0:40]

    img5=resized_img[44:84,44:84]

    img6=resized_img[44:84,88:128]

    img7=resized_img[88:128,0:40]

    img8=resized_img[88:128,44:84]

    img9=resized_img[88:128,88:128]

    img10=resized_img2[0:40,0:40]

    img11=resized_img2[0:40,44:84]

    img12=resized_img2[0:40,88:128]

    img13=resized_img2[44:84,0:40]

    img14=resized_img2[44:84,44:84]

    img15=resized_img2[44:84,88:128]

    img16=resized_img2[88:128,0:40]

    img17=resized_img2[88:128,44:84]

    img18=resized_img2[88:128,88:128]

    # img1부터 img9까지 랜덤하게 셔플
    shuffled_images = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11, img12, img13, img14, img15, img16, img17, img18]
    np.random.shuffle(shuffled_images)

    # 가로 3개, 세로 3개로 합치기
    row1 = np.concatenate((shuffled_images[0], shuffled_images[1], shuffled_images[2],shuffled_images[9], shuffled_images[10], shuffled_images[11]), axis=1)
    row2 = np.concatenate((shuffled_images[3], shuffled_images[4], shuffled_images[5],shuffled_images[12], shuffled_images[13], shuffled_images[14]), axis=1)
    row3 = np.concatenate((shuffled_images[6], shuffled_images[7], shuffled_images[8],shuffled_images[15], shuffled_images[16], shuffled_images[17]), axis=1)

    concatenated_img = np.concatenate((row1, row2, row3), axis=0)
    if (label == 'dog' and label2== 'dog'):
        concatenated_label = 0
    elif(label == 'dog' and label2== 'bird'):
        concatenated_label = 1
    elif(label == 'bird' and label2== 'bird'):
        concatenated_label = 2
    else:
        concatenated_label = 1
    return concatenated_img, concatenated_label

folder_path='C:/vscode/python/testall'
csv_file_path = 'C:/vscode/python/test_annotation.csv'

with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["filepath", "label"]) # 헤더 작성
    for i in range(0,2000):
        files_list = select_random_files(folder_path, 2)
        concat_img, concat_label = img_division(files_list[0], files_list[1])

        image_name = 'concat_img_' + str(i) + '.jpg'
        label = concat_label

        cv2.imwrite('C:/vscode/python/test/' + image_name, concat_img)

        writer.writerow([image_name, label])
    
    



