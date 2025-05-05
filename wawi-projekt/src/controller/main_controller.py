from model.inventory_manager_model import InventoryManager
from model.product_model import Product
from view.product_form_view import ProductFormView

class MainController:
    """
    The MainController class acts as the central controller of the application.

    It connects the view (ProductFormView) with the model (InventoryManager) 
    and handles user interactions, such as adding or removing products.

    Attributes:
        inventory_manager (InventoryManager): Manages the inventory of products.
        view (ProductFormView): The graphical user interface for product management.

    Methods:
        __init__(): Initializes the MainController instance.
        addProduct(product: Product): Adds a new product to the inventory.
        removeProduct(productId: int): Removes a product from the inventory by its ID.
        start(): 
    """
    def __init__(self):
        """
        Initializes a new instance of the MainController class.

        Attributes:
            inventory_manager (InventoryManager): An instance of InventoryManager to manage products.
            view (ProductFormView): An instance of ProductFormView to handle the user interface.
        """
        self.inventory_manager = InventoryManager()
        self.view = ProductFormView()


    def addProduct(self, product: Product):
        """
        Adds a new product to the inventory.
        """

        
    def removeProduct(self, productId: int):
        """
        Removes a product from the inventory by its ID.
        """

    
    def start(self):
        pass
        