import streamlit as st

# Set page configuration
st.set_page_config(page_title="Personal Portfolio", page_icon=":briefcase:", layout="wide")


# Home Section
def home():
    st.title("Welcome to My Portfolio!")
    st.image("fazal.jpeg", width=200)
    st.subheader("Data Analyst | Data Scientist | Power BI | Python | Web Scraping | C++")
    st.write(
        """ 
I am currently pursuing a Bachelor's degree at the University of Central Punjab, with a strong focus on programming, data science, data analysis, and developing user-friendly applications. With a passion for turning data into actionable insights and creating intuitive digital solutions, I have successfully completed several projects that showcase my technical skills and creativity.Explore my portfolio to learn more about my expertise, view my projects, and find out how we can connect. I look forward to collaborating with you!
"""
    )
    
    
    st.markdown("<h2 style='text-align: center;'>Socials</h2>", unsafe_allow_html=True)

    # Custom HTML and CSS for Social Buttons
    st.markdown(
        """
        <style>
        .social-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .social-buttons a {
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
        }
        .facebook { background-color: #4267B2; }
        .linkedin { background-color: #0077B5; }
        .instagram { background-color: #E1306C; }
        .Email { background-color: #1DA1F2; }
        </style>
        <div class="social-buttons">
            <a href="https://facebook.com/profile.php?id=100054048482305" target="_blank" class="facebook">Facebook</a>
            <a href="www.linkedin.com/in/fazalelahi-programmer" target="_blank" class="linkedin">LinkedIn</a>
            <a href="https://instagram.com/f.elahi1767/profilecard/?igsh=MXBhbHY3eGNwY3BpaA==" target="_blank" class="instagram">Instagram</a>
            <a href="https://mail.google.com/mail/u/0/#inbox" target="_blank" class="Email">Email</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# About Me Section
def about_me():
    st.header("About Me")
    st.write(
        """
        Aspiring Data Scientist with strong skillset in Python programming, data manipulation, and machine learning. Specializing in data science and predictive modeling, delivering efficient solutions and actionable recommendations. Completed multiple high quality projects which helped me to grow logical , creative thinking and understanding of technical skills importance. I also have experienced with MySQL for relational database management and querying.
        My expertise are in programming, data science, Mysql, and data analysis and web scraping like beautiful soup and scrapy.
        """
    )
    st.write("## Education")
    st.write("- Bachelor's in Data Science, University of Central Punjab (2022 - 2026)")
    st.write("- Intermediate in Computer Science, KIPS College (2022)")
    st.write("- Matriculation in Computer Science, Dvisional Public School (2020)")
    
    st.write("## Expertise")
    st.write("- Backend Development (Python, C++)")
    st.write("- Data Analysis (Pandas, NumPy, SQL)")
    st.write("- Data Visualization (Matplotlib, Seaborn, Power BI)")
    st.write("- Machine Learning (Scikit-learn)")
    st.write("- Web Scraping (Beautiful Soup, Scrapy)")
    
    st.write("## Languages")
    st.write("- English")
    st.write("- Urdu")
    st.markdown("<h2 style='text-align: center;'>Socials</h2>", unsafe_allow_html=True)

    # Custom HTML and CSS for Social Buttons
    st.markdown(
        """
        <style>
        .social-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .social-buttons a {
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
        }
        .facebook { background-color: #4267B2; }
        .linkedin { background-color: #0077B5; }
        .instagram { background-color: #E1306C; }
        .Email { background-color: #1DA1F2; }
        </style>
        <div class="social-buttons">
            <a href="https://facebook.com/profile.php?id=100054048482305" target="_blank" class="facebook">Facebook</a>
            <a href="www.linkedin.com/in/fazalelahi-programmer" target="_blank" class="linkedin">LinkedIn</a>
            <a href="https://instagram.com/f.elahi1767/profilecard/?igsh=MXBhbHY3eGNwY3BpaA==" target="_blank" class="instagram">Instagram</a>
            <a href="https://mail.google.com/mail/u/0/#inbox" target="_blank" class="Email">Email</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

def projects():
    # Define project details
    project_data = [
        {
            "title": "Airline Passenger Sales Analysis",
            "description": "Real-time dashboard optimizing sales and operational performance.",
            "image": "airline.jpeg", 
            "details": """
            **Process:**
            - It analyzes the sales of airline passenger consumer prices.
            - Performed data handling and data manipulation to make data formatted and find meaningful insights form the data.
            - Performed statstical analysis on the data to fulfill business requirements.
            - Visualization has been added to understand the sales and make informed and meaningful decisions. 
            
            **Technologies:** Python, Pandas, Matplotlib, Seaborn
            """,
            "extra_info": "- **Project link**: [Source Code](https://drive.google.com/file/d/11Umw_AfehR_aHLxRH4AAKVSa2nddYN7m/view?usp=drive_link)"
            
        },
        {
            "title": "Interactive Sales Dashboard using Knime",
            "description": "A interactive sales dashboard for acheiving business goals.",
            "image": "download.jpeg",  
            "details": """
                **Process:**
                - This project involved extracting data from various sources, transforming it into a suitable format, and loading it into a data warehouse for analysis. 
                - The data was then visualized using Knime to create an interactive dashboard that allows users to explore the data and gain insights in real time. 
                - The dashboard includes various visualizations such as bar charts, line graphs, and pie charts to help users understand the data and make informed decisions.
                
                **Technologies:** Knime
            """,
            "extra_info": "- **Project link**: [Source Code](https://drive.google.com/file/d/1CAGm-buirOlAs_GRqh3-CevP1S1_ukxm/view?usp=drive_link)"
        },
        {
            "title": "Data Analysis for Stock Sales ",
            "description": "Analyze the stock sales data to make informed decisions.",
            "image": "stock.jpeg",  
            "details": """
            **Process:**
            - Stock market analysis performed on different companies to find the best company performed in stock market.
            - Data handling and data manipulation has been performed to make data formatted and find meaningful insights form the data.
            - Machine learning model has been added to predict the future stock price. 
            - visualization has been added to understand the sales and make informed and meaningful decision.
            
            **Technologies:** Python, Pandas, Matplotlib, Seaborn, Scikit-learn
            """,
            "extra_info": "- **Project link**: [Source Code](https://drive.google.com/file/d/1_WdAk1XEYbz1aeGoZVGhBS04ZVTYIPZW/view?usp=drive_link)"
        },
    ]

    if "current_project" not in st.session_state:
        st.session_state.current_project = None

    if st.session_state.current_project is None:
        st.title("Projects")

        cols = st.columns(3)

        with cols[0]:
            st.image(project_data[0]["image"], use_column_width=True, caption="Airline Passenger Sales Analysis")
            st.subheader(project_data[0]["title"])
            st.write(project_data[0]["description"])
            if st.button("View Details", key="view_0"):
                st.session_state.current_project = 0

        # Second project in the second column
        with cols[1]:
            st.image(project_data[1]["image"], use_column_width=True, caption="Interactive Sales Dashboard using Knime")
            st.subheader(project_data[1]["title"])
            st.write(project_data[1]["description"])
            if st.button("View Details", key="view_1"):
                st.session_state.current_project = 1

        # Third project in the third column
        with cols[2]:
            st.image(project_data[2]["image"], use_column_width=True, caption="Data Analysis for Stock Sales")
            st.subheader(project_data[2]["title"])
            st.write(project_data[2]["description"])
            if st.button("View Details", key="view_2"):
                st.session_state.current_project = 2

    else:
        project_index = st.session_state.current_project
        project = project_data[project_index]

        st.title(project["title"])
        st.image(project["image"], use_column_width=True)
        st.write(project["details"])

        if "extra_info" in project:
            st.write(project["extra_info"])

        if st.button("Back to Projects"):
            st.session_state.current_project = None



def certificates():
    st.header("Certificates")
    
    # Example certificates
    certificates_data = [
        {
            "title": "Cloud Explorer with Microsoft Technologies Certificate",
            "issuer": "Microsoft Leran",
            "link": "https://drive.google.com/file/d/1reD51iRaxG_X9jmEL6euTWuQVS2xjITo/view?usp=drive_link"
        },
        {
            "title": "Machine Learning",
            "issuer": "Udemy",
            "link": "https://drive.google.com/file/d/1xmMBxN5exaRXWo3lETS-jvPFU0dffjgS/view?usp=drive_link"
        },
        {
            "title": "MS Excel VBA Certification",
            "issuer": "Udemy",
            "link": "https://drive.google.com/file/d/1yQzqXniUkBL3DQ-QOqWJNLwMI_c2USb_/view?usp=drive_link"
        }
    ]
    
    for cert in certificates_data:
        st.write(f"### {cert['title']}")
        st.write(f"**Issuer:** {cert['issuer']}")
        st.write(f"[View Certificate]({cert['link']})")

    st.markdown("<h2 style='text-align: center;'>Socials</h2>", unsafe_allow_html=True)

    # Custom HTML and CSS for Social Buttons
    st.markdown(
        """
        <style>
        .social-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .social-buttons a {
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
        }
        .facebook { background-color: #4267B2; }
        .linkedin { background-color: #0077B5; }
        .instagram { background-color: #E1306C; }
        .Email { background-color: #1DA1F2; }
        </style>
        <div class="social-buttons">
            <a href="https://facebook.com/profile.php?id=100054048482305" target="_blank" class="facebook">Facebook</a>
            <a href="www.linkedin.com/in/fazalelahi-programmer" target="_blank" class="linkedin">LinkedIn</a>
            <a href="https://instagram.com/f.elahi1767/profilecard/?igsh=MXBhbHY3eGNwY3BpaA==" target="_blank" class="instagram">Instagram</a>
            <a href="https://mail.google.com/mail/u/0/#inbox" target="_blank" class="Email">Email</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
# Skills Section
def skills():
    st.header("Technical Skills")
    skills_data = {
        "Python": 90,
        "DSA": 80,
        "OOP": 75,
        "SQL": 70,
        "Data Analytics": 85,
        "Web Scraping": 80,
        "Power BI": 75,
        "C++": 85
    }
    
    for skill, level in skills_data.items():
        st.write(f"{skill}")
        st.progress(level / 100)
    
    st.write("-------------")
    st.subheader("Soft Skills")
    st.write("- Communication")
    st.write("- Problem Solving")
    st.write("- Teamwork")
    st.write("- Time Management")
    st.write("- Creativity")

    st.markdown("<h2 style='text-align: center;'>Socials</h2>", unsafe_allow_html=True)

    # Custom HTML and CSS for Social Buttons
    st.markdown(
        """
        <style>
        .social-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .social-buttons a {
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
        }
        .facebook { background-color: #4267B2; }
        .linkedin { background-color: #0077B5; }
        .instagram { background-color: #E1306C; }
        .Email { background-color: #1DA1F2; }
        </style>
        <div class="social-buttons">
            <a href="https://facebook.com/profile.php?id=100054048482305" target="_blank" class="facebook">Facebook</a>
            <a href="www.linkedin.com/in/fazalelahi-programmer" target="_blank" class="linkedin">LinkedIn</a>
            <a href="https://instagram.com/f.elahi1767/profilecard/?igsh=MXBhbHY3eGNwY3BpaA==" target="_blank" class="instagram">Instagram</a>
            <a href="https://mail.google.com/mail/u/0/#inbox" target="_blank" class="Email">Email</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Contact Section
def contact():

    st.markdown("""
    <style>
        .contact {
            background-color: #f0f0f5;
            padding: 20px;
            border-radius: 10px;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)
# User needs to fill the form to contact me
    st.header("Contact Me")
    with st.form("Contact Form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.success("Thank you for reaching out! I'll get back to you soon.")

    st.markdown('</section>', unsafe_allow_html=True)

    st.markdown("<h2 style='text-align: center;'>Socials</h2>", unsafe_allow_html=True)

    # Custom HTML and CSS for Social Buttons
    st.markdown(
        """
        <style>
        .social-buttons {
            display: flex;
            justify-content: center;
            gap: 10px;
        }
        .social-buttons a {
            text-decoration: none;
            padding: 10px 20px;
            border-radius: 5px;
            color: white;
            font-weight: bold;
        }
        .facebook { background-color: #4267B2; }
        .linkedin { background-color: #0077B5; }
        .instagram { background-color: #E1306C; }
        .Email { background-color: #1DA1F2; }
        </style>
        <div class="social-buttons">
            <a href="https://facebook.com/profile.php?id=100054048482305" target="_blank" class="facebook">Facebook</a>
            <a href="www.linkedin.com/in/fazalelahi-programmer" target="_blank" class="linkedin">LinkedIn</a>
            <a href="https://instagram.com/f.elahi1767/profilecard/?igsh=MXBhbHY3eGNwY3BpaA==" target="_blank" class="instagram">Instagram</a>
            <a href="https://mail.google.com/mail/u/0/#inbox" target="_blank" class="Email">Email</a>
        </div>
        """,
        unsafe_allow_html=True,
    )
    

def main():
    tabs = st.tabs(["Home", "About Me", "Projects", "Certificates", "Skills", "Contact"])
    with tabs[0]:
        home()
    with tabs[1]:
        about_me()
    with tabs[2]:
        projects()
    with tabs[3]:
        certificates()
    with tabs[4]:
        skills()
    with tabs[5]:
        contact()

# Run the App
if __name__ == "__main__":
    main()

