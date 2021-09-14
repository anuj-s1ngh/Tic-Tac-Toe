import tkinter as tk


gameplay_order = ["O", "X", "O", "X", "O", "X", "O", "X", "O"]


def clear_all_wids(root):
    for wid in root.winfo_children():
        if (wid.winfo_class() != "Canvas") and (wid.winfo_class() != "Label"):
            wid.destroy()


def show_exit_btn(root):
    exit_btn = tk.Button(
        root,
        text="Exit Game",
        width=15,
        height=3,
        command=root.destroy,
        bg="red",
        fg="white",
        font=("Roboto", 12)
    )
    exit_btn.grid(
        row=2,
        column=1,
    )

