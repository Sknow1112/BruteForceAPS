# BruteForceAPS

This project is a Python-based Cybersec script that checks for subdomains of a given domain. It uses the `requests` library to send HTTP requests and the `concurrent.futures` library to handle multithreading to make checking each subdomain faster.

## Features

- Checks the status of a subdomain.
- Generates all possible subdomain combinations.
- Uses multithreading to speed up the process.
- Prints out all successful subdomains and errors.

## Requirements

- Python 3.6 or higher
- `requests` library
- `concurrent.futures` library

## Usage

1. Clone the repository.
2. Install the required libraries using pip:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the script:
    ```bash
    python APSVersionExecutor.py
    ```
4. Enter the domain when prompted.

## Code Structure

- `check_subdomain(subdomain, domain)`: This function checks the status of a subdomain.
- `get_subdomains(domain)`: This function generates all possible subdomain combinations and checks their status.
- `main()`: This function is the entry point of the application.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Thanks!

## License

[MIT](https://choosealicense.com/licenses/mit/)
