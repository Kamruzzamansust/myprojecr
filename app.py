from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Enable CORS (Cross-Origin Resource Sharing) to allow requests from Streamlit
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows requests from all origins, you can refine it to specific origins
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load your data
df = pd.read_csv('Data/data.csv')

@app.get("/data")
async def get_data():
    return df.to_dict(orient='records')

@app.get("/missing_values")
async def calculate_missing_values():
    missing_values = df.isna().sum().to_dict()
    
    print(missing_values)