# Mutual Fund Insights Dashboard

An end-to-end data analytics project that processes real-world Indian mutual fund data using Python and visualizes actionable investment insights in Power BI. This project bridges the gap between raw data wrangling and business intelligence, providing a "Top 30 Low-Risk, High-Return" fund screener for retail investors.

## 🎯 Business Objective
To analyze a universe of 2,500+ mutual funds, identify key performance drivers, and build an interactive dashboard that helps investors balance risk (Standard Deviation), cost (Expense Ratio), and reward (3-Year Returns).

## 🛠️ Technical Stack
- **Data Engineering:** Python (Pandas, NumPy) for handling missing values, type coercion, and feature engineering.
- **Business Intelligence:** Power BI Desktop (DAX, Custom Tooltips, Interactive Slicers).
- **Advanced Analytics:** Python (Seaborn, Matplotlib) integrated directly into Power BI for correlation heatmaps.

## 🚀 Key Features & Methodology
1. **Automated Data Cleaning:** Handled real-world data imperfections (e.g., forward-filling missing 5-year returns with 3-year proxies, coercing string formats to numeric).
2. **Custom Feature Engineering:** Created a proprietary `risk_adjusted_score` metric: `(3YR Return * 0.6) + (Sharpe * 10) - (Expense Ratio * 5)` to objectively rank funds.
3. **Interactive Fund Screener (Page 1):** Filters the top 30 equity funds by AMC, category, and risk level, featuring a classic "Risk vs. Return" efficient frontier scatter plot.
4. **Market Deep Dive (Page 2):** Visualizes Assets Under Management (AUM) by category, Top 10 AMC performance, and expense ratio distributions.
5. **Advanced Analytics (Page 3):** Native Python correlation heatmap revealing the statistical relationship between fund costs, volatility, and historical returns.

## 📈 Key Insights
- **Cost Matters:** Funds with an expense ratio > 1.5% consistently showed lower risk-adjusted returns (Sharpe Ratio) compared to their direct-plan counterparts.
- **Risk-Return Tradeoff:** Small Cap and Sectoral funds exhibit high 3-year returns but come with disproportionately high Standard Deviation (volatility), validating the need for the custom risk-adjusted scoring.

## ⚙️ How to Reproduce
1. Clone this repository.
2. Run `python clean_mutual_funds.py` to process the raw `comprehensive_mutual_funds_data.csv` and generate `top_30_mutual_funds.csv`.
3. Open `Mutual_Fund_Dashboard.pbix` in Power BI Desktop.
4. Ensure Python scripting is enabled in *File > Options > Python scripting* to render the Page 3 heatmap.

## ⚠️ Data Limitations
- The dataset represents a static snapshot of the Indian mutual fund market. Past performance (1YR, 3YR, 5YR) does not guarantee future results.
- Some newer funds have missing 5-year return data, which was logically imputed using 3-year returns for scoring purposes.
