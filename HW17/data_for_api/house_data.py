import json


class HouseData:
    def __init__(self, **kwargs):
        self.name = "Gryffindor" if "name" not in kwargs.keys() else kwargs['name']
        self.founder = "Godric Gryffindor" if "blood" not in kwargs.keys() else kwargs['blood']
        self.ghost = "Nearly-Headless Nick" if "marital" not in kwargs.keys() else kwargs['marital']
        self.common_room = "Gryffindor Tower" if "boggart" not in kwargs.keys() else kwargs['boggart']
        self.best_students = ['Hermione Hranger', 'Harry Potter',
                              'Sirius Black'] if "best_students" not in kwargs.keys() else kwargs['best_students']

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
