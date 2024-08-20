import streamlit as st
from email.message import EmailMessage
from send_email import sendEmail

st.set_page_config(page_title="Contact", page_icon=":envelope:", layout="wide")

st.markdown("[Github](https://github.com/watch14) 🔍")
st.markdown("[Linkedin](https://www.linkedin.com/in/maamoun-chebbi-a791b3159/) :briefcase:")

with st.form(key='my_form'):
    userEmail = st.text_input("Email")
    message = st.text_area("Message")
    file = st.file_uploader("Attach File")
    
    mail = f"""\
Subject: Email From Portfolio

    From: {userEmail}

    {message}
    """
    
    if st.form_submit_button("Send"):
        if not userEmail:
            st.warning("Please enter your email")
        elif not message:
            st.warning("Please enter your message")

        else:    # Add the file as an attachment to the email
            if file is not None:
                file_content = file.read()
                file_name = file.name
                file_type = file.type
                mail.add_attachment(file_content, maintype='application', subtype=file_type, filename=file_name)

            # Send the email
            try:
                sendEmail(mail)
                st.success("Email sent successfully ✅")
                st.balloons()
            except Exception as e:
                st.error(f"Email not sent. Error: {str(e)}")
