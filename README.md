# EVision — Smart EV Innovation Analyzer

**A data-driven platform for evaluating and analyzing electric vehicle innovation through AI-powered insights and predictive modeling.**

---

## Problem Statement

The electric vehicle market is rapidly evolving with hundreds of models offering varying combinations of battery capacity, efficiency, performance, and pricing. Consumers, analysts, and industry professionals struggle to objectively compare EVs across multiple dimensions of innovation and value.

**EVision** solves this by computing a comprehensive **Innovation Score** that quantifies how innovative an electric vehicle is based on technical capabilities, energy intelligence, and user value — providing a single metric to compare and analyze EVs objectively.

---

## Innovation Score Methodology

The Innovation Score is a weighted composite metric ranging from 0-100, calculated using three core dimensions:

### Formula

```
Innovation Score = (Tech Edge × 0.40) + (Energy Intelligence × 0.40) + (User Value × 0.20)
```

### Component Breakdown

**1. Tech Edge (40%)**
Evaluates cutting-edge performance and capabilities
- Battery Capacity (kWh)
- Top Speed (km/h)
- Acceleration 0-100 km/h (seconds, inverted)

**2. Energy Intelligence (40%)**
Measures efficiency and charging capabilities
- Efficiency (Wh/km, inverted)
- Range (km)
- Fast Charge Speed (km/h of charge)

**3. User Value (20%)**
Assesses affordability and cost-effectiveness
- Price (Euro, inverted and weighted)

Each feature is normalized using min-max scaling before aggregation, ensuring balanced contribution across different units and scales.

---

## Machine Learning Workflow

### Dataset Overview
- **Total Vehicles:** 360 electric vehicle models
- **Features:** 7 technical and pricing attributes
- **Target Variable:** Innovation Score (computed)

### Pipeline

1. **Exploratory Data Analysis (EDA)**
   - Distribution analysis of all features
   - Outlier detection and handling
   - Statistical profiling of EV characteristics

2. **Feature Engineering**
   - Min-max normalization of all features
   - Weighted composite score calculation
   - Feature interaction analysis

3. **Correlation Analysis**
   - Identified strong correlations between battery capacity and range
   - Analyzed price-performance relationships
   - Validated scoring formula assumptions

4. **Predictive Modeling**
   - Algorithm: Linear Regression
   - Performance: **R² = 0.99**
   - Use Case: Predict Innovation Score from raw features
   - Enables score estimation for new EV models

### Key Insights

The high R² score validates that the Innovation Score formula effectively captures the linear relationships between EV features and overall innovation potential. This allows the model to accurately predict innovation scores for vehicles not yet in the dataset.

---

## Streamlit Web Application

EVision extends beyond analysis into an interactive web platform built with Streamlit, offering real-time EV exploration and AI-powered insights.

### Application Features

#### 🏠 Home
- Project overview and methodology
- Quick navigation hub
- Feature highlights

#### 💬 AI Chat
- Conversational interface powered by **Google Gemini AI**
- Natural language queries about EVs
- Persistent chat history within sessions
- Context-aware responses about the dataset

#### 📊 Innovation Score
- Interactive EV comparison dashboard
- Sortable and filterable data tables
- Visual score breakdowns
- Top performers by category

#### ℹ️ About
- Detailed scoring methodology
- Technical documentation
- Project background and vision

### UI/UX Enhancements

- **Custom CSS Styling:** Modern, responsive design with brand-consistent color palette
- **Lottie Animations:** Smooth, engaging visual elements for enhanced user experience
- **Persistent State Management:** Chat history and user preferences maintained across page navigation
- **Responsive Layout:** Optimized for desktop and tablet viewing

---

## AI Assistant Capabilities

The integrated Gemini AI assistant provides intelligent analysis and answers questions such as:

- "Which EV has the best efficiency under €40,000?"
- "Compare the top 5 EVs by Innovation Score"
- "What's the relationship between battery capacity and range?"
- "Recommend an EV for long-distance travel with fast charging"
- "Explain why a specific vehicle scored high/low"

The AI has access to the complete EV dataset and can perform complex queries, comparisons, and recommendations based on user preferences.

---

## Tech Stack

### Data Science & ML
- **Python 3.x** — Core programming language
- **Pandas** — Data manipulation and analysis
- **NumPy** — Numerical computing
- **Scikit-learn** — Machine learning modeling
- **Matplotlib / Seaborn** — Data visualization

### Web Application
- **Streamlit** — Interactive web framework
- **Lottie** — Animation integration
- **Custom CSS** — Styling and theming

### AI Integration
- **Google Gemini API** — Conversational AI and natural language processing
- **LangChain** (optional) — AI orchestration and prompt management

### Development Tools
- **Jupyter Notebook** — Exploratory analysis
- **Git** — Version control
- **VS Code** — Development environment

---

## Project Structure

```
evision/
│
├── data/
│   └── ev_data.csv                 # Raw EV dataset (360 vehicles)
│
├── notebooks/
│   ├── 01_eda.ipynb                # Exploratory data analysis
│   ├── 02_feature_engineering.ipynb # Score calculation
│   └── 03_modeling.ipynb           # ML model training
│
├── app/
│   ├── Home.py                     # Streamlit main entry point
│   ├── pages/
│   │   ├── 1_💬_AI_Chat.py        # Gemini AI chat interface
│   │   ├── 2_📊_Innovation_Score.py # Score dashboard
│   │   └── 3_ℹ️_About.py          # About page
│   ├── utils/
│   │   ├── scoring.py              # Innovation score logic
│   │   ├── ai_handler.py           # Gemini API integration
│   │   └── visualizations.py      # Chart generators
│   └── assets/
│       ├── style.css               # Custom styling
│       └── animations/             # Lottie files
│
├── models/
│   └── innovation_model.pkl        # Trained linear regression model
│
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
└── .env.example                    # Environment variables template
```

---

## Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key (for AI features)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/evision.git
cd evision
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
# Add your GEMINI_API_KEY to .env
```

5. Run the Streamlit app:
```bash
streamlit run app/Home.py
```

The application will open in your default browser at `http://localhost:8501`

---

## Model Performance

| Metric | Value |
|--------|-------|
| Algorithm | Linear Regression |
| R² Score | 0.99 |
| Training Samples | 288 (80%) |
| Test Samples | 72 (20%) |
| Features | 7 |

The near-perfect R² score indicates that the Innovation Score formula successfully captures the underlying patterns in EV innovation metrics.

---

## Future Scope

### Short-term Enhancements
- Add more EV models as market data becomes available
- Implement user authentication for personalized recommendations
- Export comparison reports and visualizations

### Medium-term Features
- Expand scoring dimensions (safety ratings, software features, charging network access)
- Real-time data updates via web scraping or API integration
- Multi-model ML comparison (Random Forest, XGBoost)

### Long-term Vision
- Mobile application (React Native/Flutter)
- Community-driven reviews and ratings
- Predictive analytics for future EV market trends
- Integration with dealer inventory and pricing APIs

---

## Acknowledgments

- EV dataset sourced from [kaggle/ev-database]
- Google Gemini AI for powering conversational features
- Streamlit community for excellent documentation and support

---

**Built with 🔋 for a sustainable future**
