import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_details = response.json() #This will convert to JSON / Dictionary format
print(complete_details)