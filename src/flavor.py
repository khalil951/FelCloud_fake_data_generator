class Flavor:
    def __init__(self, name , vcpu, ram, disk, price):
        self.name = name
        self.vcpu = vcpu
        self.ram = ram
        self.disk = disk
        self.price = price

    def describe(self):
        print(f"Name: {self.name}")
        print(f"VCPU: {self.vcpu}")
        print(f"Ram: {self.ram}")
        print(f"Disk: {self.disk}")
        print(f"Price: {self.price}")
        print("")  

class SmallFlavor(Flavor):
    def __init__(self):
        super().__init__(name  = "Atto.S" , vcpu=1, ram=1.0, disk=20, price=0.0070)

    def describe(self):
        super().describe()


class MediumFlavor(Flavor):
    def __init__(self):
        super().__init__(name ="Micro.S" , vcpu=12, ram=8.0, disk=300, price=0.2000)

    def describe(self):
        super().describe()

class LargeFlavor(Flavor):
    def __init__(self):
        super().__init__(name ="RAM.XL" , vcpu=16, ram=64.0, disk=200 , price=0.3900)

    def describe(self):
        super().describe() 

class XXLFlavor(Flavor):
    def __init__(self):
        super().__init__(name = "RAM.XXXL", vcpu=48, ram=128.0, disk=500, price=0.8500)

    def describe(self):
        super().describe()    