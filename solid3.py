#Liskov Substitution Principle

class KitchenAppliance():
    def on():
        pass
    def off():
        pass

class KitchenApplianceWithTemp(KitchenAppliance):
    def set_temp():
        pass

class Toaster(KitchenApplianceWithTemp):
    def on():
        pass
    def off():
        pass
    def set_temp():
        pass

class Juicer(KitchenApplianceWithTemp):
    def on():
        pass
    def off():
        pass