import streamlit as st
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Portfolio - Daniel Wang",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.2rem;
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .project-card {
        padding: 1.5rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin-bottom: 1rem;
        cursor: pointer;
        transition: transform 0.2s;
    }
    .project-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    .skill-badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        margin: 0.2rem;
        background-color: #1f77b4;
        color: white;
        border-radius: 15px;
        font-size: 0.85rem;
    }
    .skill-container {
        display: flex;
        flex-wrap: wrap;
        gap: 0.3rem;
        margin-bottom: 0.5rem;
    }
    .section-header {
        color: #1f77b4;
        border-bottom: 2px solid #1f77b4;
        padding-bottom: 0.5rem;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
            
    .stMarkdown p {
        margin-bottom: 0.3rem;}
    </style>
""", unsafe_allow_html=True)

# Sample project data
PROJECTS = {
    "swimming_rank": {
        "title": "🏊 SwimmingRank Website",
        "short_desc": "A web application for tracking and ranking swimming performance.",
        "skills": ["Python", "NiceGui", "PostgreSQL", "Databasing", "Web Development"],
        "purpose": """
        Developed to help swimmers and coaches easily track performance metrics, analyze trends, and compare results across different meets. The platform provides a user-friendly interface for data entry and visualization.
        The data is pulled via USASwimming API and stored in a PostgreSQL database, allowing for efficient querying and analysis. The 
        website is writting in python using NiceGui, which provides a simple way to create interactive web applications completely in Python. 
        The link is found here: https://swimmingrank.org/""",
        "takeaways": [
            "Learned how to integrate third-party APIs for data collection",
            "Designed and implemented a relational database schema for performance data",
            "Learned how to quickly query from PostgreSQL using efficient SQL queries",
            "Built a responsive web interface using NiceGui",
            "Implemented data visualization features for performance analysis"
        ],
        "code": """"""""},
    "stock_sr": {
        "title": "📈 Stock Support/Resistance Levels Predictor",
        "short_desc": "LSTM (Long Short Term Memory) model to predict stock reaction to support and resistance levels based on historical price data.",
        "skills": ["Python", "Pytorch", "Numpy", "Matplotlib", "Machine Learning"],
        "purpose": """
        Designed to help myself identify potential price reversal points by predicting how the SPY will react to key support and resistance levels. 
        The model uses historical price data collected from Databento to calculate previous key levels and trains an LSTM neural network to predict the likelihood of price bouncing or breaking through those levels.
        The model achieved an accuracy of around 70% in predicting price reactions, providing valuable insights.
        """,
        "takeaways": [
            "Learned how to train a basic LSTM model for time series prediction using Pytorch",
            "Feature engineering to identify key support and resistance levels from historical price data",
            "Visualize the model's predictions against actual price movements using Matplotlib"
        ],
        "code": """"""
    },
}

# Resume data
RESUME_DATA = {
    "name": "Daniel Wang",
    "title": "University of Georgia - Electrical Engineering and Computer Science",
    "email": "Daniel.Wang@uga.edu",
    "phone": "412-218-5555",
    "location": "Athens, GA",
    "linkedin": "linkedin.com/in/daniel-w-6113b9268/",
    "summary": """
    I'm a senior engineering student at the University of Georgia looking for a full-time position in data analysis or embedded engineering. I'm well versed in Python, SQL, and various ML frameworks. """,
    "experience": [
        {
            "title": "Data Engineer Intern",
            "company": "Qorvo.",
            "period": "May 2024 - Aug 2025",
            "responsibilities": [
                "Developed several Spotfire visualization tools to reduct product failure analysis time and provide a cleaner way to present findings to team.",
                "Collaborated with colleagues in failure analysis of thousands of failed parts, including X-Ray imaging.",
                "Developed a Python application from scratch to analyze final test results of different Qorvo products",
                "Optimized Spotfire visualizations via IronPython scripts and data connection with ApacheSpark",
                "Used Databricks API and SQLAlchemy to pull data from Data Warehouse."
            ]
        },
        {
            "title": "Machine Learning Research Assistant",
            "company": "University of Georgia",
            "period": "May 2023 - Mar 2024",
            "responsibilities": [
                "Developed Python predictive machine learning model to determine if chickens are sick based on video feed",
                "Implemented YoloV8, OpenCV to identify and track chickens, feed, and water to help analyze their behavior",
                "Utilized RoboFlow to label data in an efficient manner"
            ]
        }
    ],
    "education": [
        {
            "degree": "B.S. in Electrical Engineering",
            "school": "University of Georgia",
            "year": "2022-2026"
        }
    ],
    "skills": {
        "Programming": ["Python", "SQL", "R"],
        "ML/AI": ["Scikit-learn", "PyTorch"],
        "Data": ["Pandas", "NumPy", "SQL"],
        "Visualization": ["Matplotlib", "Plotly", "Seaborn", "Spotfire"],
        "Tools": ["Git", "Streamlit", "Jupyter"]
    }
}

