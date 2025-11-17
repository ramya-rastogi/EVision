import streamlit as st
import google.generativeai as genai
from streamlit_lottie import st_lottie
import requests
from mykey import API_KEY

# ----------------------------------------------------------
# 🔧 CONFIGURE GEMINI
# ----------------------------------------------------------
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("models/gemini-2.5-flash")

# ----------------------------------------------------------
# 🎨 PAGE SETUP
# ----------------------------------------------------------
st.set_page_config(
    page_title="EVision - Smart EV Innovation Analyzer",
    layout="wide",
    page_icon="⚡",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------
# 🌈 CUSTOM CSS
# ----------------------------------------------------------
st.markdown("""
<style>
body {
    background-color: #0A1929;
}
.big-title {
    font-size: 40px;
    font-weight: 700;
    color: #00E5FF;
    text-align: center;
    margin-bottom: 10px;
}
.subtitle {
    text-align: center;
    color: #B0BEC5;
    font-size: 18px;
    margin-bottom: 25px;
}
.chat-box {
    background-color: #1E3A5F;
    border-radius: 15px;
    padding: 20px;
    margin: 10px 0;
    border-left: 4px solid #00E5FF;
}
.user {
    color: #E0F7FA;
    font-weight: bold;
}
.bot {
    color: #00E5FF;
    font-style: italic;
}
.metric-card {
    background: linear-gradient(135deg, #1E3A5F 0%, #0D47A1 100%);
    padding: 20px;
    border-radius: 10px;
    border: 1px solid #00E5FF;
    margin: 10px 0;
}
footer {
    visibility: hidden;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------
# 💫 LOAD LOTTIE ANIMATIONS (with fallback)
# ----------------------------------------------------------
def load_lottie_url(url: str):
    try:
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()
    except:
        return None

# ✅ EV-themed Lottie URLs
ev_anim = load_lottie_url("https://lottie.host/embed/91b49831-b7a7-4b0a-bb6d-2de2f1e8e8c8/N3Dek5LWzH.json")  # Electric car
charging_anim = load_lottie_url("https://lottie.host/embed/c9a8e0e5-0c6c-4a9f-9c8e-e8c5e0e5e8c5/battery.json")  # Charging station

# ----------------------------------------------------------
# 🧭 SIDEBAR
# ----------------------------------------------------------
st.sidebar.title("⚡ EVision")
st.sidebar.markdown("Your **Smart EV Innovation Analyzer** 🚗🔋")
st.sidebar.divider()

page = st.sidebar.radio("Navigate", ["🏠 Home", "🤖 AI Chat", "📊 Innovation Score", "ℹ️ About Us"])

# ----------------------------------------------------------
# 🏠 HOME PAGE
# ----------------------------------------------------------
if page == "🏠 Home":
    st.markdown("<div class='big-title'>Welcome to EVision ⚡</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Composite Innovation Score for Electric Vehicles - Beyond Traditional Metrics</div>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 1])
    with col1:
        if ev_anim:
            st_lottie(ev_anim, height=350, key="ev")
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/2554/2554968.png", width=300)

    with col2:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.markdown("### 🎯 Innovation Score Components")
        st.markdown("""
        **1. Technological Advancement (40%)**
        - Battery technology & range
        - Autonomous features
        - Software integration
        
        **2. Energy Efficiency (30%)**
        - kWh/100km efficiency
        - Charging speed
        - Regenerative braking
        
        **3. User Value (30%)**
        - Price-to-performance ratio
        - Total cost of ownership
        - Practicality & reliability
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("### 🌟 Why EVision?")
    st.write("""
    - 🔬 **Holistic Benchmarking**: Compare Tesla, BYD, MG, and more using composite scores  
    - 📊 **Objective Analysis**: Data-driven insights beyond marketing hype  
    - 🚀 **Future-Ready**: Evaluates innovation that matters for sustainable transportation  
    - 💡 **Smart Comparisons**: AI-powered recommendations based on your needs  
    """)

    st.markdown("### 🚀 Get Started!")
    st.success("Head over to the **AI Chat** section to analyze EVs or check **Innovation Scores**!")

# ----------------------------------------------------------
# 💬 CHAT PAGE
# ----------------------------------------------------------
elif page == "🤖 AI Chat":
    st.markdown("<div class='big-title'>EVision AI Assistant 🧠</div>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Ask me about EV comparisons, innovation scores, or buying recommendations!</div>", unsafe_allow_html=True)

    # Initialize chat memory with EV context
    if "conversation" not in st.session_state:
        system_prompt = """You are EVision AI, an expert electric vehicle analyst. You help users understand 
        EV technology, compare vehicles using a composite Innovation Score that weighs:
        - Technological Advancement (40%): battery tech, autonomy, software
        - Energy Efficiency (30%): kWh/100km, charging, regen braking
        - User Value (30%): price-performance, TCO, practicality
        
        Focus on brands like Tesla, BYD, MG, Tata, Mahindra, Hyundai, and others. Provide data-driven, 
        objective analysis. Be technical yet accessible."""
        
        st.session_state.conversation = [{"role": "user", "parts": [system_prompt]}]

    user_input = st.text_input(
        "💬 Ask EVision:",
        key="user_input",
        placeholder="e.g., Compare Tesla Model 3 vs BYD Seal using the Innovation Score"
    )

    if st.button("Send 💥") and user_input.strip() != "":
        st.session_state.conversation.append({"role": "user", "parts": [user_input]})

        context = st.session_state.conversation[-8:]  # Keep more context for technical discussions
        try:
            with st.spinner("⚡ EVision is analyzing..."):
                response = model.generate_content(context)
                reply = response.text
        except Exception as e:
            reply = f"⚠️ Error: {str(e)}"

        st.session_state.conversation.append({"role": "model", "parts": [reply]})

    st.markdown("### 💬 Chat History")
    for i, message in enumerate(st.session_state.conversation):
        if i == 0:  # Skip system prompt
            continue
        if message["role"] == "user":
            st.markdown(f"<div class='chat-box user'>👤 <b>You:</b> {message['parts'][0]}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='chat-box bot'>⚡ <b>EVision:</b> {message['parts'][0]}</div>", unsafe_allow_html=True)

# ----------------------------------------------------------
# 📊 INNOVATION SCORE PAGE
# ----------------------------------------------------------
elif page == "📊 Innovation Score":
    st.markdown("<div class='big-title'>Innovation Score Methodology 📊</div>", unsafe_allow_html=True)
    
    st.markdown("### 🧮 How We Calculate Innovation Score")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.markdown("### 🔬 Technology (40%)")
        st.markdown("""
        - Battery capacity & chemistry
        - Range (EPA/WLTP)
        - Autonomous driving features
        - OTA updates & software
        - Charging capability (kW)
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.markdown("### ⚡ Efficiency (30%)")
        st.markdown("""
        - kWh per 100km
        - Real-world efficiency
        - Regenerative braking
        - Thermal management
        - Charging speed (10-80%)
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
        st.markdown("### 💎 User Value (30%)")
        st.markdown("""
        - Price-to-range ratio
        - Total cost of ownership
        - Reliability ratings
        - Practicality (space, cargo)
        - Warranty & support
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    
    st.markdown("### 🎯 Example: Calculate a Score")
    
    brand = st.selectbox("Select Brand", ["Tesla", "BYD", "MG", "Tata", "Mahindra", "Hyundai"])
    model_name = st.text_input("Model Name", placeholder="e.g., Model 3, Seal, ZS EV")
    
    if st.button("🔍 Analyze Innovation Score"):
        if model_name.strip():
            query = f"Analyze the {brand} {model_name} using the EVision Innovation Score methodology. Provide scores for Technology (40%), Efficiency (30%), and User Value (30%), along with a final composite score out of 100."
            
            with st.spinner("⚡ Calculating Innovation Score..."):
                try:
                    response = model.generate_content(query)
                    st.markdown("<div class='chat-box bot'>", unsafe_allow_html=True)
                    st.markdown(f"### ⚡ {brand} {model_name} - Innovation Analysis")
                    st.markdown(response.text)
                    st.markdown("</div>", unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a model name")

# ----------------------------------------------------------
# ℹ️ ABOUT US
# ----------------------------------------------------------
elif page == "ℹ️ About Us":
    st.markdown("<div class='big-title'>About EVision 🌟</div>", unsafe_allow_html=True)
    st.markdown("""
    EVision was created to bring **objective, data-driven analysis** to the electric vehicle market.  
    
    **The Problem:**
    - 🔋 Traditional metrics (range, price) don't tell the full story  
    - 📊 Marketing claims often overshadow real innovation  
    - 🤔 Buyers struggle to compare EVs objectively across brands  

    **Our Solution:**  
    A **composite Innovation Score** that weighs technological advancement, energy efficiency, and 
    real-world user value to create holistic benchmarks for EVs from Tesla, BYD, MG, and beyond.
    """)

    st.markdown("### 💻 Tech Stack")
    st.write("""
    - **Frontend:** Streamlit ⚡  
    - **AI Engine:** Google Gemini AI 🤖  
    - **Language:** Python 🐍  
    - **Focus:** Data-driven EV Analysis 🔬  
    """)

    st.markdown("### 🎯 Project Vision")
    st.info("""
    **EVision aims to democratize EV knowledge** by making sophisticated analysis accessible to everyone.
    Whether you're a first-time buyer or an EV enthusiast, our Innovation Score helps you see beyond 
    the marketing to understand which vehicles truly push the boundaries of electric mobility.
    """)

    st.markdown("### 👨‍💻 Creator")
    st.success("""
    Developed by **Ramya**, passionate about sustainable transportation and AI innovation.  
    ✨ Empowering informed EV decisions through technology & data.
    """)

    st.balloons()