import tkinter as tk
import tkinter.ttk as ttk

from matrix import *

'''
Весь gui как кирпичики, осталось их слепить вместе...
'''

# ФРЕЙМ ДЛЯ ВВОДА РАЗМЕРНОСТЕЙ МАТРИЦ
class DimFrame(ttk.Frame):
    def __init__(self, parent, name, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        ttk.Label(self, text=name).pack(side=tk.LEFT, padx=3)
        self.rows_entry = ttk.Entry(self)
        self.cols_entry = ttk.Entry(self)

        self.rows_entry.pack(side=tk.LEFT, padx=3)
        ttk.Label(self, text='x').pack(side=tk.LEFT, padx=3)
        self.cols_entry.pack(side=tk.LEFT, padx=3)

    def get(self):
        return int(self.rows_entry.get()), int(self.cols_entry.get())


# ФРЕЙМ ДЛЯ СОЗДАНИЯ/ВВОДА МАТРИЦЫ
class MatrixEntry(ttk.Frame):
    def __init__(self, parent, dim: tuple, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.cols, self.rows = cols, rows = dim
        self.matrix = []
        for i in range(rows):
            for j in range(cols):
                entry = ttk.Entry(self)
                entry.grid(row=i, column=j, padx=1, pady=1)
                self.matrix.append(entry)

    def get(self):
        m = []
        for e in self.matrix:
            print(e.get())
            m.append(float(e.get()))
        return np.array(m).reshape(self.rows, self.cols)


# ФРЕЙМ ДЛЯ УНАРНЫХ ОПЕРАЦИЙ С МАТРИЦАМИ (inverse, eigen)
class UnaryFrame(ttk.Frame):
    def __init__(self, parent, operation, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)

        # MATRIX
        self.A = None
        self.lb = None

        self.dim_frame = DimFrame(self, name='Введите размерность')

        self.b_build_matrix = ttk.Button(
            self.dim_frame,
            text='Добавить',
            command=self.create_matrix
        )

        self.b_calculate = ttk.Button(
            self,
            text='Вычислить',
            command=lambda: self.compute(option=operation)
        )

        self.b_clear = ttk.Button(
            self.dim_frame,
            text='Очистить',
            command=lambda: self.clear()
        )

        # PLACING
        self.dim_frame.pack(pady=30)
        self.b_build_matrix.pack(side=tk.LEFT, padx=3)
        self.b_clear.pack(side=tk.LEFT, padx=2)
        self.b_calculate.pack(side=tk.BOTTOM)

    def create_matrix(self):
        if self.A is None:
            self.A = MatrixEntry(self, dim=self.dim_frame.get())
            self.A.pack()

    def compute(self, option):
        if option == 'eigen':
            res = eigen_values(self.A.get())
            self.lb = ttk.Label(self, text=res)
            self.lb.pack()
        elif option == 'inverse':
            res = inverse(self.A.get())
            self.lb = ttk.Label(self, text=res)
            self.lb.pack()

    def clear(self):
        self.A.pack_forget()
        self.lb.pack_forget()
        self.A = None




# ФРЕЙМ ДЛЯ БИНАРНЫХ ОПЕРАЦИЙ С МАТРИЦАМИ (add, mul)
class BinaryFrame(ttk.Frame):
    def __init__(self, parent, operation, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)

        self.A = None
        self.B = None
        self.lb = None

        self.dim_frame = DimFrame(self, name='Введите размерность')

        self.b_build_matrix = ttk.Button(
            self.dim_frame,
            text='Добавить',
            command=self.create_matrix
        )

        self.b_calculate = ttk.Button(
            self,
            text='Вычислить',
            command=lambda: self.compute(option=operation)
        )

        self.b_clear = ttk.Button(
            self.dim_frame,
            text='Очистить',
            command=lambda: self.clear()
        )
        # PLACING
        self.dim_frame.pack(pady=30)
        self.b_build_matrix.pack(side=tk.LEFT, padx=3)
        self.b_clear.pack(side=tk.RIGHT, padx=2)
        self.b_calculate.pack(side=tk.BOTTOM)

    def create_matrix(self):
        if self.A is None:
            self.A = MatrixEntry(self, dim=self.dim_frame.get())
            self.A.pack()
        elif self.B is None:
            self.A.pack_forget()
            self.B = MatrixEntry(self, dim=self.dim_frame.get())
            self.B.pack()

    def compute(self, option):
        if option == 'add':
            res = add(self.A.get(), self.B.get())
            self.lb = ttk.Label(self, text=res)
            self.lb.pack()
        if option == 'mult':
            res = mul(self.A.get(), self.B.get())
            self.lb = ttk.Label(self, text=res)
            self.lb.pack()

    def clear(self):
        self.A.pack_forget()
        self.B.pack_forget()
        self.lb.pack_forget()
        self.A = None
        self.B = None



# ОСНОВНОЕ ПРИЛОЖЕНИЕ
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(side='top', fill='both', expand=1)
        self.widgets = {
            'Умножение': BinaryFrame(self, operation='mult'),
            'Сложение': BinaryFrame(self, operation='add'),
            'Обратная матрица': UnaryFrame(self, operation='inverse'),
            'Собственные значения': UnaryFrame(self, operation='eigen')
        }
        for name, frame in self.widgets.items():
            frame.pack(expand=1, fill='both')
            self.notebook.add(frame, text=name)


HEIGHT = 400
WIDTH = 900


def start():
    root = tk.Tk()
    root.geometry(f'{WIDTH}x{HEIGHT}')
    MainApplication(root).pack(fill="both", expand=1)
    root.mainloop()
