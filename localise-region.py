import cv2
import os

def detect_bright_spots(image_path, threshold_value=200, min_contour_area=50):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
   
    # Find contours
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.imshow("ninary image", contours);
    # Filter the contours based on minimum contour area
    filtered_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > min_contour_area]

    # Calculate the area of each bright spot (circle) separately and print it on the image
    for i, contour in enumerate(filtered_contours):
        (x, y), radius = cv2.minEnclosingCircle(contour)
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(image, center, radius, (0, 255, 0), 2)  # Green circle

        area = cv2.contourArea(contour)
        area_text = f"Area: {area:.2f} sq. pixels"
        cv2.putText(image, area_text, (int(x) - 30, int(y) + radius + 15),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)  # Print the area as text on the image
    
    cv2.imshow('Detected Bright Spots', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return image

if __name__ == "__main__":
    """
    image_paths = ["C:\\Users\\One-Exploit's\\Desktop\\projects\\amu_sat\\sat_img\\sat0.png",
                   "C:\\Users\\One-Exploit's\\Desktop\\projects\\amu_sat\\sat_img\\sat1.png",
                   "C:\\Users\\One-Exploit's\\Desktop\\projects\\amu_sat\\sat_img\\sat2.png",
                   "C:\\Users\\One-Exploit's\\Desktop\\projects\\amu_sat\\sat_img\\sat3.png",
                   "C:\\Users\\One-Exploit's\\Desktop\\projects\\amu_sat\\sat_img\\sat4.png",
                   "C:\\Users\\One-Exploit's\\Desktop\\projects\\amu_sat\\sat_img\\sat5.png",
                   "C:\\Users\\One-Exploit's\\Desktop\\projects\\amu_sat\\sat_img\\sat6.png",
                   "C:\\Users\\One-Exploit's\\Desktop\\projects\\amu_sat\\sat_img\\sat7.png",
                   "C:\\Users\\One-Exploit's\\Desktop\\projects\\amu_sat\\sat_img\\sat8.png"];
                   """
    
    for k in range(0,16):   
        image_paths=str("C:\\Users\\One-Exploit's\\Desktop\\1 Projects\\amu_sat\\sat_img\\sat{}.png".format(k))
        processed_image = detect_bright_spots(image_paths)
        output_path = f"C:\\Users\\One-Exploit's\\Desktop\\1 Projects\\amu_sat\\sat_out\\sat{k}.png"
        cv2.imwrite(output_path, processed_image)
        k=k+1;
