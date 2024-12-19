# 📊 **Financial Analysis Chatbot**

This project is an end-to-end system that collects, processes, and analyzes financial data for companies such as **Apple**, **Microsoft**, and **Tesla**, and provides an interactive **chatbot interface** for users to ask about financial metrics. Users can inquire about **revenue**, **net income**, **liabilities**, **assets**, and **growth metrics** for the supported companies. 

## 🚀 **Project Overview**
This project is divided into the following stages:
1. **Data Collection & Cleaning**: Gathering raw financial data from various sources and ensuring its consistency and quality.  
2. **Data Transformation & Calculation**: Calculating key financial metrics like growth rates, changes in net income, and liabilities trends.  
3. **Data Storage**: Storing the cleaned and processed data in a **CSV file** for easy access.  
4. **Chatbot Development**: Building a chatbot that interacts with users to provide information on specific financial metrics for Apple, Microsoft, and Tesla.  
5. **Web Application**: Creating a simple web-based user interface using **Flask** where users can chat with the bot.  

---

## 📚 **Table of Contents**
- [Data Collection & Cleaning](#-data-collection--cleaning)
- [Data Transformation & Calculation](#-data-transformation--calculation)
- [Data Storage](#-data-storage)
- [Chatbot Development](#-chatbot-development)
- [Web Application](#-web-application)
- [How to Run the Project](#-how-to-run-the-project)
- [Technologies Used](#-technologies-used)
- [Future Improvements](#-future-improvements)

---

## 📡 **1. Data Collection & Cleaning**
The first step was to gather raw financial data for **Apple**, **Microsoft**, and **Tesla**. Data sources may include: 
- **Financial reports (10-K, 10-Q) from company websites** 
- **Stock market APIs (e.g., Alpha Vantage, Yahoo Finance, etc.)**
- **Manual collection from company balance sheets, income statements, and cash flow statements**

### 🔍 **Steps in Data Cleaning**
- **Handling missing values**: Missing financial data for any year is filled using the previous year's data or marked as "N/A" if no previous data is available.  
- **Data normalization**: Ensuring that revenue, net income, and other key metrics are all in the same currency and are properly formatted.  
- **Data standardization**: Renaming columns to standardized names like `Total Revenue`, `Net Income`, `Total Assets`, and `Total Liabilities`.  

**Example of the Raw Data:**
| Year  | Company   | Total Revenue | Net Income | Total Assets | Total Liabilities |
|------|-----------|---------------|------------|--------------|-------------------|
| 2022 | Apple     | 394.33B       | 99.8B      | 352.76B      | 287.9B             |
| 2022 | Microsoft | 198.27B       | 72.7B      | 411.68B      | 198.4B             |
| 2022 | Tesla     | 81.46B        | 12.6B      | 83.24B       | 26.8B              |

---

## 📈 **2. Data Transformation & Calculation**
Once the financial data is cleaned, the next step is to **calculate additional financial metrics**. Key metrics include:

### 📊 **Key Metrics Calculated**
1. **Revenue Growth (%)**:
   \
   Revenue Growth = (Current Year Revenue−Previous Year Revenue) / Previous Year Revenue × 100
   \
   
2. **Net Income Change (%)**:  
   \
   Net Income Change = (Current Year Net Income−Previous Year Net Income) / Previous Year Net Income × 100
   \
    
4. **Assets Growth (%)**:  
   \
   Assets Growth = (Current Year Assets−Previous Year Assets) / Previous Year Assets × 100
   \

5. **Liabilities Change (%)**:
   \
   Liabilities Change = (Current Year Liabilities−Previous Year Liabilities) / Previous Year Liabilities × 100 
   \

---

## 💾 **3. Data Storage**
After calculations, the financial data is stored in a CSV file for easy access. The structure of the CSV file is as follows:

**File Name:** `financial_data_with_correct_growth.csv`  
**Columns in the CSV file:**
- **Company**: Name of the company (Apple, Microsoft, Tesla)  
- **Year**: Fiscal year for the financial data  
- **Total Revenue**: Total revenue of the company  
- **Net Income**: Company's profit for the year  
- **Total Assets**: Company's total assets  
- **Total Liabilities**: Company's total liabilities  
- **Revenue Growth (%)**: Year-on-year revenue growth  
- **Assets Growth (%)**: Year-on-year growth in total assets  

---

## 🤖 **4. Chatbot Development**
The chatbot is responsible for answering user queries on **financial metrics** for the selected company. Users can ask questions such as:
- **"What is the total revenue for Apple?"**  
- **"How has Tesla's net income changed?"**  
- **"What are Microsoft's total liabilities this year?"**  

### 🛠️ **Logic for Chatbot**
1. **Input Handling**: The chatbot receives queries from the user.  
2. **Query Matching**: It matches user queries with a set of predefined questions, such as:  
   - Total Revenue  
   - Net Income Change  
   - Revenue Growth  
   - Total Liabilities  
   - Assets Growth  
3. **Response Generation**: It extracts the answer from the CSV file and returns it to the user.  

---

## 🌐 **5. Web Application**
The web application is built using **Flask**. It provides an interface for users to interact with the chatbot.

### 🛠️ **Features**
- **User-friendly interface** with a chat window for interacting with the bot.  
- **Company Dropdown** where users can select a company from Apple, Microsoft, and Tesla.  
- **Real-time messaging** between the user and the chatbot.  

---

## 📋 **How to Run the Project**
Follow these steps to run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Abdoelbahli/financial-chatbot.git
   cd financial-chatbot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask Application**:
   ```bash
   python BCG.py
   ```

4. **Access the Chatbot**:  
   Open your browser and go to:  
   ```
   http://127.0.0.1:5000/
   ```

---

## 🛠️ **Technologies Used**
- **Python**: For back-end processing and data analysis.  
- **Pandas**: For cleaning, transforming, and calculating financial metrics.  
- **Flask**: To build the web-based chatbot.  
- **HTML, CSS, and JavaScript**: For creating the front-end interface.  

---

## 🔮 **Future Improvements**
- **Add more companies**: Support for more companies like Google, Amazon, and Meta.  
- **Dynamic Data Sources**: Instead of using a CSV file, connect to an API for real-time financial data.  
- **Advanced NLP**: Implement NLP-based query processing to better understand user queries.  
- **Data Visualization**: Show financial metrics using charts for better user experience.  
- **User Authentication**: Secure access to the chatbot.  

---

If you have any questions or would like to suggest improvements, feel free to contact us or submit an issue. 🚀
