class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


class RegistrationLog:

    def __init__(self, file_input, file_output_wrong, file_output_good):
        self.file_name = file_input
        self.out_file_name_wrong = file_output_wrong
        self.out_file_name_good = file_output_good
        self.file = self.write_file_wrong = self.write_file_good = self.line = None

    def validation_file(self):
        with open(self.file_name, mode="r", encoding="utf8") as self.file:
            with open(self.out_file_name_wrong, mode='w', encoding='utf8') as self.write_file_wrong:
                with open(self.out_file_name_good, mode='w', encoding='utf8') as self.write_file_good:
                    self.log_formatting()

    def unpacking_and_check_file(self):
        self.line = self.line[:-1]
        name, email, age = self.line.split()
        check_age = int(age)
        if not name.isalpha():
            raise NotNameError()
        for symbol in ['@', '.']:
            if symbol not in email:
                raise NotEmailError()
        if not 10 < check_age < 100:
            raise ValueError()

    def log_formatting(self):
        for self.line in self.file:
            try:
                self.unpacking_and_check_file()
            except NotNameError:
                content_wrong = f'{self.line} (Некоректное имя)\n'
                self.write_file_wrong.write(content_wrong)
            except NotEmailError:
                content_wrong = f'{self.line} (Некоректный email)\n'
                self.write_file_wrong.write(content_wrong)
            except ValueError:
                content_wrong = f'{self.line} (Некоректный возраст)\n'
                self.write_file_wrong.write(content_wrong)
            else:
                content_good = self.line + '\n'
                self.write_file_good.write(content_good)


check_reg_file = RegistrationLog(file_input="registrations.txt", file_output_wrong="registrations_bad.log",
                                 file_output_good="registrations_good.log")
check_reg_file.validation_file()
