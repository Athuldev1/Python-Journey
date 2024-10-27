from tkinter import *
from tkinter import messagebox
import string
from random import randint, choice, shuffle


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Input fields cannot be empty!")
    elif "@" not in email:
        messagebox.showinfo(
            title="Error", message="Please enter a valid email address."
        )
    else:
        is_ok = messagebox.askokcancel(
            title=website,
            message=f"Save the following information?\nEmail: {email}\nPassword: {password}",
        )
        if is_ok:
            try:
                with open("data.txt", "a") as data_file:
                    data_file.write(
                        f"Website: {website} | Username/Email: {email} | Password: {password}\n"
                    )
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)
            except Exception as e:
                messagebox.showerror(
                    title="File Error", message=f"Could not save data: {e}"
                )


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="Day-57_Password_Generator\logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# Labels and Entries
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_label = Label(text="Email:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "athulkp@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3, columnspan=2, sticky="EW")

# Buttons
password_button = Button(text="Generate Password", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW", padx=5, pady=5)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW", padx=5, pady=5)

window.mainloop()
