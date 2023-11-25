import cv2
import numpy as np

def detect_bright_spots(image_path, threshold_value):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Threshold the image to obtain binary mask
    _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Iterate through the contours and calculate the area and intensity
    bright_spot_areas = []
    bright_spot_intensities = []
    for contour in contours:
        area = cv2.contourArea(contour)
        bright_spot_areas.append(area)

        # Calculate the average intensity within the contour
        mask = np.zeros_like(gray, dtype=np.uint8)
        cv2.drawContours(mask, [contour], 0, 255, -1)
        intensity = np.mean(gray[mask > 0])
        bright_spot_intensities.append(intensity)

        # Draw contour on the image
        cv2.drawContours(image, [contour], 0, (0, 255, 0), 2)  # Green color, thickness = 2

    # Calculate the total area of the image
    total_area = np.sum(bright_spot_areas)

    return bright_spot_areas, bright_spot_intensities, total_area, image

# Path to your satellite image
image_path = 'sat1.png'

# Set the threshold value
threshold_value = 200

# Detect bright spots, calculate their areas and intensities, get the total area, and obtain the image with contours
spot_areas, spot_intensities, total_area, image_with_contours = detect_bright_spots(image_path, threshold_value)

# Print the areas and intensities of the bright spots
for i, area in enumerate(spot_areas):
    intensity = spot_intensities[i]
    print(f"Bright spot {i+1} area: {area} pixels, intensity: {intensity}")

# Print the total area of the image
print(f"Total area of the image: {total_area} pixels")
print("intesity of satellite:",(area/total_area));

# Display the image with contours
cv2.imwrite("region-of-intrest.png",image_with_contours)
cv2.imshow("Bright Spots", image_with_contours)
cv2.waitKey(0)
cv2.destroyAllWindows()
