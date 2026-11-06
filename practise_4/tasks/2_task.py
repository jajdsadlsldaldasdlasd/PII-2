# Создайте иерархию классов для различных типов транспортных средств (Необходим один родительский класс и 3 дочерних).
# Реализуйте метод, который позволяет каждому транспортному средству возвращать собственное описание (Метод в каждом классе должен иметь одинаковое название).
# Продемонстрируйте вызов данного метода для каждого транспортного средства.

# Отрабатываемый принцип: Полиморфизм

class Transport:
    def __init__(self, name):
        self.name = name

    def description(self):
        return "Транспорт"

class Car(Transport):
    def description(self):
            return f"Этот транспорт - {self.name}, у него есть колеса и двигатель."


class Plane(Transport):
    def description(self):
                return f"Этот транспорт - {self.name}, у него есть крылья и он высоко летает."


class Bike(Transport):
    def description(self):
                return f"Этот транспорт - {self.name}, у него есть колеса и педали."


plane = Plane("Boeing")
plane.description()