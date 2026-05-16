# FastMCP Demo Project

This repository contains a collection of Model Context Protocol (MCP) servers built using the `FastMCP` framework. It showcases three different implementations ranging from simple utility tools to a full-featured expense tracking system with both local and remote capabilities.

## Project Structure

The project consists of three main server implementations:

1.  **ExpenseTracker (main.py)**: A local, synchronous SQLite-based expense manager using standard I/O (stdio).
2.  **SpendsEyes (remote_server.py)**: An advanced, asynchronous version of the expense tracker that runs over HTTP.
3.  **Demo Server (demo_server.py)**: A simple server providing utility tools for dice rolling and basic math.

---

## 1. ExpenseTracker (`main.py`)
This is the standard implementation of the expense tracking system.

-   **Transport**: `stdio` (Standard input/output)
-   **Database**: Local `expenses.db` using synchronous `sqlite3`.
-   **Tools**:
    -   `add_expense`: Log new spending.
    -   `update_expense`: Modify existing entries.
    -   `delete_expense`: Remove entries by ID.
    -   `list_expenses`: Filter entries by date range.
    -   `summarize`: Get totals aggregated by category.
-   **Resources**:
    -   `expense://categories`: Provides a list of valid expense categories from `categories.json`.

---

## 2. SpendsEyes Remote (`remote_server.py`)
A specialized version of the expense tracker designed for remote access and higher performance.

-   **Transport**: `HTTP` (Runs on `http://0.0.0.0:8000`)
-   **Database**: Uses `aiosqlite` for non-blocking database operations. The database is stored in the system's temporary directory for write-access reliability.
-   **Key Differences**:
    -   Fully asynchronous tool implementations.
    -   Includes a `server_info` resource at `infp://server`.
    -   Hardened with better error handling for read-only environments.
-   **Initialization**: Automatically initializes the schema and performs a write-access test on startup.

---

## 3. Demo Server (`demo_server.py`)
A lightweight server used for testing MCP connectivity and basic tool execution.

-   **Transport**: `stdio`
-   **Tools**:
    -   `roll_dice`: Generates random numbers simulating n-sided dice.
    -   `add`: A simple utility to sum two integers.

---

## Installation & Setup

### Prerequisites
Ensure you have Python installed. It is recommended to use a virtual environment.

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Running the Servers

**To run the standard Expense Tracker (stdio):**
```bash
python main.py
```

**To run the Remote SpendsEyes Server (HTTP):**
```bash
python remote_server.py
```

**To run the Demo Server:**
```bash
python demo_server.py
```

## Configuration for MCP Clients
When connecting these to an MCP client (like Claude Desktop), use the absolute path to your python executable and the script path for `stdio` servers, or the URL for the `remote_server`.

*Note: For `remote_server.py`, ensure your firewall allows traffic on port 8000.*