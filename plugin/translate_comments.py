import re
from googletrans import Translator

def translate_file_comments(file_path, target_language="en", output_file=None):
    """
    Переводит комментарии в Python-файле на указанный язык и сохраняет в новый файл.

    :param file_path: Путь к файлу Python.
    :param target_language: Язык перевода (например, 'en' для английского).
    :param output_file: Имя выходного файла (опционально).
    """
    translator = Translator()

    # Читаем содержимое файла
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Переводим многострочные комментарии """ ... """ или ''' ... '''
    def translate_multiline_comments(match):
        quote_type = match.group(1)
        inner_comment = match.group(2)
        try:
            translated = translator.translate(inner_comment, dest=target_language).text
            return f"{quote_type}{translated}{quote_type}"
        except Exception as e:
            print(f"Ошибка перевода: {e}")
            return match.group(0)

    content = re.sub(r'("""|\'\'\')(.*?)(\1)', translate_multiline_comments, content, flags=re.DOTALL)

    # Переводим однострочные комментарии #
    def translate_inline_comments(match):
        code_part = match.group(1)
        comment_part = match.group(2).strip()
        try:
            translated_comment = translator.translate(comment_part, dest=target_language).text
            return f"{code_part}# {translated_comment}"
        except Exception as e:
            print(f"Ошибка перевода: {e}")
            return match.group(0)

    content = re.sub(r"(.*?#)(.*)", translate_inline_comments, content)

    # Определяем выходной файл
    if not output_file:
        output_file = file_path.replace(".py", f"_translated_{target_language}.py")

    with open(output_file, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Переведенные комментарии сохранены в файл: {output_file}")
    return output_file


# Если файл запускается напрямую
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Перевод комментариев в Python-файле.")
    parser.add_argument("file_path", help="Путь к файлу Python.")
    parser.add_argument("--lang", default="en", help="Целевой язык перевода.")
    args = parser.parse_args()

    translate_file_comments(args.file_path, target_language=args.lang)
