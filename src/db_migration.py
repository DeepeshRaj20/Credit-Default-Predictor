import pandas as pd
from sqlalchemy import create_engine
import urllib.parse

try:
    db = pd.read_csv("data/loan_data.csv")
    print(db.head())

    raw_password = "Deepesh@20"
    safe_password = urllib.parse.quote_plus(raw_password)

    # 2. Connection String (Dhyan se apna password dalo)
    # Format: mysql+pymysql://root:PASSWORD@localhost/credit_db
    # this is creating roadmap to connect to MySQL database named 'credit_db' using username 'root' and the provided password.
    engine = create_engine(f"mysql+pymysql://root:{safe_password}@localhost/credit_db")

    # 3. Migration: CSV to MySQL
    print("⏳ Dumping data to MySQL... Please wait.")
    #Here you are moving the data from the DataFrame (db) to a MySQL table named 
    #'loan_records'. If the table already exists, it will be replaced. 
    #The index=False argument ensures that the DataFrame index is not included as a
    #column in the MySQL table.
    db.to_sql('loan_records', con=engine, if_exists='replace', index=False)
    print("🔥 SUCCESS! Data 'loan_records' shifted to MySQL.")
except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print(f"An error occurred: {e}")