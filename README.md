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


### Installing (using either macOS/Linux's Terminal or Windows' Command Prompt)

1. Extraction of W25_4495_S2_JuanCarlosK folder

Extract W25_4495_S2_JuanCarlosK-main.zip and make sure that the extracted folder will have the files because there is a tendency that the extracted folder will have another folder before you are able to get the files. You also have to make sure when you run the virtual environment, you are able to locate the exact location of the W25_4495_S2_JuanCarlosK folder otherwise it will not run properly.

2. Set Up a Virtual Environment (Optional but Recommended)

For macOS/Linux (Terminal):
python -m venv env
source env/bin/activate

For Windows (Command Prompt):
python -m venv env
env\Scripts\activate

3. Install Dependencies

For macOS/Linux (Terminal)/For Windows (Command Prompt):
pip install beautifulsoup4 requests pandas numpy lxml transformers torch sentencepiece scipy scikit-learn tqdm ipywidgets scrapy

4. Run the Application

using macOS/Linux's Terminal, run:

cd ~/Desktop/W25_4495_S2_JuanCarlosK/lal_injury_risk

python manage.py runserver

using Windows' Command Prompt, run:

cd %USERPROFILE%\Desktop\W25_4495_S2_JuanCarlosK/lal_injury_risk
(e.g. cd OneDrive\Desktop\W25_4495_S2_JuanCarlosK/lal_injury_risk) #since W25_4495_S2_JuanCarlosK is the folder with the file

python manage.py runserver

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
