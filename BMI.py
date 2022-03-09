# CheckInput
def CheckInput(Weight, Height):
    i = False
    j = False
    while (i == False and j == False):
        ## Weight
        if (i == False):
            try:
                ValW = int(Weight)
                i == True
            except ValueError:
                try:
                    ValW = float(Weight)
                    i == True
                except ValueError:
                    Weight = input("Your value type is not valid for your Weight, please input a number. (WEIGHT): ")
        
        ## Height
        if (j == False):
            try:
                ValH = int(Height)
                j = True
            except ValueError:
                try:
                    ValH = float(Height)
                    j = True
                except ValueError:
                    Height = input("Your value type is not valid for your Height, please input a number. (HEIGHT): ")

    return ValW, ValH


# # BMI Function
def BMICalculator(Weight, Height):
    ## Global Truths
    UnderweightMax = 18.5
    OverweightMin = 25.0
    ObeseMin = 30.0

    ## Inputs
    BodyWeightLB = float(Weight)
    BodyHeightIN = float(Height)
    

    ## Maths
    BodyWeightKG = BodyWeightLB * 0.45
    BodyHeightM = BodyHeightIN * 0.025
    HeightSquaredM = BodyHeightM ** 2
    BMI = BodyWeightKG / HeightSquaredM

    ## If-thens (category)
    if BMI < UnderweightMax:
        category = "Underweight"
    elif BMI >= UnderweightMax and BMI < OverweightMin:
        category = "Normal weight"
    elif BMI > OverweightMin and BMI < ObeseMin:
        category = "Overweight"
    elif BMI >= ObeseMin:
        category = "Obese"
    else:
        category = 0

    return BMI, category


# Main
## Inputs
Weight = input("Input your body weight in pounds(lbs): ")
Height = input("Input your physical height in inches(in): ")
Weight, Height = CheckInput(Weight, Height)
        
BMI, category = BMICalculator(Weight, Height)


## Prints
print("You are {} with a Body Mass Index (BMI) of {}".format(category, BMI))
input("Press enter to exit.")