from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:
    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
        )

    async def execute(
            self,
            command,
            *args,
            fetch: bool = False,
            fetchval: bool = False,
            fetchrow: bool = False,
            execute: bool = False,
    ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    # async def create_table_certificate_data_user(self):
    #     sql = """
    #     CREATE TABLE IF NOT EXISTS certificate_data (
    #     id SERIAL PRIMARY KEY,
    #     full_name VARCHAR(255) NOT NULL,
    #     username varchar(255) NULL,
    #     telegram_id BIGINT NOT NULL UNIQUE
    #     );
    #     """
    #     await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join(
            [f"{item} = ${num}" for num, item in enumerate(parameters.keys(), start=1)]
        )
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = """
            INSERT INTO certificate_data_user (full_name, username, telegram_id, created_at, updated_at)
            VALUES($1, $2, $3, timezone('Asia/Tashkent', now()), timezone('Asia/Tashkent', now()))
            RETURNING *
        """
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)
    async def select_all_certificate_data_user(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)
    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM certificate_data_user WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_certificate_data_user(self):
        sql = "SELECT COUNT(*) FROM certificate_data_user"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE certificate_data_user SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def delete_certificate_data_user(self):
        await self.execute("DELETE FROM certificate_data_user WHERE TRUE", execute=True)

    async def drop_certificate_data_user(self):
        await self.execute("DELETE FROM certificate_data_user;", execute=True)


    ### Mahsulotlar uchun jadval (table) yaratamiz


    # async def create_table_certificates(self):
    #     sql = """
    #     CREATE TABLE IF NOT EXISTS Certificates (
    #         id SERIAL PRIMARY KEY,
    #         telegram_id BIGINT NOT NULL,
    #         ism_familiya VARCHAR(255) NULL,
    #         phone_number BIGINT NULL,
    #         email VARCHAR(255)  NULL,
    #         password VARCHAR(255)  NULL,
    #         certificate_link VARCHAR(255)  NULL,
    #         chek VARCHAR(255) NOT NULL 
    #     );
    #     """
    #     await self.execute(sql, execute=True)

    async def add_product(
    self,
    telegram_id,
    ism_familiya,
    phone_number,
    email,
    password,
    certificate_link,
    chek,
):
        sql = """
            INSERT INTO certificate_data_certificate
                (telegram_id, ism_familiya, phone_number, email, password, certificate_link, chek, created_at, updated_at)
            VALUES ($1, $2, $3, $4, $5, $6, $7, timezone('Asia/Tashkent', now()), timezone('Asia/Tashkent', now()))
            RETURNING *
        """
        return await self.execute(
            sql,
            telegram_id,
            ism_familiya,
            phone_number,
            email,
            password,
            certificate_link,
            chek,
            fetchrow=True,
        )

    async def select_user_certificate(self, **kwargs):
        sql = "SELECT * FROM certificate_data_certificate WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def update_certificate_phone_number(self, phone_number, telegram_id):
        # Convert phone_number to integer
        phone_number = int(phone_number)

        sql = "UPDATE certificate_data_certificate SET phone_number=$1 WHERE telegram_id=$2"
        return await self.execute(sql, phone_number, telegram_id, execute=True)
    async def update_certificate_fullname(self, ism_familiya, chek):
        # Convert phone_number to integer
        sql = "UPDATE certificate_data_certificate SET ism_familiya=$1 WHERE chek=$2"
        return await self.execute(sql, ism_familiya, chek, execute=True)
    async def update_certificate_email(self, email, chek):
        # Convert phone_number to integer
        sql = "UPDATE certificate_data_certificate SET email=$1 WHERE chek=$2"
        return await self.execute(sql, email, chek, execute=True)
    async def update_certificate_password(self, password, chek):
        # Convert phone_number to integer
        sql = "UPDATE certificate_data_certificate SET password=$1 WHERE chek=$2"
        return await self.execute(sql, password, chek, execute=True)
    async def update_certificate_link(self, certificate_link, chek):
        # Convert phone_number to integer
        sql = "UPDATE certificate_data_certificate SET certificate_link=$1 WHERE chek=$2"
        return await self.execute(sql, certificate_link, chek, execute=True)

    async def drop_certificates(self):
        # Drop (delete) all records from the "Certificates" table
        await self.execute("DELETE FROM Certificates;", execute=True)

        # Drop (delete) the entire "Certificates" table
