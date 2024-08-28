import pandas as pd
import pyodbc
import uvicorn

#Set up connection to SQL Server
server_name = "Your_Server_Name"
db_name = "Your_DB_Name"
conn = pyodbc.connect('DRIVER={SQL Server}; \
                      SERVER=' + server_name + '; \
                      DATABASE=' + db_name + '; \
                      Trusted_Connection=yes;')


from fastapi import FastAPI

app = FastAPI()

@app.post("/excel_to_sql")
async def excel_to_sql():
    #Read Excel sheet data
    df = pd.read_excel('AnganwadiCenter.xlsx')
    
    #Transfer data to SQL Server
    cursor = conn.cursor()
    for index, row in df.iterrows():
        cursor.execute('INSERT INTO Your_Table_Name (Column1, Column2, Column3) \
                        values (?, ?, ?)',
                        row['Column1'], row['Column2'], row['Column3'])
    cursor.commit()
    return {"message": "Data transfer successful!"}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=3000)
