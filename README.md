# IITM_FINAL-PROJECT-DTM4A
**Introduction**

Retail Sales Forecast employs advanced machine learning techniques, data preprocessing, feature enhancement, and comprehensive algorithm assessment and selection.It integrates Exploratory Data Analysis (EDA) to find trends, patterns, and data insights. It offers users interactive tools to explore top-performing stores and departments, conduct insightful feature comparisons, and obtain personalized sales forecasts. With a commitment to delivering actionable insights, the project aims to optimize decision-making processes within the dynamic retail landscape.

**Key Technologies and Skills** :
- Python
- Numpy
- Pandas
- Matplotlib
- PostgreSQL
- Scikit-Learn
- Plotly
- Matplotlib
- Seaborn
- Pickle

**Features**:

**Data Preprocessing**:

- **Data Understanding**: The dataset comprises store, sales, and features data, offering details on store attributes like name, department, date, type, size, weekly sales, and environmental factors such as holiday status, temperature, fuel price, multiple markdowns, CPI, and unemployment. The primary focus is on predicting weekly sales, serving as the target variable for our modeling endeavors. This initial exploration forms the basis for subsequent data preprocessing and model development.

- **Encoding and Data Type Conversion**: The process involves preparing categorical features for modeling by transforming them into numerical representations, considering their inherent nature and relationship with the target variable. Simultaneously, data types are converted to align with the modeling process requirements, ensuring seamless integration and compatibility. This step facilitates the effective utilization of categorical information in the subsequent stages of the project.

- **Handling Null Values**: Notably, the 'MarkDown' columns present a challenge with over 50% null values, while other columns exhibit minimal null values. To address this, we employ machine learning models to predict and impute the missing values, ensuring a more complete and robust dataset for subsequent analysis and modeling. This strategic approach allows us to mitigate the impact of missing data on the overall quality of our dataset.

- **Feature Improvement**: Emphasizing enhanced modeling effectiveness, we concentrate on refining the dataset. This involves creating new features to extract deeper insights and enhance overall dataset efficiency. Evaluation, conducted through `Seaborn's Heatmap`, reveals that, aside from Size and Type with correlation values of 0.21 and 0.17 (absolute value) respectively, no other columns exhibit a strong correlation with weekly sales. This underscores the need for strategic feature enhancement to bolster the predictive power of our model.


**Machine Learning Regression Model**:

- **Algorithm Assessment**: In the realm of regression, our primary objective is to predict the continuous variable of weekly sales. Our journey begins by splitting the dataset into training and testing subsets. We systematically apply various algorithms, evaluating them based on training and testing accuracy using the R2 (R-squared) metric, which signifies the coefficient of determination. This process allows us to identify the most suitable base algorithm tailored to our specific data.

- **Algorithm Selection**: After thorough evaluation, two contenders, the Extra Trees Regressor and Random Forest Regressor, demonstrate commendable testing accuracy. Upon checking for any overfitting issues in both training and testing, both models exhibit strong performance without overfitting concerns. I choose the Random Forest Regressor for its ability to strike a balance between interpretability and accuracy, ensuring robust performance on unseen data.


- **Model Persistence**: We conclude this phase by saving our well-trained model to a pickle file. This strategic move enables us to effortlessly load the model whenever needed, streamlining the process of making predictions on weekly sales in future applications.



**Exploratory Data Analysis (EDA) -
- **Data Visualization**: EDA employs visual techniques to represent the statistics graphically. Visualizations consisting of histograms, box plots, scatter plots, line plots, heatmaps, and bar charts assist in identifying styles, trends, and relationships within the facts.

**Features**: 
- Embark on a detailed analysis to understand how the different ranges of features affect weekly sales. Explore the impact of various feature ranges on sales, considering both date-wise and store-wise perspectives. 
- This examination covers features such as type, size, holiday, temperature, fuel price, CPI, unemployment, and multiple markdowns. The comprehensive study ensures a thorough grasp of how each feature uniquely influences the data, offering valuable insights into sales patterns.

**Prediction**: 
- Users provide input parameters such as date, store, department, holiday, temperature, fuel price, CPI, unemployment, and multiple markdowns. Leveraging the pre-trained Random Forest Regressor model stored in a pickle file, the system predicts weekly sales based on the user's input. 
- Users can experiment with various combinations of input values, allowing our machine learning regression model to dynamically forecast weekly sales tailored to the provided data parameters. This interactive feature enhances user engagement and facilitates personalized predictions.


