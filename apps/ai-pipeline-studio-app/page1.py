import streamlit as st
import base64
from pathlib import Path


# -----------------------------
# 1. Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Pipeline Studio",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Path settings
APP_DIR = Path(__file__).resolve().parent
ASSETS_DIR = APP_DIR / "assets"

# -----------------------------
# 2. Core CSS Styles (Tech Aesthetic + Animations)
# -----------------------------
def load_css():
    st.markdown("""
        <style>
        /* Global Background: Deep Space Radial Gradient */
        .stApp {
            background: radial-gradient(circle at 50% 30%, #1e202e 0%, #0d1117 60%, #000000 100%);
            color: #ffffff;
        }

        /* Hide default header and menu */
        header {visibility: hidden;}
        #MainMenu {visibility: hidden;}

        /* -----------------------
           Animation Definitions
           ----------------------- */
        /* 1. Floating Image Animation */
        @keyframes float {
            0% { transform: translateY(0px); }
            50% { transform: translateY(-20px); }
            100% { transform: translateY(0px); }
        }
        
        /* 2. Neon Text Glow Animation */
        @keyframes glow {
            0% { text-shadow: 0 0 5px rgba(0,210,255,0.2); }
            50% { text-shadow: 0 0 20px rgba(0,210,255,0.6), 0 0 30px rgba(0,100,255,0.4); }
            100% { text-shadow: 0 0 5px rgba(0,210,255,0.2); }
        }

        /* -----------------------
           Component Styles
           ----------------------- */
        /* Hero Title */
        .hero-title {
            font-size: 72px;
            font-weight: 800;
            background: linear-gradient(90deg, #ffffff, #85d7ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            animation: glow 3s infinite alternate;
            margin-bottom: 0px;
        }

        /* Subtitle */
        .hero-subtitle {
            font-size: 20px;
            color: rgba(255, 255, 255, 0.7);
            margin-bottom: 30px;
            font-family: 'Courier New', monospace;
        }

        /* Glassmorphism Card */
        .glass-card {
            background: rgba(255, 255, 255, 0.03);
            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);
            border: 1px solid rgba(255, 255, 255, 0.08);
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
            transition: transform 0.3s;
        }
        .glass-card:hover {
            border-color: rgba(0, 210, 255, 0.3);
            transform: scale(1.01);
        }

        /* Tech Tags */
        .tech-tag {
            display: inline-block;
            padding: 5px 12px;
            border-radius: 4px;
            background: rgba(0, 210, 255, 0.1);
            border-left: 3px solid #00d2ff;
            color: #85d7ff;
            font-size: 12px;
            font-weight: bold;
            margin-right: 10px;
            margin-bottom: 15px;
            letter-spacing: 1px;
        }

        /* Floating Image Class */
        .floating-img {
            animation: float 6s ease-in-out infinite;
            width: 100%;
            border-radius: 20px;
            filter: drop-shadow(0 0 20px rgba(0,200,255,0.2));
        }

        /* Bottom Feature Grid */
        .feature-box {
            background: rgba(13, 17, 23, 0.8);
            border: 1px solid #30363d;
            border-radius: 12px;
            padding: 20px;
            text-align: center;
        }
        .feature-icon { font-size: 30px; margin-bottom: 10px; }
        .feature-head { color: #fff; font-weight: bold; margin-bottom: 5px; }
        .feature-desc { color: #8b949e; font-size: 14px; }

        </style>
    """, unsafe_allow_html=True)

load_css()

# -----------------------------
# 3. Helper Function: Load Images
# -----------------------------
def get_img_as_base64(file_path):
    if not file_path.exists():
        return None
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# -----------------------------
# 4. Page Layout
# -----------------------------

# Top spacing
st.write("##")

# Main two-column layout
col_text, col_img = st.columns([1.2, 1], gap="large")

