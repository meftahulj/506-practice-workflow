import pandas as pd
import numpy as np 
num_var = 27
str_var = "Hi, my name is Mef"
list_var = [1,2,3,4,5,6]
Dictionary_var = {
    "Full name" : "Meftahul Jannat", 
    "Favorite Sports": ["Badminton", "Basketball", "Pickleball"], 
    "Classes": {
        "503" : "Black Benz", 
        "506" : "Hants Williams"
    }
}
print ("Number variable:", num_var)
print ("String Variable:", str_var)
print ("List Variable:", list_var)
print ("Dictionary Variable:", Dictionary_var)

def bmi_calc (weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        bmi_category = "Normal"
    else: 
        bmi_category = "Overweight"
    return bmi, bmi_category
weight_kg = 68
height_m = 1.62

bmi_final, health_status = bmi_calc(weight_kg, height_m)
print("BMI:", bmi_final)
print("Health Status:", health_status)