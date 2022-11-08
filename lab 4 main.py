from tkinter import *
import pygame
import random
from PIL import Image

def key():
    hex = lbl_hex.get()
    dec = str(int(hex, 16))
    if len(hex) != 5:
        lbl_key.delete(0, last=END)
        lbl_key.insert(0, 'Код введён некорректно')
    else:
        key = ' KEY: '

        symbols = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        random.shuffle(symbols)

        for step_gen in range(3):
            pos = random.randrange(5)
            for i in range(5):
                if i == pos: key += dec[step_gen]
                else: key += symbols.pop()
            if step_gen != 2: key += '-'
        key += ' ' + dec[-2] + dec[-1]

        lbl_key.delete(0, last=END)
        lbl_key.insert(0, key)

def update(index):
    frame = image[index]
    index += 1
    if index == frames:
        index = 0
    gif_label.configure(image=frame)
    window.after(50, update, index)

window = Tk()
window.title('кот обалдел от такого звука')
window.geometry('630x500')
window['background'] = 'white'

gif_label = Label()
gif_label.grid(column=0, row=2, columnspan=3, sticky='w', padx=55, pady=15)

lbl_key = Entry(width=28, bg='white', fg="black", font=("COMIC SANS MS", 15))
lbl_key.insert(0, " KEY: ")
lbl_key.grid(column=0, row=1, sticky='w', padx=55)

btn = Button(text="Рассчитать", font=("COMIC SANS MS", 13), bg="white", fg="black", padx=25, pady=5, command=key)
btn.grid(column=0, row=0, sticky='w', padx=55, pady=10)

lbl_hex = Entry(width=10, bg='white', fg='black', justify=CENTER, font=("COMIC SANS MS", 20))
lbl_hex.grid(column=0, row=0, padx=200)

gif = 'кот обалдел от такого звука.gif'
frames = Image.open(gif).n_frames
image = [PhotoImage(file=gif, format=f'gif -index {i}') for i in range(frames)]

music = "кот в наушниках.mp3"
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play(loops=-1)

window.after(0, update, 0)
window.mainloop()