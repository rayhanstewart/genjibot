#All of this is lowkey useless
import cv2
import numpy as np
# Create a VideoCapture object and read from input file 
cap = cv2.VideoCapture(r'')

# Check if camera opened successfully 
if (cap.isOpened() == False):
    print("Error opening video file")

    # Read until video is completed
while (cap.isOpened()):

    # Capture frame-by-frame
    ret, frame = cap.read()
    if ret == True:
        # Read and resize image.
        img = cv2.resize(frame,(1080,720))
        # Convert to grayscale.
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Blur using 3 * 3 kernel.
        gray_blurred = cv2.blur(gray, (3, 3))
        rows = gray.shape[0]


        # Apply Hough transform on the blurred image.
        detected_circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, rows / 8,
 param1=100, param2=30,
 minRadius=1, maxRadius=30)


        # Draw circles that are detected.
        if detected_circles is not None:

            # Convert the circle parameters a, b and r to integers.
            detected_circles = np.uint16(np.around(detected_circles))

            for pt in detected_circles[0, :]:
                a, b, r = pt[0], pt[1], pt[2]

                # Draw the circumference of the circle.
                cv2.circle(img, (a, b), r, (0, 255, 0), 2)

                # Draw a small circle (of radius 1) to show the center.
                cv2.circle(img, (a, b), 1, (0, 0, 255), 3)

                # Display the resulting frame
                cv2.imshow("Detected Circle", img)

        # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Break the loop
    else:
        break

# When everything done, release 
# the video capture object 
cap.release()

# Closes all the frames 
cv2.destroyAllWindows() 