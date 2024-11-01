import json
import os
import threading
from tkinter import filedialog

# Функция для загрузки данных из JSON файла
def load_json(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print("Файл не найден.")
        return None
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON.")
        return None

# Функция для сохранения данных в JSON файл
def save_json(file_path, data):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print("Данные успешно сохранены.")
    except Exception as e:
        print(f"Ошибка при сохранении файла: {e}")


def _play_sound_in_thread(sound):
    os.system(f'afplay {sound}')

def play_sound(sound):
    thread = threading.Thread(target=_play_sound_in_thread, args=(sound,))
    thread.start()

def open_file():
    '''Запрашивает открытие файла через окно.'''
    file_path = filedialog.askopenfilename(
        title="Выберите файл",
        filetypes=(("vin.json", "*.json"), ("Все файлы", "*.*"))
    )
    if file_path:
        return file_path
    else:
        return 0

success = 'resources/success.mp3'
fox_unlock = 'resources/fox_unlock.mp3'
failed = 'resources/failed.mp3'