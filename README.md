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

cd %USERPROFILE%\Desktop\playanalytics
(e.g. cd OneDrive\Desktop\playanalytics)

python manage.py runserver

Open your browser and go to http://127.0.0.1:8000/ (or localhost:8000 - which is usually the default)

## How to Use the App

Step 1: Landing Page – Click "Start" to go to the User Registration and Login.

Step 2: User Registration and Login - If first time user, click "Register here" and input Username and Password (two times) and click "Register". If already registered, simply input Username and Password and click "Login". This brings user to the Dashboard page.

Step 3: Dashboard Page – Initially empty until players are added so click on "Prediction" in the navigation bar to go to the Prediction page.

Step 4: Prediction Page – Enter player stats and injury history to get an AI-driven risk prediction by clicking "Predict". View risk bar charts. To refresh prediction, click "New Prediction" which will bring you back to the Prediction page with empty fields for inputting again. If satisfied, click on "Save to Profile".

Step 5: Profiles Page (Profile Picture, Performance Statistics, and Injury History portion) – User will see the first player added in the Profiles page if "Save to Profile" had been clicked on from the Prediction page. Click on the name of the player. Once the user is in the Profile page of the player, click "Edit Player" so user is transported to the edit part of the player's profile. Once there, the user can add a profile photo (which the user will see by clicking on "Choose File" and selecting a photo wherever it is located in the user's computer), and/or edit stats (note: editing performance stats does not change the predicted risk label per se but the user can change the label as long as it is inputted as either "Low", "Low-Medium", "Medium", "Medium-High", or "High" which will affect the charts in the Dashboard page that the user will be able to see. If user does not input it in those predicted risk labels, the charts in the Dashboard page will not show). If satisfied with changes, click "Save Changes", otherwise, click "Cancel". If user wants to delete the profile of the player, simply click "Delete Player" and the player will disappear from the Profile page and if that was the first one, the Profile page will be blank. User can also bypass the Prediction page if he/she simply wants to add a player and go from there which is done by going back to the Profiles page and clicking "Add New Player". Input fields for Add New Player are the same as Edit Player.

Step 6: Profiles Page (Notes portion) – User can also add notes in the Notes field. Simply write any note (like performance from a previous game, injury that took place, rehabilitation progress since injury, training regimen, food diary, journal log, thoughts at the moment, et cetera) and click on "Add Note". Entry of note will show below with date and time when note was created. To edit note if user wishes to add anything to the entry, click "Edit" and edit anything in the note field. Once satisfied, click "Save Changes" otherwise, click "Cancel". If user wants to delete the entry of note, click "Delete".

Step 7: Dashboard Page (again) – Visuals and summary indicators update in real-time as more data is added.

Note: Keep adding player data to enrich the dashboard insights and track trends.

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

ChatGPT Plus (AI tool) - Assisted in every step of the app’s creation: ideas generation, algorithm benchmarking, prediction, creating the kanban board, coding (with comments), debugging, report creation (including ReadMe file), survey creation, and data analysis.

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

I. Research Journals and Studies
1. Owen, R., Owen, J. A., & Evans, S. (2024). Artificial intelligence for sport injury prediction. In Artificial Intelligence for Sport Injury Prediction. Springer.

2. Lu, Y., Pareek, A., Lavoie-Gagne, O. Z., Forlenza, E. M., Patel, B. H., Reinholz, A. K., Forsythe, B., & Camp, C. L. (2022). Machine learning for predicting lower extremity muscle strain in National Basketball Association athletes. The Orthopaedic Journal of Sports Medicine, 10(7), 23259671221111742. 

3. Papageorgiou, G., Sarlis, V., & Tjortjis, C. (2024). Evaluating the effectiveness of machine learning models for performance forecasting in basketball: A comparative study. Knowledge and Information Systems, 66, 4333–4375. 

4. Chmait, N., & Westerbeek, H. (2021). Artificial intelligence and machine learning in sport research: An introduction for non-data scientists. Frontiers in Sports and Active Living, 3, Article 682287.
 
5. Dindorf, C., Bartaguiz, E., Gassmann, F., & Fröhlich, M. (2022). Conceptual structure and current trends in artificial intelligence, machine learning, and deep learning research in sports: A bibliometric review. Preprint. 

6. Li, S., & Zhang, W. (2022). Evaluation method of basketball teaching and training effect based on wearable devices. Frontiers in Physics, 10, Article 900169.

7. Yang, X. (2024). Construction of measurement index system of basketball players’ specific physical fitness training based on AI intelligence and neural network. Molecular & Cellular Biomechanics, 21(1), 250. 

8. Georgievski, B., & Vrtagic, S. (2021). Machine learning and the NBA game. Journal of Physical Education and Sport. 

9. Simenz, C. J., Dugan, C. A., & Ebben, W. P. (2005). Strength and conditioning practices of National Basketball Association strength and conditioning coaches. The Journal of Strength and Conditioning Research, 19(3), 495–504.

