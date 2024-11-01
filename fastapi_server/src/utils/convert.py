import base64

import cv2
import numpy as np


def image_from_base64(base64_image: str):

    base64_image = base64_image.split(",")[1]
    image_data = base64.b64decode(base64_image)
    np_array = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(np_array, cv2.IMREAD_COLOR)

    return image


def image_to_base64(image: np.ndarray):

    _, buffer = cv2.imencode(".jpg", image)
    image_base64 = base64.b64encode(buffer).decode("utf-8")
    image_base64 = "data:image/jpg;base64, " + image_base64

    return image_base64
