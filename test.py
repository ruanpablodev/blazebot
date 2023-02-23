from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

wins = 1000
wins2 = str(wins)
loss = 20
loss2 = str(loss)
branco = 3000
branco2 = str(branco)

if wins < 10:
    wins = "00" + wins2

if wins < 100:
    wins = "0" + wins2

if wins < 1000:
    wins = wins2

if wins < 10000:
    wins = wins2


if branco < 10:
    branco = "00" + branco2

if branco < 100:
    branco = "0" + branco2

if branco < 1000:
    branco = branco2

if branco < 10000:
    branco = branco2


if loss < 10:
    loss = "00" + loss2

if loss < 100:
    loss = "0" + loss2

if loss < 1000:
    loss = loss2

if loss < 10000:
    loss = loss2

print(wins)

img = Image.open("status.png")
draw = ImageDraw.Draw(img) 
font = ImageFont.truetype("good times rg.otf", 70) 
draw.text((145, 490), wins, (255, 255, 255), font=font) 
draw.text((575, 490), loss, (255, 255, 255), font=font) 
draw.text((1050, 490), branco, (255, 255, 255), font=font) 
aaaa = img.convert('RGB')
aaaa.save('./testes/sample.jpg')  