import requests
import aiohttp

def get_question():
    """Fetches a question for you form random-api
    """
    url = "https://random-api-nu.vercel.app/api/question"
    res = requests.get(url)
    if res.status_code == 200:
        data = res.json()
        question = data["question"]
        return question
    else:
        error = "STATUS_CODE != 200\nThe API is not responding to this endpoint currently."
        return error
    
async def get_question_():
    """Fetches a question for you form random-api
    """
    url = "https://random-api-nu.vercel.app/api/question"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as res:
            if res.status == 200:
                data = await res.json()
                question = data["question"]
                return question
            else:
                error = "STATUS_CODE != 200\nThe API is not responding to this endpoint currently."
                return error