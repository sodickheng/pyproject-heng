# example.db
import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert data
c.execute("INSERT INTO users (name, age) VALUES ('Steve', 32)")
c.execute("INSERT INTO users (name, age) VALUES ('Alfred', 23)")

# Commit the changes
conn.commit()

# Retrieve data
c.execute("SELECT * FROM users")
rows = c.fetchall()
for row in rows:
    print(row)

# Update data
c.execute("UPDATE users SET age = 99 WHERE name = 'Alfred'")
conn.commit()

# Delete data
c.execute("DELETE FROM users WHERE name = 'Steve'")
conn.commit()

# Close the connection
conn.close()
