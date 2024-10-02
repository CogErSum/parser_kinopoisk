from tkinter import *
from mysql.connector import MySQLConnection, Error
import getpass
import random

movies = []
def connect_and_paste(query):
    try:
        with MySQLConnection(
            host='localhost',
            user='root',
            password=getpass.getpass(),
            database='movies'
        ) as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                connection.commit()
    except Error as e:
        print(e)
def connect_and_get(query):
    try:
        with MySQLConnection(
            host='localhost',
            user='root',
            password=getpass.getpass(),
            database='movies'
        ) as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute(query)
                result = cursor.fetchall()
                for row in result:
                    movies.append(row['name'])
    except Error as e:
        print(e)

connect_and_get('select * from films')

root = Tk()
root.title('Movies')
root.geometry('600x500')

frm_main = Frame(
    master=root
)

frm_btn = Frame(
    master=root
)

frm_rand_movie = Frame(
    master=root,
    width=20,
    height=20,
    border=5,
    borderwidth=1,
    relief=RIDGE
)

lbl_rand_movie = Label(
    master=frm_rand_movie,
    text=f'Рандомное кино \nна этот вечер:\n {random.choice(movies)}'
)

def rand_movie_click_close():
    frm_rand_movie.place_forget() 
btn_random_movie_close = Button(
    master=frm_rand_movie,
    text='Закрыть',
    command=rand_movie_click_close
)

def rand_movie_click():
    frm_rand_movie.place(x=250,y=200)
    lbl_rand_movie.grid(column=0,row=0)
    btn_random_movie_close.grid(column=0,row=1)

btn_random_movie = Button(
    master=frm_btn,
    text='Выбрать \nрандомное кино',
    width=20,
    borderwidth=5,
    command=rand_movie_click
)

btn_all_movies = Button(
    master=frm_btn,
    text='Просмотреть \nвсе кино',
    width=20,
    borderwidth=5
)

movies_var = Variable(value=movies)
listbox_movies = Listbox(
    master=frm_main,
    listvariable=movies_var,
    width=50,
    height=20
)

listbox_movies.pack()
btn_random_movie.grid(column=0,row=0)
btn_all_movies.grid(column=0,row=1)
frm_btn.grid(column=0,row=0)
frm_main.grid(column=1,row=0)
root.mainloop()