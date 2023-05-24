from src.imageTreatment import imageTreatment
import cv2
import numpy as np
import matplotlib.pyplot as plt

image_treatment = imageTreatment()
images_01 = []
images_01.append(cv2.imread(r'input/fruit1.jpg'))
images_01.append(cv2.imread(r'input/fruit2.jpg'))

# Questão 1.1:
image_result = image_treatment.tam2(images_01[0])
cv2.imwrite('output/quest_1.1.jpg',image_result)

# Questão 1.2:
image_result = image_treatment.tamm(images_01[0])
cv2.imwrite('output/quest_1.2.jpg',image_result)

# Questão 1.3:
image_result = image_treatment.merge_image(images_01[0],images_01[1])
cv2.imwrite('output/quest_1.3.jpg',image_result)