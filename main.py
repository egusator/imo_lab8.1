import tkinter as tk


window = tk.Tk()
window.title("8.1")
window.geometry('520x300')  # Set initial size
window.maxsize(520, 300)  # Prevent resizing beyond 520x300
window.resizable(0, 1)  # Disable horizontal resizing

question_label = tk.Label(window, text="Пойти сегодня в университет?", font=("Arial", 20))
question_label.pack()

answer_label = tk.Label(window, text="Ответ:", font = ("Arial", 16))
answer_label.pack()
answer_label.place(x=180, y=50)

answer_val_label = tk.Label(window, text="...", font = ("Arial", 16))
answer_val_label.pack()
answer_val_label.place(x=250, y=50)

import random

def button_clicked():
    random_value = random.random()
    if (random_value < 0.5):
        answer_val_label.configure(text="Да!")
    else:
        answer_val_label.configure(text="Нет!")

# Creating a button with specified options
button = tk.Button(window,
                   text="Получить ответ",
                   command=button_clicked,
                   activebackground="blue",
                   activeforeground="white",
                   font=("Arial", 18))

button.place(x = 140, y = 100)

window.mainloop()