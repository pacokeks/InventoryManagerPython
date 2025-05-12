# WaWi - Warehouse Management System

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

WaWi (short for Warehouse Management) is a comprehensive desktop application designed for small to medium-sized businesses to manage their inventory and customer data. Built with Python and PyQt5, this application implements solid object-oriented programming principles and design patterns to provide a robust, maintainable solution for warehouse management.

![WaWi Screenshot](screenshots/wawi-screenshot.png)

## Features

### Product Management
- **Add Products**: Create new product entries with validation for name, price, and quantity
- **View Products**: Browse all products in a list view with detailed information
- **Remove Products**: Delete single or multiple products at once with optional silent mode
- **Price Handling**: Supports both decimal point and comma notation (e.g., 10.99 or 10,99)
- **Stock Tracking**: Monitor inventory levels with quantity tracking
- **Data Validation**: Built-in validation ensures data integrity

### Customer Management
- **Add Customers**: Store comprehensive customer information
- **View Customers**: Browse and search customer records
- **Remove Customers**: Delete customer records individually or in batch operations
- **Contact Information**: Store name, address, email, and phone information
- **Email Validation**: Ensures properly formatted email addresses

### Database System
- **Dual Database Support**: 
  - **SQLite**: Lightweight file-based database for single-user scenarios
  - **MariaDB/MySQL**: Robust server-based solution for multi-user environments
- **Configuration Interface**: User-friendly dialog for database settings
- **Connection Testing**: Built-in test functionality to verify database connectivity
- **Automatic Initialization**: Creates required tables and structures automatically
- **Connection Pooling**: Efficient database connection management

### User Interface
- **Tab-Based Navigation**: Intuitive switching between product and customer management
- **Form Validation**: Real-time feedback on input errors
- **Batch Operations**: Multi-select capability for efficient bulk actions
- **Silent Mode Operations**: Option to suppress confirmation messages for experienced users
- **Tooltips**: Contextual help throughout the interface
- **Consistent Design**: Uniform appearance and behavior across all application sections

## Architecture

WaWi implements a strict Model-View-Controller (MVC) architectural pattern to ensure separation of concerns and maintainability:

### Model Layer
- **Base Classes**:
  - `BaseModel`: Abstract base class for all model entities with common functionality
  - `BaseManager`: Abstract base class for database operations with template method pattern

- **Entity Models**:
  - `Product`: Represents inventory items with name, price, and quantity attributes
  - `Customer`: Stores customer data with validation for email format

- **Managers**:
  - `ProductManager`: Handles CRUD operations for products
  - `CustomerManager`: Manages customer data persistence

- **Database Abstraction**:
  - `DatabaseInterface`: Abstract interface ensuring consistent database access
  - `MariaDBConnection`: Adapter for MariaDB/MySQL databases
  - `SQLiteConnection`: Adapter for SQLite databases
  - `DatabaseConnectionFactory`: Factory pattern implementation for creating appropriate connections
  - `DatabaseConfig`: Configuration management with JSON persistence

### View Layer
- **Base Classes**:
  - `BaseFormView`: Template for all form-based views with common UI elements

- **Specialized Views**:
  - `ProductFormView`: UI for product management
  - `CustomerFormView`: UI for customer management
  - `DatabaseSettingsDialog`: Configuration interface for database settings

### Controller Layer
- `MainController`: Central controller managing application flow and connecting models with views
- Implements event handling for all user interactions

## Implementation Details

### Database Layer

The application uses a sophisticated database abstraction layer:

- **Adapter Pattern**: Both `MariaDBConnection` and `SQLiteConnection` implement the same `DatabaseInterface`
- **Strategy Pattern**: Database strategy can be switched at runtime without affecting other components
- **Factory Pattern**: `DatabaseConnectionFactory` creates the appropriate connection based on configuration
- **Singleton-like Configuration**: `DatabaseConfig` manages a centralized configuration with JSON persistence
- **Query Repository**: `DatabaseQueries` centralizes all SQL queries for maintainability

### Error Handling

Robust error handling is implemented throughout the application:

- **Exception Handling**: Appropriate try-except blocks with specific error types
- **Logging**: Comprehensive logging through `LoggerService` with configurable levels
- **User Feedback**: Clear error messages displayed to users
- **Graceful Degradation**: Falls back to SQLite if MariaDB connection fails

### Code Structure

The project follows clean code principles:

