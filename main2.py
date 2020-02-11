import tkinter as tk
from tkinter import ttk
import pandas as pd


def get_date_range(df):

    l =  list(set(df['Pgm Date']))
    l.sort()
    return {i for i in l}


def get_movie_names(df):
    names = list(set(df['Program Name']))
    names.sort()
    return names  # list({i for i in l})


def callbackFunc(event):
    print("New Element Selected")


def main():
    df = pd.read_excel('ratings.xlsx', parse_dates=['Pgm Date'])
    # date_range = get_date_range(df)
    movie_names = get_movie_names(df)
    app = tk.Tk()
    app.geometry('200x100')

    labelTop = tk.Label(app,
                        text="Choose movie")
    labelTop.grid(column=0, row=0)

    combo_example = ttk.Combobox(app,
                                values=movie_names)

    combo_example.grid(column=0, row=1)
    # combo_example.current(1)
    combo_example.bind("<<ComboboxSelected>>", callbackFunc)
    x = combo_example.get()
    print(x)
    # print(f"film: {combo_example.get()}")
    # print(combo_example.current(), combo_example.get())
    app.mainloop()




if __name__ == '__main__':
    main()
