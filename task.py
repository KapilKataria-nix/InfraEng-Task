import csv, random
from datetime import datetime, timedelta

def random_data():
    order_id = random.randint(1000, 9999)
    customer_id = random.randint(100, 999)
    order_date = (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%d-%m-%y')
    product_id = random.randint(1, 100)
    product_name = f"Product{product_id}"
    product_price = round(random.uniform(10, 1000), 2)
    quantity = random.randint(1, 10)

    return [order_id, customer_id, order_date, product_id, product_name, product_price, quantity]



def writer_csv():
    data_length = 10
    with open('orders.csv','w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Order_ID', 'Customer_ID', 'Order_Date', 'Product_ID', 'Product_Name', 'Product_Price', 'Quantity'])
        for _ in range(data_length):
            writer.writerow(random_data())

