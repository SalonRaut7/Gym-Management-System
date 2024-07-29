# # import streamlit as st
# # import psycopg2
# # from admin_interface import render_admin_interface
# # from admin_login import admin_login

# # header_section = st.container()
# # main_section = st.container()
# # login_section = st.container()
# # logout_section = st.container()

# # # Function to establish a database connection
# # def connect_to_database():
# #     try:
# #         # Connect to PostgreSQL database
# #         conn = psycopg2.connect(
# #             dbname='gym',
# #             user='postgres',
# #             password='kthamalai123',
# #             host='localhost',
# #             port=5432
# #         )
# #         return conn
# #     except psycopg2.Error as e:
# #         st.error("Error connecting to PostgreSQL database: {}".format(e))

# # def show_main_page(cursor, conn):
# #     with main_section:
# #         st.title("Gym Management System")  # Title at the top
# #         render_admin_interface(cursor, conn)  # Render the admin interface after successful login

# # def logged_out_clicked():
# #     st.session_state['logged_in'] = False

# # def show_logout_page():
# #     login_section.empty()
# #     with logout_section:
# #         st.button("Log Out", key="logout_button", on_click=logged_out_clicked)  # Unique key for the logout button

# # def logged_in_clicked(username, password, cursor, conn):
# #     if admin_login(cursor, username, password):
# #         st.session_state['logged_in'] = True
# #         show_logout_page()
# #         show_main_page(cursor, conn)  # Call show_main_page after successful login
# #     else:
# #         st.session_state['logged_in'] = False
# #         st.error("Invalid username or password")

# # def show_login_page(cursor, conn):
# #     st.title("Gym Management System")  
# #     st.write("Please log in to access the system.")  
# #     with login_section:
# #         if not st.session_state.get('logged_in', False):
# #             username = st.text_input(label="Username:", value="")
# #             password = st.text_input(label="Password:", value="", type="password")
# #             st.button("Login", on_click=logged_in_clicked, args=(username, password, cursor, conn))

# # def main():
# #     global conn, cursor

# #     conn = connect_to_database()
# #     cursor = conn.cursor()

# #     with header_section:
# #         if 'logged_in' not in st.session_state:
# #             st.session_state['logged_in'] = False
# #             show_login_page(cursor, conn)
# #         else:
# #             if st.session_state['logged_in']:
# #                 show_logout_page()
# #                 show_main_page(cursor, conn)
# #             else:
# #                 show_login_page(cursor, conn)

# # if __name__ == "__main__":
# #     main()




# # import streamlit as st
# # import psycopg2
# # from admin_interface import render_admin_interface
# # from admin_login import admin_login

# # header_section = st.container()
# # main_section = st.container()
# # login_section = st.container()
# # logout_section = st.container()

# # # Function to establish a database connection
# # def connect_to_database():
# #     try:
# #         # Connect to PostgreSQL database
# #         conn = psycopg2.connect(
# #             dbname='gym',
# #             user='postgres',
# #             password='kthamalai123',
# #             host='localhost',
# #             port=5432
# #         )
# #         return conn
# #     except psycopg2.Error as e:
# #         st.error("Error connecting to PostgreSQL database: {}".format(e))

# # def show_main_page(cursor, conn):
# #     with main_section:
# #         st.title("Welcome to Gym Management System")
# #         st.write("Here, you can manage members, plans, salaries, and attendance.")
# #         st.write("")  # Add empty space for better layout
# #         st.write("")  # Add empty space for better layout
# #         render_admin_interface(cursor, conn)  # Render the admin interface

# # def logged_out_clicked():
# #     st.session_state['logged_in'] = False

# # def show_logout_page():
# #     login_section.empty()
# #     with logout_section:
# #         st.button("Log Out", key="logout_button", on_click=logged_out_clicked)

# # def logged_in_clicked(username, password, cursor, conn):
# #     if admin_login(username, password):
# #         st.session_state['logged_in'] = True
# #         show_logout_page()
# #         show_main_page(cursor, conn)  # Call show_main_page after successful login
# #     else:
# #         st.session_state['logged_in'] = False
# #         st.error("Invalid username or password")

# # # def logged_in_clicked(username, password):
# # #     if admin_login(username, password):
# # #         st.session_state['logged_in'] = True
# # #     else:
# # #         st.session_state['logged_in'] = False
# # #         st.error("Invalid username or password")

# # def show_login_page(cursor, conn):
# #     st.title("Welcome to Gym Management System")  
# #     st.write("Please log in to access the system.")  
# #     with login_section:
# #         if not st.session_state.get('logged_in', False):
# #             username = st.text_input(label="Username:", value="")
# #             password = st.text_input(label="Password:", value="", type="password")
# #             st.button("Login", on_click=logged_in_clicked, args=(username, password, cursor, conn))

