import requests

while True:
    try:
        ID = int(input("Podaj liczbę w przedziale od 1 do 10: "))
        assert 1 <= ID <= 10
        break

    except AssertionError:
        print("Podano liczbę spoza zakresu!!")

    except ValueError:
        print("Podaj liczbę!!")

url = f"https://jsonplaceholder.typicode.com/users/{ID}"

response = requests.get(url)
print(f"Status zapytania: {response.status_code}")
print(f"Dane użytkownika o indeksie {ID}: \nImie i nazwisko: {response.json()['name']}\nNick: "
      f"{response.json()['username']}")


while True:
    try:
        decision = input("Czy podoba Ci się ten nick?(tak lub nie): ").lower()
        assert decision == "tak" or decision == "nie"
        if decision == "nie":
            nick = input("Podaj nowy nick: ")
            changedNick = {"username": nick}
            response = requests.patch(url, json=changedNick)
            print(f"Oto wszystkie dane o użytkowniku: {response.json()}")
        else:
            print(f"Oto wszystkie dane o użytkowniku: {response.json()}")
        break

    except AssertionError:
        print("Wpisz tak lub nie!!")

url2 = f"https://jsonplaceholder.typicode.com/photos/{ID}"
response2 = requests.get(url2)

print(f"Zdjęcie z albumu o podanym ID: {response2.json()['url']}")
