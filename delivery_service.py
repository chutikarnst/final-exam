class Person():
    def __init__(self,name):
        self.name = name

    def introduce(self):
        print(f"Hi, I'm {self.name}.")

class Customer(Person):
    def __init__(self,name,address):
        super().__init__(name)
        self.address = address

    def place_order(self,item):
        return DeliveryOrder(self.name,item)

class Driver(Person):
    def __init__(self,name,vehicle):
        super().__init__(name)
        self.vehicle = vehicle

    def deliver(self,order):
        print(f"{self.name} is delivering {order.item} to {order.customer} using {self.vehicle}.")
        order.status = "delivered"

class DeliveryOrder():
    def __init__(self,customer,item):
        self.customer = customer
        self.item = item
        self.status = "preparing"

    def assign_driver(self,driver):
        self.driver = driver.name

    def summary(self):
        if self.status == "preparing":
            return f"Order Summary:\n"\
            f"Item: {self.item}\n"\
            f"Customer: {self.customer}\n"\
            f"Status: {self.status}\n"\
            f"Driver: {self.driver}"
        
if __name__ == "__main__":
    Alice = Customer("Alice", "Wonderland")
    Bob = Customer("Bob","Cave")
    David = Driver("David","motorcycle")

    Alice.introduce()
    Bob.introduce()
    David.introduce()
    print()
    order1 = Alice.place_order("Laptop")
    order2 = Bob.place_order("Headphones")
    order1.assign_driver(David)
    order2.assign_driver(David)
    
    print(order1.summary())
    print()
    print(order2.summary())
    print()

    David.deliver(order1)
    David.deliver(order2)
    print()

    print("Final Status:")
    print(f"Order for {order1.item} → {order1.status}")
    print(f"Order for {order2.item} → {order2.status}")
