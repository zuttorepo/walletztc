from fastapi import FastAPI
from routes import wallet, transaction

app = FastAPI(title="ZuttoWalletCoin API")

app.include_router(wallet.router, prefix="/wallet", tags=["Wallet"])
app.include_router(transaction.router, prefix="/tx", tags=["Transaction"])

@app.get("/")
def read_root():
    return {"status": "ZuttoWalletCoin API is running"}
