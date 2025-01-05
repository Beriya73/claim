import asyncio
import logging
from client import Client
from config import DROP_ABI, DROP_MANAGER_CONTRACT
from termcolor import colored
from web3 import AsyncWeb3, AsyncHTTPProvider
from custom_exception import *

# Настройка логирования
file_log = logging.FileHandler('claim.log', encoding='utf-8')
console_out = logging.StreamHandler()
logging.basicConfig(handlers=(file_log, console_out),
                    level=logging.INFO,
                    format="%(asctime)s %(levelname)s %(message)s")

class Claim(Client):
    """
    Класс для взаимодействия с контрактом Claim.

    Атрибуты:
        private_key (str): Приватный ключ для Ethereum аккаунта.
        proxy (str): Прокси для HTTP запросов.
        chain_name (str): Имя сети.
        chain_id (int): ID сети.
        explorer_url (str): URL блокчейн эксплорера.
        rpc_url (str): URL RPC эндпоинта.
        eip_1559 (bool): Использовать ли EIP-1559 транзакции.
        w3 (AsyncWeb3): Экземпляр Web3.
        address (str): Ethereum адрес, полученный из приватного ключа.
        drop_contract (Contract): Контракт для взаимодействия.
    """

    def __init__(self, private_key, proxy):
        """
        Инициализирует экземпляр Claim.

        Аргументы:
            private_key (str): Приватный ключ для Ethereum аккаунта.
            proxy (str): Прокси для HTTP запросов.
        """
        self.private_key = private_key
        request_kwargs = {'proxy': f'http://{proxy}'}
        self.chain_name = "Arbitrum One"
        self.chain_id = 42161
        self.explorer_url = "https://arbiscan.io/"
        self.rpc_url = "https://arbitrum.llamarpc.com"
        self.eip_1559 = True

        try:
            self.w3 = AsyncWeb3(AsyncHTTPProvider(self.rpc_url, request_kwargs=request_kwargs))
            self.address = self.w3.to_checksum_address(self.w3.eth.account.from_key(self.private_key).address)
        except Exception as er:
            logging.error(f"{er}")
            raise InvalidPrivateKey(f"Недействительный приватный ключ! {er}")

        self.drop_contract = self.get_contract(contract_address=DROP_MANAGER_CONTRACT, abi=DROP_ABI)

    async def registration(self):
        """
        Регистрирует пользователя в контракте.

        Возвращает:
            str: Хэш транзакции регистрации.
        """
        try:
            register_transaction = await self.drop_contract.functions.register().build_transaction(await self.prepare_tx())
            logging.info(f'Make approve for {DROP_MANAGER_CONTRACT}')
            return await self.send_transaction(register_transaction)
        except Exception as e:
            logging.error(f"Ошибка при регистрации: {e}")
            raise TransactionError(f"Ошибка при регистрации: {e}")

    async def check_registration(self):
        """
        Проверяет, зарегистрирован ли пользователь.

        Возвращает:
            bool: True, если пользователь зарегистрирован, иначе False.
        """
        try:
            return await self.drop_contract.functions.registeredUsers(self.address).call()
        except Exception as e:
            logging.error(f"Ошибка при проверке регистрации: {e}")
            raise TransactionError(f"Ошибка при проверке регистрации: {e}")

    async def get_claimbale_tokens(self):
        """
        Получает количество токенов, доступных для клейма.

        Возвращает:
            int: Количество токенов, доступных для клейма.
        """
        try:
            tokens_left = await self.drop_contract.functions.claimableTokens(self.address).call()
            return tokens_left
        except Exception as e:
            logging.error(f"Ошибка при получении доступных токенов: {e}")
            raise TransactionError(f"Ошибка при получении доступных токенов: {e}")

    async def claim_tokens(self, amount):
        """
        Клеймит указанное количество токенов.

        Аргументы:
            amount (int): Количество токенов для клейма.

        Возвращает:
            str: Хэш транзакции клейма.
        """
        try:
            claim_transaction = await self.drop_contract.functions.claim(amount).build_transaction(await self.prepare_tx())
            logging.info(f'П{DROP_MANAGER_CONTRACT}')
            return await self.send_transaction(claim_transaction)
        except Exception as e:
            logging.error(f"Ошибка при клейме токенов: {e}")
            raise TransactionError(f"Ошибка при клейме токенов: {e}")

async def main():
    """
    Основная функция для взаимодействия с пользователем и контрактом Claim.
    """
    proxy = ""
    private_key = input(colored("Введите свой private key: ", 'light_green'))
    claim = Claim(private_key, proxy)

    while True:
        try:
            if await claim.check_registration():
                count_tokens = await claim.get_claimbale_tokens()
                logging.info(f"У вас осталось {int(count_tokens / 10**18)} токенов для клейма")
                if count_tokens == 0:
                    logging.warning("У вас не осталось токенов! Выходим")
                    break
            else:
                logging.warning(f"Ваш адрес {claim.address}, не зарегистрирован")
                logging.info(f"Регистрирую в контракте!")
                await claim.registration()
                await asyncio.sleep(5)
                logging.info(f"Вы зарегистрированы!")
                continue

            while True:
                try:
                    quantity = int(input("Введите количество токенов для клейма (Если 0, выйти из программы): ")) * 10**18
                    if quantity == 0:
                        exit(0)
                    elif quantity > count_tokens:
                        logging.warning("Введеное значение превышает количество оставшихся токенов!")
                        continue
                    elif quantity < 0:
                        logging.warning("Введеное значение меньше 0!")
                        continue
                    logging.info(f"Делаю клейм...")
                    await claim.claim_tokens(quantity)
                    break
                except ValueError:
                    logging.error("Некорректный символ, введите еще раз")
        except Exception as e:
            logging.error(f"Ошибка в основном цикле: {e}")
            raise

# Запуск основной функции
asyncio.run(main())
