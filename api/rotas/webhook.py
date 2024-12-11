from fastapi import Request, APIRouter, HTTPException
from utils.tipo_mensagem import DefineTratamentoMensagem
import json 

router = APIRouter()

@router.post("")
async def webhook(request: Request):
    if request is None:
        raise HTTPException(status_code=400, detail="Request is empty")
    
    try:
        data = await request.json()
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    
    try:
        print(data)

    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error extracting fields: {str(e)}")
    
    return {"status": "ok"}