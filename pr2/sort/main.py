from tkinter import *
from sort import q_sort, merge_sort

def sort1(arr):
    res = q_sort([int(i) for i in list(arr.split(' '))])
    tmp = ' '.join([str(i) for i in res])
    lable_res_value.config(text='Быстрая сортировка ' + tmp)


def sort2(arr):
    res = merge_sort([int(i) for i in list(arr.split(' '))])
    tmp = ' '.join([str(i) for i in res])
    lable_res_value.config(text='Сортировка слиянием ' + tmp)


window = Tk()
window.title('Практика №2')
window.geometry('400x400')


lable_enter_arr = Label(window, text='Введите массив',
                        font=('Times new roman', 12))
lable_enter_arr.place(x=5, y=5)
enter_arr = Entry(window, width=33,
                  font=('Times new roman', 11))
enter_arr.place(x=120, y=7)

button_qsort = Button(window, text='Быстрая сортировка',
                      command=lambda: sort1(enter_arr.get()))
button_qsort.place(x=60, y=45)

button_mergesort = Button(window, text='Сортировка слиянием',
                          command=lambda: sort2(enter_arr.get()))
button_mergesort.place(x=200, y=45)

lable_res = Label(window, text='Результат',
                  font=('Times new roman', 14))
lable_res.place(x=150, y=90)
lable_res_value = Label(window, text='',
                  font=('Times new roman', 12))
lable_res_value.place(x=50, y=130)

window.mainloop()