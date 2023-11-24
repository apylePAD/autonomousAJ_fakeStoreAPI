# autonomousAJ_fakeStoreAPI/autonomousAJ_fakeStoreAPI/config.py
import os
import getpass
import inquirer
from dotenv import load_dotenv

load_dotenv()

class Global_Config:
    def __init__(self):
        self.BASE_PATH = self.determine_base_path()
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.all_scripts = self.find_all_scripts()
        self.app_run_choices = ['all'] + self.all_scripts
        self.APP_RUN_INPUT = None

    def __repr__(self):
        return f"GlobalConfig(BASE_PATH={self.BASE_PATH}, script_dir={self.script_dir}, all_scripts={self.all_scripts}, app_run_choices={self.app_run_choices}, APP_RUN_INPUT={self.APP_RUN_INPUT})"
    
    def determine_base_path(self):
        current_user = getpass.getuser()
        base_path_env = os.getenv(f"BASE_PATH_{current_user.upper()}")

        if base_path_env:
            return base_path_env
        else:
            print(f"Current user or system not recognized. Please set the environment variable 'BASE_PATH_{current_user.upper()}'")
            return None
        
    def find_all_scripts(self):
        excluded_files = ['__init__.py', 'auth.py', 'config.py', 'run.py', 'utils.py']
        return [f.replace('.py', '') for f in os.listdir(self.script_dir) if f.endswith('.py') and f not in excluded_files]
    
    def prompt_app_run_choices(self):
        choices = [
            inquirer.List('APP_RUN_CHOICE',
                message='Which portion(s) of the app do you want to run?:',
                choices=self.app_run_choices),
        ]
        return inquirer.prompt(choices)["APP_RUN_CHOICE"]


global_config = Global_Config()