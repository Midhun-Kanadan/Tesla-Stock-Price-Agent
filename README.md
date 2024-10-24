
# Tesla Stock Price Agent

This repository contains a Python-based AI agent that fetches and plots Tesla stock prices for the last month. The agent leverages the `AutoGen` framework, `Ollama` models, and the `yfinance` library to retrieve and visualize stock data.

## Features

- Uses `Ollama` and `AutoGen` to implement an AI agent that retrieves and processes stock data.
- Fetches real-time Tesla stock prices for the last month.
- Plots the stock data using `matplotlib` for easy visualization.

## Repository Name

**Tesla Stock Price Agent**

## Prerequisites

- Python 3.7 or later
- Ollama installed on your local machine (with a supported model like `llama3.2:latest`)
- `AutoGen` framework
- `yfinance` and `matplotlib` libraries for stock data and plotting.

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/tesla-stock-agent.git
cd tesla-stock-agent
```

### 2. Install Required Libraries

Run the following command to install the necessary dependencies:

```bash
pip install -r requirements.txt
```

The `requirements.txt` should include:

```text
autogen
ollama
yfinance
matplotlib
```

### 3. Install and Run Ollama

Make sure Ollama is installed and running with the appropriate model (`llama3.2:latest`). You can install Ollama by following the official guide [here](https://ollama.ai/).

### 4. Run the Script

```bash
python tesla_stock_agent.py
```

The agent will automatically retrieve the latest Tesla stock prices for the last month and plot the data.

## Example Usage

After running the script, you will see a plot similar to the following:

```plaintext
A chart of Tesla stock prices for the last month, labeled with dates and stock prices in USD.
```

## Contributing

Feel free to fork this repository and submit pull requests if you want to enhance the functionality of this agent.

## License

This project is licensed under the MIT License.