II. Books
1. Braun, N. (2023). Learn to code with basketball.

2. Matthes, E. (2023). Phyton crash course 3rd edition: A hands-on, project-based introduction to programming. No Starch Press.

3. Foran, B. (2026). Complete conditioning for basketball: National Basketball Strength & Conditioning Association. Human Kinetics.

4. Gillett, J. & Burgos, B. (2020). Strength Training for Basketball: National Strength and Conditioning Association. Human Kinetics.

III. Websites
1. National Basketball Association. (n.d.). NBA official website. https://www.nba.com 
(Note: NBA player performance statistics and profile pictures from two famous players, LeBron James and Luka Dončić, from the current Los Angeles Lakers were obtained here and used for the app)

2. Pro Sports Transactions Archive. (n.d.). Pro Sports Transactions. https://www.prosportstransactions.com/ 
(Note: NBA player injury statistics were obtained here and used for the app)

3. Braun, N. (2025). Fantasy Math: Fantasy sports predictions and analytics. Fantasy Math. https://fantasymath.com/

4. Broni, K. (2020). KenBroTech. YouTube. https://www.youtube.com/@KenBroTech

5. Gilermo, D. (n.d.). NBA players stats [Dataset]. Kaggle. https://www.kaggle.com/datasets/drgilermo/nba-players-stats/data 

6. Lauton, L. (n.d.). NBA injury stats (1951-2023) [Dataset]. Kaggle. https://www.kaggle.com/datasets/loganlauton/nba-injury-stats-1951-2023

7. Lounias, T. (n.d.). NBA stat scrape and analysis [Kaggle Notebook]. Kaggle. https://www.kaggle.com/code/themelissoulounias/nba-stat-scrape-and-analysis

8. Chiodi, A. (n.d.). NBA injury forecasting [Code notebook]. Kaggle. https://www.kaggle.com/code/anthonychiodi/nba-injury-forecasting

9. Liu, I. C. (n.d.). NBA player stats and injured data from ‘13 to ‘23 [Dataset]. Kaggle. https://www.kaggle.com/datasets/icliu30/nba-player-stats-and-injured-data-from-13-to-23

IV. AI Tools Section
1. ChatGPT Plus (AI tool) - Assisted in every step of the app’s creation: ideas generation, algorithm benchmarking, prediction, creating the kanban board, coding (with comments), debugging, report creation (including ReadMe file), survey creation, and data analysis.

V. Technology Stack
1. Amazon. (2024). Amazon Prime [E-commerce platform]. https://www.amazon.com/prime

2. Bootstrap Team. (2024). Bootstrap (Version 5) [Front-end framework]. https://getbootstrap.com

3. Braun, N. (2024). Fantasy Math [Sports data science platform]. https://www.fantasymath.com

4. Canva. (2024). Canva Pro [Design software]. https://www.canva.com

5. Chart.js Contributors. (2024). Chart.js (Version 4) [JavaScript charting library]. https://www.chartjs.org

6. DataCamp. (2024). DataCamp [Online learning platform]. https://www.datacamp.com

7. Django Software Foundation. (2024). Django (Version 5.2) [Web framework]. https://www.djangoproject.com

6. GitHub. (2024). GitHub [Code hosting platform]. https://github.com

7. Hipp, D. R. (2024). SQLite (Version 3) [Database engine]. https://www.sqlite.org

8. Hunter, J. D. (2007). Matplotlib: A 2D graphics environment. Computing in Science & Engineering, 9(3), 90–95. https://matplotlib.org

9. Microsoft. (2024). Microsoft Office 365 [Productivity suite]. https://www.microsoft.com/microsoft-365

10. Microsoft. (2024). Microsoft Forms [Survey tool]. https://forms.office.com

11. Microsoft. (2024). Microsoft Outlook [Email client]. https://outlook.office.com

12. Microsoft. (2024). Microsoft Excel [Spreadsheet software]. https://www.microsoft.com/microsoft-365/excel

13. NumPy Developers. (2024). NumPy (Version 2) [Python library]. https://numpy.org

14. OpenAI. (2024). ChatGPT (GPT-4) [Large language model]. https://chat.openai.com/

15. Pandas Development Team. (2024). Pandas (Version 2) [Python library]. https://pandas.pydata.org

16. Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., ... & Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825–2830. https://scikit-learn.org

17. Python Software Foundation. (2024). Python (Version 3.12) [Programming language]. https://www.python.org

18. Tieleman, T. (2024). Joblib (Version 1.4) [Model serialization tool]. https://joblib.readthedocs.io

19. Willison, A. (2024). Pillow (Version 11.1) [Image processing library]. https://python-pillow.org

20. Udemy. (2024). Udemy [Online learning platform]. https://www.udemy.com

21.YouTube. (2024). YouTube [Video sharing platform]. https://www.youtube.com

VI. Instructor
1. Nikhil Bhardwaj’s CSIS4260 Special Topics in Data Analytics - he made the researcher do an assignment which required him to use benchmarks and dashboards to compare the algorithms that were used.
























