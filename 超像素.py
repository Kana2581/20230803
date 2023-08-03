import cv2

def superpixel_segmentation(image_path, num_superpixels=1000):
    image = cv2.imread(image_path)
    
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
    
    slic = cv2.ximgproc.createSuperpixelSLIC(image=lab_image, region_size=30)
    
    slic.iterate(num_iterations=50)
    slic.enforceLabelConnectivity(min_element_size=50)
    
    labels = slic.getLabels()
    num_superpixels = slic.getNumberOfSuperpixels()
    print(num_superpixels)
    
    mask = slic.getLabelContourMask()
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    image_with_contour = cv2.addWeighted(image, 0.8, mask, 1.0, 0)


    superpixel_image = image.copy()
    for i in range(num_superpixels):
        superpixel_image[labels == i] = image[labels == i].mean(axis=0)

    superpixel_image = cv2.addWeighted(superpixel_image, 0.8, mask, 1.0, 0)
    return labels, num_superpixels, image_with_contour,superpixel_image


image_path = "D:/CB3B2CEFAC9B94DBDE568628EEE3F0E96020DA14_size45_w770_h513.jpg"  
num_superpixels = 1000  
labels, num_superpixels, image_with_contour, superpixel_image = superpixel_segmentation(image_path, num_superpixels)


#cv2.imshow("Superpixel Segmentation", image_with_contour)
cv2.imshow("Superpixel Image", superpixel_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
   