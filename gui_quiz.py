import tkinter as tk
import tkinter.font as tkfont
from tkinter import ttk
from tkinter import messagebox

# Quiz questions and options with scores
quiz_data = [
    {
        "question": "I enjoy trying new and adventurous activities.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I am open to exploring unfamiliar places and cultures.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I appreciate and enjoy engaging with complex and abstract ideas.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I am often drawn to artistic and creative experiences.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I am receptive to new and innovative ways of thinking.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I like to challenge traditional beliefs and norms.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I am curious and eager to learn about various topics.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I find beauty in artistic expression, such as music, literature, or visual arts.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I am open to considering alternative viewpoints and perspectives.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I seek out opportunities to expand my knowledge and skills.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I enjoy spending time with large groups of people and being social.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I feel energized and enthusiastic after attending social events or parties.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I am comfortable taking the lead in group activities or discussions.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I often initiate conversations with strangers or acquaintances.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I prefer working in a team or group rather than working alone.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I express my emotions and thoughts openly with others.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I seek out new friendships and social connections.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I feel at ease being the center of attention in a group setting.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I enjoy participating in public speaking or performing in front of others.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I actively seek out opportunities for social interaction and stimulation.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I find it essential to be considerate and empathetic towards others.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I am generally patient and understanding with people's mistakes and shortcomings.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I am willing to help others, even if it inconveniences me.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I find it easy to forgive and forget when someone has wronged me.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I am comfortable cooperating and compromising in conflicts.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I am known for being warm and compassionate towards others.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I value maintaining harmonious relationships with others.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I often put others' needs ahead of my own.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I avoid confrontation and prefer to keep the peace.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I frequently consider other people's opinions and feelings when making decisions.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I am highly organized and disciplined in managing my daily tasks and responsibilities.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I am usually punctual and reliable in meeting deadlines.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I prefer to keep my living space clean and orderly.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I follow a set schedule or routine in my daily life.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I pay close attention to details and avoid making careless mistakes.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I set clear goals and work diligently to achieve them.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I am known for being disciplined and self-controlled.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I like to finish tasks before taking a break or relaxing.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I strive to keep my promises and commitments.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "People consider me dependable and responsible.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I often experience intense feelings of anxiety or worry.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I find it challenging to stay calm and composed in stressful situations.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I tend to get easily upset or irritated by minor inconveniences.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I have difficulty recovering from negative emotions or setbacks.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I frequently dwell on negative thoughts and past regrets.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I am prone to experiencing mood swings and emotional ups and downs.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I worry excessively about future events.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I find it challenging to control my emotional reactions to situations.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I often feel overwhelmed by life's challenges and pressures.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    },
    {
        "question": "I struggle to maintain a positive outlook and handle stress effectively.",
        "options": ["Very Inaccurate", "Somewhat Inaccurate", "Neither Agree Nor Disagree", "Somewhat Accurate", "Very Accurate"],
        "scores": [1, 2, 3, 4, 5]
    }
]

# Create the main application window
root = tk.Tk()
root.title("Personality Trait Assessment")
root.geometry("600x400")

# Title
title_font = tkfont.Font(size=16, weight="bold")
title_label = tk.Label(root, text="Big 5 Personality Quiz", font=title_font)
title_label.pack(pady=10)

# Demographics Page
def begin_quiz():
    # Get the entered demographic information
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    ethnicity = ethnicity_combobox.get()
    age = age_combobox.get()
    gender = gender_combobox.get()
    
    # You can store or process the demographic information as needed (e.g., save to variables or a database).

    demographics_frame.pack_forget()  # Hide the demographics page
    quiz_frame.pack()  # Show the quiz page
    show_question()

demographics_frame = ttk.LabelFrame(root, text="Demographics")
demographics_frame.pack(pady=10)

# Function to remove grayed-out text when the entry field is clicked
def on_entry_click(event):
    if name_entry.get() == "(Optional)":
        name_entry.delete(0, "end")
        name_entry.config(foreground="black")

def on_phone_click(event):
    if phone_entry.get() == "(Optional)":
        phone_entry.delete(0, "end")
        phone_entry.config(foreground="black")

def on_email_click(event):
    if email_entry.get() == "(Optional)":
        email_entry.delete(0, "end")
        email_entry.config(foreground="black")

# Name field
name_label = ttk.Label(demographics_frame, text="Name:")
name_label.grid(row=0, column=0, padx=5, pady=5)
name_entry = ttk.Entry(demographics_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)
name_entry.insert(0, "(Optional)")
name_entry.bind("<FocusIn>", on_entry_click)
name_entry.config(foreground="gray")

# Phone number field
phone_label = ttk.Label(demographics_frame, text="Phone Number:")
phone_label.grid(row=1, column=0, padx=5, pady=5)
phone_entry = ttk.Entry(demographics_frame)
phone_entry.grid(row=1, column=1, padx=5, pady=5)
phone_entry.insert(0, "(Optional)")
phone_entry.bind("<FocusIn>", on_phone_click)
phone_entry.config(foreground="gray")

# Email field
email_label = ttk.Label(demographics_frame, text="Email:")
email_label.grid(row=2, column=0, padx=5, pady=5)
email_entry = ttk.Entry(demographics_frame)
email_entry.grid(row=2, column=1, padx=5, pady=5)
email_entry.insert(0, "(Optional)")
email_entry.bind("<FocusIn>", on_email_click)
email_entry.config(foreground="gray")

ethnicity_label = ttk.Label(demographics_frame, text="Race/Ethnicity:")
ethnicity_label.grid(row=3, column=0, padx=5, pady=5)
ethnicity_options = ["Hispanic", "African American", "Caucasian", "Asian American / Pacific Islander", "2 or more Races", "Prefer not to say"]
ethnicity_combobox = ttk.Combobox(demographics_frame, textvariable=ethnicity_label, values=ethnicity_options, state="readonly")
ethnicity_combobox.grid(row=3, column=1, padx=5, pady=5)

age_label = ttk.Label(demographics_frame, text="Age:")
age_label.grid(row=4, column=0, padx=5, pady=5)
age_options = ["Below 18", "18-25", "26-35", "36-45", "46-55", "56-65", "66-75", "76-85", "Prefer not to say"]
age_combobox = ttk.Combobox(demographics_frame, textvariable=age_label, values=age_options, state="readonly")
age_combobox.grid(row=4, column=1, padx=5, pady=5)

gender_label = ttk.Label(demographics_frame, text="Gender:")
gender_label.grid(row=5, column=0, padx=5, pady=5)
gender_options = ["Male", "Female", "Non-Binary", "Prefer not to say"]
gender_combobox = ttk.Combobox(demographics_frame, textvariable=gender_label, values=gender_options, state="readonly")
gender_combobox.grid(row=5, column=1, padx=5, pady=5)

begin_quiz_button = ttk.Button(demographics_frame, text="Begin Quiz", command=begin_quiz)
begin_quiz_button.grid(row=6, columnspan=2, padx=5, pady=10)


# Quiz Page
quiz_frame = ttk.Frame(root)

# Variables to store user's answers
user_answers = []

# Index to keep track of the current question
current_question_index = 0

def show_next_question():
    global current_question_index

    # Save the answer for the current question
    selected_option = answer_var.get()
    if selected_option:
        # Appends integer (1,2,3,4,5) corresponding to selected option
        user_answers.append(int(selected_option))
    else:
        user_answers.append(0)  # If no option is selected, score as 0

    # Move to the next question
    current_question_index += 1

    # Update progress bar
    progress_var.set((current_question_index / len(quiz_data)) * 100)

    # Check if all questions are answered
    if current_question_index == len(quiz_data):
        show_result()
    else:
        show_question()

def show_question():
    question_label.config(text=quiz_data[current_question_index]["question"])
    answer_var.set("")  # Clear the selected answer for the new question
    for i in range(5):
        option_buttons[i].config(text=quiz_data[current_question_index]["options"][i])

# Create the question label
question_label = ttk.Label(quiz_frame, text="", wraplength=300)
question_label.pack(pady=10)

# Option selection variable
answer_var = tk.StringVar()

# Create option buttons
option_buttons = []
for i in range(5):
    frame = ttk.Frame(quiz_frame)  # Create a separate frame for each button
    frame.pack(side=tk.TOP, padx=10, pady=5, anchor=tk.W)  # Stack the frames vertically and anchor them to the west (left-aligned)
    button = ttk.Radiobutton(frame, text="", variable=answer_var, value=i + 1)
    option_buttons.append(button)
    button.pack(side=tk.LEFT)  # Align the buttons colinearly inside their respective frames

# Next button
next_button = ttk.Button(quiz_frame, text="Next", command=show_next_question)
next_button.pack(pady=10)

# Progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(quiz_frame, variable=progress_var, maximum=100)
progress_bar.pack(side=tk.BOTTOM, fill=tk.X)  # Set fill=tk.X for the progress_bar

# Function to display the final score
def show_result():
    quiz_frame.pack_forget()
    result_frame = ttk.Frame(root)
    result_frame.pack(pady=20)

    user_scores = [20, 14, 14, 38, 8]

    for num in range(0, len(user_answers), 5):
        user_scores[0] += user_answers[num] * (-1) ** num
        user_scores[1] -= user_answers[num+1] * (-1) ** num
        user_scores[2] += user_answers[num+2] * (-1) ** num
        user_scores[3] -= user_answers[num+3] * (-1) ** num
        user_scores[4] += user_answers[num+4] * (-1) ** num
        
    result_E = ttk.Label(result_frame, text=f"Extroversion (E): {user_scores[0]}")
    result_E.pack(pady=10)
    result_A = ttk.Label(result_frame, text=f"Agreeableness (A): {user_scores[1]}")
    result_A.pack(pady=10)
    result_C = ttk.Label(result_frame, text=f"Conscientiousness (C): {user_scores[2]}")
    result_C.pack(pady=10)
    result_N = ttk.Label(result_frame, text=f"Neuroticism (N): {user_scores[3]}")
    result_N.pack(pady=10)
    result_O = ttk.Label(result_frame, text=f"Openness to Experience (O): {user_scores[4]}")
    result_O.pack(pady=10)

# Start the application with the demographics page
demographics_frame.pack()

# Run the application
root.mainloop()
