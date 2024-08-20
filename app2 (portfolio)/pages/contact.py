import streamlit as st
import smtplib
from email.message import EmailMessage


st.set_page_config(page_title="contact", page_icon=":envelope:", layout="wide")


st.markdown("[Github](https://github.com/watch14) 🔍")
st.markdown("[Linkedin](https://www.linkedin.com/in/maamoun-chebbi-a791b3159/) :briefcase:")

st.write(f"Email: chebbimaamoun@gmail.com ✅")


email = st.text_input("Email")
message = st.text_area("Message")
if st.button("Send"):
    # Code to send the email with the message
    # You can use a library like smtplib to send the email
    # Make sure to handle any errors that may occur during the email sending process
    # Here's an example using smtplib:

    msg = EmailMessage()
    msg.set_content(message)

    msg['Subject'] = 'New message from Protfolio contact form'
    msg['From'] = email
    msg['To'] = 'chebbimaamoun@gmail.com'  # Replace with your email address

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login('your-email@example.com', 'your-password')  # Replace with your email and password
            smtp.send_message(msg)
            st.success("Message sent successfully!")
    except Exception as e:
        st.error(f"An error occurred while sending the message: {e}")