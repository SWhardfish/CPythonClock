"""
CPython Clock on SSD1306 OLED 128x64

https://learn.adafruit.com/ssd1306-oled-displays-with-raspberry-pi-and-beaglebone-black/usage
"""

import time
from time import gmtime, strftime
from datetime import datetime
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64  # Change to 64 if needed
BORDER = 1


# Use for SPI
spi = board.SPI()
oled_cs = digitalio.DigitalInOut(board.D5)
oled_dc = digitalio.DigitalInOut(board.D6)
oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

# Draw a smaller inner rectangle
draw.rectangle(
    (BORDER, BORDER, oled.width - BORDER - 1, oled.height - BORDER - 1),
    outline=0,
    fill=0,
)

# Load default font.
font = ImageFont.load_default()
#font = ImageFont.truetype("arial.ttf", 2)

#showtime = strftime("%a  %d %b  %Y %X",gmtime())
while True:
    now = datetime.now()
    nowday = now.strftime("%A")
    nowdate = now.strftime("%d %b %Y")
    nowtime = now.strftime("%H:%M:%S")
    # Clear display.
    draw.rectangle((2,5,120,50), outline=0, fill=0)
    # Draw Some Text
    text2 = nowday
    text1 = nowdate
    text = nowtime
    (font_width2, font_height2) = font.getsize(text2)
    (font_width1, font_height1) = font.getsize(text1)
    (font_width, font_height) = font.getsize(text)
    draw.text(
        (oled.width // 2 - font_width2 // 2, 12),
        text2,
        font=font,
        fill=255,
    )
    draw.text(
        (oled.width // 2 - font_width1 // 2, 22),
        text1,
        font=font,
        fill=255,
    )
    draw.text(
        (oled.width // 2 - font_width // 2, 37),
        text,
        font=font,
        fill=255,
    )

    # Display image
    oled.image(image)
    oled.show()
    time.sleep(1)
