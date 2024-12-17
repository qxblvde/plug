README.md

# Comment Translator

## Описание проекта
`comment_translator` — это Python-утилита для перевода комментариев в Python-файлах на указанный язык с использованием библиотеки `googletrans`. Она поддерживает как однострочные комментарии (`# ...`), так и многострочные комментарии (`""" ... """` или `''' ... '''`).

## Возможности
- Автоматический перевод однострочных и многострочных комментариев в Python-коде.
- Сохранение результата в новом файле с указанием языка перевода.
- Простая интеграция как скрипта командной строки или модуля.

---

## **Установка**

### 1. Установка через `pip`
Склонируйте репозиторий или скачайте код, затем выполните:

```bash
pip install .
```
2. Установка зависимостей вручную

Если не используете setup.py, установите googletrans вручную:
```bash
pip install googletrans==4.0.0-rc1
```
Использование

1. В качестве скрипта командной строки

После установки через pip, запускайте утилиту напрямую:

translate-comments <file_path> --lang <target_language>

	•	<file_path> — путь к файлу Python с комментариями.
	•	--lang — целевой язык перевода (по умолчанию: английский en).

Пример:

translate-comments my_script.py --lang ru

2. В качестве Python-модуля

Вы можете использовать функцию translate_file_comments из модуля в своих программах:

from comment_translator import translate_file_comments

# Переводим комментарии из файла test.py на русский
output = translate_file_comments("test.py", target_language="ru")
print(f"Комментарии переведены и сохранены в: {output}")

Пример работы

Исходный файл test.py:

# This is a simple function
def add(a, b):
    """
    Adds two numbers and returns the result.
    """
    return a + b

Команда для перевода:

translate-comments test.py --lang ru

Результат в test_translated_ru.py:

# Это простая функция
def add(a, b):
    """
    Добавляет два числа и возвращает результат.
    """
    return a + b

Содержимое репозитория
	•	translate_comments.py — основной файл с логикой перевода.
	•	setup.py — файл для установки проекта и настройки CLI.
	•	README.md — документация проекта.

Разработка

Установка зависимостей для разработки:

pip install -r requirements.txt

Проверка работы скрипта локально:

python translate_comments.py <file_path> --lang <target_language>

Автор
	•	Сивак Максим Сергеевич М3105
---

### **Объяснение файлов**

- `README.md` предоставляет **полное описание** проекта, инструкции по установке, использованию и примеры.
- Описание включает как использование командной строки (CLI), так и интеграцию через Python-модуль.

---

### **Файл setup.py**

`setup.py` позволяет установить проект как пакет и создать CLI-команду `translate-comments`. Код корректен и отвечает требованиям для упаковки Python-проектов.

После выполнения установки через `pip install .`, будет доступна команда:

```bash
translate-comments <file_path> --lang <language>

Эта команда вызывает функцию translate_file_comments, определённую в модуле.
