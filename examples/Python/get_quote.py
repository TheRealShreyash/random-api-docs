import requests
import aiohttp


def get_quote(author: bool):
    """Fetches a quote for you form random-api
    'author': pass in True or False in order to decide whether you need author name or not
    """
    url = "https://random-api-nu.vercel.app/api/quote"
    res = requests.get(url)
    if res.status_code == 200:
        if author == True:
            data = res.json()
            quote = data["quote"]
            author = data["author"]
            final_quote = f"{quote}\n\t~{author}"
            return final_quote
        else:
            data = res.json()
            quote = data["quote"]
            return quote
    else:
        error = (
            "STATUS_CODE != 200\nThe API is not responding to this endpoint currently."
        )
        return error


async def get_quote_(author: bool):
    """Fetches a quote for you form random-api
    'author': pass in True or False in order to decide whether you need author name or not
    """
    url = "https://random-api-nu.vercel.app/api/quote"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as res:
            if res.status == 200:
                if author == True:
                    data = await res.json()
                    quote = data["quote"]
                    author = data["author"]
                    final_quote = f"{quote}\n\t~{author}"
                    return final_quote
                else:
                    data = res.json()
                    quote = data["quote"]
                    return quote
            else:
                error = "STATUS_CODE != 200\nThe API is not responding to this endpoint currently."
                return error
