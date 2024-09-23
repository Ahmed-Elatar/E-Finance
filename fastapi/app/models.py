from pydantic import BaseModel

# --------------------------------- Models-----------------------------------


class TickerData(BaseModel):
    
    ticker : str
    sender : str


