# Python_projects

🏥 **Hospital Patient Data Analysis – Data Analysis with Pandas**
This project presents an end-to-end analysis of synthetic hospital patient records using the pandas library in Python. 
The dataset simulates real-world patient data and includes information such as admission/discharge dates, diagnoses, treatment costs, departments, doctors, and patient demographics.
The insights of analysis can guide hospital management, finance teams, and clinical operations in making data-driven decisions related to resource planning, cost control, and patient care strategy.

🔍 **What I Did**
The goal of this project was to clean, transform, and analyze patient data to extract meaningful insights that can support decision-making in a healthcare setting. 
Below are the core areas of analysis:

✅ **Data Cleaning & Preparation**
    Handled missing values in key columns like Doctor Name, Length of Stay, and Treatment Cost.
    Converted date columns to proper datetime format to enable time-based analysis.
    Created new columns (Out-of-Pocket, Age Group) to enrich the dataset and provide additional context.

✅ **Exploratory Analysis**
    Measured and compared the average length of stay across departments, helping to identify resource-intensive areas.
    Analyzed treatment costs by gender, revealing possible differences in cost patterns.
    Identified the most common diagnoses, useful for healthcare planning and resource allocation.
    Analyzed monthly admission trends, highlighting patient volume fluctuations across the year.

✅ **Grouping & Aggregation**
    Calculated total and average treatment costs per department and doctor, which can guide budgeting and staffing.
    Counted the number of patients treated by each doctor, useful for performance and workload assessment.

✅ **Filtering & Advanced Insights**
    Isolated high-cost patients (above 90th percentile), which is essential for financial auditing and risk assessment.
    Sorted patients by length of stay, helping spot long-term cases that may need specialized care.

📊 **Key Insights Summary**
    1. Neurology has the longest average patient stays, while Cardiology has the shortest — indicating differences in care intensity and efficiency.
    2. Male patients incur the highest average treatment costs, highlighting potential cost disparities across genders.
    3. The top diagnoses — Migraine, Hypertension, and Cancer — reflect key areas for medical focus and resource allocation.
    4. October, November, and April see the highest admission volumes, useful for staffing and capacity planning.
    5. Cardiology generates the highest total treatment cost, while Neurology balances longer stays with moderate total costs.
