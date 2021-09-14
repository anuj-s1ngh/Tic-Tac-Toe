import tkinter as tk
from utils import gameplay_order, clear_all_wids, show_exit_btn


# Root Window
root=tk.Tk()
root.title("Tic Tac Toe")
# root.geometry("500x500")

# Canvas on top of Root Window
canvas = tk.Canvas(root)
canvas.grid(
    row=0,
    column=0,
    columnspan=3,
    rowspan=4
)


# Gameplay
player_gameplay = []

# Buttons
btn_list = [
    [],
    [],
    []
]
btn_text_list = [
    [],
    [],
    []
]


def show_restart_btn():
    restart_btn = tk.Button(
        root,
        text="Restart Game",
        width=15,
        height=3,
        command=show_btns,
        bg="#4287f5",
        fg="white",
        font=("Roboto", 12)
    )
    restart_btn.grid(
        row=1,
        column=1,
    )


def reset_game(winner):
    global help_text, btn_list, btn_text_list, player_gameplay

    player_gameplay = []

    btn_list = [
        [],
        [],
        []
    ]
    btn_text_list = [
        [],
        [],
        []
    ]

    clear_all_wids(root)

    help_text.set(f"Player '{winner}' Wins.")

    show_restart_btn()
    show_exit_btn(root)



def who_wins():
    global player_gameplay, btn_text_list
    check_list = [[] for _ in range(0,8)]

    for i in range(0, 3):
        for j in range(0, 3):
            check_list[i].append(btn_text_list[i][j].get())
            check_list[i+3].append(btn_text_list[j][i].get())
            if i == j:
                check_list[6].append(btn_text_list[i][j].get())
                check_list[7].append(btn_text_list[i][2-i].get())
    
    for check_item in check_list:
        if (len(set(check_item)) == 1) and (check_item[0] != ""):
            winner = check_item[0]
            break
        else:
            winner = None
    
    if ((winner is not None) or (len(player_gameplay) >= 9)):
        reset_game(winner)
    else:
        help_text.set(f"Player '{gameplay_order[len(player_gameplay)]}' 's turn.")  # value of gameplay_text is outdated.



def freeze_btns():
    global btn_text_list, btn_list
    for i in range(0, 3):
        for j in range(0, 3):
            btn_text = btn_text_list[i][j].get()
            if btn_text != "":
                btn = tk.Button(
                    root,
                    textvariable=btn_text_list[i][j],
                    width=10,
                    height=5,
                    state=tk.DISABLED,
                    font=("Roboto", 15)
                )
                btn.grid(
                    row=i+1,
                    column=j,
                    sticky="nsew"
                )
                btn_list[i][j] = btn


def show_char(row, col):
    global btn_text_list, btn_list, player_gameplay, gameplay_order, help_text

    btn_text = btn_text_list[row][col]

    if btn_text.get() == "":
            gameplay_text = gameplay_order[len(player_gameplay)]
            btn_text.set(gameplay_text)
            player_gameplay.append(gameplay_text)

            freeze_btns()

            who_wins()

    elif btn_text.get() != "":
        btn_text.set("")
        player_gameplay.pop()


def show_btns():
    global btn_text_list, btn_list, help_text

    help_text = tk.StringVar()
    help_text.set("Player 'O' will go first.")
    help_text_lbl = tk.Label(
        root,
        textvariable=help_text,
        height=3,
        font=("Roboto", 15)
    )
    help_text_lbl.grid(
        row=0,
        column=0,
        columnspan=3
    )

    for i in range(0, 3):
        for j in range(0, 3):
            btn_text = tk.StringVar()
            btn_text.set("")
            btn = tk.Button(
                root,
                textvariable=btn_text,
                width=10,
                height=5,
                command=lambda row=i, col=j: show_char(row, col),
                font=("Roboto", 15)
            )
            btn.grid(
                row=i+1,
                column=j,
                sticky="nsew"
            )
            btn_text_list[i].append(btn_text)
            btn_list[i].append(btn)


def show_start_btn():
    start_btn = tk.Button(
        root,
        text="Start Game",
        width=15,
        height=3,
        command=show_btns,
        bg="#4287f5",
        fg="white",
        font=("Roboto", 12)
    )
    start_btn.grid(
        row=1,
        column=1,
    )


show_start_btn()
show_exit_btn(root)




root.mainloop()
