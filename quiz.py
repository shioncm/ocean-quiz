from string import ascii_lowercase

QUESTIONS = [
    "I am the life of the party",
    "I feel little concern for others",
    "I am always prepared",
    "I get stressed out easily",
    "I have a rich vocabulary",
    "I don't talk a lot",
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
    "I m quick to understand things",
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

def calc_score(ALL_USER_CHOICES):
    score_E = 20
    score_A = 14
    score_C = 14
    score_N = 38
    score_O = 8

    score_E_l = []
    score_A_l = []
    score_C_l = []
    score_N_l = []
    score_O_l = []

    for i in range(0, len(ALL_USER_CHOICES)):
        question_num = i + 1

        if question_num == (1 OR 6 OR 11 OR 16 OR 21 OR 31 OR 36 OR 41 OR 46):
            score_E_l.append(question_num) # find better solution

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

    
