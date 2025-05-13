import requests

init_currency = input("Enter the initial currency (e.g. USD): ").upper()
target_currency = input("Enter the target currency (e.g. EGP): ").upper()


while True:
    try :
        amount = float((input("enter the amont that you wamt to covert ")))
    except:
        print ("please enter a postive amount")    
        continue
    if amount == 0 :
        print(" the amount has to be greater that 0 ")
        continue
    else :
            break

url = f"https://api.apilayer.com/currency_data/convert?to={target_currency}&from={init_currency}&amount={amount}"

payload = {}
headers= {
  "apikey": "8SADEJpciNPq7zoZIM3eAVZVI50seBBm"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
if (status_code) != 200:
     print(" sorry try again")
     quit()
result = response.json()
converted_amount= result["result"]
print(f"The amount is {converted_amount} {target_currency}")
