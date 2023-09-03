import sqlite3
import csv

DATABASE_NAME = 'reagent_stocktaking.db'

def create_table():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reagent (
            cas_no TEXT PRIMARY KEY,
            name_substance TEXT NOT NULL,
            total_g FLOAT NOT NULL,
            class_substance TEXT NOT NULL,
            location TEXT NOT NULL,
            descrip TEXT NOT NULL,
            molecular_weight FLOAT NOT NULL,
            molecular_formula TEXT NOT NULL       
        )
    ''')

    conn.commit()
    conn.close()

def upload_sql(obj):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute('''
                INSERT or REPLACE INTO reagent (cas_no, name_substance, total_g, class_substance, location, descrip, molecular_weight, molecular_weight)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (obj['cas_no'], obj['name_substance'], obj['total_g'], obj['class_substance'], obj['location'], obj['descrip'], obj['molecular_weight'], obj['molecular_weight'], obj['molecular_formula']))
    conn.commit()
    conn.close()


def import_csv_data():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    with open('table.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            print(row)
            cursor.execute('''
                INSERT or IGNORE INTO reagent (cas_no, name_substance, total_g, class_substance, location, descrip, molecular_weight, molecular_formula)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (row['cas_no'], row['name_substance'], row['total_g'], row['class_substance'], row['location'], row['descrip'], row['molecular_weight'], row['molecular_formula'],))

    conn.commit()
    conn.close()


# функция запрос. Вывести реагент из таблицы , с таким то ключом

def search_by_key_sql(cas_no):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM reagent WHERE cas_no = ?''', (cas_no,))

    rows = cursor.fetchall()

    conn.commit()
    conn.close()
    return rows

def search_by_class_substance_sql(class_substance):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM reagent WHERE class_substance = ?''', (class_substance,))

    rows = cursor.fetchall()

    conn.commit()
    conn.close()
    print(rows)
    return rows

def search_by_name_substance_sql(name_substance):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM reagent WHERE LOWER(name_substance) = LOWER(?)''', (name_substance,))

    rows = cursor.fetchall()

    conn.commit()
    conn.close()
    print(rows)
    return rows

def change_mass_by_cas_sql(cas_no, delta_g):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(f"UPDATE reagent SET total_g = total_g + ? WHERE cas_no = ?", (delta_g, cas_no,))
    print(delta_g)
    conn.commit()
    conn.close()

def delete_record_by_key_sql(cas_no):
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reagent WHERE cas_no = ?", (cas_no,))
    conn.commit()
    conn.close()
