#!/usr/local/bin/python3

##

moscow = {
    "city": "Москва",
    "temperature": "20"
    }
print(moscow.get("city"))
moscow["temperature"] = int(moscow["temperature"]) - 5
print(moscow.get("temperature"))

print(moscow.get("country", "Russia"))
moscow["date"] = "27.05.2019"
print(len(moscow))
