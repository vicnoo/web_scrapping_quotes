# import sqlite3
# conn = sqlite3.connect('myQuotes.db')
# curr = conn.cursor()
# # curr.execute("""CREATE TABLE quotes_tb(
# #             title text
# #             ,author text
# #             ,tag text
# #             )""")
# curr.execute(""" INSERT INTO quotes_tb VALUES ('Python is awesome','building with python', 'python')""")
# conn.commit()
# conn.close()