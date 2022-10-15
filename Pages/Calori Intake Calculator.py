import streamlit as st
import random
class Calories():
    def __init__(self, weight, height, age, sex):
        self.weight = weight
        self.height = height
        self.age = age
        self.sex = sex
    def bf(self):
        bf = 10.2107142857142 +1.22571429 *self.accu_mesure -0.01428571 *self.accu_mesure**2
        return round(bf ,1)
    def LBM(self):
        return self.weight *( 1 -self.bf( ) /100)
    def BMR(self, sex):
        if sex == "M"or'm' :
            bmr = ((10 *self.weight) + (6.25 *self.height) - ( 5 *self.age) + 5)
        else:
            bmr = ((10 *self.weight) + (6.25 *self.height) - ( 5 *self.age) - 161)
            # bmr = 370 + 21.6*self.LBM()
        return bmr

    def TDEE(self, act_mult = 1.4):
        '''Calculate total daily energy expenditure'''

        return round(self.BMR(self.sex ) *act_mult)

    def bulk(self, percentage = 0.2, act_mult = 1.4):
        '''Calculate bulk calories'''

        return round(self.TDEE(act_mult = act_mult ) *( 1 +percentage))

    def cut(self, percentage = 0.2, act_mult = 1.4):
        '''Calculate cut calories'''

        return round(self.TDEE(act_mult = act_mult ) *( 1 -percentage))

    def protein_intake(self, weight, mult = 0.9):
        '''Calculate protein intake'''

        return round(self.weight *mult)

st.title("Calorie Intake Calculator")
st.subheader('Lets estimate your calorie intake..')

# enter age
age = st.number_input("Enter your age: ",step = 1)
sex = st.text_input("Enter your sex (M for Male and F for Female): ", max_chars=1)

try:
    if sex not in ['M', 'F','m','f']:
        raise AssertionError('Please enter the letter M or F')
except AssertionError as e:
    print(e)

# enter weight in kg
while True:
    try:
        weight = st.number_input("Enter your weight in kg: ")
        # asserting weight is in Kg
        if not weight < 120:
            raise AssertionError('Weight needs to be in Kg. e.g: 61, 84..')
        break
    except AssertionError as e:
        print(e)

    # enter height in cm
height = st.number_input("Enter your height in cm: ")

try:
    # asserting height in cm
    if not height > 100:
        raise AssertionError('Height needs to be in centimeters. e.g: 167, 179..')
except AssertionError as e:
    print(e)

C = Calories(weight, height, age, sex)

st.text('''
1.2 - Sedentary: Little or no physical activity.
1.3 - Lightly Active: Light exercise or activity 1-3 days per week.
1.5 - Moderately Active: Moderate exercise or activity 3-5 days per week.
1.7 - Very Active: Hard exercise or activity 6-7 days per week.
1.9 - Extremely Active: Hard daily exercise or activity and physical work 
''')
activity = st.number_input('''Enter your activity multiplier according to the table above (number between 1.2 to 1.9): ''')

st.text('''Your daily calorie intake:
{} for maintaining
{} for losing
{} for gaining'''.format(C.TDEE(act_mult=activity), C.cut(act_mult=activity), C.bulk(act_mult=activity)))

protein = C.protein_intake(weight)

st.text('''Your daily minimum protein intake is: {} grams'''.format(protein))
