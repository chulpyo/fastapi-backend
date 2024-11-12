# FastAPI User Management API

This repository contains a simple **FastAPI** application for managing a user list with CRUD operations.

For a detailed explanation of this code, please refer to the blog post: [Tistory: Building a Backend with FastAPI](https://teapopo.tistory.com/33), [Naver: Building a Backend with FastAPI](https://teapopo.tistory.com/33).

## Features

- **Create** a user with a unique ID
- **Read** user information by `user_id`
- **Update** user information
- **Delete** a user by `user_id`

## Installation

1. Clone the repository:
   ``` bash
   git clone https://github.com/yourusername/fastapi-user-management.git
   cd fastapi-user-management
   ```

2. Install dependencies:
   ``` bash
   pip install -r requirements.txt
   ```

3. Start the FastAPI server:
   ``` bash
   uvicorn main:app --reload
   ```

4. Visit the interactive documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to test the API.

## API Endpoints

### Create User
- **Endpoint**: `POST /users`
- **Description**: Creates a new user with a unique `user_id`.
- **Body**:
  ``` json
  {
    "name": "string",
    "age": "integer"
  }
  ```

### Get All Users
- **Endpoint**: `GET /users`
- **Description**: Returns a list of all users.

### Get User by ID
- **Endpoint**: `GET /users/{user_id}`
- **Description**: Retrieves a specific user’s details by `user_id`.

### Update User
- **Endpoint**: `PUT /users/{user_id}`
- **Description**: Updates the specified user’s `name` and/or `age`.
- **Qeury** (Optional fields): ?name=&age=

### Delete User
- **Endpoint**: `DELETE /users/{user_id}`
- **Description**: Deletes a user by `user_id`.

## Code Explanation

The code uses two models:
1. **UserCreate**: For creating users (does not include `id`).
2. **User**: Represents a full user with `id`, `name`, and `age`.

User data is stored in a dictionary (`users`) where:
- **Key**: `user_id`
- **Value**: User object

This approach ensures `O(1)` complexity for lookups, updates, and deletions.

For further explanations on each section of the code, visit the detailed blog post on [FastAPI User Management API](https://teapopo.tistory.com/33).

## Example Usage

1. **Create User**:
   ``` bash
   curl -X 'POST' \
     'http://127.0.0.1:8000/users' \
     -H 'accept: application/json' \
     -H 'Content-Type: application/json' \
     -d '{
     "name": "Alice",
     "age": 30
   }'
   ```

2. **Get User**:
   ``` bash
   curl -X 'GET' 'http://127.0.0.1:8000/users/{user_id}' -H 'accept: application/json'
   ```

3. **Update User**:
   ``` bash
   curl -X 'PUT' \
     'http://127.0.0.1:8000/users/{user_id}' \
     -H 'accept: application/json' \
     -H 'Content-Type: application/json' \
     -d '{
     "name": "Alice Updated",
     "age": 31
   }'
   ```

4. **Delete User**:
   ``` bash
   curl -X 'DELETE' 'http://127.0.0.1:8000/users/{user_id}' -H 'accept: application/json'
   ```

## Project Structure

``` plain text
fastapi-user-management/
│
├── .vscode
│   │
│   └── launch.json     # VSCode debug settings
├── main.py             # FastAPI application code
├── requirements.txt    # Project dependencies
├── .gitignore          # Repository igonore file
└── README.md           # Project documentation
```


## Dependencies

- **FastAPI**: Fast and efficient API framework
- **Uvicorn**: ASGI server for FastAPI applications

Install with:
``` bash
pip install fastapi uvicorn
```

## License

This project is licensed under the MIT License.

## Contact

For questions or suggestions, please reach out to [kim.chulpyo@gmail.com](mailto:kim.chulpyo@gmail.com).


