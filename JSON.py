"""JSON :- JavaScript Object Notation"""
# The conversion of Python to JSON is called Serialization or Encoding.
# The conversion of JSON to Python is called Deserialization or Decoding.

# Python is translated into JSON according to the following:
# dict :- object      list, tuple :- array      str :- strings       int, float :- number     True :- true     False :- false    None :- null

import json

# Python dictionary to JSON object.

citizen = dict(name="Kev", age=27, graduate= True, profession=["Engineer", "Programmer"])

ctzn = json.dumps(citizen, indent=2,                                  # Indent specifies the space from the left.
                  #separators=(":", "="),                              # Seperators define the seperating string between key and value.
                  sort_keys=False)                                    # Sorts in alphanumeric order.
print(ctzn)                                    # [1,9]

with open("JSON.txt", "w") as json_var:                               # Printing the JSON code in an external file.
    ctzn_file = json.dump(citizen, fp=json_var,  indent= 2)


# JSON object to Python dictionary.
boy ='''{
  "name": "Dave",
  "age": 26,
  "graduate": false,
  "profession": [
    "Cook",
    "Painter"
  ]
}
'''
person = json.loads(boy)                                               # Modifications made to the JSON code will affect the Python code as well.
print(person)                                  # [2]                   # The separator must be ':' or else it'll throw an error.

for i in person:                                                       # Printing the keys of the object.
    print(i)                                   # [3, 4]

with open("JSON.txt", "r") as json_var2:                               # Extracting and converting a JSON code to Python from external file.

    ctzn_file_py = json.load(json_var2)
    print(ctzn_file_py)                        # [4]


# Python Class to JSON object : Using a custom encoder

class Student:
    def __init__(self, name, age, graduate):
        self.name = name
        self.age = age
        self.grad = graduate

stud = Student("Max", 21, False)

def C_encoder(o):                                                      # A custom encoding function that takes in an object (o).
    if isinstance(o, Student):                                         # Checks if the object is an instance of the class.
        return {"Name": o.name, 'Age': o.age,                          # An object(dict) with keys and class values.
                "Graduate": o.grad, o.__class__.__name__: "Yess"}      # Accessing the name of the class as well

json_encode = json.dumps(stud, default=C_encoder)                      # Using the custom function as an JSON encoder.
print(json_encode)                               # [5]


# Python Class to JSON object : Using JSONEncoder

from json import JSONEncoder

class ecode(JSONEncoder):

    def default(self, i):                                              # Uses the class from the previous method.
        if isinstance(i, Student):
            return {"Name": i.name, 'Age': i.age, "Graduate": i.grad, i.__class__.__name__: "Yess"}
        return JSONEncoder.default(self, i)

json_encode2 = json.dumps(stud, cls=ecode)                             # Using the JSONEncoder class as encoder.
json_encode3 = ecode().encode(stud)                                    # Directly using the encoder class.
print(json_encode2, json_encode3)                # [6]                 # Both print the same output.


# JSON object to Python dict from class inputs :

json_decode = json.loads(json_encode2)                                 # Converting the JSON object from previously decoded dictionary.
print(json_decode)                               # [7]
