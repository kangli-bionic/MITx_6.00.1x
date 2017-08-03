high = 100
low = 0
print("Please think of a number between 0 and 100!")

while True:
    sec_num = (low + high)//2
    print("Is your secret number {}?".format(sec_num))
    while True:
        choice = input("Enter 'h' to indicate the guess is too high. "
                   "Enter 'l' to indicate the guess is too low. "
                   "Enter 'c' to indicate I guessed correctly. ")
        if choice in 'hlc':
            break
        else:
            print('Sorry, I did not understand your input')
            print("Is your secret number {}?".format(sec_num))
    if choice == 'c':
        print('Game over. Your secret number was: {}'.format(sec_num))
        break
    elif choice == 'h':
        high = sec_num
    else:
        low = sec_num
