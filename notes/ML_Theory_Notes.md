**ML**



-- Supervised learning:

&nbsp;	We give the machine input and the correct answer and it learns to predict.



-- Unsupervised learning:

&nbsp;	we will get the data but we are not going to predict anything, we will just

&nbsp;	find patterns, group similar items, reduce complexity, spot outliers



-- Reinforcement learning:

&nbsp;	It's like training a dog. We don't teach it everything directly, just reward him

&nbsp;	for his good behavior and ignore or punish bad behavior. (learning by trial and 	error).



**EDA (Exploratory data analysis)** - a step where you explore the data to:

&nbsp;	understand it

&nbsp;	discover patterns

&nbsp;	spot anomalies

&nbsp;	generate insights

&nbsp;	and decide what to do next





\- Steps:

&nbsp;	1) Viewing the data

&nbsp;		- head(), tail(), shape, info()

&nbsp;		- What columns do i have? What types of data?

&nbsp;	

&nbsp;	2) Summary Statistics

&nbsp;		- Mean, median, mode, std, min, max, quartiles

&nbsp;		- helps understand spread and central tendency



&nbsp;	3) Value Count

&nbsp;		- How many unique values in a column

&nbsp;		- great for categorical columns



&nbsp;	4) Missing value analysis



&nbsp;	5) Visualizations



&nbsp;	6) Target variable exploration



\- After EDA

&nbsp;	1) Handle missing values



&nbsp;	2) Strategies to handle:



&nbsp;		- drop missing rows/columns (only if very few)



&nbsp;		- input with:

&nbsp;			- mean/median: for numerical data

&nbsp;			- mode: for categorical data

&nbsp;			- Advanced: linear regression, KNN, or interpolation

&nbsp;		

&nbsp;		- remove duplicates



&nbsp;		- fix data types

&nbsp;		

&nbsp;		- Handle inconsistent categories



&nbsp;		- Detect and handle outliers



&nbsp;		- Fix logic or domain errors



**DATA PREPROCESSING:**

	Data preprocessing is about transforming valid data into a usable format.

&nbsp;	

&nbsp;	1) Encoding categorical variables

&nbsp;		There are two types:

&nbsp;			1) Label encoding (ordinal)

&nbsp;			2) One hot encoding (nominal)



&nbsp;	2) Feature transformation



&nbsp;	3) Feature Scaling



**FEATURE ENGINEERING:**

	creating new feature or transforming existing ones to expose useful patterns that 	ML models can learn from.



**FEATURE SELECTION:**

&nbsp;	selecting most useful features and removing the rest.

&nbsp;	

&nbsp;	1) Filter methods

&nbsp;	2) embedded methods

































































