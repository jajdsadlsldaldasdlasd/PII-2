from datetime import datetime


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
        return f"«{self.title}», {self.author} ({self.year} г.)"

    # Магические методы __str__ и __eq__
    def __str__(self) -> str:
        return self.info()

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return (
            self.title == other.title
            and self.author == other.author
            and self.year == other.year
        )

    # Свойство для возраста книги с декораторами (@property и сеттер)
    @property
    def age(self) -> int:
        """Вычисляет возраст книги на основе текущего года"""
        return datetime.now().year - self.year

    @age.setter
    def age(self, value: int):
        """Устанавливает год издания на основе переданного возраста"""
        if value < 0:
            raise ValueError("Возраст книги не может быть отрицательным")
        self.year = datetime.now().year - value

    # Классовый метод для создания книги из строки
    @classmethod
    def from_string(cls, book_str: str, sep: str = ","):
        """
        Создает экземпляр Book из строки формата:
        "Название, Автор, Год"
        """
        parts = [part.strip() for part in book_str.split(sep)]
        if len(parts) != 3:
            raise ValueError("Строка должна содержать: Название, Автор, Год")

        title, author, year_str = parts
        return cls(title=title, author=author, year=int(year_str))



# Проверка __str__
book1 = Book("1984", "Джордж Оруэлл", 1949)
print(book1)  
# Вывод: «1984», Джордж Оруэлл (1949 г.)

# Проверка классового метода from_string
book2 = Book.from_string("1984, Джордж Оруэлл, 1949")
print(book2)  
# Вывод: «1984», Джордж Оруэлл (1949 г.)

# Проверка __eq__
print(book1 == book2)  # True

# Проверка @property (чтение возраста)
print(f"Возраст книги: {book1.age} лет")

# Проверка @age.setter (изменение года через возраст)
book1.age = 10
print(f"Новый год издания: {book1.year}")  # текущий_год - 10