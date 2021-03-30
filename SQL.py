from sqlite3 import connect, Error

db_path = r'C:\Users\Max\source\sql_test.db'
table_names = [
    'library', 'book', 'books_in_libraries', 'bookmark', 'note'
]


def create_connection(db_file: str):
    """ create a database connection to a SQLite database
     :db_file: data_base file path. If not exists, db will be created.
     : return: Connection object
     """
    conn = None
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)
    return conn


def create_table(cursor, create_table_sql: str):
    """ create a table from the create_table_sql statement
    : param cursor: Connection object cursor
    : param create_table_sql: a CREATE TABLE statement
    : return:
    """
    try:
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)


def create_db(db_file: str):
    """ create a database with main reader tables.
        Does nothing if tables already exist.
     :db_file: data_base file path. If not exists, db will be created.
     : return:
     """
    try:
        conn = create_connection(db_file)
    except Error as e:
        print(e)
        return
    cursor = conn.cursor()
    sql_create_library_table = """  CREATE TABLE IF NOT EXISTS library(
                                        library_id integer PRIMARY KEY AUTOINCREMENT,
                                        library_name varchar(50)
                                    );"""

    sql_create_book_table = """     CREATE TABLE IF NOT EXISTS book(
                                        file_path text PRIMARY KEY,
                                        file_name text,
                                        author varchar(50),
                                        genre varchar(100),
                                        published Date,
                                        file_stopped_page integer CHECK (file_stopped_page >= 0) DEFAULT 0
                                    );"""

    sql_create_book_lib_table = """  CREATE TABLE IF NOT EXISTS books_in_libraries(
                                        link_id integer PRIMARY KEY AUTOINCREMENT,
                                        library_id integer REFERENCES library,
                                        file_path text REFERENCES book
                                    );"""

    sql_create_note_table = """      CREATE TABLE IF NOT EXISTS note(
                                        note_id integer PRIMARY KEY AUTOINCREMENT,
                                        note_text text,
                                        note_page integer CHECK (note_page >= 0),
                                        note_line integer,
                                        note_book_path text REFERENCES book
                                    );"""

    sql_create_bookmark_table = """ CREATE TABLE IF NOT EXISTS bookmark(
                                        bookmark_id integer PRIMARY KEY AUTOINCREMENT,
                                        bookmark_page integer CHECK (bookmark_page >= 0),
                                        bookmark_book_path text REFERENCES book
                                    );"""

    create_table(cursor, sql_create_library_table)
    create_table(cursor, sql_create_book_table)
    create_table(cursor, sql_create_book_lib_table)
    create_table(cursor, sql_create_note_table)
    create_table(cursor, sql_create_bookmark_table)
    conn.close()


def insert_data(db_file, table_name, row=tuple()):
    try:
        conn = connect(db_file)
    except Error as e:
        print(e)
        return
    cursor = conn.cursor()
    try:
        cursor.execute(f'select * from {table_name}')
    except Error as e:
        print(e)
        return

    col_names = list(map(lambda x: x[0], cursor.description))
    if col_names[0].endswith('_id'):
        col_names.pop(0)

    str_cols = ', '.join(col_names)
    ques_marks = ['?'] * len(col_names)
    cursor.execute(f"INSERT INTO {table_name} ({str_cols}) VALUES ({','.join(ques_marks)})", row)
    conn.commit()
    conn.close()


insert_data(db_path, 'library', ('2',))
print(1)
