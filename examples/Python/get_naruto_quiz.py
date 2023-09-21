import requests
import aiohttp


def get_naruto_quiz():
    """Fetches a Naruto Quiz for you form random-api"""
    url = "https://random-api-nu.vercel.app/api/naruto"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        question = data["question"]
        op1 = data["1"]
        op2 = data["2"]
        op3 = data["3"]
        cop = data["correct"]
        return question, op1, op2, op3, cop
    else:
        error = (
            "STATUS_CODE != 200\nThe API is not responding to this endpoint currently."
        )
        return error


async def get_naruto_quiz_():
    """Fetches a Naruto Quiz for you form random-api"""
    url = "https://random-api-nu.vercel.app/api/naruto"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as res:
            if res.status == 200:
                data = await res.json()
                question = data["question"]
                op1 = data["1"]
                op2 = data["2"]
                op3 = data["3"]
                cop = data["correct"]
                return question, op1, op2, op3, cop
            else:
                error = "STATUS_CODE != 200\nThe API is not responding to this endpoint currently."
                return error
