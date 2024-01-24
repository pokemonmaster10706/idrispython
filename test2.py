from customtkinter import *
import os
from PIL import Image

def checkbox_frame_event():
    print(f"checkbox frame modified: {scrollable_checkbox_frame.get_checked_items()}")


def radiobutton_frame_event():
    print(f"radiobutton frame modified: {scrollable_radiobutton_frame.get_checked_item()}")


def label_button_frame_event(item):
    print(f"label button frame clicked: {item}")


if __name__ == "__main__":
    set_appearance_mode("dark")

    app = CTk()
    app.title("CTkScrollableFrame example")
    app.grid_rowconfigure(0, weight=1)
    app.columnconfigure(2, weight=1)

    # create scrollable checkbox frame
    scrollable_checkbox_frame = CTkScrollableFrame(app, width=200)
    scrollable_checkbox_frame.grid(row=0, column=0, padx=15, pady=15, sticky="ns")

    scrollable_checkbox_frame.command = checkbox_frame_event
    scrollable_checkbox_frame.checkbox_list = []

    for i in range(50):
        item = f"item {i}"
        checkbox = CTkCheckBox(scrollable_checkbox_frame, text=item)
        checkbox.configure(command=scrollable_checkbox_frame.command)
        checkbox.grid(row=len(scrollable_checkbox_frame.checkbox_list), column=0, pady=(0, 10))
        scrollable_checkbox_frame.checkbox_list.append(checkbox)

    # create scrollable radiobutton frame
    scrollable_radiobutton_frame = CTkScrollableFrame(app, width=500)
    scrollable_radiobutton_frame.grid(row=0, column=1, padx=15, pady=15, sticky="ns")

    scrollable_radiobutton_frame.command = radiobutton_frame_event
    scrollable_radiobutton_frame.radiobutton_variable = StringVar()
    scrollable_radiobutton_frame.radiobutton_list = []

    for i in range(100):
        item = f"item {i}"
        radiobutton = CTkRadioButton(scrollable_radiobutton_frame, text=item, value=item, variable=scrollable_radiobutton_frame.radiobutton_variable)
        radiobutton.configure(command=scrollable_radiobutton_frame.command)
        radiobutton.grid(row=len(scrollable_radiobutton_frame.radiobutton_list), column=0, pady=(0, 10))
        scrollable_radiobutton_frame.radiobutton_list.append(radiobutton)

    # create scrollable label and button frame
    current_dir = os.path.dirname(os.path.abspath(__file__))
    scrollable_label_button_frame = CTkScrollableFrame(app, width=300)
    scrollable_label_button_frame.grid(row=0, column=2, padx=0, pady=0, sticky="nsew")

    scrollable_label_button_frame.command = label_button_frame_event
    scrollable_label_button_frame.radiobutton_variable = StringVar()
    scrollable_label_button_frame.label_list = []
    scrollable_label_button_frame.button_list = []

    for i in range(20):
        item = f"image and item {i}"
        image = CTkImage(Image.open(os.path.join(current_dir, "test_images", "chat_light.png")))
        label = CTkLabel(scrollable_label_button_frame, text=item, image=image, compound="left", padx=5, anchor="w")
        button = CTkButton(scrollable_label_button_frame, text="Command", width=100, height=24)
        button.configure(command=lambda item=item: scrollable_label_button_frame.command(item))
        label.grid(row=len(scrollable_label_button_frame.label_list), column=0, pady=(0, 10), sticky="w")
        button.grid(row=len(scrollable_label_button_frame.button_list), column=1, pady=(0, 10), padx=5)
        scrollable_label_button_frame.label_list.append(label)
        scrollable_label_button_frame.button_list.append(button)

    app.mainloop()
