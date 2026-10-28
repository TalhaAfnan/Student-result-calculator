import tkinter as tk
import matplotlib.pyplot as plt
import sqlite3

conn = sqlite3.connect(r"C:\Users\LENOVO\AppData\Local\Programs\Python\Python314\Students.db")

print("Database connected successfully")
window = tk.Tk()
window.title("Student Result Calculator")
window.geometry("600x800")
window.configure(bg="#F0F4F8")
window.resizable(False, False)

heading = tk.Label(
    window,
    text="STUDENT RESULT CALCULATOR",
    font=("Arial", 20, "bold"),
    bg="#F0F4F8",
    fg="#163A5F"
)
heading.pack(pady=25)
name_label = tk.Label(
    window,
    text="Enter Student Name:",
    font=("Arial", 11, "bold"),
    bg="#F0F4F8",
    fg="#163A5F"
)
name_label.pack()
name_result_label = tk.Label(window, text="")
name_result_label.pack()
result_label = tk.Label(window, text="")
result_label.pack()
result_frame = tk.Frame(
    window,
    bg="white",
    bd=2,
    relief="groove",
    padx=15,
    pady=10
)
result_frame.pack(pady=15)

result_label = tk.Label(
    result_frame,
    text="Your result will be appear here",
    font=("Arial", 12, "bold"),
    bg="white",
    fg="#163A5F",
    justify="left"
)
result_label.pack()

name_entry = tk.Entry(
    window,
    font=("Arial", 12),
    width=30,
    bd=2,
    relief="groove"
)
name_entry.pack()

name_entry.bind("<Return>", lambda event: father_name_entry.focus_set())

father_name_label = tk.Label(
    window,
    text="Father's Name:",
    bg="#F0F4F8"
)
father_name_label.pack()

father_name_entry = tk.Entry(window, width=30)
father_name_entry.pack()
father_name_entry.bind("<Return>", lambda event: mother_name_entry.focus_set())

mother_name_label = tk.Label(
    window,
    text="Mother's Name:",
    bg="#F0F4F8"
)
mother_name_label.pack()

mother_name_entry = tk.Entry(window, width=30)
mother_name_entry.pack()
mother_name_entry.bind("<Return>", lambda event: student_id_entry.focus_set())

student_id_label = tk.Label(
    window,
    text="Student ID:",
    bg="#F0F4F8"
)
student_id_label.pack()

student_id_entry = tk.Entry(window, width=30)
student_id_entry.pack()
student_id_entry.bind("<Return>", lambda event: bangla_entry.focus_set())

def show_name():
    name = name_entry.get()
    name_result_label.config(text="Student Name: " + name)


name_button = tk.Button(window, text="Show Name", command=show_name)
name_button.pack(pady=10)

bangla_label = tk.Label(window, text="Bangla Marks:")
bangla_label.pack()

bangla_entry = tk.Entry(window)
bangla_entry.pack()

bangla_entry.bind("<Return>", lambda event: english_entry.focus_set())

english_label = tk.Label(window, text="English Marks:")
english_label.pack()

english_entry = tk.Entry(window)
english_entry.pack()

english_entry.bind("<Return>", lambda event: math_entry.focus_set())

math_label = tk.Label(window, text="Math Marks:")
math_label.pack()

math_entry = tk.Entry(window)
math_entry.pack()

math_entry.bind("<Return>", lambda event: science_entry.focus_set())

science_label = tk.Label(window, text="Science Marks:")
science_label.pack()

science_entry = tk.Entry(window)
science_entry.pack()

science_entry.bind("<Return>", lambda event: ict_entry.focus_set())

ict_label = tk.Label(window, text="ICT Marks:")
ict_label.pack()

ict_entry = tk.Entry(window)
ict_entry.pack()

ict_entry.bind("<Return>", lambda event: calculate_result())

def clear_fields():
    name_entry.delete(0, tk.END)
    bangla_entry.delete(0, tk.END)
    english_entry.delete(0, tk.END)
    math_entry.delete(0, tk.END)
    science_entry.delete(0, tk.END)
    ict_entry.delete(0, tk.END)
    result_label.config(text="")
    name_entry.focus_set()

def calculate_result():
    try:
         bangla = float(bangla_entry.get())
         english = float(english_entry.get())
         math = float(math_entry.get())
         science = float(science_entry.get())
         ict = float(ict_entry.get())
    except ValueError:
        result_label.config(text="Please enter valid marks.")
        return
    if not all(0 <= mark <= 100 for mark in [bangla, english, math, science,ict]):
        result_label.config(text="Marks must be between 0 and 100.")
        return

    total = bangla + english + math + science + ict
    average = total / 5
    marks = [bangla, english, math, science, ict]

    subjects = ["Bangla", "English", "Math", "Science", "ICT"]

    plt.figure(figsize=(7,4))
    plt.bar(subjects, marks)
    plt.title("Student Marks")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.ylim(0, 100)
    plt.show()
    
    if average >= 80:
        grade = "A+"
    elif average >= 70:
        grade = "A"
    elif average >= 60:
        grade = "A-"
    elif average >= 50:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "F"

    if bangla >= 33 and english >= 33 and math >= 33 and science >= 33 and ict >= 33:
        status = "Pass"
    else:
        status = "Fail"

    result_label.config(
        text=(
            f"Student: {name_entry.get()}\n"
            f"Father's Name: {father_name_entry.get()}\n"
            f"Mother's Name: {mother_name_entry.get()}\n"
            f"Student ID: {student_id_entry.get()}\n"
            f"Total Marks: {total}\n"
            f"Average: {average:.2f}\n"
            f"Grade: {grade}\n"
            f"Result: {status}"
    )
)
calculate_button = tk.Button(
    window,
    text="Calculate Result",
    command=calculate_result,
    font=("Arial", 11, "bold"),
    bg="#163A5F",
    fg="white",
    padx=15,
    pady=7,
    cursor="hand2"
)
calculate_button.pack(pady=10)
clear_button = tk.Button(
    window,
    text="Clear",
    command=clear_fields,
    font=("Arial", 11, "bold"),
    bg="#D9534F",
    fg="white",
    padx=15,
    pady=7,
    cursor="hand2"
)
clear_button.pack(pady=5)
window.mainloop()
