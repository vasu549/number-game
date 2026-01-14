
''' let's build our number guessing game '''

print('=====Welcome to the number guessing game(1-100):=====')
start=1
end=100
import random
a=random.randint(start,end+1)
times=0
while True:
    b=int(input(f'''   Guess the number    :'''))
    times=times+1
    if b>a:
        print('Your number is too high🤔')
    elif a>b:
        print('Your number is too low🤭')
    else:
        print(f'you are correct ❤️❤️')
        break
print(f'yay! you guessed the {a} number in {times} times ')
