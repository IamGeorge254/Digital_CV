from pathlib import Path
import streamlit as st
from PIL import Image

# Path setting
current_dir = Path(__file__).parent if"__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "George Kinuthia CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"

# General settings
PAGE_TITLE = "Digital CV | George Kinuthia"
PAGE_ICON = ":wave:"
NAME = "George Kinuthia"
DESCRIPTION = """
    I’m a self-taught data analyst with strong technical skills in Python, SQL, data visualization, and machine learning.
    I’ve built and deployed several real-world projects that showcase my ability to extract insights, build predictive models, and create interactive dashboards for data-driven decision-making.
"""
EMAIL = "gmwaura560@gmail.com"

SOCIAL_MEDIA = {
    "GitHub" : "https://github.com",
    "LinkedIn" : "https://linkedin.com"
    }

PROJECTS = {
    "🏆 Customer Segmentation and Time Forecasting - identify key customer groups and forecast future sales trends for better marketing and business decisions." : "https://github.com/IamGeorge254/Business-Insights-Visualization",
    "🏆 Diabetes Prediction using ML (Machine Learning) - Built a Machine Learning Model." : "https://github.com/IamGeorge254/Diabetes-Prediction",
    "🏆 Streamlit Breast Cancer Predictor - Web App with Streamlit." : "https://github.com/IamGeorge254/Streamlit_Breast_Cancer_predict"
}

st.set_page_config(
    page_title = PAGE_TITLE,
    page_icon = PAGE_ICON
)

st.title("")

# --- Load CSS, PDF & Profile Pic ---
with open(css_file) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic)

# --- Hero Section ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label = " 📄 Download Resume",
        data = PDFbyte,
        file_name = resume_file.name,
        mime = "application/octet-stream"
    )
    st.write("✉️", EMAIL)

# --- Social Links ---
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Skills & Qualifications ---
st.write("#")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✅ **Dashboard Development:** 
    - Built KPI and customer segmentation dashboards Power BI for real-time business insights
- ✅ **Machine Learning Projects:**
    - Built a Diabetes Prediction model with Random Forest achieving 98% accuracy
    - Deployed a Breast Cancer Prediction Web App using Streamlit and Logistic Regression for accurate diagnosis
- ✅ **Internship Experience:**
    - As a Data Analyst Intern at Afripixel Solutions, supported the team in cleaning datasets, creating KPI reports, and building Tableau dashboards
    - Collaborated with senior analysts to deliver actionable insights to internal stakeholders
- ✅ **Certifications:**
    - Google Data Analytics – Coursera
    - Data Analysis with Python – Free Code Camp
    - ALX Data Analytics Program – Ongoing
"""
)

# --- Skills ---
st.write("#")
st.subheader("Technical Skills")
st.write(
    """
- 💻 Programming: Python(scikit-learn, pandas, numpy), SQL
- 📊 Data Visualisation: Power BI, Tableau, MS Excel, Python(Seaborn, Matplotlib)
- ⚙️ Modeling: Logistic Regression, Linear Regression, Random Forest, Decision trees
- 🗄️ Databases: Microsoft SQL, MySQL
"""
)

# --- Work History ---
st.write("#")
st.subheader("Work History")
st.write("---")

st.write("📁", "**Data Analyst Intern | Afripixel Solution**")
st.write("April 2024 – Nov 2024")
st.write(
    """
- ➤ Assisted in cleaning, transforming and analyzing datasets using Python and SQL to extract
actionable insights.
- ➤ Supported Senior Analyst in creating weekly and monthly reports on key performance indicators
(KPIs). 
- ➤ Helped design and implement dashboards in Tableau for internal Stakeholders to track business
performance.
"""
)

st.write("📁", "**Lift Technician | Specialized Engineering**")
st.write("Sept 2023 – Feb 2024")
st.write(
    """
- ➤ Always engaged with clients to have a good understanding of how the lift’s been functioning.
- ➤ Maintaining monthly maintenance records and conducting routine maintenance.  
- ➤  Responding to mechanical failures and system malfunctions. 
"""
)

# --- Projects ---
st.write("#")
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")