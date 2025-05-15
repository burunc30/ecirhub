import requests

# Əgər sən Render'də xidmətə bu linklə giriş edirsənsə, onu buraya yaz
LINK = "https://ecirhub-1.onrender.com"

def test_server():
    try:
        response = requests.get(f"{LINK}/")
        print("Server response:", response.text)
    except Exception as e:
        print("Error connecting to the server:", e)

if __name__ == "__main__":
    test_server()
