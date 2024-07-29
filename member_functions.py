import psycopg2
import streamlit as st

def view_plans(cursor):
    cursor.execute("SELECT * FROM Plans")
    plans = cursor.fetchall()
    return plans

def member_login(cursor, username, password):
    cursor.execute("SELECT member_id FROM MemberCredentials WHERE username = %s AND password = %s", (username, password))
    member = cursor.fetchone()
    return member[0] if member else None

def member_signup(cursor, conn, member_id, username, password):
    try:
        cursor.execute("SELECT * FROM Members WHERE member_id = %s", (member_id,))
        if cursor.fetchone() is None:
            st.error("Member ID does not exist. Please provide a valid Member ID.")
            return False

        cursor.execute("SELECT * FROM MemberCredentials WHERE username = %s", (username,))
        if cursor.fetchone() is not None:
            st.error("Username already exists. Please choose a different username.")
            return False

        cursor.execute("INSERT INTO MemberCredentials (member_id, username, password) VALUES (%s, %s, %s)", (member_id, username, password))
        conn.commit()
        st.success("Member signed up successfully!")
        st.session_state['show_signup'] = False  # Reset the signup state
        return True
    except psycopg2.Error as e:
        conn.rollback()
        st.error(f"Error signing up member: {e}")
        return False
