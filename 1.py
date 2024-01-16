from abc import ABC, abstractmethod

class UserInterface(ABC):
    @abstractmethod
    def display_contacts(self, contacts):
        pass

    @abstractmethod
    def display_notes(self, notes):
        pass

    @abstractmethod
    def display_commands(self):
        pass

    @abstractmethod
    def get_user_input(self):
        pass


class ConsoleInterface(UserInterface):
    def display_contacts(self, contacts):
        # Логіка виведення контактів у консоль
        pass

    def display_notes(self, notes):
        # Логіка виведення нотаток у консоль
        pass

    def display_commands(self):
        # Логіка виведення доступних команд у консоль
        pass

    def get_user_input(self):
        # Логіка отримання вводу від користувача з консолі
        pass


class App:
    def __init__(self, user_interface):
        self.user_interface = user_interface

    def run(self):
        while True:
            # Отримання введення від користувача через інтерфейс
            user_input = self.user_interface.get_user_input()

            # Обробка команд та взаємодія з додатком

            # Приклад:
            if user_input == "1":
                contacts = self.get_contacts_from_database()
                self.user_interface.display_contacts(contacts)
            elif user_input == "2":
                notes = self.get_notes_from_database()
                self.user_interface.display_notes(notes)
            elif user_input == "help":
                self.user_interface.display_commands()
            elif user_input == "exit":
                break

    def get_contacts_from_database(self):
        # Логіка отримання контактів з бази даних
        pass

    def get_notes_from_database(self):
        # Логіка отримання нотаток з бази даних
        pass


# Використання додатку з консольним інтерфейсом
console_interface = ConsoleInterface()
app = App(console_interface)
app.run()
