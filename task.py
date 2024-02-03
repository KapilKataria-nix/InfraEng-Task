import csv
import random
from datetime import datetime, timedelta

def generate_random_data():
    order_id = random.randint(1000, 9999)
    customer_id = random.randint(100, 999)
    order_date = (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%d-%m-%y')
    product_id = random.randint(1, 100)
    product_name = f"Product{product_id}"
    product_price = round(random.uniform(10, 1000), 2)
    quantity = random.randint(1, 10)

    return [order_id, customer_id, order_date, product_id, product_name, product_price, quantity]

def write_to_csv(file_path, data_length=10):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Order_ID', 'Customer_ID', 'Order_Date', 'Product_ID', 'Product_Name', 'Product_Price', 'Quantity'])
        for d in range(data_length):
            writer.writerow(generate_random_data())

def calculate_revenue_by_month(file_path):
    revenue = {}
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                order_date = datetime.strptime(row['Order_Date'], '%d-%m-%y')
                month = order_date.month
                rev = round(float(row['Product_Price']), 2) * int(row['Quantity'])
                if month in revenue:
                    revenue[month] += rev
                else:
                    revenue[month] = rev

        for k, v in revenue.items():
            print(f"Month: {k}, Total Revenue generated in each month: {v}")

    except Exception as e:
        print(f"Error Calculating Monthly Revenue: {e}")

def calculate_revenue_by_product(file_path):
    revenue = {}
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                product_name = row['Product_Name']
                rev = round(float(row['Product_Price']), 2) * int(row['Quantity'])
                if product_name in revenue:
                    revenue[product_name] += rev
                else:
                    revenue[product_name] = rev

        for k, v in revenue.items():
            print(f"Product Name: {k}, Total Revenue generated by product: {v}")

    except Exception as e:
        print(f"Error Calculating Revenue for Each Product: {e}")

def calculate_customer_revenue(file_path):
    revenue = {}
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                customer_id = row['Customer_ID']
                rev = round(float(row['Product_Price']), 2) * int(row['Quantity'])
                if customer_id in revenue:
                    revenue[customer_id] += rev 
                else:
                    revenue[customer_id] = rev

        for k, v in revenue.items():
            print(f"Customer ID: {k}, Total Revenue generated by customer: {v}")

        
    except Exception as e:
        print(f"Error Calculating Revenue for Each Customer: {e}")

def get_top_10_customers(file_path):
    revenue = {}
    try:
        with open(file_path, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                customer_id = row['Customer_ID']
                rev = round(float(row['Product_Price']), 2) * int(row['Quantity'])
                if customer_id in revenue:
                    revenue[customer_id] += rev 
                else:
                    revenue[customer_id] = rev

        top_list = sorted(revenue.items(), key=lambda x: x[1], reverse=True)[:10]

        for k, v in top_list:
            print(f"Customer ID: {k}, Total Revenue generated by customer: {v}")

    except Exception as e:
        print(f"Error in Getting Top 10 Customers: {e}")

if __name__ == '__main__':
    try:
        def task():
            csv_file_path = 'orders.csv'
            print('CSV file is created!!!!!')
            print('----------------------------------------------------------------------------------------\n')
            write_to_csv(csv_file_path)
            print('\n1. Revenue Generated in Each Month!!!!!')
            calculate_revenue_by_month(csv_file_path)
            print('\n2. Revenue Generated By Each Product!!!!!')
            print('----------------------------------------------------------------------------------------\n')
            calculate_revenue_by_product(csv_file_path)
            print('\n3. Revenue Generated By Each Customer!!!!!')
            print('----------------------------------------------------------------------------------------\n')
            calculate_customer_revenue(csv_file_path)
            print('\n4. Top-10 Customers with Highest Revenue!!!!!')
            print('----------------------------------------------------------------------------------------\n')
            get_top_10_customers(csv_file_path)
            print('\n')
        print('Select 0 to Run the Test')
        print('Select 1 to Run the Task')
        choice = int(input('\nEnter Your Choice: '))
        if choice == 1:
            print('\nThe Task is Running!!!!!\n')
            task()

    except Exception as e:
        print(f"Error: {e}")
