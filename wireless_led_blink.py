import requests

def on_relay():
    url = "http://192.168.43.7/ON"
    try:
        response = requests.get(url)
        print("Relay turned ON. Status:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error sending request:", e)

task = input("Enter command (on/off): ")

if task.lower() == "on":
    on_relay()
else:
    print("Invalid command.")
