import requests

url = "https://daily-missal.p.rapidapi.com/readings"

headers = {
	"X-RapidAPI-Key": "56c472c794msh0b140396436e607p13e6dfjsn11332428c919",
	"X-RapidAPI-Host": "daily-missal.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())