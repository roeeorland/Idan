from tkinter import *
import pandas as pd


def get_date_range(df):

    l =  list(set(df['Pgm Date']))
    l.sort()
    return {i for i in l}


def get_movie_names(df):
    l =  list(set(df['Program Name']))
    l.sort()
    return {i for i in l}


def main():

    df = pd.read_excel('ratings.xlsx', parse_dates=['Pgm Date'])
    date_range = get_date_range(df)
    movie_names = get_movie_names(df)
    window = Tk()
    window.title("Idan's project")
    lbl = Label(window, text='Idan', font=('Arial Bold', 50))
    lbl.grid(column=0, row=0)
    window.geometry('600x600')
    btn = Button(window, text='Execute query')
    btn.grid(column=20, row=20)
    btn2 = Button(window, text='in between')
    btn2.grid(column=10, row=7)


    variable = StringVar(window)

    w = OptionMenu(window, variable, movie_names)
    w.pack()

    window.mainloop()
    print()
if __name__ == '__main__':
    main()


