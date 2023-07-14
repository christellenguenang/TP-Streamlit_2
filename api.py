from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/fusion")
def get_data():
    # Importation des bases achats, clics, et impressions
    achats = pd.read_csv("achats.csv")
    clics = pd.read_csv("clics.csv")
    impressions = pd.read_csv("impressions.csv")

    # On fusionne les 3 bases
    fusion_1 = pd.merge(clics, impressions, on="cookie_id")
    fusion = pd.merge(fusion_1, achats, on="cookie_id")
    fusion = fusion.fillna("-")

    return fusion.to_dict(orient="records")
