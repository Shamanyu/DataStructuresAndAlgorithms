import json
import fileinput


class BoilerPlateCode(object):

    def get_boiler_plate_code(self):
        boiler_plate_code = """class %s(object):

    def %s(self):
        pass


from nose.tools import assert_equals, assert_raises


class %s(object):

    def %s(self):
        %s = %s()

        print("All test cases passed!")


def main():
    %s = %s()
    %s.%s()


if __name__ == '__main__':
    main()"""
        return boiler_plate_code

    def generate_boiler_plate(self, raw_data):
        raw_json_data = json.loads(raw_data)
        class_name_length = len(raw_json_data["className"])
        class_name = str(raw_json_data["className"][0]).capitalize()
        class_method = str(raw_json_data["className"][0])
        for counter in range(1, class_name_length):
            class_name += str(raw_json_data["className"][counter]).capitalize()
            class_method += ('_' + str(raw_json_data["className"][counter]))
        class_instance = class_method + '_instance'
        test_class_name = 'Test' + class_name
        test_class_method = 'test_'+class_method
        test_class_instance = test_class_method + '_instance'
        boiler_plate_code = self.get_boiler_plate_code()
        print(boiler_plate_code % (class_name, class_method,
              test_class_name, test_class_method, class_instance, class_name,
              test_class_instance, test_class_name, test_class_instance, test_class_method))


def main(file_input):
    boiler_plate_generator = BoilerPlateCode()
    boiler_plate_generator.generate_boiler_plate(file_input)


if __name__ == '__main__':
    main(''.join(fileinput.input()))
