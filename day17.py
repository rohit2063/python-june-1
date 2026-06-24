import mysql.connector

db = mysql.connector.connect(
    user ="root",
    host ="localhost",
    password ="",
    database = "python-june-1"
)
terminal = db.cursor()
# Insert query
# insert = "INSERT INTO student (name, address,phone) VALUES('Rohit', 'dang', '980');"
# terminal.execute(insert)
# db.commit()
# print(db)

# Select query
# query = "Select * from student"
# terminal.execute(query)

# result = terminal.fetchall()
# print(result)
# for i in result:
#     print(i)


# Fetch one student
query = "SELECT * FROM student WHERE name = %s"
value = ("Rohit Ghimire",)

terminal.execute(query, value)

result = terminal.fetchone()
print(result)

print("=============================")

# Update student
query = "UPDATE Student SET address = %s, phone = %s WHERE name = %s"
values = ("sindupalchowk", "9800000000", "Rohit Ghimire")

terminal.execute(query, values)
db.commit()

print("Record updated successfully")

print(f"{terminal.rowcount} record(s) updated")
print("=============================")

# Delete student
query = "DELETE FROM Student WHERE name = %s"
value = ("Rohit Ghimire",)

terminal.execute(query, value)
db.commit()

print("Record deleted successfully")
print(f"{terminal.rowcount} record(s) deleted")

print("=============================")

terminal.close()
db.close()