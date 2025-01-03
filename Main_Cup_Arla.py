from PIL import Image, ImageDraw, ImageFont

# Load the generated image and company logo
background_path = "/mnt/data/A_festive_Christmas_and_New_Year_greeting_card_des.png"
logo_path = "/mnt/data/akon-robotics-logo.jpg"

background = Image.open(background_path)
logo = Image.open(logo_path)

# Resize the logo to fit well into the design
logo_width = int(background.width * 0.2)
logo_height = int(logo_width * (logo.height / logo.width))
logo_resized = logo.resize((logo_width, logo_height))

# Calculate position for the logo (bottom center)
logo_x = (background.width - logo_width) // 2
logo_y = background.height - logo_height - 50  # Slightly above the bottom

# Paste the logo onto the background
background.paste(logo_resized, (logo_x, logo_y), logo_resized.convert("RGBA"))

# Adjust the text and elements to match the company's red branding color
draw = ImageDraw.Draw(background)
font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  # Default font path
font = ImageFont.truetype(font_path, 60)

# Overlay text with company branding colors
text = "Merry Christmas & Happy New Year"
text_color = (139, 0, 0)  # Matching AKON Robotics red
text_width, text_height = draw.textsize(text, font=font)
text_x = (background.width - text_width) // 2
text_y = 50  # Top margin for the text

# Add the text
draw.text((text_x, text_y), text, fill=text_color, font=font)

# Save the modified image
output_path = "/mnt/data/akon_robotics_christmas_greeting.png"
background.save(output_path)
output_path
