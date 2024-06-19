import os
import cv2

from PIL import Image

def yolo_process_image(img_path, save_folder, index,model):

  imgk = cv2.imread(img_path)
  print((img_path))
  image = Image.open(img_path)

  fileName=img_path.split('/')[-1].split('.')[0]
  chunk_name=img_path.split('/')[-2]
  newDir=save_folder+"/"+chunk_name+"/"+fileName
  print('heheheh'+newDir)
  os.makedirs(newDir,exist_ok=True)
  # print(",d",fileName)

  # set model parameters
  model.overrides['conf'] = 0.25  # NMS confidence threshold
  model.overrides['iou'] = 0.45  # NMS IoU threshold
  model.overrides['agnostic_nms'] = False  # NMS class-agnostic
  model.overrides['max_det'] = 1000  # maximum number of detections per image

  results = model.predict(image)

  print(results[0].boxes)
  nb_of_images=len(results[0].boxes.xyxy)
  print("FROM IMAGE: "+fileName+" NUMBER OF PHOTO EXTRACTED IS: "+str(nb_of_images))
  for i in range(len((results[0].boxes.xyxy))):
    xmin=int(results[0].boxes.xyxy[i][0]-10)
    ymin=int(results[0].boxes.xyxy[i][1])
    xmax=int(results[0].boxes.xyxy[i][2]+15)
    ymax=int(results[0].boxes.xyxy[i][3]+15)
    if xmin<0:
      xmin=11
    if ymin<0:
      ymin=11
    print(newDir+"/table"+str(index)+".jpg")
    cv2.imwrite(newDir+"/table"+str(index)+".jpg", imgk[ymin: ymax, xmin: xmax])
    index=index+1
  return index
