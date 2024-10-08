import cv2
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from .config import POSTS_URL
from .utils.convert import image_to_base64, image_from_base64

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ImageBase64Request(BaseModel):
    base64_image: str


@app.get("/posts/")
async def posts():

    try:
        response = requests.get(POSTS_URL)
        response.raise_for_status()
        posts = response.json()

    except requests.HTTPError as e:
        posts = [{}]
        raise HTTPException(status_code=e.response.status_code, detail=f"Error fetching posts: {e}")

    except Exception as e:
        posts = [{}]
        raise HTTPException(status_code=500, detail=f"Error fetching posts: {e}")

    finally:
        return {"posts": posts}


@app.post("/invert_image/")
async def invert_image(image_request: ImageBase64Request):

    try:
        image = image_from_base64(image_request.base64_image)
        inverted_image = cv2.bitwise_not(image)

        return {"inverted_image": image_to_base64(inverted_image)}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing image: {e}")
