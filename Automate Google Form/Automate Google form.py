from msilib.schema import CheckBox
from turtle import pd
from selenium import webdriver
import pandasas as pd
import time
import json
from datetime import datetime
import pathlib
import glob
import os
import sys
import faker
import numpy as np
sys.path.append(".")

f=faker.Faker()
colors=['red','blue','green','yellow','orange','purple','pink','black','white'] # You can change the colors.
names=[f.name() for _ in range(100)] # You can change the number of names.
ages=[np.random.randint(18,100) for _ in range(100)] # Create a dictionary to map the color to the index.
color_choices=[np.random.choice(colors,1)[0] for _ in range(100)]
database=pd.DataFrame(dict(name=names,color=color_choices,ages=ages)) # You can change the dataframe.
database.to_csv('Submission.csv',index=False)
database.head()

text_question_element_class='quantumWizTextinputPaperinputInput' 
checkbox_question_element_class='appsMaterialWizToggleRadiogroupOffRadio'
submit_element_class='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span' 
url="https://forms.gle/Xq7X8ZxXyZYX8Y8y9" # Change the url to your form url.
driver = webdriver.Chrome(executable_path="./chromedriver") 
driver.get(url)

def answerNameAge(driver,df,element_class,user_id):
    name=df["name"][user_id]
    age=df["ages"][user_id]
    text_answers=[name,str(age)] # You can change the text answers.
    # following the order of the questions.
    text_questions=driver.find_elements_by_class_name(element_class)
    for a,q in zip(text_answers,text_questions):
        q.send_keys(a)
    return driver

color_index_dict={"red":0,"blue":1,"green":2,"yellow":3,"orange":4,"purple":5,"pink":6,"black":7,"white":8} # You can change the color index dictionary.

def answerCheckBox(driver,df,element_class,user_id):
    color_answer=df["colors"][user_id]
    color_answer_index=color_index_dict[color_answer]
    driver.find_elements_by_class_name(element_class)[color_answer_index].click()
    return driver
def submit(driver,element_class):
    driver.find_element_by_xpath(element_class).click()
    return driver
df=pd.read_csv("./Submission.csv")
text_question_element_class='quantumWizTextinputPaperinputInput'
checkbox_question_element_class='appsMaterialWizToggleRadiogroupOffRadio'
url="https://forms.gle/Xq7X8ZxXyZYX8Y8y9" # Change the url to your form url.
driver = webdriver.Chrome(executable_path="./chromedriver")
for user_id in range(len(df)):
    driver.get(url)
    driver.maximize_window()
    driver=answerNameAge(driver,df,text_question_element_class,user_id)
    driver=answerCheckBox(driver,df,checkbox_question_element_class,user_id)
    driver=submit(driver,submit_element_class)
    time.sleep(5)