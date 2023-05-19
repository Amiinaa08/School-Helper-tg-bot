from config import bot
import random

SONGS = [
    """Now I'm better solo, solo
I never let me down, didi-down-down-down
Now I'm gonna show ya, show ya
Show you what it is you're missing out""",
    """Їде маршрутка
Як велика собача будка
На дорозі всіх підрізає
Бо шансон в салоні рубає
Владімірский централ!
Владімірский централ!
Владімірский централ!
Владімірский центра-тра-тра-тра-тра-тра-тра-тра-тра-тра-трал!""",
    """Прогноз погоди показує ймовірності дощу
Даю сигнали, щоби ти мене почув
Сьогодні я на варті, я в ефірі
Я вирішую проблеми

Прогноз погоди показує ймовірності дощу
Все під контролем, але скоро закричу
Переступаю через край, бо хочу знов
Стояти на своєму!""",
    """Хто ми з тобою?
Ми з тобою хрещені
Де ми хрещені?
В церкві на Троєщині
Це наші небеса і наші аномалії
У господа немає для нас автокефалії""",
    """У мене налитий самогон стаканчик
Біля хати бродить молодий кабанчик
Скоро буде свято, весела гулянка -
Ой яка ж чудова гарна буде п’янка
Наливай куме горілки стаканчик
Бігає по полю весело кабанчик""",
    """Mama kupila traktora, šč
Mama kupila traktora, šč
Mama kupila traktora
Trajna-nina, armagedon, nona, šč
Mama kupila traktora, šč
Mama kupila traktora, šč
Mama kupila traktora
Trajna-nina, armagedon, nona
Traktora""",
]


def get_random_song_message(message):
    random_song = random.choice(SONGS)
    bot.send_message(message.chat.id, random_song)
