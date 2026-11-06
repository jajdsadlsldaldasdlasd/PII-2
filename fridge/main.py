"""Учёт продуктов в холодильнике."""

from datetime import date, datetime


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

    def remove_product(self, name: str) -> bool:
        """Удаляет первый продукт с таким названием.

        Названия сравниваются без учёта регистра.

        Args:
            name: Название продукта.

        Returns:
            True, если продукт удалён, иначе False.
        """
        for product_name in self.products:
            if product_name.casefold() == name.casefold():
                del self.products[product_name]
                return True
        return False

    def show_products(self) -> None:
        """Показывает продукты и их сроки годности."""
        if not self.products:
            print("Холодильник пуст.")
            return

        for name, expiration_date in self.products.items():
            if expiration_date < date.today():
                status = "срок годности истёк"
            else:
                status = "годен"

            print(
                f"{name} — до {expiration_date:%d.%m.%Y} "
                f"({status})"
            )


def read_expiration_date() -> date:
    """Запрашивает дату в формате ГГГГ-ММ-ДД."""
    while True:
        value = input("Срок годности (ГГГГ-ММ-ДД): ").strip()
        try:
            return datetime.strptime(value, DATE_FORMAT).date()
        except ValueError:
            print("Введите дату, например 2026-12-31.")


def add_product_from_input(refrigerator: Refrigerator) -> None:
    """Запрашивает данные продукта и добавляет его в холодильник."""
    name = input("Название продукта: ").strip()
    if not name:
        print("Название не может быть пустым.")
        return

    expiration_date = read_expiration_date()
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
