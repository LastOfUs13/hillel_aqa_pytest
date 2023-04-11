import json


class CharacterData:
    def __init__(self, **kwargs):
        self.name = "Sirius Black" if "name" not in kwargs.keys() else kwargs['name']
        self.blood = "Pure-blood" if "blood" not in kwargs.keys() else kwargs['blood']
        self.marital = "Single" if "marital" not in kwargs.keys() else kwargs['marital']
        self.boggart = "Lord Voldemort" if "boggart" not in kwargs.keys() else kwargs['boggart']
        self.animagus = "Black dog" if "animagus" not in kwargs.keys() else kwargs['animagus']
        self.graduate = "Gryffindor" if "graduate" not in kwargs.keys() else kwargs['Gryffindor']

    @classmethod
    def from_json(cls, **kwargs):
        return cls(**kwargs)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def get_json(self):
        return json.dumps(self.__dict__)

    def update_data(self, **kwargs):
        self.__dict__.update(**kwargs)

    def get_dict(self):
        return self.__dict__
