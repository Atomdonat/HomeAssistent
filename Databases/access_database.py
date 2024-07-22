import sqlite3
import json


# class JsonDatabase:
#     def __init__(self, database_file: str) -> None:
#         self.database = sqlite3.connect(database_file)
#         self.cursor = self.database.cursor()
#         self.initialize_tables()
#
#     def initialize_tables(self) -> None:
#         create_table_query = f"""
#             CREATE TABLE IF NOT EXISTS '' (
#                 'ID' TEXT PRIMARY KEY,
#                 'Name' TEXT,
#                 'Match' TEXT,
#                 'Execute' TEXT
#             )
#         """
#         self.cursor.execute(create_table_query)
#         self.database.commit()
#
#     def add_json_to_table(self, json_file_path: str | None = None, json_data: dict | None = None) -> None:
#         if json_file_path is not None:
#             with open(json_file_path, 'r') as file:
#                 json_data = json.load(file)
#
#         sql_command = f"""
#             INSERT INTO '{json_data['type']}'(
#                 'ID',
#                 'Name',
#                 'Match',
#                 'Execute'
#             )
#             VALUES(?,?,?,?)
#         """
#         if json_data['type'] != 'user':
#             sql_values = (
#                 json_data['id'],
#                 json_data['name'],
#                 json.dumps(json_data),
#                 False
#             )
#         else:
#             sql_values = (
#                 json_data['id'],
#                 json_data['display_name'],
#                 json.dumps(json_data),
#                 False
#             )
#
#         with self.database:
#             # only new instances will be added, due to the uniqueness of the IDs.
#             # Otherwise, the error will be caught
#             try:
#                 self.cursor.execute(sql_command, sql_values)
#                 # print(f"\n Committed \'{json_data['name']}\' to Table {json_data['type']}. \n")
#
#             except Exception as e:
#                 if e is not None:
#                     print(e)
#                 # else:
#                 # print(f"\n \'{json_data['name']}\' is already known. \n")
#
#             finally:
#                 # noinspection PyStatementEffect
#                 self.cursor.lastrowid
#                 self.database.commit()
#
#     def get_json_from_table(self, table_name: str, item_id: str) -> dict:
#         cursor = self.database.execute(f'SELECT * from {table_name} WHERE ID = ?', (item_id,))
#         json_data = cursor.fetchone()[2]
#         json_data = json.loads(json_data)
#         return json_data
#

if __name__ == '__main__':
