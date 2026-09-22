# Superstore Sales & Profitability Analysis

Exploratory analysis of ~8,400 order-level records (2009-2012) from a retail superstore
dataset, plus an Excel dashboard with formula-driven KPIs and native charts.

## Key finding
Furniture carries a **2.3% profit margin** vs. **14.8% for Technology** — Tables and
Bookcases are net loss-makers despite high sales volume, driven by heavy discounting.

## How to run

```bash
pip install -r requirements.txt

python3 analyze.py       # cleans data/superstore_raw.csv -> prints summary, writes superstore_clean.csv
python3 charts.py        # reads superstore_clean.csv -> writes chart_*.png (matplotlib)
python3 build_excel.py   # reads superstore_clean.csv -> writes Superstore_Sales_Dashboard.xlsx
```

Run them in that order — `charts.py` and `build_excel.py` both depend on the
`superstore_clean.csv` that `analyze.py` produces.

## What this shows
- Data cleaning with pandas (type coercion, malformed-row handling, date parsing)
- Aggregation and margin analysis by region, category, sub-category, segment, and year
- Matplotlib visualizations: monthly sales trend, sub-category profit ranking, regional margin comparison
- Excel dashboard (`Superstore_Sales_Dashboard.xlsx`) built with openpyxl:
  SUMIFS-driven KPI cards, a region breakdown table, and native bar/pie charts that
  recalculate live in Excel (no hardcoded values — verified formulas evaluate with
  zero errors via LibreOffice recalculation)

## Project structure
```
data/superstore_raw.csv       raw dataset (input)
analyze.py                    cleaning + groupby analysis (pandas) -> superstore_clean.csv
charts.py                     matplotlib visualizations -> chart_*.png
build_excel.py                Excel dashboard with live formulas -> Superstore_Sales_Dashboard.xlsx
chart_monthly_trend.png       output: monthly sales trend
chart_subcategory_profit.png  output: profit by sub-category (best/worst)
chart_region_margin.png       output: margin % by region
Superstore_Sales_Dashboard.xlsx  output: Excel dashboard
requirements.txt              Python dependencies
```

## Tools used
Python (pandas, matplotlib), Excel (openpyxl-built formulas, SUMIFS-based aggregation, native charts)

## Author
Bhabanisankar Bhol — github.com/Mr-Bhanani
