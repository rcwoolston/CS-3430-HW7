import os
import cv2
from matplotlib import pyplot as plt

# Global variables
sharp_paths = []
blurry_paths = []
image_paths = []

# Getting the path for the test pictures
sharp_folder_path = os.path.join(os.getcwd(),'sample_images\Sample sharp images')
blurry_folder_path = os.path.join(os.getcwd(),'sample_images\Sample Blurry images')

valid_images = [".jpg",".gif",".png",".tga"]
for f in os.listdir(sharp_folder_path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    sharp_paths.append(os.path.join(sharp_folder_path,f))

for f in os.listdir(blurry_folder_path):
    ext = os.path.splitext(f)[1]
    if ext.lower() not in valid_images:
        continue
    blurry_paths.append(os.path.join(sharp_folder_path,f))

image_paths = sharp_paths + blurry_paths

answerDict = {}
folders=[]
count = 0
for i in image_paths:
    img = cv2.imread(i,0)
    edges = cv2.Canny(img,100,200)
    while 1:
        path, folder = os.path.split(i)

        if folder != "":
            folders.append(folder)
        else:
            if path != "":
                folders.append(path)

            break

        folders.reverse()
        print folders
    if edges == None:
        answerDict[count] = 'B'
    else:
        answerDict[count] = 'S'

    count+=1

img = cv2.imread(sharp_paths.pop(),0)
edges = cv2.Canny(img,100,200)

temp = edges.shape

img2 = cv2.imread(blurry_paths.pop(),0)
edges = cv2.Canny(img2,100,200)

plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()

print 'here'
