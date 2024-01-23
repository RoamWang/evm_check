import requests
from time import sleep

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}

def perform_check(wallet: str, key_word: str):
    url = f'https://airdrop-router.cl04.zetachain.com/pre-claim-status?address='
    url += f'{wallet}'
    
    response = requests.get(url, headers=headers)
    
    if response.text.find(key_word) != -1:
        print(response.text)


def check(key_word: str):
    file_path = "evm.txt"

    with open(file_path, "r") as file:
        wallets = [w.strip() for w in file]

    for _, wallet in enumerate(wallets):
        try:
            perform_check(wallet, key_word)
        except Exception as e:
            print(f'Failed to check wallet {wallet}, reason: {e}')
        finally:
            sleep(1)

if __name__ == "__main__":
    check('claimAmount')
