import random
from string import ascii_lowercase

QUESTIONS = [
    "I am the life of the party",
    "I feel little concern for others",
    "I am always prepared",
    "I get stressed out easily",
    "I have a rich vocabulary",
    "I don't talk a lot",
    "I am interested in people",
    "I leave my belongings around",
    "I am relaxed most of the time",
    "I have difficulty understanding abstract ideas",
    "I feel comfortable around people",
    "I insult people",
    "I pay attention to details",
    "I worry about things",
    "I have a vivid imagination",
    "I keep in the background",
    "I sympathize with others' feelings",
    "I make a mess of things",
    "I seldom feel blue",
    "I am not interested in abstract ideas",
    "I start conversations",
    "I am not interested in other people's problems",
    "I get chores done right away",
    "I am easily disturbed",
    "I have excellent ideas",
    "I have little to say",
    "I have a soft heart",
    "I often forget to put things back in their proper place",
    "I get upset easily",
    "I do not have a good imagination",
    "I talk to a lot of different people at parties",
    "I am not really interested in others",
    "I like order",
    "I change my mood a lot",
    "I am quick to understand things",
    "I don't like to draw attention to myself",
    "I take time out for others",
    "I shirk my duties",
    "I have frequent mood swings",
    "I use difficult words",
    "I don't mind being the center of attention",
    "I feel others' emotions",
    "I follow a schedule",
    "I get irritated easily",
    "I spend time reflecting on things",
    "I am quiet around strangers",
    "I make people feel at ease",
    "I am exacting in my work",
    "I often feel blue",
    "I am full of ideas"
]

ALL_CHOICES = "INACCURATE\t1\t2\t3\t4\t5\tACCURATE"

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
    user_choices = []

    for num, question in enumerate(QUESTIONS, start=1):
        print(f"\nQuestion {num}:")
        print(f"{question}?")
        print(ALL_CHOICES)
        while (True):
            choice = input("Choice? ")

            if choice.isnumeric() and choice.replace(".", "").isnumeric() == False and int(choice) > 0 and int(choice) < 6:
                user_choices.append(choice)
                break
            else:
                print("Invalid number. Please try again.")
    
    # For debugging purposes, ALL_USER_CHOICES will be set to a random
    # list of 50 choices, ranging from 1 to 5.
    user_choices = [random.randint(1, 5) for x in range(0, 50)]

    user_scores = calc_score(user_choices)
    end_screen(user_choices, user_scores)

def calc_score(user_choices):
    # List to store user OCEAN scores. 
    # score E : scores[0]
    # score A : scores[1]
    # score C : scores[2]
    # score N : scores[3]
    # score O : scores[4]
    scores = [20, 14, 14, 38, 8]

    for num in range(0, len(user_choices), 5):
        scores[0] += user_choices[num] * (-1) ** num
        scores[1] -= user_choices[num+1] * (-1) ** num
        scores[2] += user_choices[num+2] * (-1) ** num
        scores[3] -= user_choices[num+3] * (-1) ** num
        scores[4] += user_choices[num+4] * (-1) ** num

    return scores

def end_screen(user_choices, user_scores):
    print("\nThanks for playing!")
    print("\nThe following are your scores: ")
    print("E: " + str(user_scores[0]))
    print("A: " + str(user_scores[1]))
    print("C: " + str(user_scores[2]))
    print("N: " + str(user_scores[3]))
    print("O: " + str(user_scores[4]) + "\n")


    while(True):
        user_choice = input("Review your choices? (y/n) ")
        if(user_choice == 'y'):
            print("\n---- YOUR ANSWERS ----")
            for num, question in enumerate(QUESTIONS, start=1):
                print(f"\nQuestion {num}:")
                print(f"{question}?")
                print(user_choices[num-1])
            
            exit(0)
        elif(user_choice == 'n'):
            exit(0)
        else:
            print("Invalid input. Please try again.")

start_screen()

    
