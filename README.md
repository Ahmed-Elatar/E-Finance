# E-Finance

This project is a Django, FastAPI application that takes and stores a Stock Ticker and watches changes in the Price and volume of this ticker, and retrieves Historical data for these changes
Based on [YFinacne](https://finance.yahoo.com/markets/). The application integrates Celery and Redis for background task processing, is dockerized for easy deployment, and includes Swagger for API testing.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Functions and Classes](#functions-and-classes)
- [URLs Map](#urls-map)
- [Installation Notes](#installation-notes)

## Features
- Takes Ticker symbol and checks if it is correct using FastAPI
- Store adding symbol attempts in mongoDB
- Manages stock ticker symbols and their historical price data.
- Uses YFinance for fetching live stock data.
- Stores data in PostgreSQL.
- Utilizes Celery and Redis for asynchronous task processing.
- Dockerized for simplified deployment.
- Uses Swagger for API testing.

---

## Prerequisites
Ensure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads)
- [Docker](https://www.docker.com/get-started/)
- [Docker Compose](https://docs.docker.com/compose/install/)


---

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Ahmed-Elatar/e-finance.git
    cd e-finance
    ```

2. Build Docker containers:
    ```bash
    sudo docker-compose build
    ```

3. Create a Django superuser:
    ```bash
    sudo docker-compose run web python manage.py createsuperuser
    ```

4. Start the Docker containers:
    ```bash
    sudo docker-compose up
    ```

---


## Usage
Once running, access the application at `http://0.0.0.0:8000/`.

### Admin Panel
Go to `http://0.0.0.0:8000/admin` to access the Django admin panel using the superuser credentials created during setup.




---


## Functions and Classes
### Django
1. **`send_data_to_fastapi(data)`**  
     Sends stock ticker data to the FastAPI service for processing.
     
     **Parameters:**  
     `data` (dict): The data to be sent, including the stock symbol.
     
     **Returns:**  
     A response object from FastAPI.
  
  2. **`ReceiveTickerData(APIView)`**  
     API view that receives and processes ticker data from FastAPI.
     
    **Methods:**  
    - `POST`: Processes incoming stock data and saves valid ticker symbols to the database.

    **Returns:**  
    - `dict`: A dictionary containing a success message after processing the stock data.

    Example:
    ```{
                'symbol': "NVDA",
                'name': "NVIDIA Corporation",
                'sender': "ahmed-elatar",
                'status': "accepted",
                
            }
    ```  
  3. **`TakeSymbol(APIView)`**  
     API view for sending stock ticker symbols from the Django app to FastAPI.
     
     **Methods:**  
     - `POST`: Sends the stock symbol provided by the user to FastAPI.
  
 4. **`TickerView(RetrieveDestroyAPIView)`**  
    API view to retrieve or delete a specific ticker symbol.
     
     **Methods:**  
     - `GET`: Retrieves a ticker symbol by its ID.
     - `DELETE`: Deletes a specific ticker symbol.
  
  5. **`TickersHistoryView(ListAPIView)`**  
    API view to retrieve historical price data for all tickers.

    **Methods:**  
    - `GET`: Returns historical price data for all ticker symbols.

    **Returns:**  
    - `list`: A list of dictionaries containing the historical price data for each ticker symbol.

    Example:
    ```json
    [
        {
            "symbol": "AAPL",
            "history": [
                {"date": "2024-08-01", "price": 145.32},
                {"date": "2024-08-02", "price": 146.87}
            ]
        },
        {
            "symbol": "GOOGL",
            "history": [
                {"date": "2024-08-01", "price": 2725.6},
                {"date": "2024-08-02", "price": 2732.8}
            ]
        }
    ]
    ```
### FastAPI

1. **`receive_ticker_name(recived_data: Dict)`**  
   This function receives ticker data from Django in JSON format, checks if the ticker symbol is valid by calling `check_ticker_name()`, and then sends the result back to Django.

   **Parameters:**  
   - `recived_data` (Dict): A dictionary containing the ticker symbol sent from Django.

   **Returns:**  
   - A JSON response confirming that the data has been received.

2. **`send_awnser(data: Dict)`**  
   Sends the result of the ticker validation back to the Django application.

   **Parameters:**  
   - `data` (Dict): The validated ticker data to be sent to Django.

   **Returns:**  
   - A response object from the Django API endpoint.

3. **`check_ticker_name(data: Dict)`**  
   Validates the received ticker symbol using the yFinance API. If the symbol is valid, it adds the company name and sets the `status` field to "accepted." If invalid, it sets the `status` field to "not-accepted." The result is saved in MongoDB.

   **Parameters:**  
   - `data` (Dict): A dictionary containing the ticker symbol to be validated.

   **Returns:**  
   - A dictionary with the validation result, including the status (`"accepted"` or `"not-accepted"`) and company name if valid.

4. **`show_accepted_attempts()`**  
   Retrieves a list of accepted attempts from MongoDB. Only records with the status `"accepted"` are returned.

   **Returns:**  
   - A list of dictionaries containing data for all accepted ticker symbols.

5. **`show_not_accepted_attempts()` (Not-Accepted)**  
   Retrieves a list of not-accepted attempts from MongoDB. Only records with the status `"not-accepted"` are returned.

   **Returns:**  
   - A list of dictionaries containing data for all not-accepted ticker symbols.





---




## End-Points Map

### Django

- **Swagger UI:** [`http://0.0.0.0:8000/`](http://0.0.0.0:8000/)  
  _(Shows the Swagger documentation for the Django API)_

- **Receive Ticker Data:** [`http://0.0.0.0:8000/recive/`](http://0.0.0.0:8000/recive/)  
  _(Receives ticker data from FastAPI after validation)_

- **Submit Ticker Symbol:** [`http://0.0.0.0:8000/take-symbol/<str:symbol>`](http://0.0.0.0:8000/take-symbol/<str:symbol>)  
  _(Allows users to submit a ticker symbol)_

- **All Tickers:** [`http://0.0.0.0:8000/tickers/`](http://0.0.0.0:8000/tickers/)  
  _(Fetches a list of all tickers)_

- **Single Ticker:** [`http://0.0.0.0:8000/ticker/<int:pk>`](http://0.0.0.0:8000/ticker/<int:pk>)  
  _(Fetches a single ticker's data by primary key)_

- **Tickers History:** [`http://0.0.0.0:8000/tickers-history/`](http://0.0.0.0:8000/tickers-history/)  
  _(Shows the history of all tickers)_

- **Single Ticker History:** [`http://0.0.0.0:8000/ticker-history/<int:pk>`](http://0.0.0.0:8000/ticker-history/<int:pk>)  
  _(Shows the history of a specific ticker by primary key)_

### FastAPI

- **Receive Ticker from Django:** [`http://0.0.0.0:8001/recive-ticker/`](http://0.0.0.0:8001/recive-ticker/)  
  _(Receives ticker data from Django, checks its validity, and responds)_

- **Check Ticker Data:** [`http://0.0.0.0:8001/check-ticker-data/`](http://0.0.0.0:8001/check-ticker-data/)  
  _(Validates the ticker symbol using yFinance and updates the status)_

- **Show Accepted Attempts:** [`http://0.0.0.0:8001/show-accepted-attempts/`](http://0.0.0.0:8001/show-accepted-attempts/)  
  _(Retrieves a list of accepted ticker validation attempts from MongoDB)_

- **Show Not Accepted Attempts:** [`http://0.0.0.0:8001/show-not-accepted-attempts/`](http://0.0.0.0:8001/show-not-accepted-attempts/)  
  _(Retrieves a list of not-accepted ticker validation attempts from MongoDB)_

### Overview

- **Django** handles endpoints related to user interaction and data storage in PostgesSQL databases.
- **FastAPI** validates ticker symbols using yFinance and stores validation attempts in MongoDB.


---


## Installation Notes
1. Edit `.env` file to configure PostgreSQL database credentials and FastAPI URL.
2. Update the `docker-compose.yml` file with matching PostgreSQL credentials.





