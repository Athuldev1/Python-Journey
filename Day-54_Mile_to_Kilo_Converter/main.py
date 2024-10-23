from tkinter import *


# Conversion
def mile_to_km():
    try:
        miles = float(miles_input.get())
        km = miles * 1.609
        km_result.config(text=f"{km:.2f}") 
    except ValueError:
        km_result.config(text="Invalid Input")


# Creating a new window and configurations
window = Tk()
window.title("Mile to Kilometer Converter")
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

km_result = Label(text="0")
km_result.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2, pady=10)

window.mainloop()
