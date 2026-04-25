import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image

# إعدادات الصفحة
st.set_page_config(page_title="Moataz Sobhy Portfolio", page_icon="📊", layout="wide")

# --- تحسين التصميم بـ CSS (لإخفاء الأخطاء وتجميل المربعات) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .project-card {
        background-color: #1f2937;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #374151;
        height: 250px;
        margin-bottom: 20px;
    }
    a { color: #00CC96; text-decoration: none; font-weight: bold; }
    a:hover { color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# --- Header Section (الصورة والبيانات الشخصية) ---
col_h1, col_h2 = st.columns([1, 3])

with col_h1:
    try:
        img = Image.open("myphoto.jpg")
        st.image(img, width=180)
    except:
        st.title("👤")

with col_h2:
    st.title("Moataz Sobhy Elkholy")
    st.subheader("Data Analyst | Data Warehouse Specialist")
    st.write("📍 Tanta, Egypt")
    # الجيميل الصحيح
    st.write("📧 motazelkholy850@gmail.com")
    st.write("[LinkedIn](https://linkedin.com) | [GitHub](https://github.com)")

st.write("---")

# --- قسم أداء المشاريع (الرسم البياني) ---
st.header("📈 Data Warehouse Impact")
data = pd.DataFrame({
    "المرحلة": ["قبل التنظيم", "بعد التنظيم (DWH)"],
    "وقت الاستعلام (ثانية)": [15.5, 0.8]
})
fig = px.bar(data, x="المرحلة", y="وقت الاستعلام (ثانية)", 
             color="المرحلة", color_discrete_sequence=["#EF553B", "#00CC96"])
st.plotly_chart(fig, use_container_width=True)

st.write("---")

# --- قسم المشاريع (Featured Projects) ---
st.header("🚀 Featured Projects")
p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    st.markdown('''
    <div class="project-card">
        <h3>End-to-End DWH</h3>
        <p>تصميم مستودع بيانات متكامل بجميع الطبقات لضمان سرعة الوصول للمعلومات.</p>
        <p><b>Tools:</b> SQL Server, ETL</p>
        <a href="https://github.com/moo3taz/Data-management_project">🔗 View on GitHub</a>
    </div>
    ''', unsafe_allow_html=True)

with p_col2:
    st.markdown('''
    <div class="project-card">
        <h3>Sales Dashboard</h3>
        <p>لوحة بيانات تفاعلية لتحليل المبيعات الشهرية وتحديد نقاط القوة.</p>
        <p><b>Tools:</b> Power BI, DAX</p>
        <a href="https://novypro.com">🔗 View Dashboard</a>
    </div>
    ''', unsafe_allow_html=True)

with p_col3:
    st.markdown('''
    <div class="project-card">
        <h3>Vehicle Maintenance AI</h3>
        <p>مشروع قيد التنفيذ لتحليل بيانات صيانة السيارات والتنبؤ بالأعطال.</p>
        <p><b>Tools:</b> Python, Machine Learning</p>
        <p style="color: #orange;">🚧 In Progress</p>
    </div>
    ''', unsafe_allow_html=True)

st.write("---")

# --- التقدم والمهارات ---
st.header("🛠 Technical Toolbox")
col_s1, col_s2 = st.columns(2)
with col_s1:
    st.write("**Languages:** SQL (T-SQL), Python (Pandas, NumPy)")
    st.write("**BI Tools:** Power BI, Excel (Advanced)")
with col_s2:
    st.write("**Database:** SQL Server, Data Warehousing")
    st.progress(85, text="SQL Mastery")

# --- Footer ---
st.write("---")
st.caption("© 2026 Moataz Sobhy | Built with Python & Streamlit")
