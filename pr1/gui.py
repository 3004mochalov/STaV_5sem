import tkinter as tk


# import tkinter.ttk as ttk
class popupWindow(object):
    def __init__(self, master, parent):
        self.parent = parent
        top = self.top = tk.Toplevel(master)
        self.top.geometry('300x300')

        self.header = tk.Label(top, text="Input values")
        self.header.pack()

        self.make_grid()

        self.button_frame = tk.Frame(top)
        self.button_frame.pack(side=tk.BOTTOM)

        self.exit_button = tk.Button(
            master=self.button_frame,
            command=self.cleanup,
            text="OK"
        )
        self.exit_button.pack()

    def make_grid(self):
        self.parent.parse_input()
        self.variables_frame = tk.Frame(self.top)
        self.variables_frame.pack()
        self.entries = []
        for i, variable in enumerate(self.parent.variables):
            temp = tk.Label(self.variables_frame, text=f'{variable} = ')
            temp.grid(row=i, column=0)
            temp = tk.Entry(self.variables_frame, width=30)
            temp.grid(row=i, column=1)
            self.entries.append(temp)

    def cleanup(self):
        values = dict(zip(self.parent.variables, [int(e.get()) for e in self.entries]))
        self.parent.values = values
        self.top.destroy()


class Gui:
    def __init__(self, calculator):
        self.calculator = calculator
        self.values = None
        self.__make_window()

    def __make_window(self):
        self.window = tk.Tk()
        self.window.geometry('600x300')
        # ttk.Style().configure("TFrame", background="#333")
        # self.window["background"] = 'dark grey'
        self.input_frame = tk.Frame(master=self.window)
        self.input_frame.pack()

        self.lbl = tk.Label(master=self.input_frame, text="INPUT EXPRESSION")
        self.lbl.grid(row=0, column=0)
        self.input_row = tk.Entry(master=self.input_frame, width=80, justify='center')
        self.input_row.grid(row=1, column=0)

        self.output_frame = tk.Frame(master=self.window)
        self.output_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.current_output_postfix = tk.StringVar()
        self.output_postfix_label = tk.Label(master=self.output_frame, textvariable=self.current_output_postfix)
        self.output_postfix_label.grid(row=0, column=1, padx=10, pady=10)
        self.postfix_label = tk.Label(self.output_frame, text="POSTFIX:")
        self.postfix_label.grid(row=0, column=0, padx=10, pady=10)

        self.current_output_result = tk.StringVar()
        self.current_result_label = tk.Label(master=self.output_frame, textvariable=self.current_output_result)
        self.current_result_label.grid(row=1, column=1, padx=10, pady=10)
        self.answer_label = tk.Label(self.output_frame, text="ANSWER:")
        self.answer_label.grid(row=1, column=0, padx=10, pady=10)

        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(side=tk.BOTTOM)

        self.calculate_button = tk.Button(
            master=self.button_frame,
            command=self.popup,
            height=2,
            width=10,
            text="CALCULATE"
        )
        self.calculate_button.pack()

    def popup(self):
        # get variable values
        self.w = popupWindow(self.window, self)
        self.calculate_button["state"] = "disabled"
        self.window.wait_window(self.w.top)
        self.calculate_button["state"] = "normal"
        self.calculator.values = self.values

        # get infix string
        self.infix_string = self.input_row.get()
        self.calculator.convert(self.infix_string)
        self.current_output_postfix.set(self.calculator.postfix)

        self.calculator.calculate()
        self.current_output_result.set(self.calculator.result)

    def get_input(self):
        s = self.input_row.get()
        return s

    def parse_input(self):
        entry = self.get_input()
        self.variables = set([i for i in entry if i.isalpha()])  # баг для переменных длины больше 1

    def start(self):
        self.window.mainloop()
