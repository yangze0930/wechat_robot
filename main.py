# encoding=utf-8
import numpy as np
from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image
import os
import itchat
import time
import sys
from itchat.content import *

# print text on a ramdom selected template image
def generateTextOnPicture(img,text):
    height = img.shape[0]
    textLen = len(text)
    textStr = text

    font = ImageFont.truetype("fonts/bb1338/cartoon.TTF", 22)
    img_pil = Image.fromarray(img, mode="RGB")
    draw = ImageDraw.Draw(img_pil)

    left = max(112 - textLen * 11, 1)
    up = height - 26
    draw.text((left, up), textStr, font=font, fill=(0, 0, 0), align="center")
    filename = "%s.jpg" % (int(100 * time.time() - 140000000000))
    filepath = "temp/" + filename
    img_pil.save(filepath)
    return filepath


# accpet friend apply automatically
@itchat.msg_register(INCOME_MSG)
def save_record(msg):
    if msg['Type'] == 'Text':
        itchat.send_msg(msg['User']['NickName']+': '+msg[TEXT],toUserName='filehelper')
    elif msg['Type'] in ['Picture','Attachment','Recording','Video']:
        msg[TEXT]('temp/'+msg['FileName'])
        itchat.send_file('temp/'+msg['FileName'],toUserName='filehelper')


if __name__ == '__main__':

    itchat.auto_login(enableCmdQR=2, hotReload=True)
    try:
        itchat.run()
        print("itchat run over")
    except:
        sys.exit(1)
