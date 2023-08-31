import tkinter as tk
import random
import string
def center_window(root, width, height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")
def generate_password():
    password_length = int(length_entry.get())
    if password_length < 6:
        result_label.config(text="Password length should be at least 6")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    password_label.config(text="Generated Password:")
    result_label.config(text=generated_password)


root = tk.Tk()
root.title("Random Password Generator")
root.geometry("500x500")
root.configure(bg="white")
center_window(root, 500, 500)

frame = tk.Frame(root, bg="#F8B195")  


length_label = tk.Label(frame, text="Password Length:", bg="#F67280")
length_entry = tk.Entry(frame)
generate_button = tk.Button(frame, text="Generate Password", command=generate_password, bg="#C06C84", fg="black")
password_label = tk.Label(frame, text="", bg="#F8B195")
result_label = tk.Label(frame, text="", bg="#F8B195")


length_label.pack(pady=10)
length_entry.pack()
generate_button.pack(pady=10)
password_label.pack()
result_label.pack()


frame.pack(fill=tk.BOTH, expand=True)


root.mainloop()