# # def main():
# #     global conn, cursor

# #     conn = connect_to_database()
# #     cursor = conn.cursor()

# #     with header_section:
# #         if 'logged_in' not in st.session_state:
# #             st.session_state['logged_in'] = False
# #             show_login_page(cursor, conn)
# #         else:
# #             if st.session_state['logged_in']:
# #                 show_logout_page()
# #                 show_main_page(cursor, conn)
# #             else:
# #                 show_login_page(cursor, conn)

# # if __name__ == "__main__":
# #     main()
    
# import streamlit as st
# import psycopg2
# from admin_interface import render_admin_interface
# from admin_login import admin_login

# header_section = st.container()
# main_section = st.container()
# login_section = st.container()
# logout_section = st.container()

# # Function to establish a database connection
# def connect_to_database():
#     try:
#         # Connect to PostgreSQL database
#         conn = psycopg2.connect(
#             dbname='gym',
#             user='postgres',
#             password='kthamalai123',
#             host='localhost',
#             port=5432
#         )
#         return conn
#     except psycopg2.Error as e:
#         st.error("Error connecting to PostgreSQL database: {}".format(e))

# def show_main_page():
#     with main_section:
#         st.title("Welcome to GYM Management System")  # Title at the top
#         st.write("Here, you can manage members, see plans, update and delete members.")
#         st.write("")  # Add empty space for better layout
#         st.write("")  # Add empty space for better layout
#         render_admin_interface(cursor, conn)  # Render the admin interface after successful login

# def logged_out_clicked():
#     st.session_state['logged_in'] = False

# def show_logout_page():
#     login_section.empty()
#     with logout_section:
#         st.button("Log Out", key="logout", on_click=logged_out_clicked)

# def logged_in_clicked(username, password):
#     if admin_login(cursor, username, password):
#         st.session_state['logged_in'] = True
#     else:
#         st.session_state['logged_in'] = False
#         st.error("Invalid username or password")

# def show_login_page():
#     st.title("Welcome to GYM Management System")  
#     st.write("Please log in to access the system.")  
#     with login_section:
#         if not st.session_state.get('logged_in', False):
#             username = st.text_input(label="Username:", value="")
#             password = st.text_input(label="Password:", value="", type="password")
#             st.button("Login", on_click=logged_in_clicked, args=(username, password))


# def main():
#     global conn, cursor

#     conn = connect_to_database()
#     cursor = conn.cursor()

#     with header_section:
#         if 'logged_in' not in st.session_state:
#             st.session_state['logged_in'] = False
#             show_login_page()
#         else:
#             if st.session_state['logged_in']:
#                 show_logout_page()
#                 show_main_page()  # Call show_main_page after successful login
#             else:
#                 show_login_page()

# if __name__ == "__main__":
#     main()


#yo last ko code...
# import streamlit as st
# import psycopg2
# from admin_interface import render_admin_interface
# from admin_login import admin_login
# from member_interface import show_member_page, member_signup_page, show_signup_success_page
# from member_functions import member_login

# header_section = st.container()
# main_section = st.container()
# login_section = st.container()
# logout_section = st.container()

# # Function to establish a database connection
# def connect_to_database():
#     try:
#         # Connect to PostgreSQL database
#         conn = psycopg2.connect(
#             dbname='gym',
#             user='postgres',
#             password='kthamalai123',
#             host='localhost',
#             port=5432
#         )
#         return conn
#     except psycopg2.Error as e:
#         st.error("Error connecting to PostgreSQL database: {}".format(e))
#         return None

# def show_main_page():
#     with main_section:
#         st.title("Welcome to GYM Management System")
#         st.write("Here, you can manage members, see plans, update and delete members.")
#         render_admin_interface(cursor, conn)

# def logged_out_clicked():
#     st.session_state['logged_in'] = False
#     if 'member_id' in st.session_state:
#         del st.session_state['member_id']

# def show_logout_page():
#     login_section.empty()
#     with logout_section:
#         st.button("Log Out", key="logout", on_click=logged_out_clicked)

# def admin_logged_in_clicked(username, password):
#     if admin_login(cursor, username, password):
#         st.session_state['logged_in'] = True
#     else:
#         st.error("Invalid admin username or password")

# def member_logged_in_clicked(username, password):
#     member_id = member_login(cursor, username, password)
#     if member_id:
#         st.session_state['logged_in'] = True
#         st.session_state['member_id'] = member_id
#     else:
#         st.error("Invalid member username or password")

