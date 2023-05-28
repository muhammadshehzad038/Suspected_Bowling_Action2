import cv2

def detect_bowling_hand_from_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply a hand detection algorithm (replace this with your specific detection method)
    # For example, you can use Haar cascades or a machine learning-based approach like TensorFlow or YOLO.
    # Here, we'll use a placeholder method that simply detects if the hand is on the left or right side of the image.
    height, width, _ = image.shape
    left_side = gray[:, :width // 2]
    right_side = gray[:, width // 2:]

    if cv2.countNonZero(left_side) > cv2.countNonZero(right_side):
        return "Left-handed bowler"
    else:
        return "Right-handed bowler"

# Example usage:
image_path = "image.jpg"
hand = detect_bowling_hand_from_image(image_path)
print("The bowler is a", hand)

# Example usage
#result = detect_bowling_hand("/content/image1.jpeg")
#print(result)