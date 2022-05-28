import requests #Third party to do web scraping
from bs4 import BeautifulSoup # Used for parsing

products_to_track = [
    {
        "product_url" : "https://www.amazon.in/Test-Exclusive-646/dp/B07HGJKDRR/ref=sr_1_3?crid=DK6G2O92EVE3&dchild=1&keywords=samsung+m21+midnight+blue&qid=1632485588&s=electronics&sprefix=samsung+m21+mi%2Celectronics%2C356&sr=1-3",
        "name" : "Samsung M21-Midnight Blue",
        "target_price" : 16000
    },
    {
        "product_url" : "https://www.amazon.in/Samsung-Galaxy-64GB-Space-Black/dp/B087RT6N5L/ref=sr_1_4?dchild=1&keywords=samsung+ocean+blue+m31&qid=1631888308&sr=8-4",
        "name" : "Samsung Galaxy Black",
        "target_price" : 18000
    },
    {
        "product_url" : "https://www.amazon.in/Samsung-Galaxy-Storage-sAMOLED-Replacement/dp/B098NGDNMT/ref=sr_1_2?crid=DK6G2O92EVE3&dchild=1&keywords=samsung+m21+midnight+blue&qid=1632485588&s=electronics&sprefix=samsung+m21+mi%2Celectronics%2C356&sr=1-2",
        "name" : "Samsung M21-Arctic Blue",
        "target_price" : 10000
    },
    {
        "product_url" : "https://www.amazon.in/Samsung-Galaxy-Bluetooth-Mystic-SM-R840NZKAINS/dp/B08FN4Q6VZ/ref=sr_1_1?dchild=1&keywords=galaxy+watch+3&qid=1633074202&qsid=257-5371846-9012552&sr=8-1&sres=B08FN4Q6VZ%2CB08FN55MSH%2CB096G2JVT7%2CB08LSLDRHG%2CB092TTQX2K%2CB08F23BLBL%2CB08WX6V57T%2CB098P6TXQD%2CB09H7J4MCG%2CB08LNQR27F%2CB07H7X1187%2CB09HC6SJVR%2CB08NBZYFWS%2CB07N3ZY4G2%2CB07ZD5SBFB%2CB09698W4JB&srpt=WEARABLE_COMPUTER",
        "name" : "Samsung-Watch",
        "target_price" : 16000
    },
    {
        "product_url" : "https://www.amazon.in/gp/product/B08VB34KJ1/ref=s9_acss_bw_cg_Budget_4e1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-9&pf_rd_r=TSK3ES2JTGZSRKA1VMSR&pf_rd_t=101&pf_rd_p=8dd3aef1-94fc-4cc0-95c6-4b8c58093253&pf_rd_i=1389401031",
        "name" : "OPPO A74 5G",
        "target_price" : 16000
    }
]

def give_product_price(URL):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }  # A User Agent is nothing but a simple set of strings that any application or any browser sends in order to access the webpage.

    page = requests.get(URL, headers=headers)  # Getting information from the webpage9i.e, Scrapping)

    soup = BeautifulSoup(page.content, 'html.parser')
    product_price = soup.find(id="priceblock_ourprice")
    if (product_price is None):
        product_price = soup.find(id="priceblock_dealprice")
    return product_price.getText()

result_file = open('my_result_file.txt','w')

try:
    for every_product in products_to_track:
        returned_product_price = give_product_price(every_product.get("product_url"))
        print(returned_product_price + "-" + every_product.get("name"))
        my_product_price = returned_product_price[1:]
        my_product_price = my_product_price.replace(',', '')
        my_product_price = int(float(my_product_price))
        print(my_product_price)

        if my_product_price < every_product.get("target_price"):
            print("Available at your required price")
            result_file.write(every_product.get("name") + ' - \t' + 'Available at target price. ' + 'Current price : ' + str(my_product_price) + '\n' )
        else:
            print("Still at current price")

finally:
    result_file.close()


