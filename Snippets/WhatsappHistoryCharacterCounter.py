import re

people_characters_typed_dict = dict()

regular_expression = "(.*- )(.*): (.*)"

with open("/home/shamanyu/Downloads/Nisha2.txt") as f:
    for line in f:
        parsed_data = re.search(r"(.*- )(.*): (.*)", line)
        if parsed_data:
            typer = parsed_data.group(2)
            length_of_message = len(parsed_data.group(3))
            #print typer, length_of_message
            try:
                people_characters_typed_dict[typer] = people_characters_typed_dict[typer] + length_of_message
            except KeyError:
                people_characters_typed_dict[typer] = length_of_message

for person in people_characters_typed_dict:
    print "Person ", person, " has typed ", people_characters_typed_dict[person], " characters"
