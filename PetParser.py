import json

class Pet:
    def __init__(self, id, name, status):
        self.id = id
        self.name = name
        self.status = status

    @staticmethod
    def from_json(json_data):
        return Pet(
            id=json_data.get('id'),
            name=json_data.get('name'),
            status=json_data.get('status')
        )

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status
        }
