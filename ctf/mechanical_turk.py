#!/usr/bin/env python3

# ./images_clean.py | grep Valid

URL="https://71431fe2ff3fa3e8.247ctf.com/"
import requests


import cv2
# https://github.com/sirfz/tesserocr/issues/165
import locale
locale.setlocale(locale.LC_ALL, 'C')
from tesserocr import PyTessBaseAPI, PSM, OEM
import numpy as np
from PIL import Image


def clean_colors(img):
    # Remove dark gray noise lines color 140,140,140
    lower_black = np.array([140,140,140], dtype = "uint16")
    upper_black = np.array([141,141,141], dtype = "uint16")
    black_mask = cv2.inRange(img, lower_black, upper_black)
    img2 = cv2.bitwise_and(img, img, mask= black_mask)
    img = cv2.add(img, img2)

    # Remove light gray background color 245,245,245
    #lower_black = np.array([245,245,245], dtype = "uint16")
    #upper_black = np.array([246,246,246], dtype = "uint16")
    #black_mask = cv2.inRange(img, lower_black, upper_black)
    #img2 = cv2.bitwise_and(img, img, mask= black_mask)
    #img = cv2.add(img, img2)

    return img

def resize(img):
    #img = cv2.resize(img, None, fx=10, fy=10, interpolation=cv2.INTER_LINEAR)
    img = cv2.resize(img, None, fx=5, fy=5, interpolation=cv2.INTER_CUBIC)
    return img


def thresh_binary(img):
    th, img = cv2.threshold(img, 231, 255, cv2.THRESH_BINARY)
    return img


def thresh_otsu(img):
    th, img = cv2.threshold(img, 0, 255, cv2.THRESH_OTSU)
    return img

def brightness_contrast(img):
    alpha = 1.0 # Contrast control (1.0-3.0)
    beta = 1 # Brightness control (0-100)
    img = cv2.convertScaleAbs(img, alpha=alpha, beta=beta)
    return img


with PyTessBaseAPI(psm=PSM.SINGLE_WORD, oem=OEM.TESSERACT_ONLY) as api:
    api.SetVariable("tessedit_char_whitelist", "0123456789+")
    #api.SetVariable("load_system_dawg", "false")
    #api.SetVariable("load_freq_dawg", "false")
    #api.SetVariable("user_patterns", "pattern.txt")
    #api.SetVariable("tessedit_fix_fuzzy_spaces", "true")

    sess = requests.session()
    response = sess.get(URL)
    cookie = {'PHPSESSID': response.cookies['PHPSESSID']}

    for i in range(300):
        #print ("alert- "+str(i))

        session_raw = sess.get(URL+"/mturk.php", cookies=cookie, stream=True).raw

        #print (response)
        #print (r.headers)
        #print (r.text)
        #print (r.cookies)



        image1 = np.asarray(bytearray(session_raw.read()), dtype="uint8")
        img = cv2.imdecode(image1, cv2.IMREAD_COLOR)


        img = clean_colors(img)

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img = brightness_contrast(img)

        img = thresh_binary(img)
        #img = thresh_otsu(img)


        img = resize(img)
        img = thresh_otsu(img)
        #img = thresh_binary(img)


        api.SetImage(Image.fromarray(img))


        try:
            sp = api.GetUTF8Text().replace(" ", "").rstrip().split('+')

            #print(sp)
            #cv2.imshow('adjusted', img)
            #cv2.waitKey()


            rez = int(sp[0])+int(sp[1])
            p = sess.post(URL, data={"captcha": rez}, cookies=cookie)
            print (p.text)
        except:

            sp = api.GetUTF8Text().replace(" ", "").rstrip()
            a = sp[:6]
            b = sp[6:]
            rez = int(a)+int(b)
            p = sess.post(URL, data={"captcha": rez}, cookies=cookie)
            print (p.text)
            #print ("alert- ocr bad")