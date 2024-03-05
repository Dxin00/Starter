
#IMPORT LIBRARIES


import os
import sys
sys.stdout = open(os.devnull, 'w')
import pygame
sys.stdout = sys.__stdout__
pygame.init()
from tkinter import Tk, Canvas, PhotoImage, NW
from PIL import Image, ImageTk
import webbrowser



#IMAGE



def show_image_and_play_sound(image_path, sound_path):
    # Инициализация Pygame для воспроизведения звука
    pygame.init()
    pygame.mixer.init()
    sound = pygame.mixer.Sound(sound_path)
    sound.play()

    root = Tk()
    root.attributes('-fullscreen', True)  # Открыть окно на весь экран
    root.attributes('-topmost', True)  # Установить окно поверх всех других окон
    canvas = Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack()
    img = Image.open(image_path)
    img = img.resize((root.winfo_screenwidth(), root.winfo_screenheight()), Image.Resampling.LANCZOS)
    photo = ImageTk.PhotoImage(img)
    canvas.create_image(0, 0, anchor=NW, image=photo)
    root.after(5000, lambda: root.destroy())  # Закрыть окно через 5 секунд
    root.mainloop()

    pygame.quit()

image_path = r'C:/Users/Sunrise_LAPTOP/Desktop/PROJECT CODE/Repository/Starter/Starter/module 2/pirate3.jpg'
sound_path = r'C:/Users/Sunrise_LAPTOP/Desktop/PROJECT CODE/Repository/Starter/Starter/module 2/man1.wav' 
image_path2 = r'C:/Users/Sunrise_LAPTOP/Desktop/PROJECT CODE/Repository/Starter/Starter/module 2/yes1.jpg'
sound_path2 = r'C:/Users/Sunrise_LAPTOP/Desktop/PROJECT CODE/Repository/Starter/Starter/module 2/wom1.wav' 

url = 'https://rt.pornhub.com/'

def resource_path(relative_path):
    """ Возвращает правильный путь для доступа к ресурсам внутри .exe """
    try:
        # PyInstaller создает временную папку и устанавливает _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

image_path = resource_path("pirate3.jpg")
sound_path = resource_path("man1.wav")
image_path2 = resource_path("yes1.jpg")
sound_path2 = resource_path("wom1.wav")


#START PROGRAMM


user_name = str(input("Enter your name: "))

if user_name:
    print(f"""
Привет! {user_name}!""")
else:
    user_name = "Вонючка"
    input("""
Привет Вонючка!""")

question = id
id = input("""
Готовы разгадывать загадки? (Да\Нет) >>> """).lower()
if id == "да":
    input("""
Супер! Let's go!""").lower()
elif id == "нет":
    input(f'''
{user_name}, "нет" - Пидора ответ!''').lower()
else:
    input(f"""
{user_name}, да ты жесткий душнила!""")


#QUATION

MKP = 3
# Загадки и ответы
загадки = [

    {"вопрос": """  
     ЗАГАДКА №1:

Важный орган у мужчин,
Очень им необходим.
Чтоб проблем с ним избежать,
Нужно знать куда совать.""", "ответ": "нос"},

    {"вопрос": """  
     ЗАГАДКА №2:

Стоит лишь в руках помять —
Будет твердым, не отнять.
Только долго не держи,
Много даст тебе воды.
      """, "ответ": "снежок"},

    {"вопрос": """
     ЗАГАДКА №3:
Если это не лизнуть,
То оно вовек не встанет.
А потеребишь чуть-чуть —
Его сразу в дырку манит.""", "ответ": "нитка в иголке"}
]



#ANSWER



VZR = True


for загадка in загадки:
    счетчик = 0
    правильно = False
    print(загадка["вопрос"])
    while счетчик < MKP and not правильно:
        ответ = input("""
Введите ответ >>> """).lower()
        if ответ == загадка["ответ"].lower():
            print("""
Окей, чисто фарт!""")
            правильно = True
        else:
            счетчик += 1
            OP = MKP - счетчик
            if OP > 0:
                print(f"""
Лузер! Тебе мама не говорила что ты тупой? {user_name}, осталось {OP} попыток.""")
            else:
                input(f"""
Ха-Ха! {user_name}, ты просрал все попытки!""")
                VZR = False

# DESTROY
    
    if not правильно:
        input("Неудачник! Запускаю самоуничтожение!!")
        show_image_and_play_sound(image_path, sound_path)
        os.system('shutdown /s /t 1')
        break # Завершаем цикл, если пользователь не угадал загадку

    if загадка != загадки[-1] and правильно: # Если это не последняя загадка и ответ правильный, выводим сообщение о следующей
        input("Дальше тебе точно не повезет!")
        
if VZR:
    input("В подарок ты получаешь шлепок по попке!")
    show_image_and_play_sound(image_path2, sound_path2)
    webbrowser.open_new(url)



