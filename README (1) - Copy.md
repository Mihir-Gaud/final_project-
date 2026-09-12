# Global Happiness Report Analysis

## 📋 Overview
This project analyzes the **World Happiness Report** dataset to explore the key factors that contribute to happiness across different countries. Using data cleaning, statistical analysis, and visualization techniques, the project uncovers relationships between a country's happiness score and variables such as GDP per capita, social support, life expectancy, freedom, generosity, and perceptions of corruption.

## 🎯 Objectives
- Understand which socioeconomic and social factors are most strongly associated with national happiness scores.
- Visualize correlations between happiness score and contributing variables.
- Compare happiness trends across countries and regions.
- Derive actionable insights on what drives well-being at a national level.

## 📊 Dataset
- **Source:** [World Happiness Report Dataset](https://www.kaggle.com/) (available on Kaggle)
- **Description:** The dataset contains happiness scores and rankings for countries worldwide, along with contributing factors such as:
  - GDP per capita
  - Social support
  - Healthy life expectancy
  - Freedom to make life choices
  - Generosity
  - Perceptions of corruption

## 🛠️ Tools & Libraries
| Tool/Library | Purpose |
|---|---|
| **Pandas** | Data cleaning, wrangling, and manipulation |
| **Matplotlib** | Static data visualization |
| **Seaborn** | Statistical visualization (correlation heatmaps, regression plots, etc.) |
| **NumPy** *(optional)* | Numerical computations |
| **Jupyter Notebook** *(optional)* | Interactive analysis environment |

## 🚀 Project Workflow
1. **Data Collection** – Load the World Happiness Report dataset(s) into a Pandas DataFrame.
2. **Data Cleaning** – Handle missing values, standardize column names, and merge multi-year data if applicable.
3. **Exploratory Data Analysis (EDA)** – Generate summary statistics and explore distributions of key variables.
4. **Correlation Analysis** – Compute correlation coefficients between happiness score and each contributing factor.
5. **Visualization**
   - Heatmaps of correlations
   - Scatter plots (e.g., GDP per capita vs. Happiness Score)
   - Bar charts of top/bottom countries by happiness
   - Regional/country-wise trend comparisons
6. **Insights & Conclusion** – Summarize which factors most strongly influence happiness.

## 📁 Project Structure
```
global-happiness-analysis/
│
├── data/
│   └── world_happiness_report.csv
├── notebooks/
│   └── happiness_analysis.ipynb
├── images/
│   └── (generated charts and plots)
├── README.md
└── requirements.txt
```

## ⚙️ Installation & Setup
```bash
# Clone the repository
git clone https://github.com/your-username/global-happiness-analysis.git
cd global-happiness-analysis

# Install dependencies
pip install pandas matplotlib seaborn numpy jupyter
```

## ▶️ Usage
```bash
jupyter notebook notebooks/happiness_analysis.ipynb
```
Run the notebook cells sequentially to reproduce the data cleaning, analysis, and visualizations.

## 📈 Sample Insights (to be filled in after analysis)
- Countries with higher GDP per capita tend to report higher happiness scores.
- Social support shows a strong positive correlation with happiness.
- Life expectancy is closely tied to overall well-being rankings.

## 🤝 Contributing
Contributions, suggestions, and improvements are welcome. Feel free to open an issue or submit a pull request.

## 📄 License
This project is open-source and available under the [MIT License](LICENSE).
