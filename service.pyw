import base64
import os
import sys

import pyperclip
import qrcode
from fastapi import FastAPI, Query, HTTPException

# redirect console output
sys.stdout = open(os.devnull, 'w')
sys.stderr = open(os.devnull, 'w')

app = FastAPI()
os.environ["PYTHON_KEYRING_BACKEND"] = "keyring.backends.null.Keyring"


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
        with open(r"D:\documents\RandomScripts\clipboard_to_qr\log.txt", 'a') as f:
            f.write(f'data: {clipboard_data}')
        if not clipboard_data:
            raise HTTPException(status_code=400, detail="Clipboard is empty")

        img = qrcode.make(clipboard_data)
        img.save(r"D:\documents\RandomScripts\clipboard_to_qr\qr.png")
        os.startfile(r"D:\documents\RandomScripts\clipboard_to_qr\qr.png")
    except Exception as e:
        raise HTTPException(status_code=500,
                            detail=f"Error generating QR code: {str(e)}")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=13131)