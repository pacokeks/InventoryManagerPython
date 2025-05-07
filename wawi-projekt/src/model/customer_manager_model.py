from .customer_model import Customer
import os
import json

class CustomerManager:
    """
    CustomerManager is responsible for managing customer data.
    It provides methods to add, remove, save, load, and retrieve customers.
    
    Attributes:
        customers (list): A list of Customer objects.
        currentId (int): The ID of the currently selected customer.
        path (str): Path to the customer data file.
        
    Methods:
        addCustomer(customer): Adds a new customer to the database.
        removeCustomer(customerId): Removes a customer based on their ID.
        saveCustomer(): Saves the customers to a file.
        loadCustomers(): Loads the customers from a file.
        getCustomer(customerId): Retrieves a customer based on their ID.
    """
    def __init__(self):
        """
        Initializes the CustomerManager with an empty customer list and sets the currentId to 0.
        """
        self.customers = []
        self.currentId = 0
        self.path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "customers.json")
        self.loadCustomers()

    def addCustomer(self, customer: Customer):
        """
        Adds a new customer to the database.
        
        Args:
            customer (Customer): The customer to be added.
        """
        self.currentId += 1
        customer.customerId = self.currentId
        self.customers.append(customer)
        self.saveCustomer()

    def removeCustomer(self, customerId: int):
        """
        Removes a customer from the database based on their ID.
        
        Args:
            customerId (int): The ID of the customer to be removed.
        """
        self.customers = [customer for customer in self.customers if customer.customerId != customerId]
        self.saveCustomer()

    def saveCustomer(self):
        """
        Saves the customers to a file.
        """
        try:
            os.makedirs(os.path.dirname(self.path), exist_ok=True)
            
            with open(self.path, 'w') as file:
                json.dump([customer.toDict() for customer in self.customers], file)
        except Exception as e:
            print(f"Customer data could not be saved as .json in {self.path}! Error: {e}")
            
    def loadCustomers(self):
        """
        Loads the customers from a file.
        Sets currentId to the highest existing customerId.
        """
        try:
            with open(self.path, 'r') as file:
                data = json.load(file)
                self.customers = []
                max_id = 0
                for elem in data:
                    elem_dict = dict(elem)
                    try:
                        loaded_customer = Customer(
                            elem_dict["name"],
                            elem_dict["address"],
                            elem_dict["email"],
                            elem_dict["phone"],
                            elem_dict["customerId"]
                        )
                        self.customers.append(loaded_customer)
                        if loaded_customer.customerId > max_id:
                            max_id = loaded_customer.customerId
                    except (KeyError, ValueError) as e:
                        print(f"Error loading customer: {e}")
                self.currentId = max_id
        except (FileNotFoundError, json.JSONDecodeError):
            print(f"Customer file could not be accessed or does not exist yet!")
            self.customers = []
            self.currentId = 0

    def getCustomer(self, customerId: int) -> Customer:
        """
        Retrieves a customer from the database based on their ID.
        
        Args:
            customerId (int): The ID of the customer to be retrieved.
            
        Returns:
            Customer: The customer object if found, otherwise None.
        """
        for customer in self.customers:
            if customer.customerId == customerId:
                return customer
        return None