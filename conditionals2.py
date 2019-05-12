'''
3.3 Write a program to prompt for a score between 0.0 and 1.0. 
If the score is out of range, print an error. 
If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.
'''

score = input('Please enter a score between 0.0 and 1.0: ')

try:
    score = float(score)
except:
    print('Input not an acceptable number - please input a number. Exiting.')
    exit()

score_letter = ''

if score >= 0.9:
    letter = 'A'
elif score >= 0.8:
    letter = 'B'
elif score >= 0.7:
    letter = 'C'
elif score >= 0.6:
    letter = 'D'
else:
    letter = 'F'

print(letter)