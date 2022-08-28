import pywhatkit as pw
from sys import stdin


text = "man, tolong join grup wa sch nlc ya :D"
img = 'D:\image.jpg'

for line in stdin:
    line = '+' + line
    print('Send to number: ' + line, end='')
    pw.sendwhatmsg_instantly(line, text, 10, True, 5)
    print('Text has been sent')
    pw.sendwhats_image(line, img, '', 10, True, 10)
    print('Image has been sent')
