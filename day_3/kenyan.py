import person
''' import  person module'''

class Kenyan(person.Person):
	'''
	class kenyan that inherits from person
	'''

    def probe(self, corrupt):
    	self.corrupt = corrupt

    def is_corrupt(self):
        if self.corrupt:
            return "Yes"
        return "No"
