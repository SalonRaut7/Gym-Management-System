# # import streamlit as st
# # import psycopg2

# # # Function to authenticate user
# # def authenticate(cursor, username, password):
# #     cursor.execute("SELECT * FROM Admins WHERE username = %s AND password = %s", (username, password))
# #     admin = cursor.fetchone()
# #     return admin is not None

# # def admin_login(cursor, username, password):
# #     return authenticate(cursor, username, password)




# # admin_login.py
# import psycopg2

# def admin_login(username, password):
#     try:
#         # Connect to PostgreSQL database
#         conn = psycopg2.connect(
#             dbname='gym',
#             user='postgres',
#             password='kthamalai123',
#             host='localhost',
#             port=5432
#         )

#         cursor = conn.cursor()

#         # Execute query to check user credentials
#         cursor.execute("SELECT * FROM Admins WHERE username = %s AND password = %s", (username, password))
#         user = cursor.fetchone()

#         if user:
#             cursor.close()
#             conn.close()
#             return True
#         else:
#             cursor.close()
#             conn.close()
#             return False

#     except psycopg2.Error as e:
#         print("Error connecting to PostgreSQL database:", e)
#         return False

# admin_login.py

import psycopg2

def admin_login(cursor, username, password):
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            dbname='gym',
            user='postgres',
            password='kthamalai123',
            host='localhost',
            port=5432
        )

        # Execute query to check user credentials
        cursor.execute("SELECT * FROM Admins WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()

        if user:
            return True
        else:
            return False

    except psycopg2.Error as e:
        print("Error connecting to PostgreSQL database:", e)
        return False
    finally:
        # Close database connection
        if 'conn' in locals():
            cursor.close()
            conn.close()