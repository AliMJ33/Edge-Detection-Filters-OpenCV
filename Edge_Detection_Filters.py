import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Fig0114(b)(pills).png")

sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize= 3)
sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize= 3)
scharrx = cv2.Scharr(img, cv2.CV_8U, 1, 0)
scharry = cv2.Scharr(img, cv2.CV_8U, 0, 1)
laplacian = cv2.Laplacian(img, cv2.CV_8U, ksize= 3)

plt.subplot(2, 3, 1), plt.imshow(img, 'gray'), plt.title("Original Image"), plt.axis("off")
plt.subplot(2, 3, 2), plt.imshow(sobelx, 'gray'), plt.title("SobelX"), plt.axis("off")
plt.subplot(2, 3, 3), plt.imshow(sobely, 'gray'), plt.title("SobelY"), plt.axis("off")
plt.subplot(2, 3, 4), plt.imshow(scharrx, 'gray'), plt.title("ScharrX"), plt.axis("off")
plt.subplot(2, 3, 5), plt.imshow(scharry, 'gray'), plt.title("ScharrY"), plt.axis("off")
plt.subplot(2, 3, 6), plt.imshow(laplacian, 'gray'), plt.title("Lapacian"), plt.axis("off")

plt.show()