- **DRY (Don't Repeat Yourself)**: Common functionality extracted to base classes
- **SOLID Principles**:
  - Single Responsibility: Each class has a single purpose
  - Open/Closed: Base classes allow extension without modification
  - Liskov Substitution: Derived classes can be used in place of base classes
  - Interface Segregation: Clean interfaces with specific purposes
  - Dependency Inversion: High-level modules depend on abstractions

- **Documentation**: Comprehensive docstrings for all classes and methods
- **Type Hints**: Python type annotations used throughout the codebase

## Prerequisites

- **Python**: Version 3.6 or higher
- **PyQt5**: For the graphical user interface
- **MariaDB Connector** (optional): Required only if using MariaDB backend
- **SQLite3**: Included in Python standard library

## Installation

### Standard Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/wawi-projekt.git
cd wawi-projekt
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
# Or install directly
pip install PyQt5 mariadb
```

4. Run the application:
```bash
python view/main.py
```

### Development Setup

For development, additional packages are recommended:

```bash
pip install pytest pytest-qt pylint black
```

## Database Configuration

### SQLite (Default)

SQLite is the default database engine and requires minimal configuration:

- The database file is automatically created at `data/wawi.db`
- Tables are created on first run if they don't exist
- No additional setup is required

To customize the SQLite database location:

1. Go to `File` > `Database Settings`
2. Select `SQLite` as the database type
3. Click `Browse...` to select a different file location
4. Click `Test Connection` to verify
5. Click `Save` to apply the settings

### MariaDB/MySQL

For multi-user environments or larger deployments, MariaDB or MySQL is recommended:

1. Install and configure MariaDB/MySQL server
2. Create a new database:
```sql
CREATE DATABASE wawi CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

3. Create a user and grant permissions:
```sql
CREATE USER 'wawi_user'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON wawi.* TO 'wawi_user'@'localhost';
FLUSH PRIVILEGES;
```

4. In the WaWi application, go to `File` > `Database Settings`
5. Select `MariaDB` as the database type
6. Enter your connection details:
   - Host: `localhost` (or your server address)
   - Port: `3306` (default MariaDB port)
   - User: `wawi_user`
   - Password: `your_password`
   - Database: `wawi`
7. Click `Test Connection` to verify connectivity
8. Click `Save` to apply the settings

The application will automatically create the necessary tables on first run.

## Project Structure

The application follows a structured directory layout matching the MVC pattern:

```
wawi-projekt/
├── controller/                  # Controllers
│   └── main_controller.py       # Main application controller
│
├── data/                        # Data storage
│   ├── db_config.json           # Database configuration file
│   └── wawi.db                  # SQLite database (if used)
│
├── model/                       # Model layer
│   ├── __init__.py              # Package initialization
│   ├── app_info.py              # Application metadata and help texts
│   ├── base_manager.py          # Abstract base manager class
│   ├── base_model.py            # Abstract base model class
│   ├── customer_manager.py      # Customer data operations
│   ├── customer_model.py        # Customer entity
│   ├── database_config.py       # Database configuration handler
│   ├── database_connection_factory.py  # Connection factory
│   ├── database_interface.py    # Database abstract interface
│   ├── database_queries.py      # SQL query definitions
│   ├── logger_service.py        # Logging service
│   ├── mariadb_connection.py    # MariaDB adapter
│   ├── product_manager.py       # Product data operations
│   ├── product_model.py         # Product entity
│   └── sqlite_connection.py     # SQLite adapter
│
└── view/                        # View layer
    ├── __init__.py              # Package initialization
    ├── base_form_view.py        # Base class for form views
    ├── customer_form_view.py    # Customer form UI
    ├── database_settings_dialog.py  # Database configuration dialog
    ├── product_form_view.py     # Product form UI
    └── main.py                  # Application entry point
```

## Extending the Application

### Adding New Entity Types

The application is designed for easy extension. To add a new entity type (e.g., Suppliers):

1. **Create Model Class**:
```python
# model/supplier_model.py
from model.base_model import BaseModel

class Supplier(BaseModel):
    def __init__(self, name, contact_person, email, phone, id=None):
        super().__init__(id)
        self.name = name
        self.contact_person = contact_person
        self.email = email
        self.phone = phone
        
        self.validate()
        
    def validate(self):
        if not self.name:
            raise ValueError("Supplier name cannot be empty.")
        # Additional validation as needed
```

2. **Create Manager Class**:
```python
# model/supplier_manager.py
from model.base_manager import BaseManager
from model.supplier_model import Supplier

class SupplierManager(BaseManager):
    def __init__(self, db_connection):
        super().__init__(db_connection, Supplier)
        self.load_all()
    
    def get_table_name(self) -> str:
        return "suppliers"
    
    def model_to_db_mapping(self) -> dict:
        return {
            "name": "name",
            "contact_person": "contact_person",
            "email": "email", 
            "phone": "phone"
        }
    
    def db_to_model_factory(self, db_row: dict) -> Supplier:
        return Supplier(
            name=db_row['name'],
            contact_person=db_row['contact_person'],
            email=db_row['email'],
            phone=db_row['phone'],
            id=db_row['supplier_id']
        )
```

3. **Add Database Table Definition**:
```python
# Update model/database_queries.py by adding to create_tables_query()
'''
CREATE TABLE IF NOT EXISTS suppliers (
    supplier_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    contact_person VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    phone VARCHAR(50) NOT NULL
)
'''
```

4. **Create View Class**:
```python
# view/supplier_form_view.py
from PyQt5.QtWidgets import QLineEdit, QLabel
from view.base_form_view import BaseFormView

class SupplierFormView(BaseFormView):
    def __init__(self):
        super().__init__("Supplier")
        self._setupFormFields()
    
    # Implementation details...
```

5. **Update MainController**:
Add the new entity to the controller to integrate it with the application.

### Adding New Features

To add new features to existing entities:

1. **Update Models**: Add new attributes and validation logic
2. **Update Database**: Modify table definitions in `database_queries.py`
3. **Update Views**: Add UI elements to display/edit new attributes
4. **Update Controllers**: Implement business logic for new features

## Usage Examples

### Product Management

```python
# Create a new product
product = Product(name="Laptop", price=999.99, quantity=10)

# Add to database
product_manager = ProductManager(db_connection)
product_manager.add(product)

# Update product quantity
product.quantity = 15
product_manager.update(product)

# Get all products
all_products = product_manager.items
```

### Customer Management

```python
# Create a new customer
customer = Customer(
    name="John Doe",
    address="123 Main St, Anytown",
    email="john@example.com",
    phone="555-1234"
)

# Add to database
customer_manager = CustomerManager(db_connection)
customer_manager.add(customer)

# Find customers by email pattern
filtered_customers = [c for c in customer_manager.items if "@example.com" in c.email]
```

## Contributing

Contributions to WaWi are welcome! Here's how you can contribute to the project:

### Development Workflow

1. **Fork the Repository**:
   - Click the "Fork" button at the top right of the repository page

2. **Clone Your Fork**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/wawi-projekt.git
   cd wawi-projekt
   ```

3. **Create a Feature Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make Your Changes**:
   - Implement your feature or fix
   - Follow the existing code style
   - Add appropriate tests
   - Update documentation as needed

5. **Test Your Changes**:
   ```bash
   # Run tests (once test suite is implemented)
   pytest
   
   # Check code quality
   pylint model/ view/ controller/
   ```

6. **Commit Your Changes**:
   ```bash
   git commit -am "Add feature: your feature description"
   ```

7. **Push to GitHub**:
   ```bash
   git push origin feature/your-feature-name
   ```

8. **Create a Pull Request**:
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Select your feature branch
   - Describe your changes in detail

### Code Style Guidelines

- Follow PEP 8 coding style for Python
- Use 4 spaces for indentation (no tabs)
- Include docstrings for all classes and methods
- Use type hints for all function parameters and return values
- Keep lines under 100 characters when possible
- Use meaningful variable and function names
- Write comprehensive comments for complex logic

### Testing Guidelines

- Write unit tests for new functionality
- Ensure existing tests pass with your changes
- Cover edge cases and error conditions
- Test UI components with PyQt test tools

### Documentation Guidelines

- Update the README.md if your change affects usage or installation
- Document new features with examples
- Add docstrings to all new classes and methods
- Create or update user documentation as needed

## Troubleshooting

### Common Issues

#### Database Connection Problems

**Issue**: Unable to connect to MariaDB database
**Solution**:
- Verify MariaDB server is running
- Check username/password are correct
- Ensure database exists and user has permissions
- Verify port is correct and not blocked by firewall

**Issue**: SQLite database file is locked
**Solution**:
- Ensure no other process is using the database file
- Check file permissions
- Restart the application

#### UI Issues

**Issue**: UI elements not appearing or improperly sized
**Solution**:
- Check PyQt5 installation is complete
- Verify screen resolution is supported (minimum 800x600)
- Try resetting window size/position

#### Import Sample Data Issues

**Issue**: Sample data import fails
**Solution**:
- Check database connection is working
- Verify database tables exist
- Look for specific error messages in logs (located in application directory)

### Logging

WaWi includes comprehensive logging to help troubleshoot issues:

- Log files are stored in the application directory
- Default log level is INFO
- Set to DEBUG level for more detailed information:
  ```python
  from model.logger_service import LoggerService
  LoggerService.configure(level=logging.DEBUG)
  ```

## License

WaWi is released under the MIT License.

```
MIT License

Copyright (c) 2025 Pascal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Acknowledgments

- **PyQt5**: For providing the cross-platform GUI framework
- **MariaDB/SQLite**: For reliable database backends
- **Python**: For an excellent language for application development
- **Design Patterns**: Implementation inspired by classic software design patterns
- All contributors to this open-source project

---

## Future Development

Planned features for future releases:

- **Order Management**: Track customer orders and fulfillment
- **Reporting**: Generate sales and inventory reports
- **User Management**: Multiple user accounts with different permission levels
- **Barcode Integration**: Support for scanning product barcodes
- **Export/Import**: Data exchange with CSV/Excel formats
- **Internationalization**: Support for multiple languages
- **Dark Mode**: Alternative UI theme

## Contact

For questions, suggestions, or contributions, please:
- Open an issue on GitHub
- Submit a pull request
- Contact the project maintainer at: your.email@example.com

---

*This project was created as an educational exercise for learning Object-Oriented Programming and PyQt5 development.*
