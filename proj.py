from src.imageResize import imageResize
from src.imageTreatment import imageTreatment
import cv2
import numpy as np
import matplotlib.pyplot as plt

# _____________ Questao 01 _____________
image_resize = imageResize()
images_01 = []
images_01.append(cv2.imread(r'input/fruit1.jpg'))
images_01.append(cv2.imread(r'input/fruit2.jpg'))

# Questão 1.1:
image_result = image_resize.tam2(images_01[0])
cv2.imwrite('output/quest_1.1.jpg',image_result)

# Questão 1.2:
image_result = image_resize.tamm(images_01[0])
cv2.imwrite('output/quest_1.2.jpg',image_result)

# Questão 1.3:
image_result = image_resize.merge_image(images_01[0],images_01[1])
cv2.imwrite('output/quest_1.3.jpg',image_result)

# _____________ Questao 02 _____________
image_treatment = imageTreatment()
images_02 = []
images_02.append(cv2.imread(r'input/car.png'))
images_02.append(cv2.imread(r'input/crowd.png'))
images_02.append(cv2.imread(r'input/university.png'))

# Questão 2.1:
corrected_image = image_treatment.gamma(images_02[0], 0.4)
image_treatment.print2Pl(images_02[0], corrected_image)
cv2.imwrite('output/quest_2.1.jpg',corrected_image)

# Questão 2.2:
# equalized_image, histogram, cdf = image_treatment.equalize(images_02[0])
# image_treatment.printPl(histogram)
# image_treatment.printPl(cdf)
# image_treatment.print2Pl(images_02[0], equalized_image)
# cv2.imwrite('output/quest_2.2.jpg',equalized_image)


 