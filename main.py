from random import randint
from random import choice


def exam():
    # select difficulty of exam
    while True:
        print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")

        difficulty = input()

        if difficulty.isnumeric():
            difficulty = int(difficulty)
            break
        else:
            print("Incorrect format.")

    # generate and process 5 exam questions
    questions_asked = 0
    correct_answers = 0

    while questions_asked < 5:
        if difficulty == 1:
            equation = f"{randint(2, 9)} {choice(['+', '-', '*'])} {randint(2, 9)}"
            print(equation)

        else:
            number = randint(11, 29)
            print(number)

            equation = f"{number} ** 2"

        answer = input()

        while True:
            if answer.lstrip("-").isnumeric():
                if int(answer) == eval(equation):
                    print("Right!")
                    correct_answers += 1
                else:
                    print("Wrong!")
                break
            else:
                print("Incorrect format.")
                answer = input()

        questions_asked += 1

    print(f"Your mark is {correct_answers}/5.")

    print('Would you like to save your result to the file? Enter yes or no.')

    answer = input().lower()

    if answer == 'y' or answer == 'yes':
        username = input("What is your name?")

        with open('results.txt', 'a') as results:
            if difficulty == 1:
                results.write(f"{username}: {correct_answers}/5 in level 1 (simple operations with numbers 2-9).")

            else:
                results.write(f"{username}: {correct_answers}/5 in level 2 (integral squares 11-29).")

            print('The results are saved in "results.txt".')
            quit()

    else:
        quit()


if __name__ == '__main__':
    exam()
