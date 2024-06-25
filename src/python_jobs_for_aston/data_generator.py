import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from faker import Faker


class DataGenerator:

    def __init__(
        self,
        num_clients: int = 10000,
        max_transactions_per_client: int = 150,
        max_securities_per_client: int = 15,
        num_securities: int = 100,
    ):
        self.fake = Faker()
        # Параметры генерации данных
        self.num_clients = num_clients
        self.max_transactions_per_client = max_transactions_per_client
        self.max_securities_per_client = max_securities_per_client
        self.start_date = datetime.now() - timedelta(days=365)
        self.end_date = datetime.now()
        self.num_securities = num_securities

    # Функция для генерации случайной даты и времени
    def random_date(self, start, end):
        return start + timedelta(
            seconds=random.randint(0, int((end - start).total_seconds())),
        )

    # Генерация данных для операций с ценными бумагами
    def generate_security_transactions(self):
        security_data = []

        for client_id in range(1, self.num_clients + 1):
            num_securities = random.randint(1, self.max_securities_per_client)
            for _ in range(num_securities):
                transaction_date = self.random_date(
                    self.start_date, self.end_date
                )
                currency = np.random.choice(["USD", "RUB"])
                price = (
                    round(np.random.uniform(50, 500), 2)
                    if currency == "USD"
                    else round(np.random.uniform(4500, 45000), 2)
                )

                security_data.append(
                    {
                        "client_id": client_id,
                        "security_id": np.random.randint(100, 200),
                        "transaction_date": transaction_date,
                        "transaction_type": np.random.choice(["buy", "sell"]),
                        "quantity": np.random.randint(1, 100),
                        "currency": currency,
                        "price": price,
                    }
                )

        security_df = pd.DataFrame(security_data)
        security_df.to_csv("data/security_transactions.csv", index=False)

    # Генерация данных для банковских транзакций
    def generate_bank_transactions(self):
        transaction_data = []
        for client_id in range(1, self.num_clients + 1):
            num_transactions = random.randint(
                1, self.max_transactions_per_client
            )
            for _ in range(num_transactions):
                transaction_date = self.random_date(
                    self.start_date, self.end_date
                )
                currency = np.random.choice(["USD", "RUB"])
                amount = (
                    round(np.random.uniform(100, 10000), 2)
                    if currency == "USD"
                    else round(np.random.uniform(9000, 900000), 2)
                )

                # Добавление аномально больших сумм
                if random.random() < 0.01:
                    amount *= 10

                transaction_data.append(
                    {
                        "client_id": client_id,
                        "transaction_id": np.random.randint(1000, 10000),
                        "transaction_date": transaction_date,
                        "transaction_type": np.random.choice(
                            ["deposit", "withdrawal", "transfer"]
                        ),
                        "account_number": self.fake.iban(),
                        "currency": currency,
                        "amount": amount,
                    }
                )

        # Добавление аномально большого количества транзакций в один из дней для 3-4 клиентов
        anomalous_clients = random.sample(range(1, self.num_clients + 1), 4)
        for client_id in anomalous_clients:
            anomalous_dates = [
                self.random_date(self.start_date, self.end_date)
                for _ in range(2)
            ]
            for date in anomalous_dates:
                for _ in range(
                    100
                ):  # Аномально большое количество транзакций в один день
                    transaction_data.append(
                        {
                            "client_id": client_id,
                            "transaction_id": np.random.randint(1000, 10000),
                            "transaction_date": date,
                            "transaction_type": np.random.choice(
                                ["deposit", "withdrawal", "transfer"]
                            ),
                            "account_number": self.fake.iban(),
                            "currency": np.random.choice(["USD", "RUB"]),
                            "amount": round(np.random.uniform(100, 10000), 2),
                        }
                    )

        transaction_df = pd.DataFrame(transaction_data)
        transaction_df.to_csv("data/bank_transactions.csv", index=False)

    # Генерация данных для клиентов
    def generate_clients(self):
        # Параметры генерации данных
        num_clients = 10000

        client_data = []
        for client_id in range(1, num_clients + 1):
            client_data.append(
                {
                    "client_id": client_id,
                    "client_name": self.fake.name(),
                    "client_email": self.fake.email(),
                    "client_phone": self.fake.phone_number(),
                    "client_address": self.fake.address().replace("\n", " "),
                }
            )

        client_df = pd.DataFrame(client_data)
        client_df.to_csv("data/clients.csv", index=False)

    # Генерация данных для ценных бумаг
    def generate_securities(self):

        security_data = []
        security_types = ["stock", "bond"]
        markets = ["NYSE", "NASDAQ", "LSE"]

        for security_id in range(100, 100 + self.num_securities):
            security_data.append(
                {
                    "security_id": security_id,
                    "security_name": self.fake.company(),
                    "security_type": np.random.choice(security_types),
                    "market": np.random.choice(markets),
                }
            )

        security_df = pd.DataFrame(security_data)
        security_df.to_csv("data/securities.csv", index=False)


data_generator = DataGenerator()

generator_map = {
    "security_transactions.csv": data_generator.generate_security_transactions,
    "clients.csv": data_generator.generate_clients,
    "securities.csv": data_generator.generate_securities,
    "bank_transactions.csv": data_generator.generate_security_transactions,
}