import os
from config import db
from models.User import User


USERS = [
    {
        "id": 1,
        "first_name": "Lisabeth",
        "last_name": "Nicolson",
        "email": "lnicolson0@bluehost.com",
        "password": "11111111",
        "created_at": "Female",
        "updated_at": "103.4.2.201"
    }, {
        "id": 2,
        "first_name": "Ted",
        "last_name": "Leathley",
        "email": "tleathley1@whitehouse.gov",
        "password": "22222222",
        "created_at": "Female",
        "updated_at": "103.136.116.116"
    }, {
        "id": 3,
        "first_name": "Meriel",
        "last_name": "Keitch",
        "email": "mkeitch2@google.co.jp",
        "password": "33333333",
        "created_at": "Female",
        "updated_at": "8.109.178.17"
    }, {
        "id": 4,
        "first_name": "Vic",
        "last_name": "Dugan",
        "email": "vdugan3@webeden.co.uk",
        "password": "44444444",
        "created_at": "Male",
        "updated_at": "22.120.100.179"
    }, {
        "id": 5,
        "first_name": "Kipper",
        "last_name": "Keele",
        "email": "kkeele4@lycos.com",
        "password": "55555555",
        "created_at": "Male",
        "updated_at": "12.236.118.203"
    }, {
        "id": 6,
        "first_name": "Brion",
        "last_name": "Guys",
        "email": "bguys5@weather.com",
        "password": "66666666",
        "created_at": "Male",
        "updated_at": "112.66.193.101"
    }, {
        "id": 7,
        "first_name": "Dun",
        "last_name": "Kemmett",
        "email": "dkemmett6@cisco.com",
        "password": "77777777",
        "created_at": "Male",
        "updated_at": "78.49.219.8"
    }, {
        "id": 8,
        "first_name": "Nolie",
        "last_name": "Yoxen",
        "email": "nyoxen7@networkadvertising.org",
        "password": "88888888",
        "created_at": "Female",
        "updated_at": "119.223.108.251"
    }, {
        "id": 9,
        "first_name": "Brandon",
        "last_name": "Stollenbecker",
        "email": "bstollenbecker8@theguardian.com",
        "password": "99999999",
        "created_at": "Male",
        "updated_at": "134.233.188.41"
    }, {
        "id": 10,
        "first_name": "Katerine",
        "last_name": "Brandle",
        "email": "kbrandle9@shop-pro.jp",
        "password": "00000000",
        "created_at": "Female",
        "updated_at": "252.41.22.158"
    }
]

if os.path.exists("budget.db"):
    os.remove("budget.db")

db.create_all()


for user in USERS:
    u = User(
        user.get("email"),
        user.get("password"),
        user.get("first_name"),
        user.get("last_name"),
    )
    db.session.add(u)

db.session.commit()
