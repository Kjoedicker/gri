import os
import requests

from dotenv import load_dotenv

class Github:
    def __init__(self):
        load_dotenv()
        self.url = "https://api.github.com"
        self.token = os.getenv("GITHUB_TOKEN")

    def createRepository(self, name: str) -> (str, bool):
        requestURL = self.url + "/user/repos"

        headers = {
            "Accept": "application/vnd.github+json", 
            "Authorization": "Bearer " + self.token, 
            "X-GitHub-Api-Version": "2022-11-28"
        }

        data ={
            "name": name,
            "description": "",
            "private": "true",
            "is_template": "false",
            "homepage":"https://github.com"
        }

        response = requests.post(url=requestURL,headers=headers, json=data)
        responseData = response.json()

        statusCode = response.status_code
        if statusCode != 201:
            message = responseData["message"]
            error = responseData["errors"][0]["message"]

            return (False, f"\n\tStatus code: {statusCode}\n\tMessage: {message}\n\tError: {error}")

        return (responseData["clone_url"], False)