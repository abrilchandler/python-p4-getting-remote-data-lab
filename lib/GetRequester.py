import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        url = f'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.jsonLinks to an external site.'
        response = requests.get(self.url)
        return response.content
    


    def load_json(self):
        url = f'https://learn-co-curriculum.github.io/json-site-example/endpoints/people.jsonLinks to an external site.'
        print(url)
        response = requests.get(self.url)
        return response.json()
    
results = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json').get_response_body()
print(results)