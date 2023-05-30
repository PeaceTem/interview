import psycopg2
# use virtual environment


# Establishing a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    port="your_port",
    database="your_database",
    user="your_username",
    password="your_password"
)

# Creating a cursor object to execute SQL statements
cur = conn.cursor()

# Example: Inserting data into a table
try:
    # Creating the table if it doesn't exist
    cur.execute("CREATE TABLE IF NOT EXISTS employees (id SERIAL PRIMARY KEY, name VARCHAR, age INTEGER)")
    
    # Inserting a new row into the table
    insert_query = "INSERT INTO employees (name, age) VALUES (%s, %s)"
    data = ("John Doe", 30)
    cur.execute(insert_query, data)
    
    # Committing the transaction
    conn.commit()
    
    print("Data inserted successfully!")

except (Exception, psycopg2.DatabaseError) as error:
    print("Error occurred:", error)

finally:
    # Closing the cursor and connection
    if cur:
        cur.close()
    if conn:
        conn.close()
