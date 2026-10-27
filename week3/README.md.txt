# Supermarket Sales Analysis (Q1 2019)

## Overview
Analysis of ~1000 transactions from three supermarket branches (Jan-Mar 2019).
Goal: identify customer segments, product drivers, time trends, and actionable recommendations.

## Data
- Source: [supermarket sales dattaset](https://raw.githubusercontent.com/plotly/datasets/master/supermarket_Sales.csv)
- Size: 1000 transactions, 17 features
- Time period: January - March 2019

## Tools
- Python 3
- pandas (data manipulation)
- matplotlib + seaborn (visualization)

## Methodology
1. Load CSV and inspected (shape, dtypes, missing values)
2. Cleaned column names, parsed datetimes, extracted time features
3. Answered 5 CEO questions via groupby, pivot, and aggregation
4. Built a 2x3 dashboard summarizing key metrics
5. Wrote 7 actionable insights

## Key Findings
1. **Top product:** Food and beverages (highest revenue)
2. **Best day:** Saturday (weekend peak)
3. **Peak hour:** 19:00 (evening rush)
4. **Gender split:** ~50/50, with slight female majority
5. **Top branch:** Branch C (highest revenue)
6. **Best payment:** Credit card ($ highest total)
7. **Satisfaction:** Member customers rate slightly lower

## Recommendations
1. **Weekend staffing:** Add staff on Saturday afternoons (peak traffic)
2. **Product focus:** Expand Food & Beverages and Sports line
3. **Loyalty program:** to be reviewed
4. **Payment incentives:** Promote credit card rewards (highest revenue per transaction)
5. **Evening hours:** Ensure evening shift coverage (19:00 peak)
