# import streamlit as st
# from member_functions import view_plans, member_signup

# def show_member_page(cursor, member_id):
#     st.subheader("Member Page")
#     cursor.execute("SELECT * FROM Members WHERE member_id = %s", (member_id,))
#     member = cursor.fetchone()
#     if member:
#         st.write(f"Welcome, {member[1]} {member[2]}")
#         st.write(f"Email: {member[3]}")
#         st.write(f"Phone: {member[4]}")
#         st.write(f"Address: {member[5]}")
#         st.write(f"Date of Birth: {member[6]}")
#         st.write(f"Date Joined: {member[7]}")
#         st.write(f"Plan ID: {member[8]}")
#     st.subheader("Available Plans")
#     plans = view_plans(cursor)
#     for plan in plans:
#         st.write(f"Plan ID: {plan[0]}")
#         st.write(f"Plan Name: {plan[1]}")
#         st.write(f"Plan Cost: {plan[2]}")
#         st.write("-" * 30)
        
        
# # def member_signup_page(cursor, conn):
# #     with st.form("member_signup_form"):
# #         st.write("Member Sign Up")
# #         member_id = st.number_input("Member ID", min_value=1, step=1)
# #         username = st.text_input("Username")
# #         password = st.text_input("Password", type="password")
# #         submit_button = st.form_submit_button("Sign Up")
# #         if submit_button:
# #             if member_signup(cursor, conn, int(member_id), username, password):
# #                 # Set session state for signup success and user details
# #                 st.session_state['signup_success'] = True
# #                 st.session_state['member_id'] = member_id
# #                 st.session_state['username'] = username
# #                 st.session_state['password'] = password
# def member_signup_page(cursor, conn):
#     with st.form("member_signup_form"):
#         st.write("Member Sign Up")
#         member_id = st.number_input("Member ID", min_value=1, step=1)
#         username = st.text_input("Username")
#         password = st.text_input("Password", type="password")
#         submit_button = st.form_submit_button("Sign Up")
#         if submit_button:
#             if member_signup(cursor, conn, int(member_id), username, password):
#                 st.session_state['signup_success'] = True
#                 st.session_state['member_id'] = member_id
#                 st.session_state['username'] = username
#                 st.session_state['password'] = password

#     # Back button
#     if st.button("Back"):
#         st.session_state['page'] = 'login'

            
            
# def show_signup_success_page(member_id, username, password):
#     st.subheader("Signup Successful")
#     st.write("Your account has been created successfully. Here are your details:")
#     st.write(f"Member ID: {member_id}")
#     st.write(f"Username: {username}")
#     st.write(f"Password: {password}")
#     st.write("Please note down your credentials for future login.")


#ramro wala:
import streamlit as st
from member_functions import view_plans, member_signup

def show_member_page(cursor, member_id):
    st.subheader("Member Page")
    cursor.execute("SELECT * FROM Members WHERE member_id = %s", (member_id,))
    member = cursor.fetchone()
    # Sidebar for member options
    st.sidebar.title("Member Sidebar")
    selected_option = st.sidebar.radio("Select an option", ["View Plans", "View Information"])

    if selected_option == "View Plans":
        st.subheader("Available Plans")
        plans = view_plans(cursor)
        for plan in plans:
            st.write(f"Plan ID: {plan[0]}")
            st.write(f"Plan Name: {plan[1]}")
            st.write(f"Plan Cost: {plan[2]}")
            st.write("-" * 30)
    elif selected_option == "View Information":
        st.subheader("Member Information")
        st.write(f"Name: {member[1]} {member[2]}")
        st.write(f"Email: {member[3]}")
        st.write(f"Phone: {member[4]}")
        st.write(f"Address: {member[5]}")
        st.write(f"Date of Birth: {member[6]}")
        st.write(f"Date Joined: {member[7]}")
        st.write(f"Plan ID: {member[8]}")


def member_signup_page(cursor, conn):
    with st.form("member_signup_form"):
        st.write("Member Sign Up")
        member_id = st.number_input("Member ID", min_value=1, step=1)
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit_button = st.form_submit_button("Sign Up")
        if submit_button:
            if member_signup(cursor, conn, int(member_id), username, password):
                st.session_state['signup_success'] = True
                st.session_state['member_id'] = member_id
                st.session_state['username'] = username
                st.session_state['password'] = password

    # Back button
    if st.button("Back"):
        st.session_state['page'] = 'login'
        return  # Return early to prevent further execution of the function

    # Reset the signup state if the back button is not clicked
    if not st.session_state.get('page') == 'login':
        st.session_state['signup_success'] = False



