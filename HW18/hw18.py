import json
import xml.etree.ElementTree as ET


class Human:

    def __init__(self, name, age, gender, birth_year):
        self.name = name
        self.age = age
        self.gender = gender
        self.birth_year = birth_year

    def convert_to_json(self):
        with open("user_data.json", "w") as file:
            return file.writelines(json.dumps(self.__dict__))

    def to_xml(self):
        root = ET.Element(type(self).__name__)
        for attr, value in self.__dict__.items():
            child = ET.SubElement(root, attr)
            child.text = str(value)
        xml_str = ET.tostring(root).decode()
        xml_str = xml_str.replace("><", ">\n<")
        with open(f"{type(self).__name__}.xml", "w") as f:
            f.write(xml_str)


if __name__ == '__main__':
    dude = Human("Misha", 30, "male", 1992)
    dude.convert_to_json()
    dude.to_xml()

