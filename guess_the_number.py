#Test Project
name = input('please enter your name : ')
print('Hi', name, 'Lets play a game!' )
print('just think of a number between 1 and 99 in your mind')
print('and I will guess the right answer!')
print('If my answer is greater than your guess send g')
print('If my answer is smaller than your guess send s ')
print('and if my answer is right send c')
print('lets get started!!!')
a = 1
b = 99
import random
guess = random.randint(1, 99)
print('my guess is : ', guess)
feedback = input('How was my answer ? ')
while feedback != 'c':
    if feedback == 'g':
        a = guess
        guess = random.randint(a, b)
    elif feedback == 's':
        b = guess
        guess = random.randint(a, guess)
    print('my guess is : ', guess)
    feedback = input('How was my answer ? ')

print('Hooooray!!! I guessed your answer ', name)