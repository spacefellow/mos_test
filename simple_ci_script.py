# Предварительно активируйте виртуальное окружение командой source venv/bin/activate 

import time
from git import Repo
import os
import shutil


# Устанавливаем текущую дату
today=time.strftime('%d.%m.%Y')
# Задаем путь до директории с id текущей даты
dirpath  = f"./{today}"
# Устанавливаем ссылку на гит репозиторий
giturl = "https://github.com/heroku/node-js-getting-started.git" 

# Если такой файл есть в текущей директории, удаляем его
if os.path.exists(dirpath):
    shutil.rmtree(dirpath)
# Клонируем репозиторий
Repo.clone_from(giturl, dirpath)
# Копируем Docker файл (из п.1) в только что созданную папку
shutil.copy("./Dockerfile", dirpath)
# Переходим в эту папку с id (dd.mm.yy)
os.chdir(dirpath)
# Создаем образ docker
os.system(f"docker build -t {today} .")
# Запускаем контейнер docker
os.system(f"docker run -d -p 5001:5001 {today}")
