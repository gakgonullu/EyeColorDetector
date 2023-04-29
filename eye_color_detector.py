import cv2
import numpy as np

def is_light_blue(rgb):
    blue = rgb[0]
    green = rgb[1]
    red = rgb[2]
    if blue >= 190 and green >= 180 and blue>green and red <= 160 and abs(blue - red) >= 50 and abs(green - red) >= 50:
        return True
    else:
        return False


def is_dark_blue(rgb):
    blue = rgb[0]
    green = rgb[1]
    red = rgb[2]
    if blue >= 90 and green <= 60 and red <= 60 and abs(blue - green) <= 15 and abs(green - red) <= 15:
        return True
    else:
        return False


def is_dark_brown(rgb):
    blue = rgb[0]
    green = rgb[1]
    red = rgb[2]
    if blue <= 50 and green <= 50 and red <= 50 and abs(blue - green) <= 15 and abs(green - red) <= 15:
        return True
    else:
        return False


def is_light_brown(rgb):
    blue = rgb[0]
    green = rgb[1]
    red = rgb[2]
    if blue >= 140 and green >= 70 and red >= 20 and blue <= 60 + green and blue <= 60 + red and green <= 50 + red:
        return True
    else:
        return False


def is_dark_green(rgb):
    blue = rgb[0]
    green = rgb[1]
    red = rgb[2]
    # check if color is dark green
    if blue <= 50 and green >= 80 and red <= 70:
        return True
    
    else:
        return False

    
def is_light_green(rgb):
    blue = rgb[0]
    green = rgb[1]
    red = rgb[2]
    if blue <= 85 and green >= 80 and green<=150 and red <= 80 and green >= blue and green >= red:
        return True
    else:
        return False

def is_hazel(rgb):
    blue = rgb[0]
    green = rgb[1]
    red = rgb[2]
    print("val: ", rgb)
    print('r: ' , red, "g: ", green, "b:", blue)
    if green >= 25 and green <= 135 and red >= 50 and red <= 160 and blue >= 10 and blue <= 85:
        if abs(green - red) <= 40 and blue < red and blue < green:
            return True
    return False


def is_amber(rgb):
    blue = rgb[0]
    green = rgb[1]
    red = rgb[2]
    if blue <= 60 and green >= 60 and red >= 120 and green <= red - 60:
        return True
    else:
        return False


def is_grey(rgb):
    blue = rgb[0]
    green = rgb[1]
    red = rgb[2]
    if blue >= 80 and green >= 80 and red >= 80 and abs(blue - green) <= 15 and abs(green - red) <= 15:
        return True
    else:
        return False


def is_black(rgb):
    blue = rgb[0]
    green = rgb[1]
    red = rgb[2]
    if blue <= 15 and green <= 15 and red <= 15:
        return True
    else:
        return False


# Load the image
img = cv2.imread('path_of_image')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur to reduce noise
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply Canny edge detection to detect edges
edges = cv2.Canny(blur, 50, 150)

# Apply Hough Transform to detect circles
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)

# If circles are detected, draw a bounding box around the iris region
if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    (x, y, r) = circles[0]
    cv2.circle(img, (x, y), r, (0, 255, 0), 2)
    cv2.rectangle(img, (x-r, y-r), (x+r, y+r), (0, 255, 0), 2)
    iris = img[y-r:y+r, x-r:x+r]
    hsv = cv2.cvtColor(iris, cv2.COLOR_BGR2HSV)
    cv2.imshow('Iris Region', iris)
else:
    print("Iris not detected")

cv2.imshow('Image', img)


print(np.mean(iris, axis=(0, 1)))
# Detect the color of the iris region
if is_dark_green(np.mean(iris, axis=(0, 1))):
    print("Color detected: Dark green")
elif is_light_green(np.mean(iris, axis=(0, 1))):
    print("Color detected: Light green")
elif is_dark_blue(np.mean(iris, axis=(0, 1))):
    print("Color detected: Dark blue")
elif is_light_blue(np.mean(iris, axis=(0, 1))):
    print("Color detected: Light blue")
elif is_dark_brown(np.mean(iris, axis=(0, 1))):
    print("Color detected: Dark brown")
elif is_light_brown(np.mean(iris, axis=(0, 1))):
    print("Color detected: Light brown")
elif is_amber(np.mean(iris, axis=(0, 1))):
    print("Color detected: Amber")
elif is_black(np.mean(iris, axis=(0, 1))):
    print("Color detected: Black")
elif is_grey(np.mean(iris, axis=(0, 1))):
    print("Color detected: Grey")
elif is_hazel(np.mean(iris, axis=(0, 1))):
    print("Color detected: Hazel")
else:
    print("Color not detected")
