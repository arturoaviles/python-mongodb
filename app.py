import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

ENV_VARIABLE = os.environ.get("ENV_VARIABLE")
print(ENV_VARIABLE)