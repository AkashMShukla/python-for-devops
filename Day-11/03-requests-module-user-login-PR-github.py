import requests

response = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_details = response.json() #This will convert to JSON / Dictionary format
#print(f"\n------------ The Login of first PR User is : ------------\n {complete_details[0]["user"]["login"]}")

print("\n------------ The Login of each PR Users are as follow : ------------\n")
#for i in range(len(complete_details)):
#    print(f"{complete_details[i]["user"]["login"]}")

#OR you may use below better python code:::

for pr in complete_details:
    print(pr['user']['login'])