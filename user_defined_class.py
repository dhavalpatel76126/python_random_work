class Worker:
    def __init__(self,name):
        self.name=name
        
    def last_name(self):
        return self.name.split()[-2]

    

bob=Worker('dhaval patel')
bob.last_name()
print(bob.last_name())
