# autonomousAJ_fakeStoreAPI/run.py
import inquirer
from autonomousAJ_fakeStoreAPI.data.products_data import Products_Data

def main_menu():
    questions = [
        inquirer.List('choice',
                      message="What type of data would you like to interact with?",
                      choices=['Products', 'Exit']),
    ]
    return inquirer.prompt(questions)['choice']

def get_products_input():
    products_processor = Products_Data()
    products_processor.get_and_process_products_data()


def run():
    while True:
        choice = main_menu()
        if choice == 'Products':
            get_products_input()
        elif choice == 'Exit':
            break

if __name__ == '__main__':
    run()