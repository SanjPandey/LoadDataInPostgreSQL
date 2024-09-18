
# Load Data in PostgreSQL
import pandas as pd
from sqlalchemy import create_engine

#painting is database which is created in PostgreSQL
conn_string='postgresql://postgres:Sanj123P@localhost/painting'
db=create_engine(conn_string)
conn=db.connect()

# For Single file

df=pd.read_csv('H:/artist.csv')
df.to_sql('artist',con=conn,if_exists='replace',index=False)
print(df.info)


# For multiple files
files=['canvas_size','image_link','museum','museum_hours','product_size','subject','work']

for file in files:
    df = pd.read_csv(f'H:/{file}.csv')
    df.to_sql(file, con=conn, if_exists='replace', index=False)


