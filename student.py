class Student:

    def __init__(self, full_name, age, level, mobile, s_id=None):
        self.id = s_id
        self.full_name = full_name
        self.age = age
        self.level = level
        self.mobile = mobile

    def to_string(self):
        return 'id : ' + str(self.id) + '   ' + 'full_name : ' + str(self.full_name) + '   ' + 'age : ' + str(
            self.age) + '   ' + 'level : ' + str(self.level) + '   ' + 'mobile_number : ' + str(self.mobile) + "\n"
