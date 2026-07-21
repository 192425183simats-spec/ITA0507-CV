import cv2

img = cv2.imread(r"C:\Users\Harshitha\Downloads\HappyFish.jpg")

small = cv2.resize(img, (300, 200))
big = cv2.resize(img, (800, 600))

cv2.imshow("Original", img)
cv2.imshow("Smaller Image", small)
cv2.imshow("Bigger Image", big)

cv2.waitKey(0)
cv2.destroyAllWindows()