with col_text:
    # Header Section
    st.markdown('<div class="hero-title">AI Pipeline Studio</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">NEXT-GEN DATA SCIENCE WORKBENCH</div>', unsafe_allow_html=True)
    
    # Tech Tags
    st.markdown("""
        <div>
            <span class="tech-tag">🚀 MULTI-AGENT SYSTEM</span>
            <span class="tech-tag">⚡ AUTOMATED EDA</span>
            <span class="tech-tag">🛡️ ENTERPRISE READY</span>
        </div>
    """, unsafe_allow_html=True)

    # Interactive Glass Card
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.markdown("### 💠 Select Your Workflow Mode", unsafe_allow_html=True)
    
    scenario = st.selectbox(
        "Select Scenario",
        ["Quick Start (Onboarding)", "Deep EDA (Exploratory Analysis)", "Full Pipeline (End-to-End)", "Audit & Replay (Compliance)"],
        label_visibility="collapsed"
    )

    # Dynamic Content Mapping
    content_map = {
        "Quick Start (Onboarding)": {
            "desc": "Simply upload your CSV and let AI Agents automatically scan data, suggest cleaning strategies, and generate your first visualization report.",
            "highlight": "Best for: Rapid data quality validation, zero coding required."
        },
        "Deep EDA (Exploratory Analysis)": {
            "desc": "Integrated with Sweetviz and Correlation Funnel to uncover non-linear relationships and generate interactive HTML insight reports.",
            "highlight": "Best for: Data scientists seeking feature engineering inspiration."
        },
        "Full Pipeline (End-to-End)": {
            "desc": "Human-in-the-loop architecture. Agents write feature engineering code while you handle code review. One-click model training deployment.",
            "highlight": "Best for: Building reproducible ML pipelines."
        },
        "Audit & Replay (Compliance)": {
            "desc": "Full chain-of-custody logging. Track every data hash change with support for one-click pipeline rollback and experiment reproduction.",
            "highlight": "Best for: Finance, healthcare, and high-compliance scenarios."
        }
    }
    
    current_content = content_map[scenario]
    st.info(f"**{current_content['desc']}**\n\n*{current_content['highlight']}*")
    
    st.markdown("</div>", unsafe_allow_html=True)

    st.write("##")
    
    # Two Main Buttons
    b_c1, b_c2 = st.columns(2)
    with b_c1:
        # type="primary" applies Streamlit's accent color (usually red/pink, striking against dark themes)
        if st.button("🚀 Launch Workbench", use_container_width=True, type="primary"):
            st.switch_page("pages/app.py")
    with b_c2:
        if st.button("🔒 Privacy Policy", use_container_width=True):
            st.switch_page("pages/privacy.py")

with col_img:
    # Right side Hero Image with floating animation
    hero_path = ASSETS_DIR / "hero.png"
    hero_b64 = get_img_as_base64(hero_path)
    
    if hero_b64:
        st.markdown(
            f'<img src="data:image/png;base64,{hero_b64}" class="floating-img">',
            unsafe_allow_html=True
        )
    else:
        st.warning("⚠️ Please ensure assets/hero.png exists")

# -----------------------------
# 5. Bottom Feature Matrix (Enhanced Content)
# -----------------------------
st.write("---")
st.markdown('<div style="text-align: center; margin-bottom: 30px; opacity: 0.8;">CORE CAPABILITIES</div>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)

with f1:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">🤖</div>
        <div class="feature-head">AI Agent Driven</div>
        <div class="feature-desc">LLM-based agents automatically write Python cleaning code. Say goodbye to tedious Pandas operations.</div>
    </div>
    """, unsafe_allow_html=True)

with f2:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">📊</div>
        <div class="feature-head">Interactive Viz</div>
        <div class="feature-desc">Embedded Plotly and native Streamlit charts supporting smooth interaction with millions of data points.</div>
    </div>
    """, unsafe_allow_html=True)

with f3:
    st.markdown("""
    <div class="feature-box">
        <div class="feature-icon">💾</div>
        <div class="feature-head">Artifact Store</div>
        <div class="feature-desc">Automatic version control for all model artifacts, reports, and datasets. Full traceability at any time.</div>
    </div>
    """, unsafe_allow_html=True)