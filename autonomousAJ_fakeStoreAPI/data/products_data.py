# autonomousAJ_fakeStoreAPI/data/products_data.py
import pandas as pd
from autonomousAJ_fakeStoreAPI.api.products import Products
from autonomousAJ_fakeStoreAPI.config import global_config
from autonomousAJ_fakeStoreAPI.utils import flatten_dict_column

class Products_Data:
    def __init__(self):
        self.fake_store_products = Products()

    def get_and_process_products_data(self):
        products = self.fake_store_products.get_products()  # Fetch the products
        if isinstance(products, list):
            df = pd.DataFrame(products)

            # Flatten nested dict columns here, if necessary
            if 'rating' in df.columns:  # Assuming 'rating' is a nested column
                df = flatten_dict_column(df, 'rating')

            df = df.drop_duplicates()
            self.save_products_data(df)
            
        else:
            print("Error fetching products")

    def save_products_data(self, df):
        df.to_csv(f"{global_config.BASE_PATH}/data_files/written_files/product_data/products.csv", index=False)
        print(df)

