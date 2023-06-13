from bson.objectid import ObjectId
from pymongo.database import Database


class ShanyrakRepository:
    def __init__(self, database: Database):
        self.database = database

    def create_shanyrak(self, input: dict):
        payload = {
            "type": input['type'],
            "price": input['price'],
            "address": input['address'],
            "area": input['area'],
            "rooms_count": input['rooms_count'],
            "description": input['description'],
            "user_id": input['user_id']
        }

        self.database['shanyraks'].insert_one(payload)

    def get_shanyrak(self, user_id: str, shanyrak_id: str):
        shanyraq = self.database["shanyraks"].find_one(
            {
                "_id": ObjectId(shanyrak_id),
            }
        )

        if (shanyraq['user_id'] == user_id):
            return shanyraq

    def update_shanyrak(self, id: str, data: dict):
        self.database['shanyraks'].update_one(
            filter={"_id": ObjectId(id)},
            update={
                "$set": data
            }
        )