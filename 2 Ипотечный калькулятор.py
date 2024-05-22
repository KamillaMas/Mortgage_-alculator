from tkinter import *
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import os

first_window = Tk()
first_window.title("Эталон")
first_window.geometry('1100x800')

def open_window():
    window = Tk()
    window.title("Ипотечный калькулятор")
    window.geometry('1500x900')

    def calculate():
        type_p = type_bx.get()
        privileges_get = privileges_bx.get()
        if privileges_get == 'без льгот':
            year_perc = 13
        elif privileges_get == 'молодая семья':
            year_perc = 9
        else:
            year_perc = 5
        perc_output.configure(text=str(year_perc))
        years = int(years_en.get())
        list_choose = flats_bx.get('active')
        list_choose2 = str(list_choose)
        ind = list_choose2.rfind('цена')
        money = list_choose2[ind + 5:-5]
        prise = float(money) * 1000000
        flat_price = int(prise)
        contribution = int(contribution_en.get())
        credit_sum = flat_price - contribution
        residue = credit_sum
        m_perc = year_perc / 12 / 100

        output.delete(*output.get_children())

        if type_p == 'аннуитетный':
            total_rate = (1 + m_perc) ** (years * 12)
            month_pay = (credit_sum * m_perc * total_rate) / (total_rate - 1)
            for i in range(years * 12):
                percent_part = (residue * m_perc)
                loan_part = (month_pay - percent_part)
                residue -= loan_part
                output.insert('', END, values=(i + 1, int(loan_part // 1), int(percent_part // 1), int(month_pay // 1), int(residue // 1)))

        else:
            m_repayment = credit_sum / (years * 12)
            for i in range(years * 12):
                percent_part = residue * m_perc
                month_pay = m_repayment + percent_part
                residue -= m_repayment
                output.insert('', END, values=(i + 1, int(m_repayment // 1), int(percent_part // 1), int(month_pay // 1), int(residue // 1)))


    frame = Frame(window, padx=10, pady=10)
    frame.pack(expand = True)

    flats_bx = Listbox(frame, width= 50, height=47)
    flats_bx.grid(row=1, column=1, rowspan=6)
    for i in ('1 :  1 комната,  3-ий этаж,  цена 4 млн.', '2 :  2 комнаты,  5-ый этаж,  цена 7 млн.', '3 :  1 комната,  5-ый этаж,  цена 4 млн.',
              '4 :  3 комнаты,  7-ой этаж,  цена 10 млн.', '5 :  1 комната,  10-ый этаж,  цена 4 млн.', '6 :  2 комнаты,  10-ый этаж,  цена 8 млн.',
              '7 :  3 комнаты,  10-ый этаж,  цена 10 млн.', '8 :  3 комнаты,  11-ый этаж,  цена 10 млн.', '9 :  1 комната,  14-ый этаж,  цена 5 млн.',
              '10 : 2 комнаты,  14-ый этаж,  цена 8.5 млн.', '11 : 2 комнаты,  15-ый этаж,  цена 8.5 млн.', '12 : 3 комнаты,  15-ый этаж,  цена 11 млн.',
              '13 : 2 комнаты,  17-ый этаж,  цена 8.5 млн.', '14 : 3 комнаты,  17-ый этаж,  цена 11.5 млн.', '15 : 2 комнаты,  19-ый этаж,  цена 9 млн.'):
        flats_bx.insert(END, i)
    flats_bx.selection_set(first=0)

    type_lb = Label(frame, text="Тип платежа:")
    type_lb.grid(row=1, column=2)
    privileges_lb = Label(frame, text="Льготы:")
    privileges_lb.grid(row=2, column=2)
    years_lb = Label(frame, text="Срок выплат:")
    years_lb.grid(row=3, column=2)
    contribution_lb = Label(frame, text="Первый взнос:")
    contribution_lb.grid(row=4, column=2)
    perc_lb = Label(frame, text="Годовая ставка:")
    perc_lb.grid(row=5, column=2, pady=5)

    types = ['аннуитетный', 'дифференцированный']
    type_bx = ttk.Combobox(frame, values=types)
    type_bx.current(0)
    type_bx.grid(row=1, column=3)
    privileges = ['без льгот', 'молодая семья', 'IT-ипотека']
    privileges_bx = ttk.Combobox(frame, values=privileges)
    privileges_bx.current(0)
    privileges_bx.grid(row=2, column=3, pady=7)

    perc_output = Label(frame, text='')
    perc_output.grid(row=5, column=3)

    years_en = Entry(frame)
    default_text = "20"
    years_en.insert(0, default_text)
    years_en.grid(row=3, column=3)
    contribution_en = Entry(frame)
    default_text = "500000"
    contribution_en.insert(0, default_text)
    contribution_en.grid(row=4, column=3, pady=7)

    calc_btn = Button(frame, text="РАССЧИТАТЬ", command=calculate)
    calc_btn.grid(row=1, rowspan=5, column=4, padx=15, sticky='nsew')

    heads = ['№',"Платеж по долгу","Платеж по процентам","Весь платеж","Остаток долга"]
    output = ttk.Treeview(frame, show="headings", height=33)
    output['columns'] = heads
    for header in heads:
        output.heading(header, text=header, anchor='center')
        output.column(header, anchor='center')
    output.grid(row=6, column=2, columnspan=3, padx=15, pady=15)
    window.mainloop()

frame1 = Frame(first_window, padx=10, pady=10)
frame1.pack(expand = True)

img = ImageTk.PhotoImage(Image.open("Etalon.jpeg"))
img_lb = Label(frame1, image=img, height=500, width=1050)
img_lb.grid(row=1, column=1)

calc_btn = Button(frame1, text="Рассчитать ипотеку", command=open_window, height=13, width=50)
calc_btn.grid(row=2, column=1, pady=20)

first_window.mainloop()