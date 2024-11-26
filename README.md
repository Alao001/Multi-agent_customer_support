# Multi-agent_customer_support

This project demonstrates how to automate customer support using the CrewAI framework. It leverages a multi-agent system to efficiently handle and resolve customer inquiries.

#Key Features:

Agent-Based Approach: Employs two AI agents:

-Support Agent: Handles customer inquiries, providing comprehensive and informative responses.

-Quality Assurance Agent: Reviews responses for accuracy, completeness, and adherence to company standards.

Knowledge Base Integration: Leverages external knowledge sources (e.g., Hugging Face documentation) to deliver accurate information.
Streamlit Interface: Provides a user-friendly web interface for customers to submit inquiries.
CrewAI Orchestration: Manages the workflow, task assignment, and communication between agents.


Clone the Repository:
git clone https://github.com/Alao001/Multi-agent_customer_support

Install Dependencies:

pip install -r requirements.txt

Set Up API Keys: Create a .env file in your project directory and add the following:

OPENAI_API_KEY=your_openai_api_key

Run the Streamlit App:

streamlit run app.py
