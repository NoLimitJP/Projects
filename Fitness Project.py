import random
f = open("Out.txt", "w")
#we're looking to randomize inputs so that our program can be flexible to user input
def randomWeight():
    x = random.randint(0,300)
    return x
def randomHeight():
    x = random.uniform(0.0,2.0) # random.uniform produces random integers
    return round(x, 2)
    #This bmi calc takes 2 arguments one for height and one for weight then calculates the bmi
def bmiCalc(x,y):
    f.write(f"weight: {x}\n")
    f.write(f"height: {y} meter(s) \n")
    level = x/float(y**2)
    if level < 18.5:
        f.write("BMI: Underweight\n")
    if level >= 18.5 and level<25:
        f.write("BMI: Normal\n")
    if level >= 25 and level < 30:
        f.write("BMI: Overweight\n")
    if level > 30:
        f.write("BMI: Obese\n")
    f.close()
    
bmiCalc(randomWeight(), randomHeight())
