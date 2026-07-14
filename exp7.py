import cv2

# Video path
video = cv2.VideoCapture(r"C:\Users\Harshitha\Downloads\16276390_1080_1920_50fps.mp4")

if not video.isOpened():
    print("Error: Could not open the video.")
    exit()

print("Press 'q' to quit.")

while True:
    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Video", frame)

    # Change the value below for different speeds:
    # 100 = Slow Motion
    # 30  = Normal Speed
    # 10  = Fast Motion
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
