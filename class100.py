class Car(object):
    def __init__(self, model, color, company, speed):
        self.model = model
        self.color = color
        self.company = company
        self.speed = speed
    def start(self):
        print(self.model)
    def stop(self):
        print(self.company)
    
etios =  Car("etios","gray","toyota", 1000)
creta =  Car("creta","white","hyundai", 1000)
print(etios.start())
print(etios.stop())
print(creta.start())
print(creta.stop())
    