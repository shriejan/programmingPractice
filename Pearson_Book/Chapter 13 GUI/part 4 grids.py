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

def append(value):
    data = skrn.get()
    skrn.delete(0, tk.END)
    skrn.insert(0, data + value)
    
for row in range(4):
    for column in range(4):
        value = buttons[row][column]  # Capture the current button value
        a = tk.Button(keypad, text=value, width=5, height=2, command=lambda v=value: append(v))
        a.grid(row=row, column=column, padx=5, pady=5)
        

    


        


tk.mainloop()