# # def show_login_page():
# #     with login_section:
# #         if not st.session_state.get('logged_in', False):
# #             user_type = st.radio("Login as", ["Admin", "Member"])
# #             username = st.text_input("Username")
# #             password = st.text_input("Password", type="password")
# #             if user_type == "Admin":
# #                 st.button("Login as Admin", on_click=admin_logged_in_clicked, args=(username, password))
# #             else:
# #                 st.button("Login as Member", on_click=member_logged_in_clicked, args=(username, password))
# #                 st.write("Not a member?")
# #                 if st.button("Sign Up"):
# #                     member_signup_page(cursor, conn)
# def show_login_page():
#     with login_section:
#         if not st.session_state.get('logged_in', False):
#             user_type = st.radio("Login as", ["Admin", "Member"])
#             username = st.text_input("Username")
#             password = st.text_input("Password", type="password")
#             if user_type == "Admin":
#                 st.button("Login as Admin", on_click=admin_logged_in_clicked, args=(username, password))
#             else:
#                 st.button("Login as Member", on_click=member_logged_in_clicked, args=(username, password))
#                 st.write("Not a member?")
#                 if st.button("Sign Up"):
#                     st.session_state['show_signup'] = True

# # Check for the show_signup state outside of the login_section container
#                 if st.session_state.get('show_signup', False):
#                     member_signup_page(cursor, conn)

                    

# # def main():
# #     global conn, cursor

# #     conn = connect_to_database()
# #     if conn is not None:
# #         cursor = conn.cursor()

# #         with header_section:
# #             if 'logged_in' not in st.session_state:
# #                 st.session_state['logged_in'] = False
# #                 show_login_page()
# #             elif st.session_state['logged_in']:
# #                 show_logout_page()
# #                 if 'member_id' in st.session_state:
# #                     show_member_page(cursor, st.session_state['member_id'])
# #                 elif 'signup_success' in st.session_state and st.session_state['signup_success']:
# #                     # Display signup success page with user details
# #                     show_signup_success_page(st.session_state['member_id'], st.session_state['username'], st.session_state['password'])
# #                 else:
# #                     show_main_page()
# #             else:
# #                 show_login_page()
# def main():
#     global conn, cursor

#     conn = connect_to_database()
#     if conn is not None:
#         cursor = conn.cursor()

#         with header_section:
#             if 'logged_in' not in st.session_state:
#                 st.session_state['logged_in'] = False
#                 show_login_page()
#                 if st.session_state.get('show_signup', False):
#                     member_signup_page(cursor, conn)
#             else:
#                 if st.session_state['logged_in']:
#                     show_logout_page()
#                     if 'member_id' in st.session_state:
#                         show_member_page(cursor, st.session_state['member_id'])
#                     else:
#                         show_main_page()
#                 else:
#                     show_login_page()

# if __name__ == "__main__":
#     main()


#thik thik code
# import streamlit as st
# import psycopg2
# from admin_interface import render_admin_interface
# from admin_login import admin_login
# from member_interface import show_member_page, member_signup_page
# from member_functions import member_login

# header_section = st.container()
# main_section = st.container()
# login_section = st.container()
# logout_section = st.container()

# # Function to establish a database connection
# def connect_to_database():
#     try:
#         # Connect to PostgreSQL database
#         conn = psycopg2.connect(
#             dbname='gym',
#             user='postgres',
#             password='kthamalai123',
#             host='localhost',
#             port=5432
#         )
#         return conn
#     except psycopg2.Error as e:
#         st.error("Error connecting to PostgreSQL database: {}".format(e))
#         return None

# def show_main_page():
#     with main_section:
#         st.title("Welcome to GYM Management System")
#         st.write("Here, you can manage members, see plans, update and delete members.")
#         render_admin_interface(cursor, conn)

# # def logged_out_clicked():
# #     st.session_state['logged_in'] = False
# #     if 'member_id' in st.session_state:
# #         del st.session_state['member_id']
# def logged_out_clicked():
#     st.session_state['logged_in'] = False
#     if 'member_id' in st.session_state:
#         del st.session_state['member_id']
#     st.session_state['page'] = 'login'  # Reset the page state to login


# def show_logout_page():
#     login_section.empty()
#     with logout_section:
#         st.button("Log Out", key="logout", on_click=logged_out_clicked)

# def admin_logged_in_clicked(username, password):
#     if admin_login(cursor, username, password):
#         st.session_state['logged_in'] = True
#         st.session_state['page'] = 'main'
#     else:
#         st.error("Invalid admin username or password")

# def member_logged_in_clicked(username, password):
#     member_id = member_login(cursor, username, password)
#     if member_id:
#         st.session_state['logged_in'] = True
#         st.session_state['member_id'] = member_id
#         st.session_state['page'] = 'member'
#     else:
#         st.error("Invalid member username or password")

