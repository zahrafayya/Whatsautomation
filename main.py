import pywhatkit as pw

text = "ini text yang mau dikirim"
img = 'D:\image.jpg'

pw.sendwhatmsg_instantly('+62811111111111', text, 10, True, 5)
pw.sendwhats_image('+628111111111', img, '', 10, True, 10)

