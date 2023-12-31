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

# Function to display option to start or end the quiz
def start_screen():
    print("To start the OCEAN quiz, enter 's'")
    print("To exit this app, enter 'q'")
    
    # Loop to ensure user input is valid (s or q)
    while(True):
        user_choice = input("Enter 's' to start or 'q' to quit quiz: ")

        if(user_choice == 's'):
            run_quiz()
        elif(user_choice == 'q'):
            exit(0)
        else:
            print("Invalid input. Please try again.")

# Function to show questions and choices corresponding to question
def run_quiz():
    user_choices = []

    for num, question in enumerate(QUESTIONS, start=1):
        print(f"\nQuestion {num}:")
        print(f"{question}?")
        print(ALL_CHOICES)
        # Loop to guarrantee user cannot move to next question until a
        # valid choice is entered.
        while (True):
            choice = input("Choice? ")
            if choice.isdigit()  and int(choice) > 0 and int(choice) < 6:
                user_choices.append(int(choice))
                break
            else:
                print("Invalid number. Please try again.")
    
    # For debugging purposes, ALL_USER_CHOICES can be set to a random
    # list of 50 choices, ranging from 1 to 5, with line below
    # user_choices = [random.randint(1, 5) for x in range(0, 50)]

    user_scores = calc_score(user_choices)
    end_screen(user_choices, user_scores)

# Function to calculate the user score for each of the five
# personality categories
def calc_score(ul):
    # List to store user OCEAN scores. 
    # score E : scores[0]
    # score A : scores[1]
    # score C : scores[2]
    # score N : scores[3]
    # score O : scores[4]
    user_scores = [0, 0, 0, 0, 0]

    user_scores[0] = 20 + ul[0] - ul[5] + ul[10] - ul[15] + ul[20] - ul[25] + ul[30] - ul[35] + ul[40] - ul[45]
    user_scores[1] = 14 - ul[1] + ul[6] - ul[11] + ul[16] - ul[21] + ul[26] - ul[31]  + ul[36] + ul[41] + ul[46]
    user_scores[2] = 14 + ul[2] - ul[7] + ul[12] - ul[17] + ul[22]  - ul[27] + ul[32] - ul[37] + ul[42] + ul[47] 
    user_scores[3] = 38 - ul[3] + ul[8] - ul[13] + ul[18] - ul[23] - ul[28] - ul[33] - ul[38] - ul[43] - ul[48]
    user_scores[4] = 8 + ul[4] - ul[9] + ul[14] - ul[19] + ul[24] - ul[29] + ul[34] + ul[39] + ul[44] + ul[49] 

    return user_scores

# Function to display all five user scores, the maximum score,
# and optionally review all answered to questions.
def end_screen(user_choices, user_scores):
    print("\nThanks for playing!")
    print("\nThe following are your scores: ")
    
    print("     Extroversion (E): " + str(user_scores[0]))
    print("     Agreeableness (A): " + str(user_scores[1]))
    print("     Conscientiousness (C): " + str(user_scores[2]))
    print("     Neuroticism (N): " + str(user_scores[3]))
    print("     Openness to Experience (O): " + str(user_scores[4]) + "\n")
    
    max_score = max(user_scores)

    if max_score == user_scores[0]:
        print("Your max score is Extroversion (E)\n")
    elif max_score == user_scores[1]:
        print("Your max score is Agreeableness (A)\n")
    elif max_score == user_scores[2]:
        print("Your max score is Conscientiousness (C)\n")
    elif max_score == user_scores[3]:
        print("Your max score is Neuroticism (N)\n")
    elif max_score == user_scores[4]:
        print("Your max score is Openness to Experience (O)\n")

    # Loop to ensure user chooses y or n
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