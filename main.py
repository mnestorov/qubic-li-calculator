import requests
import json
from datetime import datetime, timedelta
from pycoingecko import CoinGeckoAPI
import os

def clear_screen():
    """Clears the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def fetch_token():
    """Authenticates with the Qubic API and returns a token."""
    url = 'https://api.qubic.li/Auth/Login'
    body = {'userName': 'guest@qubic.li', 'password': 'guest13@Qubic.li', 'twoFactorCode': ''}
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json-patch+json'}
    response = requests.post(url, data=json.dumps(body), headers=headers)
    response.raise_for_status()
    return response.json()['token']

def get_network_stats(token):
    """Fetches and returns network statistics."""
    url = 'https://api.qubic.li/Score/Get'
    headers = {'Accept': 'application/json', 'Authorization': f'Bearer {token}'}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()

def calculate_earnings(my_hashrate, network_stat, qubic_price):
    """Calculates and prints the estimated earnings."""
    epoch_number = network_stat['scoreStatistics'][0]['epoch']
    epoch97_begin = datetime.strptime('2024-02-21 12:00:00', '%Y-%m-%d %H:%M:%S')
    current_epoch_begin = epoch97_begin + timedelta(days=7 * (epoch_number - 97))
    current_epoch_end = current_epoch_begin + timedelta(days=7) - timedelta(seconds=1)
    current_epoch_progress = (datetime.utcnow() - current_epoch_begin) / timedelta(days=7)

    net_hashrate = network_stat['estimatedIts']
    net_avg_scores = network_stat['averageScore']
    net_sols_per_hour = network_stat['solutionsPerHour']
    
    pool_reward = 0.85
    income_per_one_its = pool_reward * qubic_price * 1000000000000 / net_hashrate / 7 / 1.06
    cur_sol_price = 1479289940 * pool_reward * current_epoch_progress * qubic_price / (net_avg_scores * 1.06)

    print('\n\nCurrent Epoch Info')
    print('---')
    print(f'Current epoch: {epoch_number}')
    print(f'Epoch start UTC: {current_epoch_begin}')
    print(f'Epoch end UTC: {current_epoch_end}')
    print(f'Epoch progress: {100 * current_epoch_progress:.1f}%\n')
    print('Network info:')
    print(f'Estimated network hashrate: {net_hashrate:,} it/s')
    print(f'Average score: {net_avg_scores:.1f}')
    print(f'Scores per hour: {net_sols_per_hour:.1f}\n')
    print('Income estimations:')
    print('Using pool with fixed 85% reward\n')
    print(f'Qubic price: {qubic_price:.8f}$')
    print(f'Estimated income per 1 it/s per day: {income_per_one_its:.4f}$\n')
    print(f'Your estimated income per day: {my_hashrate * income_per_one_its:.2f}$')
    print(f'Estimated income per 1 sol: {cur_sol_price:.2f}$')
    print(f'Your estimated sols per day: {24 * my_hashrate * net_sols_per_hour / net_hashrate:.1f}\n')
    print('################################################################################')
    print('################################################################################\n\n')

def main():
    clear_screen()
    print('################################################################################')
    print('#####                                                                     ######')
    print('#####                      QUBIC EARNINGS CALCULATOR                      ######')
    print('#####                                                                     ######')
    print('################################################################################\n')
    
    my_hashrate = float(input("Please enter your total hashrate of your rigs (in it/s): "))
    
    token = fetch_token()
    network_stat = get_network_stats(token)
    
    cg_client = CoinGeckoAPI()
    prices = cg_client.get_price(ids='qubic-network', vs_currencies='usd')
    qubic_price = prices['qubic-network']['usd']
    
    calculate_earnings(my_hashrate, network_stat, qubic_price)

if __name__ == "__main__":
    main()
