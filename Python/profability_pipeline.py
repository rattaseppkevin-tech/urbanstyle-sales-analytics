import os
import logging
import pandas as pd
import numpy as np
from dotenv import load_dotenv
from supabase import create_client

# 1. LOGGING CONFIGURATION
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("pipeline.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def run_pipeline():
    try:
        # 2. SETUP
        load_dotenv()
        supabase = create_client(os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY"))
        logger.info("Connection to Supabase established.")

        # Helper function to fetch all records from Supabase tables
        # Supabase default limit is 1000, so we paginate using range()
        def fetch_all(table_name, select_query="*"):
            data = []
            range_start = 0
            page_size = 1000
            while True:
                response = supabase.table(table_name).select(select_query).range(
                    range_start, range_start + page_size - 1
                ).execute()
                
                if not response.data:
                    break
                    
                data.extend(response.data)
                range_start += page_size
                
                # Stop if we received fewer records than the page_size (end of table)
                if len(response.data) < page_size:
                    break
            return data

        # 3. DATA FETCHING
        logger.info("Fetching all data from tables...")
        sales = pd.DataFrame(fetch_all("sales"))
        products = pd.DataFrame(fetch_all("products", "product_id, cost_price, product_name, category"))
        
        # 4. DATA TRANSFORMATION (ETL)
        logger.info("Merging data and calculating metrics...")
        
        # Merge sales with products based on product_id
        df = sales.merge(products, on="product_id", how="left")

        # Revenue and Cost calculation
        df['revenue'] = df['total_price']
        df['cost'] = (df['quantity'] * df['cost_price']).round(2)
        
        # Profit and Margin calculation (rounded to 2 decimal places)
        df['profit'] = (df['revenue'] - df['cost'].round(2)).round(2)
        df['margin_pct'] = ((df['profit'] / df['revenue'].replace(0, np.nan)) * 100).round(2)

        # 5. EXPORT
        output_path = "data/urbanstyle_final_data.csv"
        os.makedirs("data", exist_ok=True)
        df.to_csv(output_path, index=False)
        
        logger.info(f"Pipeline completed successfully! File saved at: {output_path}")

    except Exception as e:
        logger.error(f"Critical error during pipeline execution: {e}")

if __name__ == "__main__":
    run_pipeline()