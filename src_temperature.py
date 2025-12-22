# код функции/класса
def celsius_to_fahrenheit(celsius: float) -> float:
    # Конвертирует градусы Цельсия в Фаренгейт
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    # Конвертирует градусы Фаренгейт в Цельсий
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius: float) -> float:
    # Конвертирует градусы Цельсия в Кельвины
    return celsius + 273.15
