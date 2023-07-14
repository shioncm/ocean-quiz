from string import ascii_lowercase

QUESTIONS = [
    "When was the first known use of the word 'quiz'",
    "Which built-in function can get information from the user",
]

CHOICES = "INACCURATE\t1\t2\t3\t4\t5\tACCURATE"

ALL_USER_CHOICES = []

for num, question in enumerate(QUESTIONS, start=1):
    print(f"\nQuestion {num}:")
    print(f"{question}?")
    print(CHOICES)
    user_choice = int(input("Choice? "))
    ALL_USER_CHOICES.add(user_choice)

    