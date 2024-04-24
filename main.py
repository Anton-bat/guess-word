
import random
random_words = ["apple", "orange", "mango"]
given_word = random.choice(list(random_words))
counter = int(input("How many try do you want?: "))
to_show = ["*" for _ in range(len(given_word))]
while counter > 0:
    user_input = input("Give me a word or a letter:")
    if given_word == user_input:
        print("Right guess")
        break
    elif len(user_input) == 0:
        print("plese enter a suggestion")
    elif user_input not in {letter for letter in given_word}:
        print("No such letter in given word")
        counter -= 1   
    elif len(user_input) == 1:
        if user_input in given_word:
            for k, v in enumerate(given_word):
                if v == user_input:
                    to_show[k] = user_input 
                    print(to_show)
            if "*" not in to_show:
                print("You won")
                break
    else:
        pass
if counter == 0:
    print("You loose")

