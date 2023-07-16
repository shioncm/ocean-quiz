from string import ascii_lowercase

QUESTIONS = [
    "When was the first known use of the word 'quiz'",
    "Which built-in function can get information from the user",
]

CHOICES = "INACCURATE\t1\t2\t3\t4\t5\tACCURATE"

ALL_USER_CHOICES = []

def start_screen():
    print("To start the OCEAN quiz, enter 's'")
    print("To exit this app, enter 'q'")
    
    while(True):
        user_choice = input("Enter 's' or 'q': ")

        if(user_choice == 's'):
            run_quiz()
        elif(user_choice == 'q'):
            exit(0)
        else:
            print("Invalid input. Please try again.")

def run_quiz():
    for num, question in enumerate(QUESTIONS, start=1):
        print(f"\nQuestion {num}:")
        print(f"{question}?")
        print(CHOICES)
        while (True):
            user_choice = input("Choice? ")

            if user_choice.isnumeric():
                ALL_USER_CHOICES.append(user_choice)
                break
            else:
                print("Invalid number. Please try again.")
    
    end_screen()

def end_screen():
    print("\nThanks for playing!")
    
    while(True):
        user_choice = input("Review your choices? (y/n) ")
        if(user_choice == 'y'):
            print("\n---- YOUR ANSWERS ----")
            for num, question in enumerate(QUESTIONS, start=1):
                print(f"\nQuestion {num}:")
                print(f"{question}?")
                print(ALL_USER_CHOICES[num-1])
            
            exit(0)
        elif(user_choice == 'n'):
            exit(0)
        else:
            print("Invalid input. Please try again.")

start_screen()

    
