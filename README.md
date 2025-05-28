🚢 Titanic Dataset Preprocessing Project

📁 Project Overview
	This project focuses on cleaning and preprocessing the Titanic dataset. It includes handling missing values, encoding categorical variables, standardizing numerical features, and removing outliers to prepare the dataset for further machine learning or statistical analysis.

🧾 Dataset Description
	Source: Titanic dataset (CSV file)		
	Columns used: Age, Fare, Sex, Embarked, and others
	Target variable removed: Survived (for this preprocessing task)

🔧 Technologies Used
	Python
	Pandas
	NumPy
	Matplotlib
	Seaborn
	Scikit-learn

📌 Key Steps in the Project
	Loading the Data
	Used pandas.read_csv() to load the dataset.

	Exploratory Analysis
	Displayed the first few rows and basic information.

	Checked for missing values using isnull().sum().
	Handling Missing Data
	Filled missing Age values with the mean.
	Filled missing Embarked values with the mode.
	
	Dropped the Cabin column due to excessive missing data.
	Dropping Irrelevant Columns
	Removed columns like Survived, Pclass, SibSp, Parch, and Name.
	
	Encoding Categorical Variables
	Converted Sex from categorical to numerical (male=0, female=1).

	Feature Scaling
	Standardized Age and Fare using StandardScaler from sklearn.

	Outlier Removal
	Applied IQR-based filtering to remove outliers in the Age column.

	Used a violin plot for visual inspection.

📊 Visualizations
	Violin Plot of the Age distribution before outlier removal.

📂 File Structure
Titanic_Preprocessing
│
├── task1data.csv               # Input data file
├── task1.py    # Python script for data cleaning
└── README.md                   # Project documentation (this file)

🙋‍♀️ Author
Gobika Mayakrishnan B.Sc.AI & ML 


📬 Contact
For questions or collaboration, feel free to reach out via email or GitHub.
