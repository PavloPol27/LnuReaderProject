from sqlite3 import connect, Error, OperationalError, Connection


def create_connection(db_file):
    """ Create a database connection to a SQLite database.

     :param db_file: data_base file path. If not exists, db will be created
     :return: Connection object
     """
    try:
        conn = connect(db_file)
    except Error as e:
        raise e
    return conn


def create_table(cursor, create_table_sql):
    """ Create a table from the create_table_sql statement.

    :param cursor: Connection object cursor
    :param create_table_sql: a CREATE TABLE statement
    :return: None
    """
    try:
        cursor.execute(create_table_sql)
    except Error as e:
        raise e


def create_db(connection: Connection):
    """ Create a database with main reader tables.
        Does nothing if tables already exist.

     :param connection: SQLite Connection object
     :return: None
     """
    if not isinstance(connection, Connection):
        raise TypeError("Parameter 'connection' must be SQLite Connection object")
    cursor = connection.cursor()
    sql_create_library_table = """  CREATE TABLE IF NOT EXISTS library(
                                        library_id integer PRIMARY KEY AUTOINCREMENT,
                                        library_name varchar(50)
                                    );"""

    sql_create_book_table = """     CREATE TABLE IF NOT EXISTS book(
                                        file_path text PRIMARY KEY,
                                        file_name text,
                                        author varchar(50),
                                        added Date,
                                        file_stopped_page integer CHECK (file_stopped_page >= 0) DEFAULT 0,
                                        rating integer CHECK (rating >= 0 AND rating <= 10) DEFAULT 0
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


def select_col_names(connection: Connection, table_name):
    """Return column names for chosen table name

    :param connection: SQLite Connection object
    :param table_name: Name of table
    :return: list
    """
    if not isinstance(connection, Connection):
        raise TypeError("Parameter 'connection' must be SQLite Connection object")
    cursor = connection.cursor()
    try:
        cursor.execute(f"PRAGMA table_info({table_name});")
    except Error as e:
        raise e
    fetch_cols = cursor.fetchall()
    if not fetch_cols:
        raise OperationalError(f"no such table: {table_name}")
    else:
        return [x[1] for x in fetch_cols]


def select_all_data(connection: Connection, table_name):
    """Return all data from chosen table in format
        {column name : [column data] }

    :param connection: SQLite Connection object
    :param table_name: Name of table
    :return: dict
    """
    if not isinstance(connection, Connection):
        raise TypeError("Parameter 'connection' must be SQLite Connection object")
    cursor = connection.cursor()
    try:
        cursor.execute(f'SELECT * FROM {table_name}')
    except Error as e:
        raise e
    col_names = select_col_names(connection, table_name)
    all_data = cursor.fetchall()
    arr_data = [[] for _ in range(len(col_names))]
    for row in all_data:
        for i in range(len(row)):
            arr_data[i].append(row[i])
    return dict(zip(col_names, arr_data))


def select_data(connection: Connection, table_name, key):
    """Return one row with key_value = key from chosen table in format
        {column name : column data }

    :param connection: SQLite Connection object
    :param table_name: Name of table
    :param key: Key value of needed row
    :return: dict
    """
    if not isinstance(connection, Connection):
        raise TypeError("Parameter 'connection' must be SQLite Connection object")
    cursor = connection.cursor()

    col_names = select_col_names(connection, table_name)

    try:
        cursor.execute(f'SELECT * FROM {table_name} WHERE {col_names[0]} = ?', [key])
    except Error as e:
        raise e
    fetch_data = cursor.fetchone()
    if not fetch_data:
        return {}
    return dict(zip(col_names, fetch_data))


def insert_data(connection: Connection, table_name, row: tuple):
    """Insert data into table.

    :param connection: SQLite Connection object
    :param table_name: Name of table
    :param row: Data you want to insert into table
                It must be a tuple in corresponding sequence.
    :return: None
    """
    if not isinstance(connection, Connection):
        raise TypeError("Parameter 'connection' must be SQLite Connection object")
    if not isinstance(row, tuple):
        raise TypeError("Parameter 'row' must be tuple")
    cursor = connection.cursor()
    col_names = select_col_names(connection, table_name)
    if col_names[0].endswith('_id'):
        col_names.pop(0)

    str_cols = ', '.join(col_names)
    ques_marks = ['?'] * len(col_names)
    cursor.execute(f"INSERT INTO {table_name} ({str_cols}) VALUES ({','.join(ques_marks)})", row)
    connection.commit()


def update_data(connection: Connection, table_name, data, key):
    """Update data in table by specified key.
    You can update data only in Library, Book, Note tables.
    In Library you can update name
    In Book you can update name
    In Note you can update text of the note

    :param connection: SQLite Connection object
    :param table_name: Name of table
    :param data: New data
    :param key: Key value of needed row
    :return: None
    """
    if not isinstance(connection, Connection):
        raise TypeError("Parameter 'connection' must be SQLite Connection object")
    cursor = connection.cursor()
    col_names = select_col_names(connection, table_name)
    try:
        cursor.execute(f"UPDATE {table_name} SET {col_names[1]} = ? WHERE {col_names[0]} = ?", [data, key])
    except Error as e:
        raise e
    connection.commit()


def delete_data(connection: Connection, table_name, key):
    """Delete data from table by specified key.
    :param connection: SQLite Connection object
    :param table_name: Name of table
    :param key: Key value of needed row
    :return: None
    """
    if not isinstance(connection, Connection):
        raise TypeError("Parameter 'connection' must be SQLite Connection object")
    cursor = connection.cursor()
    key_name = select_col_names(connection, table_name)[0]
    try:
        cursor.execute(f"DELETE FROM {table_name} WHERE {key_name} = ?", [key])
    except Error as e:
        raise e
    connection.commit()
