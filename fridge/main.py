from datetime import date, datetime
from typing import Optional


DATE_FORMAT = "%Y-%m-%d"


class Refrigerator:
    """Хранит продукты в словаре: название и срок годности."""

    def __init__(self) -> None:
        """Создаёт пустой холодильник."""
        self.products: dict[str, date] = {}

    def add_product(self, name: str, expiration_date: date) -> None:
        """Добавляет продукт или обновляет его срок годности.

        Args:
            name: Название продукта.
            expiration_date: Срок годности.
        """
        for product_name in self.products:
            if product_name.casefold() == name.casefold():
                self.products[product_name] = expiration_date
                return

        self.products[name] = expiration_date

    def remove_product(self, number: int) -> bool:
        """Удаляет продукт по его номеру в списке.

        Args:
            number: Номер продукта, начиная с 1.

        Returns:
            True, если продукт удалён, иначе False.
        """
        product_names = list(self.products)
        if number < 1 or number > len(product_names):
            return False

        del self.products[product_names[number - 1]]
        return True

    def show_products(self) -> None:
        """Показывает продукты и их сроки годности."""
        if not self.products:
            print("Холодильник пуст.")
            return

        for number, (name, expiration_date) in enumerate(
            self.products.items(), start=1
        ):
            if expiration_date < date.today():
                status = "срок годности истёк"
            else:
                status = "годен"

            print(
                f"{number}. {name} — до {expiration_date:%d.%m.%Y} "
                f"({status})"
            )


def read_expiration_date() -> Optional[date]:
    """Запрашивает дату срока годности или возвращает None при отмене."""
    while True:
        value = input(
            "Срок годности (ГГГГ-ММ-ДД, 0 — отмена): "
        ).strip()
        if value == "0":
            return None

        try:
            return datetime.strptime(value, DATE_FORMAT).date()
        except ValueError:
            print("Введите дату, например 2026-12-31.")


def add_product_from_input(refrigerator: Refrigerator) -> None:
    """Запрашивает данные продукта и добавляет его в холодильник."""
    name = input("Название продукта (0 — отмена): ").strip()
    if name == "0":
        print("Добавление отменено.")
        return

    if not name:
        print("Название не может быть пустым.")
        return

    expiration_date = read_expiration_date()
    if expiration_date is None:
        print("Добавление отменено.")
        return

    refrigerator.add_product(name, expiration_date)
    print(f"Продукт «{name}» добавлен или обновлён.")


def run() -> None:
    """Показывает меню и выполняет выбранные действия."""
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
            add_product_from_input(refrigerator)
        elif choice == "3":
            refrigerator.show_products()
            if not refrigerator.products:
                continue

            number = input("Введите номер продукта или 0 для отмены: ").strip()
            if number == "0":
                print("Удаление отменено.")
                continue

            try:
                removed = refrigerator.remove_product(int(number))
            except ValueError:
                removed = False

            if removed:
                print("Продукт удалён.")
            else:
                print("Введите номер из списка.")
        elif choice == "0":
            print("До свидания!")
            break
        else:
            print("Неизвестная команда. Выберите пункт из меню.")


if __name__ == "__main__":
    run()
