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


# categorize the bmi to determine weight class of user
if bmi < 18.5:
    print('You are underweight')
elif 18.5 < bmi <= 24.9:
    print('You have a normal weight')
elif 25 <= bmi <= 29.9:
    print('You are overweight')
elif bmi <= 30 and bmi <= 34.9:
    print('Obesity Class I: Moderate; Watch out!')
elif bmi >= 35 and bmi <= 39.9:
    print('Obesity Class II: Severe')
else:
    print('Obesity Class III: Morbid Obesity!')