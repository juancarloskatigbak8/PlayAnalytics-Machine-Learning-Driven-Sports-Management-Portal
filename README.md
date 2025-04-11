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

1. Extraction of playanalytics.zip 

Unzip playanalytics.zip. If there's a nested folder (playanalytics/playanalytics/), ensure the inner folder is moved to a convenient location like your Desktop.

2. Set Up a Virtual Environment
Recommended: Use Python 3.11+ (Anaconda or system Python)

For macOS/Linux (Terminal):
python -m venv env
source env/bin/activate

For Windows (Command Prompt):
python -m venv env
env\Scripts\activate

3. Install Dependencies

For macOS/Linux (Terminal)/For Windows (Command Prompt):
pip install django-bootstrap5 joblib scikit-learn numpy pandas pillow 

Alternatively, install from the requirements file:
pip install -r requirements.txt

4. Run the Application

using macOS/Linux's Terminal, run:

cd playanalytics (depending on the location of the folder, suggestion would be cd ~/Desktop then cd playanalytics)

python manage.py runserver

using Windows' Command Prompt, run:

cd %USERPROFILE%\Desktop\playanalytics
(e.g. cd OneDrive\Desktop\playanalytics)

python manage.py runserver

Open your browser and go to http://127.0.0.1:8000/ (or localhost:8000 - which is usually the default)

## How to Use the App

Step 1: Landing Page – Click "Start" to go to the dashboard.

Step 2: Dashboard Page – Initially empty until players are added.

Step 3: Prediction Page – Enter player stats and injury history to get an AI-driven risk prediction. View risk bar charts.

Step 4: Save to Profile – Save prediction to the profile system.

Step 5: Profiles Page – Add player photo, edit stats, write performance notes.

Step 6: Dashboard Page (again) – Visuals and summary indicators update in real-time as more data is added.

Keep adding player data to enrich the dashboard insights and track trends.

## Built With

Django - Web framework for backend development

Bootstrap 5 - Frontend UI and styling

SQLite - Lightweight database

scikit-learn - Injury risk prediction model

Pandas, NumPy - Data processing

Joblib - ML model serialization

Pillow - Image upload handling

## Author

* **Juan Carlos Katigbak** - *Initial work to Final work* - (https://github.com/juancarloskatigbak8)

## Acknowledgments
Inspiration: A personal passion for sports + growing interest in AI and data science.

Academic Reference:
Owen, R., Owen, J. A., & Evans, S. (2024). Artificial intelligence for sport injury prediction. In Dindorf et al. (Eds.), AI in Sports, Movement, and Health. Springer.
