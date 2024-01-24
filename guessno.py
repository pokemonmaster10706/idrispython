import customtkinter as ctk
from tkinter.ttk import Progressbar

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

def get_ans(event):
    global num
    num = entry.get()
    loading_win()

def ans():
    global num
    num = entry.get()
    loading_win()

def loading_win():
    loading_window = ctk.CTkToplevel(root)
    loading_window.title("Reading your Mind")
    loading_window.attributes("-topmost", True)

    loading_label = ctk.CTkLabel(loading_window, text="Analyzing Brainwaves...")
    loading_label.pack(padx=10, pady=10)

    progress = ctk.CTkProgressBar(loading_window, mode='indeterminate')
    progress.pack(padx = 20, pady=20)

    # Simulate loading process (you can replace this with your actual logic)
    # Here, we're using the `after` method to schedule a callback after a delay
    progress.start()  # Start the progress bar

    # Update the loading text periodically
    def update_loading_text():
        l = ["Analyzing Brainwaves...","Scanning Memories...","Calculating Probabilities...","Decoding Thoughts..."]

        loading_label.configure(text=l[count],font=('Dubai',15))
        loading_window.after(500, update_loading_text)

    # Simulate loading process (you can replace this with your actual logic)
    count = -1
    def simulate_loading():
        nonlocal count
        count += 1
        if count < 3:
            loading_window.after(2000, simulate_loading)
        else:
            progress.stop()  # Stop the progress bar
            loading_window.after(10, lambda: show_message(loading_window,progress))

    update_loading_text()
    loading_window.after(1000, simulate_loading)

def show_message(loading_window, progress):
    progress.stop()  # Stop the progress bar
    loading_window.destroy()  # Close the loading window

    # Display a message box with a message
    ans_window = ctk.CTkToplevel()
    ans_window.title("Guess")
    ans_window.geometry("200x100")
    ans_window.attributes("-topmost", True)

    label = ctk.CTkLabel(ans_window, text="The Number is:", font=('Dubai',15))
    label.pack(padx=20,pady=5)

    answ = ctk.CTkLabel(ans_window,height=100,width=100, text=str(num), font=('Dubai',18))
    answ.pack(padx=20)

    ans_window.mainloop()

root = ctk.CTk()
root.geometry("300x260")
root.title("Mind Reader")

# Create a button that triggers the loading screen
main = ctk.CTkFrame(root, width=300, height=200, corner_radius=10)
main.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)
title = ctk.CTkLabel(root, corner_radius=10, text='Mind Reader' , font=('Dubai',25))
title.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

qn = ctk.CTkLabel(main, text="Think of a Number:", font=('Dubai',18))
qn.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

entry = ctk.CTkEntry(main, placeholder_text="Enter Number:", width=200, border_width=2, corner_radius=10)
entry.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

button_guess = ctk.CTkButton(main, text="Guess", width=15, border_width=0, corner_radius=8, command=ans)
button_guess.place(relx=0.5, rely=0.7, anchor=ctk.CENTER)

root.bind('<Return>', get_ans)

root.mainloop()
