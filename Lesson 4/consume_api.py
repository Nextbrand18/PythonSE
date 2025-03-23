import requests
import json

response = requests.get('https://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow')

#print(response)
#print(response.json())

#print(response.json()['items'])
'''
for questions in response.json()['items']:
    print(questions['title'])
    print(questions['link'])
    print()

'''

for questions in response.json()['items']:
    if questions['answer_count'] == 0:
        print(questions['title'])
        print(questions['link'])
        print()
    else:
        print("skipped")
    print()