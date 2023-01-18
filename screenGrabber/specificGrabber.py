import pyautogui
from PIL import Image
import pytesseract

# Prompt the user to select a region on the screen
print("Please select the region on the screen where the text is located")
x1, y1, x2, y2 = pyautogui.locateOnScreen('capture_region.png', grayscale=True, confidence=0.9)

# Capture the selected region
image = pyautogui.screenshot(region=(x1, y1, x2, y2))

# Save the image to a file
image.save('selected_region.png')

# Use OCR to extract text from the image
text = pytesseract.image_to_string(Image.open('selected_region.png'))

# Save the text to a file
with open("selected_region_text.txt", "w") as file:
    file.write(text)

print("Text from the selected region has been saved to 'selected_region_text.txt'")
