import requests
import sys
import time

BASE_URL = "http://127.0.0.1:5005"

def test_api():
    print("Testing API...")

    # 1. Test Public Endpoint
    try:
        resp = requests.get(f"{BASE_URL}/api/")
        if resp.status_code == 200:
            print("[PASS] Public Endpoint")
        else:
            print(f"[FAIL] Public Endpoint: {resp.status_code}")
    except Exception as e:
        print(f"[FAIL] Server might not be running: {e}")
        return

    # 2. Test Register
    username = f"user_{int(time.time())}"
    password = "password123"
    print(f"Registering user: {username}")
    resp = requests.post(f"{BASE_URL}/api/auth/register", json={"username": username, "password": password})
    if resp.status_code == 201:
        print("[PASS] Register")
    else:
        print(f"[FAIL] Register: {resp.text}")

    # 3. Test Login
    resp = requests.post(f"{BASE_URL}/api/auth/login", json={"username": username, "password": password})
    token = ""
    if resp.status_code == 200:
        token = resp.json().get('token')
        print("[PASS] Login")
    else:
        print(f"[FAIL] Login: {resp.text}")
        return

    # 4. Test Protected Dashboard
    headers = {"Authorization": f"Bearer {token}"}
    resp = requests.get(f"{BASE_URL}/api/dashboard", headers=headers)
    if resp.status_code == 200:
        print("[PASS] Protected Dashboard")
    else:
        print(f"[FAIL] Protected Dashboard: {resp.text}")

    # 5. Test CRUD (Create Person)
    person_data = {"nama": "Budi", "umur": 30, "alamat": "Jakarta"}
    resp = requests.post(f"{BASE_URL}/api/people", json=person_data, headers=headers)
    if resp.status_code == 201:
        print("[PASS] Create Person")
        person_id = resp.json()['data']['id']
    else:
        print(f"[FAIL] Create Person: {resp.text}")
        person_id = None

    # 6. Test CRUD (Get Person)
    resp = requests.get(f"{BASE_URL}/api/people")
    if resp.status_code == 200:
        print("[PASS] Get People")
    else:
        print(f"[FAIL] Get People: {resp.text}")

    print("Verification Finished.")

if __name__ == "__main__":
    test_api()
