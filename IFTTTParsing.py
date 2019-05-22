import re

#
# class temperature:
#     def __init__(self, x):
#         self.state = x
#
#
# class air_conditioner:
#     def __init__(self):
#         self.state = 0


class ConditionStruct:
    def __init__(self, subject: str, operator: str, value):
        self.subject = subject
        self.operator = operator
        self.value = value

    def printConditionStruct(self):
        print(self.subject + ' ' + self.operator + ' ' + self.value)


def IFTTTParser(strings, valid_abstract: dict):
    '''
    :param str: Input IFTTT rules
    :param valid_abstract: Existing abstracts, devices and room statues
    :param rule_collector: A list save IFTTT rule as tuples
    :return: None
    '''
    if_sentence, then_sentence = re.split(r"\b(if|then)\b", strings)[2], re.split(r"\b(if|then)\b", strings)[4] # split IFTTT

    if_sentence = re.split(r"\b(and)\b", if_sentence) # split multiple conditions
    while "and" in if_sentence:
        if_sentence.remove("and")
    if_conditions = [] # use to store "condition structures"
    valid_attribute_flag = 1 # use to determine that the whole sentence is valid in terms of attributes
    # print(source)
    for each in if_sentence:
        subject, operator, value = re.split(r"[ ]", each.strip())
        # print(subject, operator, value)

        # Determine whether the subject is valid. E.g. whether temprature.val is per-defined
        class_name, attr_name = subject.split(".")
        # if_valid_attributes = valid_abstract.get(class_name, [])
        # if attr_name not in if_valid_attributes:
        #     valid_attribute_flag = 0
        #     print("{}.{} is not a valid source attribute.".format(class_name, attr_name))

        if_conditions.append(ConditionStruct(subject, operator, value))

    then_sentence = re.split(r"\b(and)\b", then_sentence)  # split multiple conditions
    while "and" in then_sentence:
        then_sentence.remove("and")
    then_conditions = []  # use to store "condition structures"
    for each in then_sentence:
        subject, operator, value = re.split(r"[ ]", each.strip())
        # print(subject, operator, value)

        # Determine whether the subject is valid. E.g. whether temprature.val is per-defined
        class_name, attr_name = subject.split(".")
        # then_valid_attributes = valid_abstract.get(class_name, [])
        # if attr_name not in then_valid_attributes:
        #     valid_attribute_flag = 0
        #     print("{}.{} is not a valid source attribute.".format(class_name, attr_name))

        then_conditions.append(ConditionStruct(subject, operator, value))

    if valid_attribute_flag:
        rule_tuple = (if_conditions, then_conditions)
        return rule_tuple
    else:
        return None
if __name__ == '__main__':
    strings = "if temperature.val >= 70 and humidity.val <= 12 then air_conditioner.state = 1 and humidifier.state = 1"
    strings_2 = "if humidity.val >= 80 then ventilation_fan.state = 1"
    valid_abstract = {"temperature":["val"], "air_conditioner":["state", "power_consump"],
                      "humidity":["val"], "humidifier":["state"]}
    rule_collector = []
    rule_tuple = IFTTTParser(strings, valid_abstract)
    if rule_tuple is not None:
        rule_collector.append(rule_tuple)
    rule_tuple = IFTTTParser(strings_2, valid_abstract)
    if rule_tuple is not None:
        rule_collector.append(rule_tuple)
    print(rule_collector)
