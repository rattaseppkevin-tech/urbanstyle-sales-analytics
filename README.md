# UrbanStyle Sales Analytics Pipeline

## Project Overview
This project focuses on building an end-to-end data pipeline to analyze the profitability of UrbanStyle.ltd. By integrating sales data with product costs and category information, this pipeline provides actionable insights into profit margins and sales channel performance.

## Tech Stack
- **Python (Pandas, NumPy):** Used for ETL (Extract, Transform, Load) processes and data cleaning.
- **Supabase:** The cloud-based PostgreSQL database source.
- **Plotly:** Used for rapid data visualization and diagnostic analysis.
- **Power BI:** The final destination for interactive business intelligence dashboards.

## Key Features
- **Data Enrichment:** Merging transactional sales data with static product data to calculate real-time profitability.
- **Financial Metrics:** Automated calculation of `revenue`, `cost`, `profit`, and `margin_pct` (rounded to 2 decimal places).
- **Quality Control:** Built-in logging with `logging` library to track pipeline execution and error handling.
- **Scalability:** The pipeline is designed to be modular, allowing for easy addition of new metrics or data sources.

## Workflow
1. **Extraction:** Fetching raw data from Supabase.
2. **Transformation:** - Merging `sales` and `products` tables.
   - Calculating margins and handling potential division-by-zero errors.
3. **Visualization:** - Diagnostic analysis in Jupyter Notebooks using Plotly.
   - Final dashboard design in Power BI.

## How to Run
1. Install dependencies: `pip install pandas numpy python-dotenv supabase plotly`
2. Configure your `.env` file with `SUPABASE_URL` and `SUPABASE_KEY`.
3. Run the pipeline: `python scripts/profitability_pipeline.py`
4. Access processed data in `data/urbanstyle_final_data.csv` for your BI tools.

---
*Created for UrbanStyle.ltd Data Analysis Portfolio.*