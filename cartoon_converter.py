import cv2 as cv

image = cv.imread('data/image/1.jpg')

# Check if width or height is more than 1024
if image.shape[0] > 1024 or image.shape[1] > 1024:
    # Calculate the scaling factor
    scale = min(1024 / image.shape[0], 1024 / image.shape[1])
    # Resize the image
    image = cv.resize(image, None, fx=scale, fy=scale)

# Convert the image to grayscale
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Apply a median blur to reduce noise
blurred = cv.medianBlur(gray, 5)

# Apply adaptive thresholding to create a binary image
thresholded = cv.adaptiveThreshold(blurred, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 9, 9)

# Create a cartoon effect by applying a bilateral filter
cartoon = cv.bilateralFilter(image, 9, 75, 75)

# Merge the cartoon image with the thresholded image
cartoon = cv.bitwise_and(cartoon, cartoon, mask=thresholded)

# Show the cartoon image
cv.imshow('Cartoon', cartoon)

key = cv.waitKey(0)
if key == ord('s'):
    cv.imwrite('data/image/1_output.jpg', cartoon)

cv.destroyAllWindows()