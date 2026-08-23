"""
user_store.py
-------------
Persists manually registered users to JSON so IDs survive restarts.
The generated mock users are recreated at startup.
"""

import json
import os
from typing import List

from .models import User

_HERE = os.path.dirname(os.path.abspath(__file__))
STORE_PATH = os.path.join(_HERE, "..", "registered_users.json")


def load_registered_users() -> List[User]:
    if not os.path.exists(STORE_PATH):
        return []
    try:
        with open(STORE_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [
            User(
                user_id=entry["user_id"],
                name=entry["name"],
                is_vip=entry.get("is_vip", False),
                attendance=entry.get("attendance", 0.0),
            )
            for entry in data
        ]
    except (json.JSONDecodeError, KeyError, TypeError):
        return []


def save_new_user(user: User) -> None:
    existing = load_registered_users()
    if any(u.user_id == user.user_id for u in existing):
        return
    existing.append(user)
    _write(existing)


def _write(users: List[User]) -> None:
    with open(STORE_PATH, "w", encoding="utf-8") as f:
        json.dump(
            [
                {
                    "user_id": u.user_id,
                    "name": u.name,
                    "is_vip": u.is_vip,
                    "attendance": u.attendance,
                }
                for u in users
            ],
            f,
            indent=2,
        )
