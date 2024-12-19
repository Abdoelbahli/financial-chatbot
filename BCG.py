# 📚 Import required libraries
import pandas as pd
from flask import Flask, request, jsonify, render_template

# 📂 Load the financial data from the CSV file
df = pd.read_csv('financial_data_with_correct_growth.csv')

# 🛠️ Step 1: Define the chatbot logic
def financial_chatbot(user_query, company_name='Apple'):
    """
    This chatbot responds to various financial queries 
    for a specific company.
    """
    # Filter data for the specific company
    company_data = df[df['Company'].str.lower() == company_name.lower()]
    company_data = company_data.sort_values(by='Year', ascending=True)

    # 📢 Handle general greetings
    if any(greeting in user_query.lower() for greeting in ["hello", "hi", "hey"]):
        return "Hello! How can I help you today?"

    # Queries the user can ask
    if "total revenue" in user_query:
        total_revenue = company_data.loc[company_data['Year'].idxmax(), 'Total Revenue']
        return f"The total revenue for {company_name} in the most recent year is ${total_revenue:,.2f}."

    elif "net income change" in user_query:
        last_two_years = company_data.tail(2)
        if len(last_two_years) == 2:
            prev_year_income = last_two_years.iloc[0]['Net Income']
            current_year_income = last_two_years.iloc[1]['Net Income']
            change = ((current_year_income - prev_year_income) / prev_year_income) * 100
            direction = "increased" if change > 0 else "decreased"
            return f"The net income for {company_name} has {direction} by {abs(change):.2f}% over the last year."
        else:
            return "Not enough data to calculate net income change over the last year."

    elif "revenue growth" in user_query:
        recent_growth = company_data.loc[company_data['Year'].idxmax(), 'Revenue Growth (%)']
        return f"The revenue growth percentage for {company_name} in the most recent year is {recent_growth:.2f}%."

    elif "total liabilities" in user_query:
        total_liabilities = company_data.loc[company_data['Year'].idxmax(), 'Total Liabilities']
        return f"The total liabilities for {company_name} in the most recent year are ${total_liabilities:,.2f}."

    elif "total assets" in user_query:
        total_assets = company_data.loc[company_data['Year'].idxmax(), 'Total Assets']
        return f"The total assets for {company_name} in the most recent year are ${total_assets:,.2f}."

    elif "liabilities change" in user_query:
        last_two_years = company_data.tail(2)
        if len(last_two_years) == 2:
            prev_year_liabilities = last_two_years.iloc[0]['Total Liabilities']
            current_year_liabilities = last_two_years.iloc[1]['Total Liabilities']
            change = ((current_year_liabilities - prev_year_liabilities) / prev_year_liabilities) * 100
            direction = "increased" if change > 0 else "decreased"
            return f"The liabilities for {company_name} have {direction} by {abs(change):.2f}% over the last year."
        else:
            return "Not enough data to calculate liabilities change over the last year."

    elif "assets growth" in user_query:
        recent_growth = company_data.loc[company_data['Year'].idxmax(), 'Assets Growth (%)']
        return f"The assets growth percentage for {company_name} in the most recent year is {recent_growth:.2f}%."

    else:
        return "Sorry, I can only provide information on revenue, net income, liabilities, assets, and growth metrics."

# 📡 Step 2: Flask Web Application
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    """Render the chatbot UI."""
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Process incoming chat requests and respond."""
    try:
        data = request.get_json()
        user_query = data.get('message')
        company_name = data.get('company_name', 'Apple')  # Default to Apple if not provided
        response = financial_chatbot(user_query, company_name)
        return jsonify({ 'response': response })
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({ 'response': "An error occurred, please try again." })

if __name__ == '__main__':
    app.run(debug=True)
