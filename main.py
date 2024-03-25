# PLEASE INSTALL LIB ( pip install tkinter requests pycoingecko )
import tkinter as tk
from tkinter import messagebox
from math import exp
import requests
import json
from datetime import datetime, timedelta
from pycoingecko import CoinGeckoAPI
def calculate_income():
    try:
        myHashrate = float(entry_hashrate.get())
        rBody = {'userName': 'guest@qubic.li', 'password': 'guest13@Qubic.li', 'twoFactorCode': ''}
        rHeaders = {'Accept': 'application/json', 'Content-Type': 'application/json-patch+json'}
        r = requests.post('https://api.qubic.li/Auth/Login', data=json.dumps(rBody), headers=rHeaders)
        token = r.json()['token']
        rHeaders = {'Accept': 'application/json', 'Authorization': 'Bearer ' + token}
        r = requests.get('https://api.qubic.li/Score/Get', headers=rHeaders)
        networkStat = r.json()
        epochNumber = networkStat['scoreStatistics'][0]['epoch']
        epoch97Begin = datetime.strptime('2024-02-21 12:00:00', '%Y-%m-%d %H:%M:%S')
        curEpochBegin = epoch97Begin + timedelta(days=7 * (epochNumber - 97))
        curEpochEnd = curEpochBegin + timedelta(days=7) - timedelta(seconds=1)
        curEpochProgress = (datetime.utcnow() - curEpochBegin) / timedelta(days=7)
        netHashrate = networkStat['estimatedIts']
        netAvgScores = networkStat['averageScore']
        netSolsPerHour = networkStat['solutionsPerHour']
        crypto_currency = 'qubic-network'
        destination_currency = 'usd'
        cg_client = CoinGeckoAPI()
        prices = cg_client.get_price(ids=crypto_currency, vs_currencies=destination_currency)
        qubicPrice = prices[crypto_currency][destination_currency]
        poolReward = 0.85
        incomerPerOneITS = poolReward * qubicPrice * 1000000000000 / netHashrate / 7 / 1.06
        curSolPrice = 1479289940 * poolReward * curEpochProgress * qubicPrice / (netAvgScores * 1.06)
        sols_per_day_average = 24 * myHashrate * netSolsPerHour / netHashrate
        lambda_per_day = sols_per_day_average
        days_in_week = 7
        lambda_week = lambda_per_day * days_in_week
        P_0 = exp(-lambda_week)
        P_0_day = exp(-lambda_per_day)
        P_0_3days = exp(-lambda_per_day*3)
        messagebox.showinfo("Income Estimations", 
                            f"Your estimated income per hour: {myHashrate * incomerPerOneITS/24.0:.2f}$\n"
                            f"Your estimated income per day: {myHashrate * incomerPerOneITS:.2f}$\n"
                            f"Your estimated income per week: {myHashrate * incomerPerOneITS*7:.2f}$\n"
                            f"Your estimated income per month: {myHashrate * incomerPerOneITS*30:.2f}$\n"
                            f"Estimated income per 1 sol: {curSolPrice:.2f}$\n"
                            f"Your estimated sols per day: {sols_per_day_average:.4f}\n"
                            f"Probability of getting NO Solution within a day: {P_0_day*100:.3f}%\n"
                            f"Probability of getting NO Solution within 3 days: {P_0_3days*100:.3f}%\n"
                            f"Probability of getting NO Solution within a week: {P_0*100:.3f}%")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
root = tk.Tk()
root.title("Hashrate Income Calculator")
label_hashrate = tk.Label(root, text="Enter your total hashrate (in it/s):")
label_hashrate.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
entry_hashrate = tk.Entry(root)
entry_hashrate.grid(row=0, column=1, padx=10, pady=5)
calculate_button = tk.Button(root, text="Calculate", command=calculate_income)
calculate_button.grid(row=1, column=0, columnspan=2, pady=10)
root.mainloop()
