from random import choice
import tkinter as tk

def click_button(user_choice):
    global user_point, comp_point
    komp = choice(computer_choice)

    if user_choice == 'paper' and komp == 'stone' or user_choice == 'stone' and komp == 'scissors' or user_choice == 'scissors' and komp == 'paper':
        win = '       Gracz wygrał\n'
        user_point += 1
    elif user_choice == komp:
        win = '       Remis\n'
    else:
        win = '       Komputer wygrał\n'
        comp_point += 1


    if user_point == 3:
        label.config(text = f'GRACZ WYGRAŁ GRĘ!!\n    Gracz {user_point} : {comp_point} Komputer')
        user_point = 0
        comp_point = 0
    elif comp_point == 3:
        label.config(text = f'KOMPUTER WYGRAŁ GRĘ!!\n    Gracz {user_point} : {comp_point} Komputer')
        user_point = 0
        comp_point = 0
    else:
        label.config(text = f'{win}\nKomputer wybrał: {komp}\n    Gracz {user_point} : {comp_point} Komputer')
    

user_point = 0
comp_point = 0
computer_choice = ['stone', 'paper', 'scissors']


window = tk.Tk()
window.title('Game stone, paper, scissors')
window.geometry('410x200')


label = tk.Label(window, text = 'Wybierz: Kamień, Papier lub Nożyce', width = 30)
label.grid(column = 2, row = 0)

field = tk.Label(window, text = 'Aby rozpocząć\n musisz wybrać: \nKamień, Papier lub Nożyce', width = 30)
field.grid(row = 2, column = 2, ipadx = 4, ipady = 5)


button_stone = tk.Button(text= 'Kaimeń', command = lambda: click_button('stone'))
button_stone.grid(row = 7, column = 1, ipady = 5, ipadx = 20)

button_stone = tk.Button(text= 'Papier', command = lambda: click_button('paper'))
button_stone.grid(row = 7, column = 2, ipady = 5, ipadx = 20)

button_stone = tk.Button(text= 'Nożyce', command = lambda: click_button('scissor'))
button_stone.grid(row = 7, column = 3, ipady = 5, ipadx = 20)


window.mainloop()
