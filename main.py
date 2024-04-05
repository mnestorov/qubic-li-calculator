import requests
import json
from datetime import datetime, timedelta
from pycoingecko import CoinGeckoAPI

def clear_screen():
    """Clear the console screen in a cross-platform way."""
    command = 'cls' if os.name == 'nt' else 'clear'
    os.system(command)

def fetch_token():
    """Authenticate and return a token for further requests."""
    url = 'https://api.qubic.li/Auth/Login'
    body = {'userName': 'guest@qubic.li', 'password': 'guest13@Qubic.li', 'twoFactorCode': ''}
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json-patch+json'}
    response = requests.post(url, data=json.dumps(body), headers=headers)
    response.raise_for_status()  # This will raise an error for non-2xx responses
    return response.json()['token']

def get_network_stats(token):
    """Fetch and return network statistics using the provided token."""
    url = 'https://api.qubic.li/Score/Get'
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def calculate_earnings(network_stat, my_hashrate):
    # Your calculation logic remains the same here, just encapsulated in a function
    # Return the results as needed
    pass  # Placeholder for calculation logic

def main():
    clear_screen()
    print('### QUBIC EARNINGS CALCULATOR ###\n')
    my_hashrate = float(input("Please enter your total hashrate of your rigs (in it/s): "))
    
    try:
        token = fetch_token()
        network_stat = get_network_stats(token)
        # Use the `calculate_earnings` function to process calculations
        calculate_earnings(network_stat, my_hashrate)
    except requests.RequestException as e:
        print(f"Network request failed: {e}")
    except ValueError as e:
        print(f"Error during calculations: {e}")

if __name__ == "__main__":
    main()
