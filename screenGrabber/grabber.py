import pyautogui
from PIL import Image
import pytesseract

# Capture the screen
image = pyautogui.screenshot()

# Save the image to a file
image.save('screen.png')

# Use OCR to extract text from the image
text = pytesseract.image_to_string(Image.open('screen.png'))

# Save the text to a file
with open("screen_text.txt", "w") as file:
    file.write(text)

print("Text from the screen has been saved to 'screen_text.txt'")

# print(text)
