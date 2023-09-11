# FastAPI Person API

The FastAPI Person API is a web application that provides CRUD (Create, Read, Update, Delete) operations for managing information about people. It is built using FastAPI and SQLAlchemy and provides the following endpoints:

- `http://localhost:8000/api/all`: Retrieve a list of all people in the database.
- `http://localhost:8000/api/add`: Add new people to the database.
- `http://localhost:8000/api/{name}`: Retrieve a person's information based on their unique name.
- `http://localhost:8000/api/update/{name}`: Update a person's data by their name.
- `http://localhost:8000/api/delete/{name}`: Delete a person's data based on the entered name.

## Getting Started

To run the FastAPI Person API on your local machine, follow these steps:

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo.git


2. Change to the project directory:

    ```bash
    cd your-repo

3. Install the required Python packages:
    ```bash
    pip install -r requirements.txt


Usage
1. Start the FastAPI application:
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload

2. Access the API using the provided endpoints:

- To get a list of all people: http://localhost:8000/api/all
- To add a new person: http://localhost:8000/api/add
- To get a person by name: http://localhost:8000/api/{name}
- To update a person's data by name: http://localhost:8000/api/update/{name}
- To delete a person by name: http://localhost:8000/api/delete/{name}


### API Endpoints

# GET /api/all
    This endpoint returns a list of all people in the database.

# POST /api/add
    Use this endpoint to add new people to the database. Send a POST request with JSON data containing the person's information (e.g., name, age, address).

# GET /api/{name}
    Retrieve a person's information based on their unique name. Replace {name} in the URL with the person's actual name.

# PUT /api/update/{name}
    Update a person's data by their name. Replace {name} in the URL with the person's actual name. Send a PUT request with JSON data containing the updated information.

# DELETE /api/delete/{name}
    Delete a person's data based on the entered name. Replace {name} in the URL with the person's actual name.

### Acknowledgments
- FastAPI: https://fastapi.tiangolo.com/
- SQLAlchemy: https://www.sqlalchemy.org/
- Feel free to customize this README to include your specific project details, such as repository links, installation instructions, and any additional information about your project's usage, contributors, or deployment instructions.