import okx.Funding as Funding
from helpers import parse_keys
from time import sleep

CCY = "ETH"
DEST = 4
WALLET_TYPE = "private"
CHAIN = "ETH-Linea"


def main():
    keys = parse_keys()
    api_key = input("Enter api key")
    secret_key = input("Enter secret key")
    passphrase = input("Enter passphrase")
    quantity = float(input("Enter the quantity"))
    fund = Funding.FundingAPI(api_key, secret_key, passphrase, flag="0")
    for key in keys:
        resp = fund.withdrawal(ccy=CCY, amt=quantity, dest=DEST, toAddr=key, fee=0.0002, chain=CHAIN)
        print(resp)
        sleep(2)


if __name__ == "__main__":
    main()
