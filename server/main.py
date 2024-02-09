import torch
import uvicorn
from io import BytesIO
import base64

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from mlmodule import MlModule
from fastapi.responses import StreamingResponse

stable_dif = MlModule()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def wrapper(func):
    def wrap(*args, **kwargs):
        try:
            ret = func(*args,**kwargs)
            return ret
        except Exception as e:
            return e
    return wrap


class PromptData(BaseModel):
    prompt: str

@wrapper
@app.post("/prompt")
def process_prompt(prompt: PromptData):
    result = f"Вы ввели промпт: {prompt.prompt}"
    image = stable_dif(prompt.prompt)
    image.save(f'../images/{prompt.prompt}.png')
    img_byte_array = BytesIO()
    image.save(img_byte_array, format='PNG')
    image_base64 = base64.b64encode(img_byte_array.getvalue()).decode("utf-8")
    return {"result": result, "image": image_base64}

if __name__ == "__main__":
    uvicorn.run(app,port=3333,host="127.0.0.1")