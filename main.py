from tkinter import*
from random import*
import tkinter.ttk as ttk
from tkinter import messagebox


def proverka(pole_chisel):
    vvod_chisel = pole_chisel.get()
    if vvod_chisel == '':
        messagebox.showinfo('Введите числа!', 'Вы ничего не ввели, введите загаданные числа.')
    spic_proverka = vvod_chisel.split()
    spic_proverka = [int(i) for i in spic_proverka]
    if spic == spic_proverka:
        nb_set.tab(tab3, state="disabled")
        nb_set.tab(tab4, state="normal")
        nb_set.select(tab4)
        if lvl_count < 4:
            l1 = Label(tab4, text='Верно, следующий уровень!', font="ProunX 23 bold")
            l1.place(x = 35, y=100)
            butt_next_lvl = Button(tab4, text='Следующий уровень', font=("ProunX", 12), activebackground='green', height=1, width=20)  # Кнопка следующего уровня
            butt_next_lvl.place(x=305, y=240)
            but_exit = Button(tab4, text='Выход', font=("ProunX", 12), activebackground='red', height=1, width=15, command=win.destroy)
            but_exit.place(x=25, y=240)
            butt_next_lvl.config(command=lambda : change_lvl(l1, but_exit, butt_next_lvl))
            spic.clear()
            spic_proverka.clear()
        else:
            butt_game_win = Button(tab4, text='Конец игры', font=("ProunX", 12), activebackground='green', height=1, width=20, command= lambda : game_win(spic_proverka, l, butt_game_win))  # Кнопка следующего уровня
            butt_game_win.place(x=155, y=240)
            l = Label(tab4, text='Поздравялем, игра пройдена!', font="ProunX 23 bold")
            l.place(x = 22, y=100)
            file1(lvl_count)
            spic.clear()
            spic_proverka.clear()
    else:
        game_over(spic, spic_proverka)


#Действия в случае проигрыша
#1
def clear(spic, spic_proverka, game_over, btn_game_over, but_exit1):
    global lvl_count, count
    game_over.destroy()
    btn_game_over.destroy()
    but_exit1.destroy()
    spic.clear()
    spic_proverka.clear()
    lvl_count = 1
    count = 2

#2
def game_over(spic, spic_proverka):
    nb_set.tab(tab3, state="disabled")
    nb_set.tab(tab4, state="normal")
    nb_set.select(tab4)
    file(lvl_count)
    game_over = Label(tab4, text='Неверно, игра окончена', font="ProunX 23 bold")
    game_over.place(x = 65, y=100)
    btn_game_over = Button(tab4, text='Новая игра', font=("ProunX", 12), height=1, width=20)
    btn_game_over.place(x=305, y=240)
    but_exit1 = Button(tab4, text='Выход', font=("ProunX", 12), height=1, width=15, command=win.destroy)
    but_exit1.place(x=25, y=240)
    btn_game_over.config(command= lambda : new_game(game_over, btn_game_over, but_exit1, spic_proverka))

#3
def new_game(game_over, btn_game_over, but_exit1, spic_proverka):
    global lvl_count
    clear(spic, spic_proverka, game_over, btn_game_over, but_exit1)
    nb_set.tab(tab1, state="normal")
    nb_set.select(tab1)
    nb_set.tab(tab4, state="disabled")



#Действия в случае выйгрыша
#1
def game_win(spic_proverka, l, butt_game_win):
    massang = messagebox.askyesno("Новая игра", "Желаете начать новую игру?")
    if massang == 1:
        new_game1(spic, spic_proverka, l, butt_game_win)
    if massang == 0:
        massang1 = messagebox.askyesno("Выход", "Хотите выйти?")
        if massang1 == 1:
            win.destroy()

#2
def new_game1(spic, spic_proverka, l, butt_game_win):
    global lvl_count, count
    spic.clear()
    spic_proverka.clear()
    lvl_count = 1
    count = 2
    l.destroy()
    butt_game_win.destroy()
    nb_set.tab(tab1, state="normal")
    nb_set.select(tab1)
    nb_set.tab(tab4, state="disabled")


def change_lvl(l1, but_exit, butt_next_lvl):
    global count
    l1.destroy()
    but_exit.destroy()
    butt_next_lvl.destroy()
    if lvl_count == 2:
        lvl2(count)
    if lvl_count == 3:
        lvl3(count)


def vvod_chisel():
    nb_set.tab(tab2, state="disabled")
    nb_set.tab(tab3, state="normal")
    nb_set.select(tab3)
    pole_chisel = ttk.Entry(tab3, font="ProunX 23 bold")  # Поле ввода чисел на проверку третья вкладка
    pole_chisel.place(x=75, y=100)
    zag2 = Label(tab3, text='Введите числа через пробел', font="ProunX 13")  # Заголовок 3 вкладки
    zag2.place(x=78, y=70)
    butt3 = Button(tab3, text='Сравнить числа', font=("ProunX", 12), height=1, width=15, command= lambda : proverka(pole_chisel))  # Кнопка третей вкладки проверка чисел
    butt3.place(x=335, y=240)


