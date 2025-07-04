print("Welcome to our Quiz game!")
print('='*20)
print('Enter to start')
print('='*20)

QuizGame = {'Which keyword is used to define a function in python?' : 'def', 
            'What is extension of python file?': '.py',
            'Which keyword is use to check a condition?' :'if',
            'Set can store duplicate values?' : 'F',
            'This course is very nice?' : 'T'}

score = 0

for ques, ans in QuizGame.items():
    print(f"\nQ: {ques}")
    user_input = input('Your answer: ')
    if user_input == ans:
        print('Correct!')
        score += 1
    else:
        print('Worng answer!')
        print(f"Correct: {ans}")    
        
print(f"Your score is {score} out of 5")'''
        
        
