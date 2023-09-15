import requests
import aiohttp


def get_roast():
    """Fetches a roast for mentioned target form random-api"""
    url = "https://random-api-nu.vercel.app/api/roast"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        roast = data["roast"]
        roast_id = data["id"]  # Just to show that the API also has roast ID
        return roast
    else:
        error = (
            "STATUS_CODE != 200\nThe API is not responding to this endpoint currently."
        )
        return error


async def get_roast_():
    """Fetches a roast for mentioned target form random-api"""
    url = "https://random-api-nu.vercel.app/api/roast"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as res:
            try:
                if res.status != 200:
                    error = "STATUS_CODE != 200\nThe API is not responding to this endpoint currently."
                    return error
                data = await res.json()
                roast = data["roast"]
                roast_id = data["id"]  # Just to show that the API also has roast ID
                return roast
            except Exception as e:
                return e
