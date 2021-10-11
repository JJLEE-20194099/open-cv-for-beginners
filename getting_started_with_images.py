import cv2

# cv2.IMREAD_COLOR: 1 -> load color image
# cv2.IMREAD_GRAYSCALE 0 -> load image in grayscale mode
# cv2.IMREAD_UNCHANGED -1 -> loads image as such including alpha channel

img = cv2.imread('./data/images/OIP.jpg', 0)

# print(img)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite('data/images/OIP_grey.jpg', img)