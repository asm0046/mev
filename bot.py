import os
import json
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

INFURA_URL = os.getenv('INFURA_URL')
PRIVATE_KEY = os.getenv('PRIVATE_KEY')
WALLET_ADDRESS = os.getenv('WALLET_ADDRESS')

web3 = Web3(Web3.HTTPProvider(INFURA_URL))

if not web3.isConnected():
    print("Bağlantı başarısız")
    exit()

print("Bağlantı başarılı")

def check_arbitrage():
    # Burada arbitraj fırsatlarını kontrol etmek için kodunuzu yazın
    pass

def main():
    print("MEV bot çalışıyor...")
    while True:
        try:
            check_arbitrage()
        except Exception as e:
            print(f"Hata: {e}")

if __name__ == "__main__":
    main()
