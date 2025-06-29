from fastapi import APIRouter
from core.zt_utils import generate_mnemonic, import_from_mnemonic

router = APIRouter()

@router.get("/generate")
def generate_wallet():
    mnemonic, privkey, address = generate_mnemonic()
    return {"mnemonic": mnemonic, "privkey": privkey, "address": address}

@router.post("/import")
def import_wallet(mnemonic: str):
    privkey, address = import_from_mnemonic(mnemonic)
    return {"privkey": privkey, "address": address}
