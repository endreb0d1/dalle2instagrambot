import os
import time
import pyautogui
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
from PIL import Image

# click function
def find_on_screen():  
    find_click_point = pyautogui.locateCenterOnScreen(click_point, confidence=0.9)
    x = find_click_point[0]
    y = find_click_point[1]
    pyautogui.moveTo(x, y)

# set title variable
title = ''
old_title = title

while True:
    # set webdriver
    browser = webdriver.Firefox()
    browser.maximize_window()

    # open Dall-e 2 Reddit
    browser.get('https://www.reddit.com/r/dalle2/new/')
    time.sleep(2)

    # login
    click_point = 'img\login_button.png'
    find_on_screen()
    pyautogui.click()
    time.sleep(5)
    pyautogui.typewrite('reddit_username')
    pyautogui.press('tab')
    pyautogui.typewrite('reddit_password')
    pyautogui.press('enter')
    time.sleep(5)

    # close popup
    pyautogui.press('esc')

    # open latest post
    pyautogui.moveTo(272, 477)
    pyautogui.click()
    time.sleep(10)

    # get latest post title and save it as a variable
    pyautogui.moveTo(473,263)
    pyautogui.click()
    pyautogui.click()
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'c')
    title = pyperclip.paste()
    
    # check if image already posted
    if title != old_title:
        # format title as tags
        title = '#' + title
        title = title.replace("(", "")
        title = title.replace(" ", " #")

        # save post image
        pyautogui.moveRel(0, 250)
        pyautogui.click(button='right')
        time.sleep(1)
        click_point = 'img\save_image_as.png'
        checker = pyautogui.locateCenterOnScreen(click_point)                          
        if checker == None:
            browser.quit()
        else:
            find_on_screen()
            pyautogui.click()
            time.sleep(5)
            pyautogui.typewrite('dalle_img')
            pyautogui.press('enter')
            time.sleep(5)

            # convert to jpg if webp
            try:
                dalle_img = Image.open("dalle_img.webp").convert("RGB")
                dalle_img.save("dalle_img.jpg","jpeg")

            except:
                pass

            # open Instagram
            browser.get('https://www.instagram.com')
            time.sleep(2)

            # login
            click_point = 'img\instagram_username.png'
            find_on_screen()
            pyautogui.click()
            time.sleep(2)
            pyautogui.typewrite('instagram_username')
            time.sleep(2)
            pyautogui.press('tab')
            pyautogui.typewrite('instagram_password')
            pyautogui.press('enter')
            time.sleep(10)

            # turn off notifications
            click_point = 'img\notifications.png'
            find_on_screen()
            pyautogui.click()
            time.sleep(2)

            # upload image from PC
            click_point = 'img\add_image.png'
            find_on_screen()
            pyautogui.click()
            time.sleep(5)

            click_point = 'img\select_from_computer.png'
            find_on_screen()
            pyautogui.click()
            time.sleep(5)
            pyautogui.typewrite('d')
            pyautogui.press('enter')
            time.sleep(5)
            
            for _ in range(2):
                click_point = 'img\next.png'
                find_on_screen()
                pyautogui.click()
                time.sleep(5)

            # paste tags
            for _ in range(5):
                pyautogui.press('tab')
            pyperclip.paste()
            time.sleep(5)

            click_point = 'img\share.png'
            find_on_screen()
            pyautogui.click()
            time.sleep(5)

            browser.quit()

            # delete uploaded photos
            os.remove("dalle_img.webp")
            os.remove("dalle_img.jpg")

            old_title = title
        
    # repeat every 20 minutes    
    time.sleep(1200)