def lvl1(count):
    global lvl_count
    nb_set.select(tab2)
    nb_set.tab(tab2, state="normal")
    nb_set.tab(tab1, state="disabled")
    chislo = randint(1, 9)
    spic.append(chislo)
    chisla_lvl1['text'] = chislo
    if count >= 0:
        win.after(1000, lvl1, count - 1)
    else:
        if len(spic) == 4:
            spic.pop(3)
            print('lvl', lvl_count)
            print(spic)
            lvl_count +=1
            vvod_chisel()


def lvl2(count):
    global lvl_count
    nb_set.select(tab2)
    nb_set.tab(tab2, state="normal")
    nb_set.tab(tab4, state="disabled")
    chislo = randint(10, 99)
    spic.append(chislo)
    chisla_lvl1['text'] = chislo
    if count >= 0:
        win.after(1000, lvl2, count - 1)
    else:
        if len(spic) == 4:
            spic.pop(3)
            print('lvl', lvl_count)
            print(spic)
            lvl_count += 1
            vvod_chisel()


def lvl3(count):
    global lvl_count
    nb_set.select(tab2)
    nb_set.tab(tab2, state="normal")
    nb_set.tab(tab4, state="disabled")
    chislo = randint(100, 999)
    spic.append(chislo)
    chisla_lvl1['text'] = chislo
    if count >= 0:
        win.after(1000, lvl3, count - 1)
    else:
        if len(spic) == 4:
            spic.pop(3)
            print('lvl', lvl_count)
            print(spic)
            lvl_count += 1
            vvod_chisel()

def creat_result_win():             #окно статистики
    win_result = Toplevel(win)
    win_result.geometry('300x230')
    listbox = Listbox(win_result, width=35)
    listbox.grid(row=1, column=0, padx=45)
    label=Label(win_result, text = "Статистика", font = 'Times 15').grid(row=0, column=0, padx=45)
    with open('result.txt', 'r') as file:
        lst = file.readlines()
    for item in lst:                                         #вывод данных из файла
        listbox.insert(END, item)
    button1 = Button(win_result, text='Очистить результаты', width=17, background='lavender', command=lambda :clear1(listbox)).grid(pady=5)           #кнопка очистки


def clear1(listbox):
    with open('result.txt', 'w') as file:        # очистка статистика
        file.writelines('')
    listbox.delete(0, END)


def file(lvl_count):
    name = pole_name.get()
    with open('result.txt', 'a') as file:
        file.writelines(f'Игрок ' + name + ' дошел до уровня: ' + str(lvl_count) + '\n')                        #запись данных в файла при проигрыше


def file1(lvl_count):
    name = pole_name.get()
    with open('result.txt', 'a') as file:
        file.writelines(f'Игрок ' + name + ', прошел игру.' + '\n' + 'Его уровень: ' + str(lvl_count) + '\n')                        #запись данных в файла при выйгрыше



win = Tk()
win.geometry("500x320+550+200")
win.resizable(False, False)                  #создаем окно, указываем размеры
win.title("Угадай число")
lvl_count = 1
count = 2
spic = []


menubar = Menu(win)                       #основа выпадающего меню
win.config(menu=menubar)
settings_menu = Menu(menubar, tearoff=0)
settings_menu.add_command(label='Статистика', command=creat_result_win)                      #выпадающее меню
settings_menu.add_command(label='Выход', command=win.destroy)
menubar.add_cascade(label='Файл', menu=settings_menu)


nb_set = ttk.Notebook(win)
tab1 = Frame(nb_set)
nb_set.add(tab1, text='Меню')
tab2 = Frame(nb_set)                                 #Создание вкладок
nb_set.add(tab2, text='Игра')
tab3 = Frame(nb_set)
nb_set.add(tab3, text='Ваш ответ')
tab4 = Frame(nb_set)
nb_set.add(tab4, text='Результаты')
nb_set.pack(fill='both', expand=1)

nb_set.tab(tab2, state="disabled")                                   #Отключение вкладки 2
nb_set.tab(tab3, state="disabled")                                   #Отключение вкладки 3
nb_set.tab(tab4, state="disabled")                                   #Отключение вкладки 4


chisla_lvl1 = Label(tab2, font="ProunX 27 bold")                          #Ввывод чисел лвл1
chisla_lvl1.place(x=230, y=100)


zag1 = Label(tab1, text='Введите ваше имя: ', font=("ProunX", 13))    #Заголовок первой вкладки
zag1.place(x=35, y=75)
pole_name = ttk.Entry(tab1, font=("ProunX",15), width = 40)            #Поле ввода имени первой вкладки
pole_name.place(x=25, y=100)


butt1 = Button(tab1, text='Играть', font=("ProunX", 12), activebackground='green', height = 1, width = 15, command= lambda : lvl1(count))       #Кнопки первой вкладки
butt1.place(x=335, y=240)
butt2 = Button(tab1, text='Выход', font=("ProunX", 12), activebackground='red', height = 1, width = 15, command=win.destroy)
butt2.place(x=25, y=240)


win.mainloop()