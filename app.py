import streamlit as st
import pandas as pd
import plotly.express as px

# 1. إعدادات الصفحة
st.set_page_config(page_title="Moataz Elkholy Portfolio", layout="wide")

# 2. كود الـ CSS لتنسيق الموقع
st.markdown("""
    <style>
    .project-card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #334155;
        margin-bottom: 25px;
        height: 280px;
        transition: 0.3s;
    }
    .project-card:hover { border-color: #38bdf8; }
    .project-card h3 { color: #38bdf8; margin-top:0; }
    .project-card p { color: #cbd5e1; font-size: 14px; line-height: 1.6; }
    .project-card .tools { color: #94a3b8; font-weight: bold; font-size: 13px; }
    .project-link {
        background-color: #38bdf8;
        color: white !important;
        padding: 8px 15px;
        border-radius: 6px;
        text-decoration: none;
        display: inline-block;
        margin-top: 15px;
        font-weight: bold;
    }
    .contact-info {
        background-color: #0f172a;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# 3. الهيدر التعريفي
# --- الهيدر مع صورتك الشخصية ---
col1, col2 = st.columns([1, 4])

with col1:
    # هنا غيرنا الاسم لـ myphoto.jpg عشان يطابق الملف اللي أنت رافعه
    try:
        st.image("myphoto.jpg", width=150)
    except:
        st.write("👤") # احتياطي لو حصل مشكلة في التحميل

with col2:
    st.title("Moataz Sobhy Elkholy")
    st.subheader("Data Analyst | BI Developer")

# 4. قسم التواصل
st.markdown(f"""
<div class="contact-info">
    📍 Tanta, Egypt | 🎓 Faculty of Computers and AI <br>
    📧 <b>Email:</b> <a href="mailto:moatazelkholy850@gmail.com">moatazelkholy850@gmail.com</a> <br>
    🐙 <b>GitHub:</b> <a href="https://github.com/moo3taz" target="_blank">github.com/moo3taz</a> <br>
    🔗 <b>LinkedIn:</b> <a href="https://www.linkedin.com/in/moataz-sobhy-elkholy/" target="_blank">linkedin.com/in/moataz-elkholy</a>
</div>
""", unsafe_allow_html=True)

# 5. قائمة المشاريع (تعديل الأقواس لمنع الـ TypeError)
projects = [
    {
        "title": "Data Management (Engineering , Analytics) ",
        "desc": "Integrated data warehouse design with multi-layer architecture to ensure fast access to information.",
        "tools": "SQL Server, ETL, Data Modeling, Power Bi",
        "link": "https://github.com/moo3taz/Data-management_project"
    },
    
]

st.header("🚀 Featured Projects")
cols = st.columns(3)

for i, p in enumerate(projects):
    with cols[i % 3]:
        # استخدمنا % هنا بدل f-string للأمان وتجنب الأقواس
        card_html = """
        <div class="project-card">
            <h3>%s</h3>
            <p>%s</p>
            <p class="tools">🛠 Tools: %s</p>
            <a href="%s" target="_blank" class="project-link">View Project</a>
        </div>
        """ % (p['title'], p['desc'], p['tools'], p['link'])
        st.markdown(card_html, unsafe_allow_html=True)

# 6. الرسم البياني
st.write("---")
st.header("📊 Data Warehouse Impact")
impact_data = pd.DataFrame({
    "Stage": ["Before Organizing", "Post-Regulation (DWH)"],
    "Query Time (Sec)": [15.5, 0.8]
})
fig = px.bar(impact_data, x="Stage", y="Query Time (Sec)", color="Stage",
             color_discrete_sequence=["#EF553B", "#00CC96"])
st.plotly_chart(fig, use_container_width=True)
# --- التقدم والمهارات ---
st.header("🛠 Technical Skills")
col_s1, col_s2 = st.columns(2)
with col_s1:
    st.write("**Data Visualization :** Power BI (DAX, Power Query) , Excel (Advanced Dashboards)")
    st.write("**Database Management :** SQL (Joins, Subqueries, Aggregations)")
    st.write("**Programming :** Python (Pandas, NumPy, Matplotlib)")
    st.write("**Analytical Skills :** Statistics, Data Cleaning, ETL Processes, (EDA)")
with col_s2:
    st.write("**Database:** SQL Server, Data Warehousing")
    st.progress(85, text="SQL Mastery")

# --- Footer ---
st.write("---")
st.caption("© 2026 Moataz Sobhy | Built with Python & Streamlit")
