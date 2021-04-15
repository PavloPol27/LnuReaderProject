import sqlite3
import unittest
import database as db
import os.path
from sqlite3 import Connection, Error


class TestConnection(unittest.TestCase):
    def setUp(self) -> None:
        self.real_path = r'C:\Users\Max\source\sql_test.db'
        self.unreal_path = r'D:\something'
        self.int_path = 1
        self.float_path = 2.5

    def test_str_path(self):
        self.assertTrue(Connection, db.create_connection(self.real_path))
        with self.assertRaises(Error):
            db.create_connection(self.unreal_path)

    def test_num_path(self):
        with self.assertRaises(TypeError):
            db.create_connection(self.int_path)
            db.create_connection(self.float_path)


class TestCreating(unittest.TestCase):
    def setUp(self) -> None:
        self.file_path = r'C:\Users\Max\source\sql_test.db'
        self.conn = db.create_connection(self.file_path)
        self.str_conn = 'Something'
        self.int_conn = 1

    def test_creating(self):
        creating = db.create_db(self.conn)
        self.assertTrue(creating is None)
        self.assertTrue(os.path.exists(self.file_path))


class TestSelect(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = db.create_connection(r'C:\Users\Max\source\sql_test.db')
        self.real_table_name = 'library'
        self.empty_table_name = 'bookmark'
        self.unreal_table_name = 'magazine'
        self.int_table_name = 1

        self.real_key = 2
        self.unreal_key = 228

    def test_select_cols(self):
        cols = db.select_col_names(self.conn, self.real_table_name)
        self.assertTrue(isinstance(cols, list))
        self.assertFalse(not cols)
        with self.assertRaises(sqlite3.OperationalError):
            db.select_col_names(self.conn, self.unreal_table_name)
            db.select_col_names(self.conn, self.int_table_name)

    def test_select_all(self):
        data = db.select_all_data(self.conn, self.real_table_name)
        self.assertTrue(isinstance(data, dict))
        self.assertFalse(not data)
        with self.assertRaises(Error):
            db.select_all_data(self.conn, self.unreal_table_name)
            db.select_all_data(self.conn, self.int_table_name)

    def test_select(self):
        data = db.select_data(self.conn, self.real_table_name, self.real_key)
        empty_data = db.select_data(self.conn, self.real_table_name, self.unreal_key)
        self.assertTrue(isinstance(data, dict))
        self.assertFalse(not data)
        self.assertEqual(data['library_id'], 2)
        self.assertTrue(not empty_data)

        with self.assertRaises(Error):
            db.select_data(self.conn, self.int_table_name, self.real_key)
            db.select_data(self.conn, self.unreal_table_name, self.real_key)


class TestInsert(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = db.create_connection(r'C:\Users\Max\source\sql_test.db')
        self.table_name = 'library'
        self.unreal_table_name = 'magazine'
        self.insert_data = ('name1',)
        self.inserted_int = 1
        self.inserted_dict = {"s": 2}

    def test_insert(self):
        len_before_insert = len(db.select_all_data(self.conn, self.table_name)['library_id'])
        inserting = db.insert_data(self.conn, self.table_name, self.insert_data)
        self.assertTrue(inserting is None)
        len_after_insert = len(db.select_all_data(self.conn, self.table_name)['library_id'])
        self.assertTrue(len_after_insert == len_before_insert + 1)
        with self.assertRaises(Error):
            db.insert_data(self.conn, self.unreal_table_name, self.insert_data)


class TestUpdate(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = db.create_connection(r'C:\Users\Max\source\sql_test.db')
        self.table_name = 'library'
        self.updated = 'updated'
        self.key = db.select_all_data(self.conn, self.table_name)['library_id'][-1]

    def test_update(self):
        old_value = db.select_all_data(self.conn, self.table_name)['library_name'][-1]
        update = db.update_data(self.conn, self.table_name, self.updated, self.key)
        new_value = db.select_all_data(self.conn, self.table_name)['library_name'][-1]
        self.assertTrue(update is None)
        self.assertTrue(old_value != new_value)
        self.assertTrue(new_value == self.updated)
        db.update_data(self.conn, self.table_name, old_value, self.key)

        with self.assertRaises(Error):
            db.update_data(self.conn, 'invalid table', self.updated, self.key)
            db.update_data(self.conn, self.table_name, {'dict': 5}, self.key)


class TestDelete(unittest.TestCase):
    def setUp(self) -> None:
        self.conn = db.create_connection(r'C:\Users\Max\source\sql_test.db')
        self.table_name = 'book'
        self.deleted_key = 'str1'
        self.deleted_val = 'str2'

    def test_delete(self):
        db.insert_data(self.conn, self.table_name, (self.deleted_key, self.deleted_val, '', '', '', ''))
        delete = db.delete_data(self.conn, self.table_name, self.deleted_key)
        self.assertTrue(delete is None)
        after_deleting = db.select_data(self.conn, self.table_name, self.deleted_key)
        self.assertTrue(not after_deleting)

        with self.assertRaises(Error):
            db.delete_data(self.conn, 'invalid table', self.deleted_key)
            db.delete_data(self.conn, self.table_name, {'invalid': 'key'})
            db.delete_data(self.conn, self.table_name, 228)


if __name__ == "__main__":
    unittest.main()
