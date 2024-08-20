import streamlit as st
from email.message import EmailMessage
from send_email import sendEmail  # Ensure this imports your own sendEmail function

st.set_page_config(page_title="Contact", page_icon=":envelope:", layout="wide")

st.markdown("[Github](https://github.com/watch14) 🔍")
st.markdown("[Linkedin](https://www.linkedin.com/in/maamoun-chebbi-a791b3159/) :briefcase:")

with st.form(key='my_form'):
    userEmail = st.text_input("Email")
    message_body = st.text_area("Message")
    file = st.file_uploader("Attach File")
    
    if st.form_submit_button("Send"):
        if not userEmail:
            st.warning("Please enter your email")
        elif not message_body:
            st.warning("Please enter your message")
        else:
            # Create an EmailMessage object
            mail = EmailMessage()
            mail.set_content(message_body)
            mail['Subject'] = 'Email From Portfolio'
            mail['From'] = userEmail
            mail['To'] = 'maamounchebbi@gmail.com'  # Replace with your recipient email

            # Add the file as an attachment to the email
            if file is not None:
                file_content = file.read()
                file_name = file.name
                file_type = file.type.split('/')[1]  # Extract subtype from file type
                mail.add_attachment(file_content, maintype='application', subtype=file_type, filename=file_name)

            # Send the email
            success = sendEmail(mail)
            if success:
                st.success("Email sent successfully ✅")
                st.balloons()
            else:
                st.error("Email not sent. Please check your SMTP configuration and credentials.")
