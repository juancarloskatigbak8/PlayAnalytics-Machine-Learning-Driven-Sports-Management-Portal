# Project Title

Sports Management Portal for Injury Prevention, Performance, and Athlete Management Using Machine Learning:
presented by Juan Carlos Katigbak 300366535 to Padmapriya Arasanipalai Kandhadai CSIS4495 Applied Research Project Section 002

## About the Project

Design
Develop a web-based portal incorporating ML models for injury prediction, performance analytics, and training customization.

Objectives
a.Create a database to store athlete profiles and performance metrics. 
b.Train an ML model to predict injury risks using historical data.
c.Build interactive dashboards for visualizing performance trends.

### Folders Included

ReportsAndDocuments/ - Contains all reports and documentation related to the project.
Implementation/ - Stores all code implementations, including backend, frontend, and machine learning models.
Misc/ - References such as Books, Research Journals and Studies, and Websites.


### Installing

Follow these steps to set up the development environment:

1. Clone the Repository

git clone https://github.com/juancarloskatigbak8/sports-management-portal.git
cd sports-management-portal

2. Set Up a Virtual Environment (Optional but Recommended)

python -m venv env
source env/bin/activate  # On macOS/Linux
env\Scripts\activate  # On Windows

3. Install Dependencies

pip install -r requirements.txt

4. Set Up the Database

python manage.py migrate

5. Run the Application

python manage.py runserver

6. Access the Portal

Open your browser and go to http://127.0.0.1:8000/

## Running the tests

Run automated tests to validate system functionality:

python manage.py test

### Break down into end to end tests

Notes: Explain what these tests test and why

```
Give an example
```

### And coding style tests

Notes: Explain what these tests test and why

```
Give an example
```

## Deployment

Notes: Add additional notes about how to deploy this on a live system

## Built With

Django - Web framework for backend development

Bootstrap - Frontend styling

SQLite - Database management

Matplotlib & Seaborn - Data visualization tools

scikit-learn - Machine learning model development

## Author

* **Juan Carlos Katigbak** - *Initial work to Final work* - (https://github.com/juancarloskatigbak8)

## Acknowledgments
Notes:
* Inspiration - Passion of mine to do something in the Sports Industry coupled with my recent interest in the emerging Data Analytics/Science and AI space
* Reference - main reference which inspired me to do this project is this:
  
  Owen, R., Owen, J. A., & Evans, S. (2024). Artificial intelligence for sport injury prediction.
  In C. Dindorf, E. Bartaguiz, F. Gassmann, & M. Fröhlich (Eds.),
  Artificial intelligence in sports, movement, and health (pp. [page range if known]). Springer.
