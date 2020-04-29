#######################################################
#           This library made by Ali Daho
#           Purpose of this lib, it is for password
#           and create a hash
#######################################################

class Coded:
    def __init__(self, info):
        self.info = info

        #Split function
    def split(self):
        return [char for char in self.info]

        #Store it into new variable
    def convert_list(self):
        values_list = self.split()
        return values_list

        #Convert new list into ascii
    def convert_ascii(self):
        new_list = self.convert_list()
        total = 0
        for value in new_list:
            value = ord(new_list[total])
            new_list[total] = value
            total+=1
        return new_list

        #Apply math : sum((p[i]/n)*100)<n=>total, i=0>
    def apply_algo(self):
        hash = 0
        total_number = 0
        new_list = self.convert_ascii()
        for value in new_list:
            hash += new_list[total_number]/40*100*10000
            total_number+=1
        return hash
