from fastapi import APIRouter
from core.zt_signer import build_and_sign_tx

router = APIRouter()

@router.post("/send")
def send_transaction(from_addr: str, to_addr: str, amount: float, privkey: str):
    raw_tx = build_and_sign_tx(from_addr, to_addr, amount, privkey)
    return {"raw_tx": raw_tx}

@router.post("/sign")
def sign_only(from_addr: str, to_addr: str, amount: float, privkey: str):
    raw_tx = build_and_sign_tx(from_addr, to_addr, amount, privkey)
    return {"signed": raw_tx}
