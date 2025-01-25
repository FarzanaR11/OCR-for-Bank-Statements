import cv2
import pytesseract

def extract_text(image_path):
    img = cv2.imread(image_path)
    text = pytesseract.image_to_string(img)
    return text

if __name__ == "__main__":
    text = extract_text("bank_statement.jpg")
    print("Extracted Text:", text)
