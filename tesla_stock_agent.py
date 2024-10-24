
from autogen import AssistantAgent, UserProxyAgent
from autogen.coding import LocalCommandLineCodeExecutor
import yfinance as yf
import matplotlib.pyplot as plt
from pathlib import Path

# Set up the code executor
workdir = Path("coding")
workdir.mkdir(exist_ok=True)
code_executor = LocalCommandLineCodeExecutor(work_dir=workdir)

# User Proxy Agent to execute the code returned by Assistant Agent
user_proxy_agent = UserProxyAgent(
    name="User",
    code_execution_config={"executor": code_executor},
    is_termination_msg=lambda msg: "FINISH" in msg.get("content")
)

# Ollama Assistant Agent
config_list = [{"model": "llama3.2:latest", "api_type": "ollama", "client_host": "http://localhost:11434"}]
assistant_agent = AssistantAgent(
    name="Ollama Assistant",
    llm_config={"config_list": config_list}
)

# Fetch and plot Tesla stock data
def fetch_and_plot_stock():
    stock_data = yf.download('TSLA', period="1mo")
    plt.plot(stock_data.index, stock_data['Close'], label='Tesla Stock Price')
    plt.title('Tesla Stock Prices for the Last Month')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()

# Initiate the chat to provide the task
chat_result = user_proxy_agent.initiate_chat(
    assistant_agent,
    message="Provide code to fetch Tesla stock data and plot the results."
)

# Execute the plotting function
fetch_and_plot_stock()
