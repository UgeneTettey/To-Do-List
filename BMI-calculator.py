# a python file for calculating BMI

def get_bmi():
    # greeting
    print('I am a BMI calculator...')

    # receive user inputs as float
    weight = float(input('Enter your weight(in kg): '))
    height = float(input('Enter your height(in meters): '))

    # calculate bmi
    bmi = weight/height**2
    return round(bmi, 2)   #round the bmi to be able to categorize 

bmi = get_bmi()
print(f'Your BMI is {bmi}')

# add lines to convert bmi in cases where weight and height are gven in other units
# categorize the bmi to fit