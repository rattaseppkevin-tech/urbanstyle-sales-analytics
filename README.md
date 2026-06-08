# UrbanStyle Sales & Profitability Analytics Pipeline

An end-to-end data engineering and business intelligence solution that automates ETL processes from cloud databases and transforms raw transactional data into strategic, margin-driven business insights.

## 📸 Executive Dashboard Preview

[Dashboard](https://github.com/rattaseppkevin-tech/urbanstyle-sales-analytics/blob/main/Dashboard/urbanstyle_sales_dashboard.pdf), 
[SQL Analysis](https://github.com/rattaseppkevin-tech/urbanstyle-sales-analytics/blob/main/SQL/profitability_analysis.sql), 
[Pipeline](https://github.com/rattaseppkevin-tech/urbanstyle-sales-analytics/blob/main/Python/profability_pipeline.py)
---

## 🚨 The Business Problem (The "Why?")
Many retail businesses track top-line Revenue but remain blind to their true net profitability in real-time. UrbanStyle.ltd faced three critical operational bottlenecks:
1. **Siloed Data:** Transactional sales logs were locked in a cloud database (Supabase), completely separate from manufacturing cost and product category tables.
2. **Manual Excel Labor:** The finance team spent hours manually exporting, merging, and cleaning data every week, leading to human error and delayed reporting.
3. **Growth Blindspots:** Management couldn't instantly identify which sales channels (Online vs. Physical) or product lines yielded the highest profit margins, risking inefficient marketing spend.

---

## 💡 The Solution & Business Impact
This project replaces manual reporting with a fully automated data pipeline and an interactive executive dashboard, delivering immediate business value:

* **100% Automated ETL:** Saves the data team hours of manual work weekly by engineering a hands-off Python pipeline.
* **True Profit Visibility:** Shifts the company focus from vanity metrics (Revenue) to sanity metrics (**Net Profit** and **Profit Margin %**).
* **Proactive Risk Mitigation:** Highlights immediate operational anomalies—such as the sharp revenue decline observed between 2024 ($1.47M) and 2025/2026—allowing executives to pivot strategy before it impacts the bottom line.

---

## 🛠️ Tech Stack & Architecture
* **Data Source:** Supabase (Cloud-based PostgreSQL)
* **Ingestion & Transformation:** Python (`Pandas`, `NumPy`)
* **Data Warehouse / Storage:** Local Cleaned Data Layer (`.csv`)
* **Business Intelligence:** Power BI Desktop (Interactive Visualizations & Slicers)

---

## ⚙️ Core Data Pipeline Features (Backend)
The Python script (`profitability_pipeline.py`) acts as a robust production-grade ETL tool featuring:

1.  **API Pagination Handling:** Supabase enforces a strict 1,000-row request limit. The script implements an automated pagination algorithm (`while True` loops) to seamlessly stream large-scale datasets.
2.  **Financial Enrichment:** Automatically joins transactional records with product cost maps on `product_id` to compute core KPIs:
    $$\text{Revenue} = \text{Total Price}$$
    $$\text{Cost} = \text{Quantity} \times \text{Cost Price}$$
    $$\text{Profit} = \text{Revenue} - \text{Cost}$$
3.  **Edge-Case Protection:** Uses safe division logic (`replace(0, np.nan)`) to prevent fatal script crashes caused by any zero-price test transactions in the database.
4.  **Production Logging:** Writes execution updates and system warnings directly to `pipeline.log` for seamless enterprise debugging.

---

## 📊 Strategic Business Insights Delivered (Frontend)
The Power BI interface translates the processed data into immediate strategic plays:

| Dashboard Section | Data Metric Discovered | Strategic Business Action |
| :--- | :--- | :--- |
| **Executive Summary** | **$2.91M** Total Revenue at a **37%** Average Margin. | Validates overall company health and sets the baseline for future quarterly performance targets. |
| **Profit by Category** | **Shoes** (jalanõud) and **Men's Clothing** are the highest drivers of net profit. | Management should scale up inventory and marketing budgets for these high-margin categories. |
| **Revenue by Channel** | Physical stores account for **65.39%** of sales vs. **34.61%** via Online channels. | Indication to optimize online conversion or run targeted ad campaigns to boost lower-overhead e-commerce sales. |
| **Interactive UX** | Custom glassmorphic container filters with a dedicated global state reset action. | Empowers regional store managers to instantly drill down into specific locations (Tallinn, Pärnu) without cluttering the view. |

---

## 🚀 How to Run & Replicate

### 1. Environment Setup
Clone this repository and install the production dependencies:
```bash
pip install pandas numpy python-dotenv supabase
---
*Created for UrbanStyle.ltd Data Analysis Portfolio.*
