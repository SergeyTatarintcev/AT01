# main.py
from __future__ import annotations
from typing import Optional
import requests


def get_random_cat_image(api_key: Optional[str] = None, timeout: int = 10) -> Optional[str]:
   
    url = "https://api.thecatapi.com/v1/images/search"
    headers = {"x-api-key": api_key} if api_key else None

    try:
        resp = requests.get(url, headers=headers, timeout=timeout)
    except requests.RequestException:
        return None

    if resp.status_code != 200:
        return None

    try:
        data = resp.json()
        # ожидаемый формат: список из одного объекта c полем "url"
        if isinstance(data, list) and data and isinstance(data[0], dict):
            img_url = data[0].get("url")
            if isinstance(img_url, str) and img_url.startswith(("http://", "https://")):
                return img_url
    except ValueError:
        # невалидный JSON
        return None

    return None
