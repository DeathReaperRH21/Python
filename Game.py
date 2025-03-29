import tkinter as tk
from tkinter import messagebox
import random  # Import random to select random math questions
import os


# Create the main window
window = tk.Tk()
window.title("Clicker Game")
window.configure(bg="firebrick4")




print("Clicker Game")
script_dir = os.path.dirname(__file__)
image_path = os.path.join(script_dir, 'Picture', 'Reveille.png')




original_image = tk.PhotoImage(file=image_path)


clicks = 0
click_multiplier = 1  # Multiplier starts at 1
upgrade_cost = 20  # Minimum upgrade cost starts at 20
# Load the image and start with a smaller size
original_image = tk.PhotoImage(file=image_path)
button_image = original_image.subsample(2, 2)  # Start small




# List of math questions and their answers
math_questions = [
   {"question": " If you have 1/2 of a pizza and eat 1/4 of the pizza, how much pizza is left?", "answer": "1/4"},
   {"question": "What is 123 + 45?", "answer": "168"},
   {"question": "If Phil has ½ of a pizza and Kiana has ⅓ of a pizza, how much pizza do they have together?", "answer": "5/6"},
   {"question": "What is 78 - 32?", "answer": "46"},
   {"question": "John has 16 pencils and he gives 5 of them to Sarah. How many does John have left?", "answer": "11"},
   {"question": "What is 15 + 30", "answer": "45"},
   {"question": "Timmy has 25 apples and gives 5 away how many apples does Timmiy have left?", "answer": "20"},
   {"question": "7 + __ = 22", "answer": "15"},
   {"question": "What is 60 + 27 - 20?", "answer": "67"},
   {"question": "Tasha has 80 markers that she will put into boxes, each box can hold 8 markers. How many boxes will she need?", "answer": "10"}
]












def click():
   global clicks, click_multiplier
   clicks += click_multiplier  # Increment clicks based on the multiplier
   click_label.config(text=f"Total Clicks: {clicks}")  # Update the display dynamically
 
   if clicks >= 12000:  # Winning condition
       win_game()




def ask_math_question():
   # Select a random math question
   question_data = random.choice(math_questions)
   question = question_data["question"]
   correct_answer = question_data["answer"]




   # Create a pop-up window for the question
   question_window = tk.Toplevel(window)
   question_window.title("Math Questions")
   question_window.configure(bg="firebrick4")
 
   # Add a label for the question
   question_label = tk.Label(question_window, text=question, font=("Helvetica", 16), bg="firebrick4", fg="white")
   question_label.pack(pady=10)




   # Correct answer logic
   def check_answer(answer):
       global clicks, click_multiplier
       if answer == correct_answer:
           tk.messagebox.showinfo("Correct!", "That's right!")
           click_multiplier *= 3  # Increment the multiplier for the upgrade
           click_label.config(text=f"Total Clicks: {clicks}")  # Update the display dynamically
           question_window.destroy()  # Close the question window after answering
       else:
           tk.messagebox.showinfo("Incorrect", f"The correct answer was {correct_answer}. The upgrade cannot proceed.")
           question_window.destroy()  # Close the question window after answering








   # Add answer entry field
   answer_entry = tk.Entry(question_window, font=("Helvetica", 14))
   answer_entry.pack(pady=5)




   # Add submit button
   submit_button = tk.Button(question_window, text="Submit", command=lambda: check_answer(answer_entry.get()), bg="white", fg="black")
   submit_button.pack(pady=5)




def purchase_upgrade():
   global clicks, upgrade_cost
   if clicks >= upgrade_cost:
       clicks -= upgrade_cost
       click_label.config(text=f"Total Clicks: {clicks}")  # Update the display dynamically after purchase
       # Increment the upgrade cost for the next purchase
       upgrade_cost *= 2  # Increase cost by 15 times each time
       # Update the upgrade button to reflect new cost
       upgrade_button.config(text=f"Purchase Upgrade ({upgrade_cost} Clicks)")
     
       # Show a math question pop-up
       ask_math_question()
   else:
       tk.messagebox.showinfo("Not Enough Clicks", f"You need at least {upgrade_cost} clicks to purchase this upgrade.")




def win_game():
   global button_image
   image_path2 = os.path.join(script_dir,'Picture', 'Reveillewin.png')
   button_image = tk.PhotoImage(file=image_path2)  # Load the winning image
   click_button.config(image=button_image)  # Change the button image to the winning image
   click_button.image = button_image  # Keep a reference to the image
   click_label.config(text="You Win!")  # Update the label to show winning message
   upgrade_button.config(state=tk.DISABLED)  # Disable the upgrade button
 




# Create the display for click count
click_label = tk.Label(window, text=f"Total Clicks: {clicks}", font=("Helvetica", 16), bg="firebrick4", fg="white")
click_label.pack(pady=10)




# Create a button with the initial small image
click_button = tk.Button(window, image=button_image, command=click)
click_button.pack(pady=100)




# Create the upgrade button
upgrade_button = tk.Button(window, text=f"Purchase Upgrade ({upgrade_cost} Clicks)", font=("TimeNewRoman", 12), bg="white", fg="black", command=purchase_upgrade)
upgrade_button.pack(pady=10)






click_labe2 = tk.Label(window, text=f"12000 Clicks to Win", font=("Helvetica", 16), bg="firebrick4", fg="white")
click_labe2.pack(pady=5)


# Start the Tkinter event loop
window.mainloop()

