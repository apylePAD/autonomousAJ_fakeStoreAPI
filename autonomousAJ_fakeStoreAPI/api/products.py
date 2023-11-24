# autonomousAJ_fakeStoreAPI/api/products.py
import requests

class Products():
    def get_products(self):
        url = "https://fakestoreapi.com/products"
        response = requests.get(url)
        
        if response.status_code == 200:
            products = response.json()
            return products
        else:
            return "Error: Unable to fetch products"
        
        

 