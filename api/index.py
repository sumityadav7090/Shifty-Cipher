from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def shifty_cipher(text, shift):
    result = []
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result.append(chr(shifted))
        else:
            result.append(char)
    return ''.join(result)

@app.post("/encrypt")
async def encrypt(request: Request):
    data = await request.json()
    text = data.get("text", "")
    shift = data.get("shift", 0)
    cipher = shifty_cipher(text, int(shift))
    return JSONResponse(content={"cipher": cipher})
