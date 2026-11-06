"""Простая консольная программа для учёта продуктов в холодильнике."""

from dataclasses import dataclass
from datetime import date, datetime


DATE_FORMAT = "%Y-%m-%d"


@dataclass
class Product:
    """Продукт с датой окончания срока годности."""

    name: str
    expiration_date: date

    def is_expired(self) -> bool:
        """Проверяет, истёк ли срок годности продукта."""
        return self.expiration_date < date.today()


class Refrigerator:
    """Хранит продукты и управляет ими."""

    def __init__(self) -> None:
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в холодильник."""
        self.products.append(product)

    def remove_product(self, name: str) -> bool:
        """Удаляет первый продукт с указанным названием."""
        for product in self.products:
            if product.name.casefold() == name.casefold():
                self.products.remove(product)
                return True
        return False

    def show_products(self) -> None:
        """Печатает список продуктов и их срок годности."""
        if not self.products:
            print("Холодильник пуст.")
            return

        for product in self.products:
            status = "срок годности истёк" if product.is_expired() else "годен"
            print(
                f"{product.name} — до {product.expiration_date:%d.%m.%Y} "
                f"({status})"
            )


def read_expiration_date() -> date:
    """Запрашивает дату в формате ГГГГ-ММ-ДД."""
    while True:
        value = input("Срок годности (ГГГГ-ММ-ДД): ").strip()
        try:
            return datetime.strptime(value, DATE_FORMAT).date()
        except ValueError:
            print("Введите корректную дату, например 2026-12-31.")


def run() -> None:
    """Запускает меню холодильника."""
    refrigerator = Refrigerator()

    while True:
        print("\nХолодильник")
        print("1. Показать продукты")
        print("2. Добавить продукт")
        print("3. Удалить продукт")
        print("0. Выход")
        choice = input("Выберите действие: ").strip()

        if choice == "1":
            refrigerator.show_products()
        elif choice == "2":
            name = input("Название продукта: ").strip()
            if not name:
                print("Название не может быть пустым.")
                continue
            refrigerator.add_product(Product(name, read_expiration_date()))
            print(f"Продукт «{name}» добавлен.")
        elif choice == "3":
            name = input("Название продукта: ").strip()
            if refrigerator.remove_product(name):
                print(f"Продукт «{name}» удалён.")
            else:
                print("Такого продукта нет в холодильнике.")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неизвестная команда. Выберите пункт из меню.")


if __name__ == "__main__":
    run()
