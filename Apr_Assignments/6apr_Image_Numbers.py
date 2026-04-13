import cv2
img = cv2.imread("image.jpg")
print("Image Shape:", img.shape)
print("First Pixel Value:", img[0][0])
print("Number of Channels:", img.shape[2])
print("\nSample Pixel Values:")
for i in range(3):
    for j in range(3):
        print(f"Pixel[{i},{j}] =", img[i][j])