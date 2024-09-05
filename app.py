import streamlit as st
import altair as alt
import pandas as pd
from PIL import Image

# Page config
st.set_page_config(page_title="Giyeon Lee's Portfolio", layout="wide")

# Custom CSS
st.markdown("""
<style>
    body {
        color: white;
        background-color: #1E1E1E;
    }
    .stApp {
        background-color: #1E1E1E;
    }
    .main {
        padding: 0rem 2rem;
    }
    .stApp > header {
        background-color: transparent;
    }
    h1, h2, h3 {
        color: #4ECCA3;
    }
    .step-title {
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #4ECCA3;
    }
    .css-18e3th9 {
        padding-top: 1rem;
        padding-bottom: 10rem;
        padding-left: 5rem;
        padding-right: 5rem;
    }
    .css-1d391kg {
        padding-top: 2rem;
        padding-right: 1rem;
        padding-bottom: 2rem;
        padding-left: 1rem;
    }
    h1 {
        font-size: 42px;
    }
    h2 {
        font-size: 32px;
        border-bottom: 1px solid #4ECCA3;
        padding-bottom: 10px;
    }
    h3 {
        font-size: 24px;
        margin-top: 1.5rem;
    }
    .stExpander {
        border: 1px solid #4ECCA3;
        border-radius: 5px;
        margin-bottom: 1rem;
    }
    .stExpander > div > div > div > div > div > p {
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("Giyeon Lee's Portfolio")

# About Me
col1, col2 = st.columns([1, 2])
with col1:
    image = Image.open("assets/profile.jpg")
    st.image(image, width=300)
with col2:
    st.header("About Me")
    st.markdown("""
    <div style="background-color: #2C2C2C; padding: 20px; border-radius: 5px;">
    <ul style="list-style-type: none; padding-left: 0;">
    <li>📛 <strong style="color: #4ECCA3;">Name:</strong> 이기연 (Giyeon Lee)</li>
    <li>🎂 <strong style="color: #4ECCA3;">Date of Birth:</strong> 1997.05.16</li>
    <li>📧 <strong style="color: #4ECCA3;">E-Mail:</strong> rldus3512@naver.com</li>
    <li>🎓 <strong style="color: #4ECCA3;">Education:</strong> Korea Aerospace Univ. Software Engineering</li>
    <li>📞 <strong style="color: #4ECCA3;">Contact:</strong> 010-8643-9761</li>
    <li>🧠 <strong style="color: #4ECCA3;">MBTI:</strong> ESTJ</li>
    </ul>
    </div>
    
    안녕하세요, 저는 이기연입니다. 주로 Java와 Python을 사용하여 풀스택 개발을 하고 있으며, QA 경험도 갖추고 있습니다.
    """, unsafe_allow_html=True)

# Career Timeline
st.header("Career Timeline")

career_data = pd.DataFrame([
    {"start": "2016-03-01", "end": "2023-02-28", "event": "Korea Aerospace Univ. 재학 및 졸업"},
    {"start": "2021-09-01", "end": "2021-12-31", "event": "ICT 학점 이수 인턴제"},
    {"start": "2023-01-04", "end": "2023-09-30", "event": "NHN Service 인턴 (QA 및 레퍼런스 조사)"},
    {"start": "2023-12-18", "end": "2024-06-14", "event": "Hanwha Systems BEYOND SW CAMP (Full Stack Developer)"},
    {"start": "2023-07-04", "end": "2024-08-29", "event": "Himedia AI-X(AI Advanced Project)"}
])

career_data['start'] = pd.to_datetime(career_data['start'])
career_data['end'] = pd.to_datetime(career_data['end'])

chart = alt.Chart(career_data).mark_bar().encode(
    x=alt.X('start', title='Period'),
    x2='end',
    y=alt.Y('event', title='Experience', sort='-x'),
    color=alt.Color('event', legend=None, scale=alt.Scale(scheme='teals')),
    tooltip=['event', 'start', 'end']
).properties(
    width=700,
    height=300,
    title='Career Timeline'
).configure_axis(
    labelColor='white',
    titleColor='white'
).configure_title(
    color='#4ECCA3'
)

st.altair_chart(chart, use_container_width=True)

# Skills
st.header("Skills")
st.markdown("""
<div style="background-color: #2C2C2C; padding: 20px; border-radius: 5px;">

### Tech Stack
[![My Skills](https://skillicons.dev/icons?i=java,spring,py,mysql,git,githubactions,docker,aws)](https://skillicons.dev)

### Development Tools
[![My Skills](https://skillicons.dev/icons?i=github,idea,pycharm,vscode,notion,discord)](https://skillicons.dev)

### Operating Systems
[![My Skills](https://skillicons.dev/icons?i=apple,windows,linux,ubuntu)](https://skillicons.dev)

</div>
""", unsafe_allow_html=True)

# Projects
st.header("Projects")

projects = [
    {
        "title": "Jiwoo",
        "period": "2024.07.14 ~ 2024.08.15 (1개월)",
        "description": "1인 창업 지원 AI 서비스",
        "role": "서비스 기획, 개발 형상 관리, CI/CD, 기능단위 Backend 개발, AI 서버 및 VectorDB 환경 구축",
        "tech_stack": "Java, Spring, SpringBoot, Python, Milvus, React.js, Flutter, Amazon EC2, Amazon RDS, MariaDB, Docker, GitHub Actions"
    },
    {
        "title": "KMS",
        "period": "2024.04.17 ~ 2024.06.14 (2개월)",
        "description": "집단 지성을 위한 지식 관리 시스템",
        "role": "서비스 기획, 개발 형상 관리, CI/CD, 기능단위 Backend 개발",
        "tech_stack": "Java, Spring, SpringBoot, Vue.js, Amazon Elastic Beanstalk, Amazon EC2, Amazon Route53, Amazon RDS, MariaDB, GitHub Actions"
    }
]

for project in projects:
    with st.expander(f"{project['title']}"):
        st.markdown(f"**Period:** {project['period']}")
        st.markdown(f"**Description:** {project['description']}")
        st.markdown(f"**Role:** {project['role']}")
        st.markdown(f"**Tech Stack:** {project['tech_stack']}")

# Education
st.header("Education")
st.markdown("""
<div style="background-color: #2C2C2C; padding: 20px; border-radius: 5px;">

### Korea Aerospace University
- **Major:** Software Engineering
- **Period:** 2016.03 ~ 2023.02 (Graduated)

</div>
""", unsafe_allow_html=True)

# Contact
st.header("Contact")
st.markdown("""
<div style="background-color: #2C2C2C; padding: 20px; border-radius: 5px;">

- **Email:** rldus3512@naver.com
- **Phone:** 010-8643-9761

</div>
""", unsafe_allow_html=True)