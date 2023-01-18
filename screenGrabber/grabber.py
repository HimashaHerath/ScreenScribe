import pyautogui
from PIL import Image
import pytesseract

# Capture the screen
image = pyautogui.screenshot()

# Save the image to a file
image.save('screen.png')

# Use OCR to extract text from the image
text = pytesseract.image_to_string(Image.open('screen.png'))
print(text)
