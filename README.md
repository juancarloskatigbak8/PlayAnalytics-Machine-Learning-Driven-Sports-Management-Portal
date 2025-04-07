# Project Title

PlayAnalytics, an AI-Driven Sports Management Portal:
presented by Juan Carlos Katigbak 300366535 to Padmapriya Arasanipalai Kandhadai CSIS4495 Applied Research Project Section 002

## About the Project

PlayAnalytics is a sports management portal utilizing machine learning to predict injury risks and deliver data-driven insights tailored specifically for basketball athletes. By integrating predictive analytics, PlayAnalytics empowers athletes to proactively minimize injury risks and optimize training effectiveness.

### Folders Included

ReportsAndDocuments/ - Contains all reports and documentation related to the project.
Implementation/ - Stores all code implementations, including backend, frontend, and machine learning models.
Misc/ - References such as Books, Research Journals and Studies, and Websites.


### Installing (using either macOS/Linux's Terminal or Windows' Command Prompt)

1. Extraction of playanalytics folder from W25_4495_S2_JuanCarlosK-main folder

Extract W25_4495_S2_JuanCarlosK-main.zip and make sure that the extracted folder will have the files because there is a tendency that the extracted folder will have another folder before you are able to get the files. You then need to extract the playanalytics folder and put it somewhere where you can start the app, like on the Desktop.


2. Set Up a Virtual Environment

For macOS/Linux (Terminal):
python -m venv env

For Windows (Command Prompt):
python -m venv env
env\Scripts\activate

3. Install Dependencies

For macOS/Linux (Terminal)/For Windows (Command Prompt):
pip install django-bootstrap5 joblib scikit-learn numpy pandas

4. Run the Application

using macOS/Linux's Terminal, run:

cd playanalytics (depending on the location of the folder, suggestion would be cd ~/Desktop then cd playanalytics)

python manage.py runserver

using Windows' Command Prompt, run:

cd %USERPROFILE%\Desktop\W25_4495_S2_JuanCarlosK-main/playanalytics
(e.g. cd OneDrive\Desktop\W25_4495_S2_JuanCarlosK-main/playanalytics) #since W25_4495_S2_JuanCarlosK-main is the folder with the file

python manage.py runserver

Open your browser and go to http://127.0.0.1:8000/ (or localhost:8000 - which is usually the default)

## Running the tests

Run automated tests to validate system functionality:

python manage.py test

## Built With

Django - Web framework for backend development

Bootstrap - Frontend styling

SQLite - Database management

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
