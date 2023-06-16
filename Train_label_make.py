import csv
import os

# 저장할 CSV 파일 경로와 파일 이름
csv_file = "C:/vscode/python/train_annotation.csv"

# CSV 파일 열기
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)

    # 첫 번째 행에 컬럼 이름 작성
    writer.writerow(["filepath", "label"])

    folder_path = "C:/vscode/python/train"  # 이미지 파일들이 저장된 폴더 경로
    bird_label_start = 0  # bird 레이블 시작 값
    dog_label_start = 9  # dog 레이블 시작 값
    file_name_list=os.listdir(folder_path)
    file_name_list.sort()
    folder_path1='train/'

    for file_name in file_name_list:
        image_name = os.path.splitext(file_name)[0]  # 확장자 제거

        label = -1  # 기본적으로 -1로 설정

        if image_name.startswith("bird") and image_name[-1].isdigit():
            label = bird_label_start+int(image_name[-1])-1
        elif image_name.startswith("dog") and image_name[-1].isdigit():
            label = dog_label_start+int(image_name[-1])-1

        # 파일 경로와 레이블 작성 후 저장
        file_path = folder_path1+file_name
        writer.writerow([file_path, label])

print("CSV 파일이 성공적으로 생성되었습니다.")