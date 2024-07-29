import streamlit as st
import psycopg2

# Function to retrieve all members from the database
def view_members(cursor):
    cursor.execute("SELECT * FROM Members")
    members = cursor.fetchall()
    return members

# Function to retrieve all available plans from the database
def view_plans(cursor):
    cursor.execute("SELECT * FROM Plans")
    plans = cursor.fetchall()
    return plans

# Function to add a new member to the database
def add_member(cursor, conn, first_name, last_name, email, phone, address, date_of_birth, plan_id):
    try:
        cursor.execute("INSERT INTO Members (first_name, last_name, email, phone, address, date_of_birth, date_joined, plan_id) VALUES (%s, %s, %s, %s, %s, %s, CURRENT_DATE, %s)",
                (first_name, last_name, email, phone, address, date_of_birth, plan_id))
        conn.commit()
        st.success("Member added successfully!")
    except psycopg2.Error as e:
        st.error("Error adding member: {}".format(e))

# Function to update an existing member in the database
def update_member(cursor, conn, member_id, first_name, last_name, email, phone, address, date_of_birth, plan_id):
    try:
        cursor.execute("UPDATE Members SET first_name = %s, last_name = %s, email = %s, phone = %s, address = %s, date_of_birth = %s, plan_id = %s WHERE member_id = %s",
                (first_name, last_name, email, phone, address, date_of_birth, plan_id, member_id))
        conn.commit()
        st.success("Member updated successfully!")
    except psycopg2.Error as e:
        st.error("Error updating member: {}".format(e))

# Function to delete a member from the database
def delete_member(cursor, conn, member_id):
    try:
        cursor.execute("DELETE FROM MemberCredentials WHERE member_id = %s", (member_id,))
        cursor.execute("DELETE FROM Members WHERE member_id = %s", (member_id,))
        conn.commit()
        st.success("Member deleted successfully!")
    except psycopg2.Error as e:
        st.error("Error deleting member: {}".format(e))
        


def render_admin_interface(cursor, conn):
    # st.subheader("Admin Interface")   
    st.sidebar.subheader("Admin Interface")

    # Options for admin
    options = ["View Members", "Add Member", "Update Member", "View Plans", "Delete Member"]
    choice = st.sidebar.selectbox("Select Option", options)

    # View members
    if choice == "View Members":
        st.subheader("View Members")
        members = view_members(cursor)
        for member in members:
            st.write("Member ID:", member[0])
            st.write("First Name:", member[1])
            st.write("Last Name:", member[2])
            st.write("Email:", member[3])
            st.write("Phone:", member[4])
            st.write("Address:", member[5])
            st.write("Date of Birth:", member[6])
            st.write("Date Joined:", member[7])
            st.write("Plan ID:", member[8])
            st.write("-"*30)
    # Add member
    elif choice == "Add Member":
        st.subheader("Add Member")
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        address = st.text_input("Address")
        date_of_birth = st.date_input("Date of Birth")

        # Retrieve available plans
        plans = view_plans(cursor)
        plan_names = [plan[1] for plan in plans]
        selected_plan_name = st.selectbox("Select Plan", plan_names)

        # Get the ID of the selected plan
        selected_plan_id = None
        for plan in plans:
            if plan[1] == selected_plan_name:
                selected_plan_id = plan[0]
                break

        if st.button("Add Member"):
            add_member(cursor, conn, first_name, last_name, email, phone, address, date_of_birth, selected_plan_id)

    # Update member
    elif choice == "Update Member":
        st.subheader("Update Member")
        member_id_update = st.number_input("Enter Member ID to Update")
        if member_id_update:
            member_to_update = None
            members = view_members(cursor)
            for member in members:
                if member[0] == member_id_update:
                    member_to_update = member
                    break
            if member_to_update:
                first_name = st.text_input("First Name", value=member_to_update[1])
                last_name = st.text_input("Last Name", value=member_to_update[2])
                email = st.text_input("Email", value=member_to_update[3])
                phone = st.text_input("Phone", value=member_to_update[4])
                address = st.text_input("Address", value=member_to_update[5])
                date_of_birth = st.date_input("Date of Birth", value=member_to_update[6])

                # Retrieve available plans
                plans = view_plans(cursor)
                plan_names = [plan[1] for plan in plans]
                selected_plan_name = st.selectbox("Select Plan", plan_names, index=member_to_update[8] - 1)

                # Get the ID of the selected plan
                selected_plan_id = None
                for plan in plans:
                    if plan[1] == selected_plan_name:
                        selected_plan_id = plan[0]
                        break

                if st.button("Update Member"):
                    update_member(cursor, conn, member_id_update, first_name, last_name, email, phone, address, date_of_birth, selected_plan_id)

    # View plans
    elif choice == "View Plans":
        st.subheader("View Plans")
        plans = view_plans(cursor)
        for plan in plans:
            st.write("Plan ID:", plan[0])
            st.write("Plan Name:", plan[1])
            st.write("Plan Cost:", plan[2])
            st.write("-" * 30)

    # Delete member
    elif choice == "Delete Member":
        st.subheader("Delete Member")
        member_id_delete = st.number_input("Enter Member ID to Delete")
        if st.button("Delete Member"):
            delete_member(cursor, conn ,member_id_delete)

