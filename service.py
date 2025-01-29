import base64
import os

import pyperclip
import qrcodepip
from fastapi import FastAPI, Query, HTTPException

app = FastAPI()


@app.get("/send")
async def send(data: str = Query(..., description="Base64 encoded data")):
    try:
        decoded_data = base64.b64decode(data).decode("utf-8")
        pyperclip.copy(decoded_data)
        return {"message": "Data copied to clipboard"}
    except Exception as e:
        raise HTTPException(status_code=400,
                            detail=f"Error processing data: {str(e)}")



@app.get("/receive")
async def receive():
    try:
        clipboard_data = pyperclip.paste()
        if not clipboard_data:
            raise HTTPException(status_code=400, detail="Clipboard is empty")

        img = qrcode.make(clipboard_data)
        img.save("qr.png")
        os.startfile("qr.png")
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=f"Error generating QR code: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=13131)