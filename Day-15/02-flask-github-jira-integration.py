# This code sample uses the 'requests' library:
# http://docs.python-requests.org
'''
import requests
from requests.auth import HTTPBasicAuth
import json
from flask import Flask

app = Flask(__name__)

# Define a route that handles GET requests
@app.route('/createJira', methods=['POST']) #This is a Decorator; This tells flask Run this function createJira() when someone opens /createJira URL.
def createJira():
    url = "https://akashshukla.atlassian.net/rest/api/3/issue"
    API_TOKEN=""
    auth = HTTPBasicAuth("", API_TOKEN)
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }
    payload = json.dumps( {
        "fields": {
        "description": {
            "content": [
                {
                    "content": [
                        {
                            "text": "Order entry fails when selecting supplier.",
                            "type": "text"
                        }
                    ],
                    "type": "paragraph"
                    }
                ],
            "type": "doc",
             "version": 1
        },
        "project": {
           "key": "AB"
        },
        "issuetype": {
            "id": "10006"
        },
        "summary": "Main order flow broken",
    },
    "update": {}
    } )
    response = requests.request(   #we are sending Jira API Request
        "POST",
        url,
        data=payload,
        headers=headers,
        auth=auth
    )
    return json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": "))      #You'll see the reponse from jira in webhook logs as we triggered the API from there.
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

'''