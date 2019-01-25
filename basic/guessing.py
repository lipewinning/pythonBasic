secret_word = 'giraffe'
guess = ''
maximum_guess = 4
guess_count = 1

while guess_count <= maximum_guess:

    guess = input('Enter guess: ')

    if guess == secret_word:
        print('You won')
        break

    if guess_count == maximum_guess:
        print('You have had your chance')
        break

    guess_count += 1


print('End')
