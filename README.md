# 🚗⚡ EVision: Electric Vehicle Innovation Scoring

> *Quantifying electric vehicle innovation through data-driven intelligence*

## 📌 Overview

This project introduces a **composite Innovation Score** for electric vehicles that goes beyond traditional metrics. **EVision** combines technological advancement, energy efficiency, and user value to create a holistic benchmark that objectively compares EVs across brands like Tesla, BYD, and MG.

## 🎯 What Makes an EV "Innovative"?

The Innovation Score synthesizes three critical dimensions:

| Dimension | Weight | What It Measures | Key Features |
|-----------|--------|------------------|--------------|
| **Tech Edge** | 40% | Engineering prowess & charging capability | Fast charge speed, Top speed |
| **Energy Intelligence** | 40% | Sustainability & battery optimization | Efficiency, Range |
| **User Value** | 20% | Affordability & practicality | Price, Acceleration |

### 🧮 The Formula

```
Innovation Score = 0.4(TechEdge) + 0.4(EnergyIntelligence) + 0.2(UserValue)
```

Where:
- **TechEdge** = 0.5 × norm(Fast_charge) + 0.5 × norm(Top_speed)
- **EnergyIntelligence** = 0.6 × norm(Efficiency) + 0.4 × norm(Range)
- **UserValue** = 0.5 × (1 - norm(Price)) + 0.5 × (1 - norm(Acceleration))

*Weights can be adjusted based on project focus: sustainability, performance, or affordability.*

## 📊 Dataset

- **360 electric vehicles** from various manufacturers
- **7 core features**: Battery size, Efficiency, Fast charge, Price, Range, Top speed, Acceleration
- Cleaned and preprocessed with missing values handled via mean imputation
- Outliers in pricing addressed using IQR-based capping

## 🔬 Analysis Workflow

### 1️⃣ EDA & Feature Engineering (`EV_EDA.pdf`)
- Exploratory data analysis with distribution plots
- Feature scaling using MinMaxScaler
- Innovation Score computation
- Correlation analysis revealing:
  - **Top_speed** (0.90) and **Battery** (0.85) as strongest positive correlators
  - **Acceleration** (-0.74) as a negative correlator
  - **Efficiency** shows weak correlation (0.08) - removed from modeling

### 2️⃣ Predictive Modeling (`InnovationScore_model.pdf`)
- **Algorithm**: Linear Regression with GridSearchCV
- **Performance Metrics**:
  - R² Score: **0.990** (test set)
  - Cross-validation R²: **0.992** ± 0.002
  - RMSE: **0.010**
  - MAE: **0.007**
- Model demonstrates excellent fit with minimal overfitting
- Saved artifacts: `linear.pkl` and `columns_linear.pkl`

## 🎨 Key Visualizations

- Distribution plots for all features
- Learning curves showing model convergence
- Residual plots confirming homoscedasticity
- Predictions vs Actuals scatter plot

## 🚀 Why This Matters

✨ **For Manufacturers**: Identify innovation gaps and benchmark against competitors  
🌱 **For Policy Makers**: Encourage sustainable EV design through quantifiable metrics  
💰 **For Consumers**: Make informed decisions based on holistic vehicle value  
📈 **For Researchers**: Use as a framework for multi-dimensional EV analysis

## 📦 Project Structure

```
├── EV_cars.csv                          # Raw dataset
├── EV_cleaned_InnovationScore.csv       # Processed dataset with scores
├── EV_EDA.pdf                           # Exploratory analysis notebook
├── InnovationScore_model.pdf            # Model training notebook
├── linear.pkl                           # Trained model
└── columns_linear.pkl                   # Feature columns
```

## 🛠️ Technologies Used

- **Data Processing**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn
- **Modeling**: Scikit-learn (Linear Regression, GridSearchCV)
- **Persistence**: Joblib

## 🔮 Future Enhancements

- Incorporate real-time market data
- Add brand-specific innovation trends
- Expand to include environmental impact scores
- Deploy as an interactive web dashboard

---

**Built with 🔋 for the future of sustainable mobility**
