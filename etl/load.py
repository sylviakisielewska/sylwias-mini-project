import mysql.connector

def load_data_to_mysql(data, host='localhost', user='root', password='root', database='cafe'):
    conn = None  # initialize to avoid UnboundLocalError
    
    try:
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        cursor = conn.cursor()

        insert_query = """
        INSERT INTO products (drink, qty, price, branch, payment_type, datetime)
        VALUES (%s, %s, %s, %s, %s, %s)
        """

        for row in data:
            cursor.execute(insert_query, (
                row['drink'],
                row['qty'],
                row['price'],
                row['branch'],
                row['payment_type'],
                row['datetime']
            ))

        conn.commit()
        print(f"✅ Loaded {cursor.rowcount} rows into the database.")
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