# Initialize session state for navigation
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'home'
if 'selected_project' not in st.session_state:
    st.session_state.selected_project = None

# Sidebar navigation
with st.sidebar:
    st.title("Navigation")
    if st.button("🏠 Home & Resume", use_container_width=True):
        st.session_state.current_page = 'home'
        st.session_state.selected_project = None
    
    if st.button("💼 Projects", use_container_width=True):
        st.session_state.current_page = 'projects'
        st.session_state.selected_project = None
    
    st.markdown("---")
    st.markdown("### Quick Links")
    st.markdown(f"📧 {RESUME_DATA['email']}")
    st.markdown(f"🔗 [{RESUME_DATA['linkedin']}](https://{RESUME_DATA['linkedin']})")

# Main content area
if st.session_state.current_page == 'home':
    # Header
    st.title("Hi! I'm " + RESUME_DATA["name"], text_alignment="center")
    st.markdown(RESUME_DATA['summary'])
    # About section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown('<h2 class="section-header">Work Experience</h2>', unsafe_allow_html=True)
        for exp in RESUME_DATA["experience"]:
            st.markdown(f"**{exp['title']}** at *{exp['company']}*")
            st.caption(exp['period'])
            for resp in exp['responsibilities']:
                st.write(f"• {resp}")
            st.write("")
    
    with col2:
        st.markdown('<h2 class="section-header">Contact</h2>', unsafe_allow_html=True)
        st.write(f"📧 {RESUME_DATA['email']}")
        st.write(f"📱 {RESUME_DATA['phone']}")
        st.write(f"📍 {RESUME_DATA['location']}")
        
        st.markdown('<h2 class="section-header">Education</h2>', unsafe_allow_html=True)
        for edu in RESUME_DATA["education"]:
            st.markdown(f"**{edu['degree']}**")
            st.write(edu['school'])
            st.write(edu['year'])
            st.write("")
    
    # Skills section
    st.markdown('<h2 class="section-header">Technical Skills</h2>', unsafe_allow_html=True)
    cols = st.columns(len(RESUME_DATA["skills"]))
    for idx, (category, skills) in enumerate(RESUME_DATA["skills"].items()):
        with cols[idx]:
            st.markdown(f"**{category}**")
            for skill in skills:
                st.markdown(f'<span class="skill-badge">{skill}</span>', unsafe_allow_html=True)

elif st.session_state.current_page == 'projects':
    if st.session_state.selected_project is None:
        # Project gallery view
        st.title("💼 My Projects")
        st.write("Click on any project to learn more about it!")
        
        # Display projects in grid
        for project_id, project in PROJECTS.items():
            with st.container(border=True):
                col1, col2 = st.columns([3, 1])
                
                with col1:
                    st.markdown(f"### {project['title']}")
                    st.write(project['short_desc'])
                    skills_html = '<div class="skill-container">'
                    for skill in project['skills']:
                        skills_html += f'<span class="skill-badge">{skill}</span>'
                    skills_html += '</div>'
                    st.markdown(skills_html, unsafe_allow_html=True)

                
                with col2:
                    if st.button("View Details →", key=f"btn_{project_id}"):
                        st.session_state.selected_project = project_id
                        st.rerun()
                
                st.markdown('</div>', unsafe_allow_html=True)
    
    else:
        # Individual project view
        project = PROJECTS[st.session_state.selected_project]
        
        if st.button("← Back to Projects"):
            st.session_state.selected_project = None
            st.rerun()
        
        st.title(project['title'])
        
        # Skills
        st.markdown("**Technologies Used:**")
        skills_html = '<div class="skill-container">'
        for skill in project['skills']:
            skills_html += f'<span class="skill-badge">{skill}</span>'
        skills_html += '</div>'
        st.markdown(skills_html, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Purpose
        st.markdown('<h2 class="section-header">Purpose & Overview</h2>', unsafe_allow_html=True)
        st.write(project['purpose'])
        
        # Takeaways
        st.markdown('<h2 class="section-header">Key Takeaways</h2>', unsafe_allow_html=True)
        for takeaway in project['takeaways']:
            st.write(f"• {takeaway}")
        
        # Code
        st.markdown('<h2 class="section-header">Code Implementation</h2>', unsafe_allow_html=True)
        st.code(project['code'], language='python')
        
        st.markdown("---")
        if st.button("← Back to Projects", key="back_bottom"):
            st.session_state.selected_project = None
            st.rerun()
