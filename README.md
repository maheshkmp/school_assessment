# School Assessment Project

This Django-based project manages school assessment data, including schools, students, subjects, and assessment summaries.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

## Setup

1. Clone the repository:

- git clone <repository-url>
- cd school_assessment


2. Create a virtual environment:


3. Activate the virtual environment:
- On Windows:
  ```
  venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

4. Install required packages:

 - pip install -r requirements.txt


5. Apply database migrations:

 - python manage.py migrate
   

6. Create a superuser:
   
 - python manage.py createsuperuser

   
## Running the Project

1. Start the development server
 
 - python manage.py runserver

2. Access the application at `http://localhost:8000`

3. To access the admin interface, go to `http://localhost:8000/admin` and log in with your superuser credentials.

## Importing Data

To import data from a CSV file:

1. Place your CSV file in a known location.
2. Run the following command:
  - python manage.py import_csv path/to/your/csv/file.csv

Replace `path/to/your/csv/file.csv` with the actual path to your CSV file.

## Project Structure

- `core/`: Main application directory
- `models.py`: Contains all model definitions
- `views.py`: Contains view functions
- `admin.py`: Admin interface configurations
- `management/commands/import_csv.py`: Command for importing CSV data
- `school_assessment/`: Project settings directory
- `templates/`: HTML templates

## Available Pages

- Dashboard: `http://localhost:8000/`
- School List: `http://localhost:8000/schools/`
- Student List: `http://localhost:8000/students/`
- Summary List: `http://localhost:8000/summaries/`

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.   








