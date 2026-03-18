import psycopg2

conn = psycopg2.connect(
    dbname = 'test_w10',
    user = 'pp2',
    password = 'pp2123',
    host = 'localhost',
    port='5432'
)


# try: 
#     cur = conn.cursor()
#     cur.execute("""
#                 CREATE TABLE IF NOT EXIST Users (
#                     id SERIAL PRIMARY KEY,
#                     name VARCHAR(128),
#                     email VARCHAR(128)
#                 );
#                 """)
#     conn.commit()
#     cur.close()
#     conn.close()
# except Exception as e:
#     print(e) 

name = input('Enter name: ')
email = input('Enter email: ')

try: 
    cur = conn.cursor()
    cur.execute(f"""
                INSERT INTO Users (id, name, email) VALUES ('3', '{name}', '{email}');
                """)
    conn.commit()

    # print(res)
    cur.close()
    conn.close()
except Exception as e:
    print(e) 

    
try: 
    cur = conn.cursor()
    cur.execute("""
                SELECT * FROM Users
                ;
                """)
    res = cur.fetchall()
    conn.commit()

    print(res)
    cur.close()
    conn.close()
except Exception as e:
    print(e) 