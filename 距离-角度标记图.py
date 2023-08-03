import cv2
import numpy as np
import matplotlib.pyplot as plt
def get_white_contour(image):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    white_contour = max(contours, key=cv2.contourArea)

    return white_contour


def draw_distance_angle_markers(image, center, num_angles=360):
    height, width = image.shape[:2]
    center_x, center_y = center
    distances = []
    step_size = 1
    for angle in range(90,450,1):
        x=center_x
        y=center_y
        while True: 
            x += step_size * np.cos(angle*np.pi/180)
            y += step_size * np.sin(angle*np.pi/180)          
            if x < 0 or y < 0 or x >= image.shape[0] or y >= image.shape[1]:
                break
            if image[int(x)][int(y)] == 255 or image[int(x)][int(y+1)]:
                break


     
        distance = np.sqrt((x-center_x)**2 + (y-center_y)**2)
    
        distances.append(distance)


    plt.plot(distances, color='b', linestyle='-')
    plt.title('Distance Line Plot')
    plt.xlabel('angles')
    plt.ylabel('Distance from center to boundary')
    plt.show()

if __name__ == "__main__":
  
    image_path = "D:/Fig1111(b)(square).tif"
    binary_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)


    white_contour = get_white_contour(binary_image)

  
    white_contour_image = np.zeros_like(binary_image)
    cv2.drawContours(white_contour_image, [white_contour], -1, 255, 1)

    cv2.imshow("White Contour", white_contour_image)
    cv2.waitKey(0)
    center_point = (white_contour_image.shape[1] // 2, white_contour_image.shape[0] // 2)


    draw_distance_angle_markers(white_contour_image, center_point)
    
  
    cv2.waitKey(0)
    cv2.destroyAllWindows()


