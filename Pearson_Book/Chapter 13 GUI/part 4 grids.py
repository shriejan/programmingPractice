import tkinter as tk 
root = tk.Tk()
root.title('Basic Grids')

screen = tk.Frame()
screen.pack(side='top')

skrn = tk.Entry(screen)
skrn.pack()

keypad = tk.Frame()
keypad.pack(side='bottom')

buttons = [
    ['1','2','3','+'],
    ['4','5','6','-'],
    ['7','8','9','*'],
    ['0','=','C','/']
]

for row in range(4):
    for column in range(4):
        button = tk.Button(keypad, text=buttons[row][column], width=5, height=2)
        button.grid(row=row, column=column, padx=5, pady=5)
    
        
        


tk.mainloop()
