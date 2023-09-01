##############################################################################################################################
#   ____  _____ ___    __  ______       __  _____  ____  _____    __  _____  ______    ____                                  #
#  / __ \/ ___//   |  /  |/  /   |     /  |/  / / / / / / /   |  /  |/  /  |/  /   |  / __ \                                 #
# / / / /\__ \/ /| | / /|_/ / /| |    / /|_/ / / / / /_/ / /| | / /|_/ / /|_/ / /| | / / / /                                 #
#/ /_/ /___/ / ___ |/ /  / / ___ |   / /  / / /_/ / __  / ___ |/ /  / / /  / / ___ |/ /_/ /                                  #
#\____//____/_/  |_/_/  /_/_/  |_|  /_/  /_/\____/_/ /_/_/  |_/_/  /_/_/  /_/_/  |_/_____/                                   #
#                                                                                           -SOCIETY CONTRIBUTIONS           #
#Microsoft educational accounts password changer (C) 2023.                                                                   #
#Written by Osama Muhammad as a society contribution.                                                                        #
#This code is fully free & open source, you can re-publish this resource without changing copyrights.                        #
#You can develop this resource and add your credits to this work, but never remove the original core credits.                #
##############################################################################################################################
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import random
import string
def generate_strong_password(length=12):
   
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    all_chars = lowercase_letters + uppercase_letters + digits + special_chars
    
    password = [
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    for _ in range(length - 4):
        password.append(random.choice(all_chars))
    
    random.shuffle(password)

    password_str = ''.join(password)
    return password_str
def click(xpath):
    driver.find_element(By.XPATH, xpath).click()
def login(email, password):
    driver.get("https://login.microsoftonline.com/")
    time.sleep(2)
    email_field = driver.find_element(By.NAME, "loginfmt")
    email_field.send_keys(email)
    email_field.send_keys(Keys.RETURN)
    time.sleep(2)
    password_field = driver.find_element(By.NAME, "passwd")
    password_field.send_keys(password)
    password_field.send_keys(Keys.RETURN)
def completeVers():
    try:
        if driver.find_element(By.XPATH, '//*[@id="lightbox"]/div[3]/div/div[2]/div/div[1]').text == 'Stay signed in?':
            click('//*[@id="idSIButton9"]')
            return "true"
        else:
                if driver.find_element(By.XPATH, '//*[@id="heading"]').text == 'More information required':
                    click('//*[@id="idSubmit_ProofUp_Redirect"]')
                    time.sleep(20)
                    click('//*[@id="root"]/div/div[2]/main/div/section[2]/div/div[2]/a')
                    time.sleep(3)
                    click('//*[@id="idSIButton9"]')
                    return 'true'
    except:
        try:
            if driver.find_element(By.XPATH, '//*[@id="heading"]').text == 'More information required':
                click('//*[@id="idSubmit_ProofUp_Redirect"]')
                time.sleep(20)
                click('//*[@id="root"]/div/div[2]/main/div/section[2]/div/div[2]/a')
                time.sleep(3)
                click('//*[@id="idSIButton9"]')
                return 'true'
        except:
            return "false"
def changePassword(oldPassword, newPassword):
    driver.get("https://account.activedirectory.windowsazure.com/ChangePassword.aspx")
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="ChangePasswordControl_OldPasswordTextBox"]').send_keys(oldPassword)
    driver.find_element(By.XPATH, '//*[@id="ChangePasswordControl_NewPasswordTextBox"]').send_keys(newPassword)
    driver.find_element(By.XPATH, '//*[@id="ChangePasswordControl_ConfirmNewPasswordTextBox"]').send_keys(newPassword)    
    click('//*[@id="ChangePasswordControl_OkButton"]/span')
    time.sleep(6)
with open("emails.txt", "r") as file:
    for line in file:
        driver = webdriver.Chrome()
        email, password = line.strip().split(":")
        cleaned_line = line.strip()
        login(email, password)
        time.sleep(3)
        if completeVers() != "false":
            time.sleep(3)
            newPassword = generate_strong_password(length=12)
            changePassword(password, newPassword)
            with open("new_emails.txt", "a") as file2:
                file2.write(email+':'+newPassword+"\n")
        else:
            print("PASSED")
        driver.quit()