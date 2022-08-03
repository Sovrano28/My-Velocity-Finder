# This simple GUI solves the derivative of an equation of motion
from tkinter import *

frame = Tk()

frame.title("Velocity finder")
frame.config(bg="#FF97BE")


def get_velocity():
    try:
        value_u = int(entry_u.get())
        value_t = int(entry_t.get())
        velocity = round(value_u + 9.81 * value_t, 2)
        if velocity != 0:
            ans_label.config(text=f"{velocity} m/s")
        else:
            ans_label.config(text=f"0")

    finally:
        pass


Label(frame, text="Calculating v using v = u + at", bg="#7F4B5F", fg="white").grid(row=0, columnspan="2")
Label(frame, text="Initial velocity").grid(row=1, sticky=W)
Label(frame, text="time").grid(row=2, sticky=W + E)
Label(frame, text="by Sovrano", fg="black").grid(row=4, column="2", sticky=W + E + N + S, padx=5, pady=5)

entry_u = Entry(frame)
entry_u.grid(row=1, column=1)
entry_t = Entry(frame)
entry_t.grid(row=2, column=1)

get_velocity = Button(frame, text="Solve", fg="white", bg="green", command=get_velocity, font=("Times New Roman", 16))
get_velocity.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W + E + N + S, padx=5, pady=5)

ans_label = Label(frame, text="final velocity")
ans_label.grid(row=3, column=0, sticky=W + E)
# I have noticed that not separating the .grid part could result in some error

mainloop()
