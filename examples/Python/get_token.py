import requests
import aiohttp


def get_token():
    """Fetches a token form random-api"""
    url = "https://random-api-nu.vercel.app/api/token"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        token = data["token"]
        return token
    else:
        error = (
            "STATUS_CODE != 200\nThe API is not responding to this endpoint currently."
        )
        return error


async def get_token_():
    """Fetches a token form random-api"""
    url = "https://random-api-nu.vercel.app/api/token"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as res:
            try:
                if res.status != 200:
                    error = "STATUS_CODE != 200\nThe API is not responding to this endpoint currently."
                    return error
                data = await res.json()
                token = data["token"]
                return token
            except Exception as e:
                return e
