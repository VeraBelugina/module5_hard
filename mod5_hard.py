import time
from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        return other.nickname == self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title #заголовок
        self.duration = duration #продолжительность
        self.time_nom = 0 #секунда остановки
        self.adult_mode = adult_mode #ограничение по возрасту

    def __eq__(self, other):
        return self.title == other.title


class UrTube:
    def __init__(self):
        self.users = [] #список объектов User
        self.videos = [] # -- Video
        self.current_user = None #текущий пользователь, User

    def add(self, *videos):
        for new_video in videos:
            if new_video not in self.videos:
                self.videos.append(new_video)

    def get_videos(self, search):
        res = []
        for video in self.videos:
            if search.lower() in video.title.lower():
                res.append(video.title)
        return res

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user not in self.users:
            self.users.append(new_user)
            self.current_user = new_user
        else:
            print(f'Пользователь {nickname} уже существует')

    def log_out(self):
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if (nickname, hash(password)) == (user.nickname, user.password):
                self.current_user = user
            return user

    def watch_video(self, title):
        if self.current_user is None:
            print(f'Войдите в аккаунт, чтобы смотреть видео')
            return
        for video in self.videos:
            if title == video.title:
                if video.adult_mode and self.current_user.age >= 18:
                    while video.time_nom < video.duration:
                        time.sleep(1)
                        video.time_nom += 1
                        print(video.time_nom)
                    video.time_nom = 0
                    print(f'Конец видео')
                else:
                    print(f'Вам нет 18 лет, пожалуйста покиньте страницу')


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
