import streamlit as st


st.set_page_config(page_title="Maamoun Chebbi", page_icon=":wave:", layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("assets/images/photo.png")
    
with col2:
    st.title("Hi, I am Maamoun Chebbi")
    content = """ 
    I am Maamoun Chebbi, a passionate and dedicated Junior Software Engineer
    with a strong focus on back-end development. With a background in both
    software engineering and graphic design, I bring a unique 
    blend of creativity and technical expertise to every project I undertake.

    I specialize in developing robust and scalable web applications, leveraging
    a range of technologies including JavaScript, TypeScript, Angular, Node.js,
    and Python. My experience includes building user-friendly interfaces 
    and efficient back-end systems, as well as integrating secure payment 
    solutions and managing complex databases.
    
    In addition to my technical skills, I have a strong foundation in graphic design,
    which allows me to contribute to the visual and user experience 
    aspects of the projects I work on. My design work spans across 
    various mediums, from digital media to print, ensuring that every
    project is visually engaging and aligned with the brand’s identity.

    As I continue to grow in my career, I am excited to take on new challenges,
    collaborate with talented teams, and contribute to impactful projects
    that make a difference. I am always open to new opportunities and connections,
    so feel free to reach out!    
    """
    st.write(content)

st.title("My Portfolio")