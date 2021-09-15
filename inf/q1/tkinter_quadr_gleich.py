from math import sqrt
from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

def quadratic_equation(a:float, b:float, c:float) -> list:
    d = b**2 - 4*a*c

    if a == 0:
        if b != 0 :
            return [linear_equation(b, c), None]
        elif c != 0:
            return ["n.l."]*2
        else:
            return ["infinte solutions"]*2
    else:
        if d > 0:
            return [(-b + sqrt(d)) / (2 * a), (-b - sqrt(d)) / (2 * a)]
        elif d == 0:
            return [-b/(2*a), None]
        else:
            return ["n.l."]*2

def linear_equation(m:float, n:float) -> float:
    return -n/m


class GUI(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.h1 = ("Times New Roman", 14)
        self.font = ("Times New Roman", 12)
        
        self.plot_size = 10
        self.plot_step_size = 1
        
        # self.parent.geometry("400x300")
        self.parent.title("Quadratische Gleichungen")
        self.create_objects()
        
        
    def create_objects(self):
        self.label = Label(self, text="f(x) = ax² + bx + c", font = self.h1).grid(row=0, columnspan=3)
        # -- Input Labels -- 
        self.label_a = Label( self, text = "a: ", font = self.font)
        self.label_b = Label( self, text = "b: ", font = self.font)
        self.label_c = Label( self, text = "c: ", font = self.font)
        
        self.label_a.grid(row = 1, padx = 2)
        self.label_b.grid(row = 2, padx = 2)
        self.label_c.grid(row = 3, padx = 2)
        
        # -- Output Labels --
        self.x1 = Label(self, text = "X1:", font = self.font)
        self.x2 = Label(self, text = "X2:", font = self.font)
        
        self.x1.grid(row=5, column = 2, padx=2, pady=2)
        self.x2.grid(row=6, column = 2, padx=2, pady=2)
        
        # -- Entrys -- 
        self.input_a = Entry( self)
        self.input_b = Entry( self)
        self.input_c = Entry( self)
        
        self.input_a.grid(row = 1, column = 2, padx = 20, pady = 5)
        self.input_b.grid(row = 2, column = 2, padx = 20, pady = 5)
        self.input_c.grid(row = 3, column = 2, padx = 20, pady = 5)
        
        # -- Buttons -- 
        self.quit = Button(self, text = "quit", font = self.font, command = self.parent.quit).grid(row=4, column = 0, padx = 5, pady = 5)
        self.calc = Button(self, text = "calc", font = self.font, command = self.calc_equation).grid(row=4, column = 1, padx = 5, pady = 5)
        self.plot = Button(self, text = "plot", font = self.font, command = self.plot).grid(row=5, column = 0, padx = 5, pady = 5)
        
    def read_input(self) -> tuple:
        a,b,c = (0,0,0)
        try:
            a = float(self.input_a.get())
            b = float(self.input_b.get())
            c = float(self.input_c.get())
        except:
            pass
        return (a,b,c)
        
    def calc_equation(self):
        a,b,c = self.read_input()
        
        outputs = quadratic_equation(a=a, b=b, c=c)
        x1,x2 = outputs
        
        self.x1.config(text = f"X1: {str(x1)}")
        self.x2.config(text = f"X2: {str(x2)}")
        
        print(x1, x2)
        
    def plot(self):
        a,b,c = self.read_input()
        points = [[a*(x**2) + b*x + c for x in range(-1*self.plot_size, self.plot_size + 1, self.plot_step_size)], [_ for _ in range(-1*self.plot_size,self.plot_size+1, self.plot_step_size)]]
        try:
            if self.plot_window:
                self.plot_window.update_plot(points)
        except Exception as e:
            self.plot_window = PlotWindow(self.parent, label_font=self.font, plot_points=points)
            print(e)
        
class PlotWindow(Toplevel):
    def __init__(self, master = None, label_font:tuple = None, plot_points:list = None):
        super().__init__(master = master)
        self.title = "Plot Window"
        
        label = Label(self, text="Graphplot:", font=label_font)
        label.pack()
        
        self.fig = Figure(figsize=(5,5) , dpi = 100)
        
        self.plot1 = self.fig.add_subplot(111)
        self.plot1.plot(plot_points[1], plot_points[0])
                
        self.canvas = FigureCanvasTkAgg(self.fig, master = self)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()
        
    def update_plot(self, points):
        self.plot1.cla()
        self.plot1.plot(points[1], points[0])
        self.canvas.draw()
        self.canvas.get_tk_widget().pack()

        
if __name__ == "__main__":
    root = Tk()
    gui = GUI(root).pack(side = "top", fill = "both", expand=True)
    root.mainloop()