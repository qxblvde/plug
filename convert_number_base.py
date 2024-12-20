import sublime
import sublime_plugin


class ConvertNumberBaseCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.window().show_input_panel(
            "Введите исходную и целевую системы счисления (например, 10 2):",
            "",
            self.on_done,
            None,
            None
        )

    def on_done(self, bases_input):
        try:
            source_base, target_base = map(int, bases_input.strip().split())
            if source_base < 2 or target_base < 2:
                sublime.error_message("Системы счисления должны быть >= 2.")
                return

            for region in self.view.sel():
                if region.empty():
                    continue

                selected_text = self.view.substr(region).strip()
                self.convert_and_replace(region, source_base, target_base, selected_text)

        except ValueError:
            sublime.error_message("Некорректный ввод. Укажите две системы счисления через пробел.")

    def convert_and_replace(self, region, source_base, target_base, text):
        try:
            decimal_value = int(text, source_base)
            converted_value = self.to_base(decimal_value, target_base)
            self.view.run_command("replace_region", {"region": [region.a, region.b], "text": converted_value})

        except ValueError:
            sublime.error_message(
                f"'{text}' не является корректным числом в системе счисления {source_base}."
            )

    def to_base(self, number, base):
        """Преобразует число из десятичной в целевую систему счисления."""
        if number == 0:
            return "0"

        digits = []
        while number > 0:
            digits.append(str(number % base))
            number //= base

        return ''.join(reversed(digits))


class ReplaceRegionCommand(sublime_plugin.TextCommand):
    def run(self, edit, region, text):
        region_obj = sublime.Region(region[0], region[1])
        self.view.replace(edit, region_obj, text)
