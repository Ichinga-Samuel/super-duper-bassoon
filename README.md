
# Project README

## Overview

This project provides a robust configuration management system using the Python class `Config`. It is designed to simplify loading and managing environment variables from `.env` files and other sources while maintaining flexibility and scalability.

The core functionality includes:
- Singleton design pattern to ensure only one instance of the `Config` class.
- Dynamic loading of environment variables using the `python-dotenv` library.
- Automatic type-safe access to environment variables with default value support.

---

## Features

1. **Singleton Pattern**:  
   The `Config` class is implemented as a singleton, ensuring only one instance exists throughout the application.

2. **Dynamic Environment Variable Loading**:  
   Automatically loads environment variables from:
   - System environment variables.
   - `.env` files or streams (e.g., configuration dictionaries).
   - Fallback defaults provided as keyword arguments.

3. **Type-Safe Attribute Access**:  
   Attributes not explicitly defined will dynamically retrieve their values from the environment. 

4. **Custom Initialization Parameters**:  
   Accepts initialization parameters for default values, allowing fine-grained control over configurations.

---

## Prerequisites

- Python 3.7 or later.
- The `python-dotenv` library. Install using:

  ```bash
  pip install python-dotenv
  ```

---

## Usage

### Step 1: Create a `.env` File (Optional)

Define environment variables in a `.env` file. For example:

```dotenv
AWS_ACCESS_KEY_ID=your_aws_key
AWS_SECRET_ACCESS_KEY=your_aws_secret
MY_SECRET=my_application_secret
```

### Step 2: Import and Initialize

Import and use the `Config` class:

```python
from main import Config

# Initialize Config with default values
config = Config(my_constant=3.14)

# Access variables dynamically or explicitly
print(config.AWS_ACCESS_KEY_ID)  # Outputs AWS key
print(config.my_constant)        # Outputs 3.14
print(config.PATH)               # System PATH variable
```

### Step 3: Overriding Defaults

Pass custom parameters during initialization to override `.env` or system values:

```python
config = Config(my_constant=42.0, CUSTOM_VAR="Custom Value")
print(config.my_constant)  # Outputs 42.0
print(config.CUSTOM_VAR)   # Outputs "Custom Value"
```

---

## Code Explanation

### Core Methods

1. **`__new__`:**  
   Implements the singleton pattern, ensuring only one instance of `Config` exists.

2. **`load_dotenv`:**  
   Leverages `dotenv` functionality to load variables and merges them with provided parameters.

3. **`set_attributes`:**  
   Dynamically sets instance attributes.

4. **`__getattr__`:**  
   Lazy loading of undefined attributes from system environment variables.

---

## Dependencies

- **[python-dotenv](https://pypi.org/project/python-dotenv/):** To load `.env` files dynamically.

---

## Customization

Feel free to extend the `Config` class by adding validation logic or pre-defined attributes to meet your application's needs.

---

## License

This project is licensed under the MIT License. See `LICENSE` for more details.

--- 

## Contributions

Contributions are welcome! If you encounter any issues or have feature suggestions, feel free to submit a pull request or open an issue on the project's repository. 

---

Happy Coding! 🚀
