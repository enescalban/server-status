# SERVER STATUS

![GitHub](https://img.shields.io/github/license/enescalban/server-status)
![GitHub last commit](https://img.shields.io/github/last-commit/enescalban/server-status)
![GitHub issues](https://img.shields.io/github/issues/enescalban/server-status)

Server Status is a Python script to check the status of a list of domains from a text file and categorize them based on their HTTP status codes.

## Requirements

- Python 3.x
- `requests`
- `urllib3`
- `pyfiglet`
- `simple_colors`

## Installation

1. Clone the repository:

```bash
git clone https://github.com/enescalban/server-status.git
cd server-status
```

2. Install the required packages:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the `server_status.py` script:

```bash
python server_status.py
```

2. Enter the name of the text file containing the list of domains (e.g., `domains.txt`):

```
Lütfen txt dosyasının adını (örn. domains.txt) girin:
```

3. The script will start checking the status of each domain and display the results:

```
SERVER STATUS
https://github.com/enescalban
__________________________________________________
example.com = 200
test.com = 403
google.com = 200
example.org = 401
...

```

4. The script will create separate text files for domains with different status codes:

```
200.txt
403.txt
401.txt
other_status.txt
```

## Note

- The script uses `requests` to check the status of each domain. Make sure to handle large lists responsibly to avoid flooding the servers with requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- [Enes Çalban](https://github.com/enescalban)

Feel free to contribute, open issues, or suggest improvements!

---

Please make sure to adjust the contents, URLs, and file paths according to your actual repository structure. Once you have added this README to your GitHub repository, users will have clear instructions on how to use the "SERVER STATUS" script and what to expect from it.
