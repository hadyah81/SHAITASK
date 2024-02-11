# استيراد مكتبة pandas لتحليل البيانات
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# تحميل المجموعة من ملف CSV أو من مصدر آخر
file_path = "Salaries .csv"
df = pd.read_csv(file_path)
#1) **Basic  ExploratioDatan**: Identify the number of rows and columns in the dataset,
# determine the data types of each column, and check for missing values in each column.
# عرض عدد الصفوف والأعمدة في المجموعة
num_rows, num_columns = df.shape
print('Number of Rows :' +str({num_rows}))#the number of rows
print('Number of Columns: ' +str({num_columns}))#the number of columns

# عرض أنواع البيانات في كل عمود
data_types = df.dtypes
print('Data Types :')#the data types of each column
print(data_types)

# التحقق من وجود قيم مفقودة في كل عمود
missing_values = df.isnull().sum()
print('missing_values :')#checking for missing values
print(missing_values)

##################################################################################################################3

#2)**Descriptive Statistics**: Calculate basic statistics mean,
# median, mode, minimum, and maximum salary, 
# determine the range of salaries, and find the standard deviation.


# Calculate mean, median, mode, minimum, and maximum
Mean_Salary = df['BasePay'].mean()
Median_Salary = df['BasePay'].median()
Mode_Salary = df['BasePay'].mode()[0]  # Mode may have multiple values, so we take the first one
Min_Salary = df['BasePay'].min()
Max_Salary = df['BasePay'].max()

# # Calculate range
Salary_Range = Max_Salary - Min_Salary

# # Calculate standard deviation
Stand_Dev_Salary = df['BasePay'].std()

# # Display the results
print(f"Mean Salary: {Mean_Salary}")
print(f"Median Salary: {Median_Salary}")
print(f"Mode Salary: {Mode_Salary}")
print(f"Minimum Salary: {Min_Salary}")
print(f"Maximum Salary: {Max_Salary}")
print(f"Salary Range: {Salary_Range}")
print(f"Standard Deviation of Salary: {Stand_Dev_Salary}")
#######################################################
#3)**Data Cleaning**: Handle missing data by suitable method with explain why you use it.
#I can clean up the data by filling in the missing values ​​with default information such as the median 
overtimepay_median = df['OvertimePay'].median()
otherpay_median = df['OtherPay'].median()
# ملء القيم المفقودة باستخدام الوسيط
df['BasePay'].fillna(Median_Salary, inplace=True)
df['OvertimePay'].fillna(overtimepay_median, inplace=True)
df['OtherPay'].fillna(otherpay_median, inplace=True)
#explain why you use it?This helps maintain data balance and reduces the potential impact of missing values ​​on the final analysis.

#####################################################################
#4)**Basic Data Visualization**: Create histograms or bar charts to visualize the distribution of salaries,
# and use pie charts to represent the proportion of employees in   
# different departments.



# Histogram for Salary Distribution
plt.figure(figsize=(10, 6))
sns.histplot(df['BasePay'], bins=20, kde=True, color='skyblue')
plt.title('Salary Distribution')
plt.xlabel('Salary')
plt.ylabel('Frequency')
plt.show()

# Pie Chart for Proportion of Employees in Different Departments
department_counts = df['Agency'].value_counts()
total_employees = department_counts.sum()
# Calculate the percentage of employees in each department
department_percentages = (department_counts / total_employees) * 100

plt.figure(figsize=(8, 8))
plt.pie(department_percentages, labels=department_percentages.index, autopct='%1.1f%%', startangle=90, colors=sns.color_palette('pastel'))
plt.title('Proportion of Employees in Different Departments')
plt.show()

###################################################
#5(**Grouped Analysis**: Group the data by one or more columns and calculate
# summary statistics for each group, and compare the average salaries across different groups.)

grouped_data = df.groupby(['EmployeeName', 'JobTitle'])

# Calculate summary statistics for each group
summary_statistics = grouped_data['BasePay'].agg(['mean', 'sum', 'min', 'max'])

# عرض الإحصائيات الموجزة
print(summary_statistics)
#######################################################
#6)**Simple Correlation Analysis**: Identify any correlation between 
# salary and another numerical column, and plot a scatter plot
# to visualize the relationship.
correlation_coefficient = df['BasePay'].corr(df['TotalPay'])

# Plot a scatter plot to visualize the relationship
plt.figure(figsize=(8, 6))
plt.scatter(df['TotalPay'], df['BasePay'], alpha=0.5)
plt.title('Scatter Plot of BasePay vs TotalPay')
plt.xlabel('TotalPay')
plt.ylabel('BasePay')
plt.grid(True)
plt.show()

# Display the correlation coefficient
print("Correlation Coefficient:", correlation_coefficient)


##################################################################


































