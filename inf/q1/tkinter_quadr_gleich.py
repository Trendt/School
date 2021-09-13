from math import sqrt
from sys import exit
from tkinter import *
from tkinter import ttk

a,b,c = (1,1,1)

def quadratic_equation(a:float, b:float, c:float) -> list:
    d = b**2 - 4*a*c

    if a == 0:
        if b != 0 :
            return [linear_equation(b, c)]
        elif c != 0:
            return ["n.l."]
        else:
            return ["infinte solutions"]
    else:
        if d > 0:
            return [(-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)]
        elif d == 0:
            return [-b/(2*a)]
        else:
            return ["n.l."]

def linear_equation(m:float, n:float) -> float:
    return -n/m


class GUI(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        
        self.parent.geometry("400x300")
        self.parent.title("Quadratische Gleichungen")
        
        self.label = Label(self, text="f(x) = ax² + bx + c").pack()
        
        
if __name__ == "__main__":
    root = Tk()
    gui = GUI(root).pack(side = "top", fill = "both", expand=True)
    root.mainloop()
# root.title("Quadratische Gleichungen")
# root.geometry("400x200")

# frame = ttk.Frame(root, borderwidth = 10, relief="ridge", padding="20")
# frame.grid()

# function_var = StringVar()
# function_label = ttk.Label( frame, textvariable=function_var)

# label_a = ttk.Label( frame, text = "a: ")
# label_b = ttk.Label( frame, text = "b: ")
# label_c = ttk.Label( frame, text = "c: ")
# input_a = ttk.Entry( frame)
# input_b = ttk.Entry( frame)
# input_c = ttk.Entry( frame)


# function_var.set("f(x) = ax² + bx + c")
# function_label.grid(row=1)

# label_a.grid(row = 2, column = 1, sticky="W")
# label_b.grid(row = 3, column = 1, sticky="W")
# label_c.grid(row = 4, column = 1, sticky="W")
# input_a.grid(row = 2, column = 3, sticky="W")
# input_b.grid(row = 3, column = 3, sticky="W") 
# input_c.grid(row = 4, column = 3, sticky="W")