# React + Python + Flask full-stack Product Application template

A full-stack web application built with **ReactJS** on the frontend and **Flask** on the backend.

The application includes Home, Products, Product Details, and About pages.
The React frontend communicates with a Flask REST API to retrieve product data.

The current application supports navigation between Home, Products, Product Details, and About pages,
retrieves product information through Flask REST endpoints, handles missing products with HTTP 404 responses,
and includes automated backend tests with Pytest.

✔️ Architecture is:

- Frontend: ReactJS | React Router | Vite | JavaScript | HTML5 | CSS3 | Fetch API | npm | Node.js
- Backend: Python | Flask | Flask-CORS | RESTful API | pip
- Testing: Pytest | Flask Test Client
- API: RESTful endpoints
- Pages: Home, Products, About
- Data: Products returned from Flask API
- Development: React on localhost:3000, Flask on localhost:5000

✔️ Project structure:

```
flask-react-app/
├── backend/
|   ├── venv/
│   ├── .env
│   ├── .env.test
|   ├── __init__.py
│   ├── app.py
│   ├── data.py
│   ├── requirements.txt
|   └── tests/
|       ├── __init__.py
|       └── test_app.py
└── frontend/
    ├── package-lock.json
    ├── package.json
    ├── .gitignore
    ├── .env.development
    ├── .env.production
    ├── .env.test
    └── src/
        ├── App.jsx
        ├── main.jsx
        ├── api.js
        ├── components/
        │   └── Navbar.jsx
        └── pages/
            ├── Home.jsx
            ├── ProductDetails.jsx
            ├── Products.jsx
            └── About.jsx
```

✔️ Set up a project with a Flask backend and a React frontend:

```bash
python --version
cd flask-react-app/backend
pip install Flask Flask-CORS
pip install python-dotenv // for Flask environment variables
python -m pip install python-dotenv
pip freeze > requirements.txt // update requirements file
clear // clear terminal

✔️ Install pip (Python Package Index)
pip --version // pip: the package installer for Python
pip show pip  // show path where pip

✔️ Update Python packages:
python -m pip install --upgrade pip
pip install --upgrade <package_name>
pip install --upgrade <package_name>==<version_number>
pip list --outdated // to check for outdated packages
pip install -r requirements.txt --upgrade

✔️ Python/Flask Testing:
$ pip install pytest

✔️ Install the packages according to requirements:
$ pip install -r requirements.txt

✔️  Start React:
cd frontend
npm run dev

✔️  Run Python Tests with pytest from the `backend` directory:
cd backend
python -m pytest -v

✔️  Create Virtual Environment
python -m venv venv

✔️  Activate Virtual Environment for Windows:
venv\Scripts\activate

✔️  Run Flask from the `backend` directory:
cd backend
venv\Scripts\activate
python app.py
```

✔️ Implemented:

- Created React + Python/Flask full-stack project.
- Routing in a Flask project.
- Separated environment-specific configuration from application code using environment variables and Vite modes
  on the frontend and python-dotenv on the Flask backend. This allows the same codebase to run against development,
  test, staging, and production APIs without hard-coded URLs or credentials.

✔️ Pytest Unit Tests

The project includes tests for the Flask API.
Tests are located in:

```text
backend/tests/test_app.py
```

The tests use Flask's built-in test client.
Expected output:

```text
tests/test_app.py::test_home PASSED                                                                                     [ 16%]
tests/test_app.py::test_health PASSED                                                                                   [ 33%]
tests/test_app.py::test_get_products PASSED                                                                             [ 50%]
tests/test_app.py::test_get_product PASSED                                                                              [ 66%]
tests/test_app.py::test_get_product_2 PASSED                                                                            [ 83%]
tests/test_app.py::test_product_not_found PASSED                                                                        [100%]
```
