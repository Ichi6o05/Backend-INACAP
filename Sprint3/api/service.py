import requests

def getClientes(session_cookies):
    try:
        url = 'http://localhost:8000/api/viewClientes/'
        # token = "6cd35ec3aa2fae07d70bb458fe9cbf1ce3e4b594"
        # headers = {"Authorization": f"Token {token}"}
        respuesta = requests.get(url, cookies=session_cookies)
        if respuesta.status_code == 200:
            #Se obtiene la lista con los usuarios.
            return respuesta.json()
        else:
            return []
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    