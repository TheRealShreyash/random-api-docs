import requests
import aiohttp


def get_trivia():
    """Fetches a trivia for you form random-api"""
    url = "https://random-api-nu.vercel.app/api/trivia"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        question = data["question"]
        op1 = data["option1"]
        op2 = data["option2"]
        op3 = data["option3"]
        cop = data["correct_option"]
        return question, op1, op2, op3, cop
    else:
        error = (
            "STATUS_CODE != 200\nThe API is not responding to this endpoint currently."
        )
        return error


async def get_trivia_():
    """Fetches a trivia for you form random-api"""
    url = "https://random-api-nu.vercel.app/api/trivia"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as res:
            if res.status == 200:
                data = await res.json()
                question = data["question"]
                op1 = data["option1"]
                op2 = data["option2"]
                op3 = data["option3"]
                cop = data["correct_option"]
                return question, op1, op2, op3, cop
            else:
                error = "STATUS_CODE != 200\nThe API is not responding to this endpoint currently."
                return error
