class CustomError(Exception):
    """Базовый класс для других исключений"""
    pass

class ContractNotFound(CustomError):
    """Вызывается, когда контракт не найден"""
    def __init__(self, message="Контракт не найден!"):
        self.message = message
        super().__init__(self.message)

class InvalidPrivateKey(CustomError):
    """Вызывается, когда приватный ключ недействителен"""
    def __init__(self, message="Недействительный приватный ключ!"):
        self.message = message
        super().__init__(self.message)

class TransactionError(CustomError):
    """Вызывается, когда происходит ошибка в транзакции"""
    def __init__(self, message="Ошибка транзакции!"):
        self.message = message
        super().__init__(self.message)
