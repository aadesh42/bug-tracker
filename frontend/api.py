import requests
from config import API_BASE_URL


def login(username, password):
    res = requests.post(
        f"{API_BASE_URL}/auth/login",
        json={"username": username, "password": password}
    )
    return res.json()


def create_bug(token, data):
    return requests.post(
        f"{API_BASE_URL}/bugs",
        headers={"Authorization": f"Bearer {token}"},
        json=data
    ).json()


def get_bugs(token):
    return requests.get(
        f"{API_BASE_URL}/bugs",
        headers={"Authorization": f"Bearer {token}"}
    ).json()


def update_bug_status(token, bug_id, status):
    return requests.patch(
        f"{API_BASE_URL}/bugs/{bug_id}/status",
        headers={"Authorization": f"Bearer {token}"},
        json={"status": status}
    ).json()
