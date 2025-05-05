from .product_model import Product

class InventoryManager:
    """
    Manages the inventory of products, including adding, removing, saving, 
    loading, and retrieving products.

    Attributes:
        products (list[Product]): A list of products in the inventory.
        currentId (int): The current product ID being processed.
    """

    def __init__(self):
        """
        Initializes a new instance of the InventoryManager class.
        """
        self.products = []
        self.currentId = None

    def addProduct(self, product: Product):
        """
        Adds a new product to the inventory.

        Args:
            product (Product): The product to be added.
        """
        pass

    def removeProduct(self, productId: int):
        """
        Removes a product from the inventory by its ID.

        Args:
            productId (int): The ID of the product to be removed.
        """
        pass

    def saveProducts(self):
        """
        Saves the current list of products to persistent storage.
        """
        pass

    def loadProducts(self):
        """
        Loads the list of products from persistent storage.
        """
        pass

    def getProduct(self, productId: int) -> Product:
        """
        Retrieves a product from the inventory by its ID.

        Args:
            productId (int): The ID of the product to retrieve.

        Returns:
            Product: The product with the specified ID, or None if not found.
        """
        pass