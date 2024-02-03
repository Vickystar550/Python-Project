class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        
    def add_items(self, name, price):
        self.items.append({
            "name": name,
            "price": price
        })
        
    def stock_price(self):
        return sum([i["price"] for i in self.items])
    
    @classmethod
    def franchise(cls, store):
        return cls(store.name + "- franchise")
    
    @staticmethod
    def store_details(store):
        return f"{store.name}, total stock price: {int(store.stock_price())}"
    









store = Store("Test")
store2 = Store("Amazon")
store2.add_items("keyboard", 160)

print(Store.franchise(store))