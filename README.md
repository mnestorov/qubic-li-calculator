# Qubic-Li Earnings Calculator

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

## Overview
The Qubic-Li Earnings Calculator is a Python-based tool designed to provide cryptocurrency miners with an estimation of their potential earnings from mining Qubic in [qubic-li](https://app.qubic.li/) pool. It calculates earnings based on the user's rig hashrate, considering current network statistics and Qubic's market price.

## Features
- **Earnings Estimation**: Calculate your daily mining earnings based on your hashrate.
- **Epoch Information**: Display information about the current mining epoch, including start and end times, and progress.
- **Network Statistics**: View key network metrics such as estimated network hashrate, average score, and solutions per hour.
- **Cryptocurrency Market Data**: Fetch the latest Qubic price from the CoinGecko API for accurate earnings calculations.

## Prerequisites

Before you start, ensure you have the following:

- Python 3.6 or newer
- pip (Python package manager)

## Installation

### Step 1: Clone the Repository

```shell
git clone https://github.com/mnestorov/qubic-li-calculator.git
cd qubic-li-calculator
```
### Step 2: Making start.sh Executable

Ensure start.sh is executable by running:

```shell
chmod +x start.sh
```

### Step 3: Install Dependencies

All required Python packages (like `requests` and `pycoingecko`) need to be installed globally:

```shell
pip3 install requests pycoingecko
```

## Usage

To run the calculator, use the provided `start.sh` script:

```shell
./start.sh
```

Follow the on-screen prompts to enter your rig's total hashrate in it/s and receive your earnings estimation.

## Development

Contributions to the Qubic Earnings Calculator are welcome! To contribute:

- Fork the repository.
- Create your feature branch (git checkout -b feature/AmazingFeature).
- Commit your changes (git commit -am 'Add some AmazingFeature').
- Push to the branch (git push origin feature/AmazingFeature).
- Open a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.

## Acknowledgments

Thanks to the CoinGecko API for providing real-time cryptocurrency market data. A big shoutout to the Qubic mining community for their insights and data contributions.
