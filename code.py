import cv2
import csv
import os

# Path to your image file
image_path = "img/india.jpg"

# Load the image
image = cv2.imread(image_path)

# Initialize QRCode detector
detector = cv2.QRCodeDetector()

# Detect and decode
data, vertices_array, _ = detector.detectAndDecode(image)

if data:
    print("QR Code Data:", data)

    # Extract image name (without folder path)
    image_name = os.path.basename(image_path)

    # Save result into a CSV file
    with open("qrcodes.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([image_name, data])

    print(f"✅ Saved to qrcodes.csv: ({image_name}, {data})")
else:
    print("No QR code found.")