# def show_login_page():
#     with login_section:
#         if not st.session_state.get('logged_in', False):
#             user_type = st.radio("Login as", ["Admin", "Member"])
#             username = st.text_input("Username")
#             password = st.text_input("Password", type="password")
#             if user_type == "Admin":
#                 st.button("Login as Admin", on_click=admin_logged_in_clicked, args=(username, password))
#             else:
#                 st.button("Login as Member", on_click=member_logged_in_clicked, args=(username, password))
#                 st.write("Not a member?")
#                 # Move the signup button outside the form
#                 if st.button("Sign Up"):
#                     st.session_state['page'] = 'signup'


# def main():
#     global conn, cursor

#     conn = connect_to_database()
#     if conn is not None:
#         cursor = conn.cursor()

#         with header_section:
#             if 'logged_in' not in st.session_state:
#                 st.session_state['logged_in'] = False
#                 st.session_state['page'] = 'login'  # Initialize the page key here
            
#             if st.session_state.get('page') == 'login':  # Use get() to avoid KeyError
#                 show_login_page()
#             elif st.session_state.get('page') == 'signup':
#                 member_signup_page(cursor, conn)
#             elif st.session_state.get('page') == 'main':
#                 show_main_page()
#                 show_logout_page()
#             elif st.session_state.get('page') == 'member':
#                 show_member_page(cursor, st.session_state['member_id'])
#                 show_logout_page()


# if __name__ == "__main__":
#     main()


import streamlit as st
import psycopg2
from admin_interface import render_admin_interface
from admin_login import admin_login
from member_interface import show_member_page, member_signup_page
from member_functions import member_login

header_section = st.container()
main_section = st.container()
login_section = st.container()
logout_section = st.container()

# Function to establish a database connection
def connect_to_database():
    try:
        # Connect to PostgreSQL database
        conn = psycopg2.connect(
            dbname='gym',
            user='postgres',
            password='kthamalai123',
            host='localhost',
            port=5432
        )
        return conn
    except psycopg2.Error as e:
        st.error("Error connecting to PostgreSQL database: {}".format(e))
        return None

def show_main_page():
    with main_section:
        st.title("Welcome to GYM Management System")
        st.write("Here, you can manage members, see plans, update and delete members.")
        render_admin_interface(cursor, conn)

def logged_out_clicked():
    st.session_state['logged_in'] = False
    if 'member_id' in st.session_state:
        del st.session_state['member_id']
    update_page_state('login')

def show_logout_page():
    login_section.empty()
    with logout_section:
        st.button("Log Out", key="logout", on_click=logged_out_clicked)

def admin_logged_in_clicked(username, password):
    if admin_login(cursor, username, password):
        st.session_state['logged_in'] = True
        update_page_state('main')
    else:
        st.error("Invalid admin username or password")

def member_logged_in_clicked(username, password):
    member_id = member_login(cursor, username, password)
    if member_id:
        st.session_state['logged_in'] = True
        st.session_state['member_id'] = member_id
        update_page_state('member')
    else:
        st.error("Invalid member username or password")

def show_login_page():
    with login_section:
        if not st.session_state.get('logged_in', False):
            user_type = st.radio("Login as", ["Admin", "Member"])
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            if user_type == "Admin":
                st.button("Login as Admin", on_click=admin_logged_in_clicked, args=(username, password))
            else:
                st.button("Login as Member", on_click=member_logged_in_clicked, args=(username, password))
                st.write("Not a member?")
                st.button("Sign Up", on_click=update_page_state, args=('signup',))

# def update_page_state(new_page):
#     st.session_state['page'] = new_page
def update_page_state(new_page):
    st.session_state['page'] = new_page
    if new_page != 'signup':
        st.session_state['show_signup'] = False


def reset_page_state():
    st.session_state['page'] = 'login'
    if 'signup_success' in st.session_state:
        del st.session_state['signup_success']

def main():
    global conn, cursor

    conn = connect_to_database()
    if conn is not None:
        cursor = conn.cursor()

        with header_section:
            if 'logged_in' not in st.session_state:
                st.session_state['logged_in'] = False
                st.session_state['page'] = 'login'
            
            if st.session_state.get('page') == 'login':
                show_login_page()
            elif st.session_state.get('page') == 'signup':
                member_signup_page(cursor, conn)
            elif st.session_state.get('page') == 'main':
                show_main_page()
                show_logout_page()
            elif st.session_state.get('page') == 'member':
                show_member_page(cursor, st.session_state['member_id'])
                show_logout_page()

if __name__ == "__main__":
    main()

