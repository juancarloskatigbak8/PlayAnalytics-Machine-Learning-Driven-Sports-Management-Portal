# Project Title

PlayAnalytics, an AI-Driven Sports Management Portal:
presented by Juan Carlos Katigbak 300366535 to Padmapriya Arasanipalai Kandhadai CSIS4495 Applied Research Project Section 002

## About the Project

PlayAnalytics is a sports management portal utilizing machine learning to predict injury risks and deliver data-driven insights tailored specifically for basketball athletes. By integrating predictive analytics, PlayAnalytics empowers athletes to proactively minimize injury risks and optimize training effectiveness.

### Folders/Files Included

playanalytics/
│
├── ReportsAndDocuments/     # Reports, research papers, documentation
├── Implementation/          # Django app code + ML model files
├── Misc/                    # Reference books, journals, articles, websites
└── playanalytics.zip        # To be used for thesis defense

### Installing (using either macOS/Linux's Terminal or Windows' Command Prompt)

1. Extraction of playanalytics.zip 

First, click on the green (<> Code) button and click on Download ZIP to be able to download the whole Repository. Extract and unzip playanalytics.zip. If there is a nested folder (playanalytics/playanalytics/), ensure the inner folder is moved to a convenient location like your Desktop.

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
pip install django django-bootstrap5 joblib scikit-learn numpy pandas pillow 


4. Run the Application

using macOS/Linux's Terminal, run:

cd playanalytics (depending on the location of the folder, suggestion would be to put it on the Desktop, then on the terminal cd ~/Desktop then cd playanalytics)

python manage.py runserver

using Windows' Command Prompt, run:

cd %USERPROFILE%\Desktop\playanalytics (depending on the location of the folder, suggestion would be to put it on the Desktop, then on the command prompt cd ~/Desktop then cd playanalytics)
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

## Technology Stack

1. Technology Used in the App

Django - Web framework for backend development

Bootstrap 5, Chart.js - Frontend UI, styling, and rendering interactive charts dynamically

SQLite - Lightweight database

Django Auth - Django built-in user registration, login, and logout system.

scikit-learn - Injury risk prediction model

Pandas, NumPy - Data processing

Joblib - ML model serialization

Pillow - Image upload handling


2. Technology Sources Used to be able to make the App

ChatGPT Plus (AI tool) - Assisted in every step of the app’s creation from coding, debugging, report writing, survey design, to predictive model benchmarking

Canva Pro (digital branding) - Used to design professional-looking progress reports, the PlayAnalytics logo, and the final presentation deck

Amazon Prime (e-commerce) – Enabled access to key physical resources like Python Crash Course (3rd ed.) that supported app functionality and planning

Fantasy Math (sports data science tool) – Served as a source of inspiration for basketball data visualizations and predictive analysis logic, especially during the prototyping and midterm phase

DataCamp (e-learning) – Provided structured online courses for learning foundational data analytics and machine learning concepts

Udemy (e-learning) – Supplemented DataCamp by offering additional practical tutorials and project-based learning for data science

GitHub (online repository for IT portfolios) – Used as the centralized version-controlled repository for the PlayAnalytics app source code and documentation submission.

YouTube (video sharing platform) - for teaching me how to integrate Machine Learning data visualization with Django especially from the channel KenBroTech.

Office 365 (productivity suite) – Microsoft Planner was used for kanban-style project tracking; Microsoft Excel for cleaning/preparing CSV datasets and daily work logs; Microsoft Outlook for advisor communication and milestone updates; Microsoft Forms for creating/distributing user feedback survey to gather insights about the app.

## Author

* **Juan Carlos Katigbak** - *Initial work to Final work* - (https://github.com/juancarloskatigbak8)

## Acknowledgments
Inspiration: A personal passion for sports + growing interest in AI and data science.

Academic Reference:
Owen, R., Owen, J. A., & Evans, S. (2024). Artificial intelligence for sport injury prediction. In Dindorf et al. (Eds.), AI in Sports, Movement, and Health. Springer.
