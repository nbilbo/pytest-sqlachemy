# pytest-sqlachemy

## Overview

The project uses pytest to test models created with SQLAlchemy. It allows you to create and run automated tests to ensure that your models work correctly.

## How to Use

### Installation

1. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate # Linux/Mac
venv\Scripts\activate.bat # Windows
```

2. Install the dependencies: 
 ```
 python -m pip install -r requirements.txt
 ```

### Running the Tests
1. To run all the tests, run the following command: 
```
python -m pytest
```

## Project Structure

- `tests/` - directory containing automated tests
- `app/` - directory containing the project's source code
- `requirements.txt` - project requirements file


## Technologies Used

- Python
- SQLAlchemy
- Pytest

## License

This project is licensed under the [MIT License](LICENSE).
