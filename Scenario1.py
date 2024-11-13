import pandas as pd
from collections import defaultdict

# Load the Excel file
# Update the path to your file here
df = pd.read_excel(r"D:\Outlier AI\marketing analysis\Scenario1.xlsx")

# Initialize an empty dictionary to hold orders and their transactions
order_dict = defaultdict(list)

# Step 1: Populate the dictionary with order IDs and their respective transactions
for _, row in df.iterrows():
    full_transaction_id = row["Order ID"]

    # Extract the base Order ID (before any '-' or '_')
    base_order_id = full_transaction_id.split('-')[0].split('_')[0]

    # Add the transaction to the list for this base order ID
    order_dict[base_order_id].append(full_transaction_id)

# Dictionary to track orders that have issues (missing the initial "_0" transaction)
orders_having_issue = {}

# Check each order ID in the dictionary to see if its corresponding "_0" transaction is missing
for base_id, transactions in order_dict.items():
    initial_order_id = base_id + '_0'
    if initial_order_id not in transactions:
        orders_having_issue[base_id] = transactions

# Print the orders with issues and count of problematic orders
print("Orders with issues:", orders_having_issue)
print("Total problematic orders:", len(orders_having_issue))

# Print the percentage of orders with issues
total_orders = len(order_dict)
percentage_issue = (len(orders_having_issue) / total_orders) * 100
print(f"Out of {total_orders} orders, {round(percentage_issue, 2)}% have issues")

# Prepare the data for the DataFrame
data = {key: ', '.join(values) for key, values in orders_having_issue.items()}

# Convert the prepared data into a DataFrame
df_output = pd.DataFrame(list(data.items()), columns=['Order ID', 'Transactions'])

# Save the DataFrame to a CSV file
output_file = r"D:\Outlier AI\marketing analysis\orders_with_issues.csv"
df_output.to_csv(output_file, index=False)
print(f"Data successfully written to {output_file}")

# Additional code to print orders that don't have "_0" ending
orders_not_ending_in_0 = []

# Iterate through each transaction in the dictionary to find those not ending in "_0"
for base_id, transactions in order_dict.items():
    for transaction in transactions:
        if not transaction.endswith('_0'):
            orders_not_ending_in_0.append(transaction)

# Print orders that do not end with "_0"
print("Orders not ending in '_0':", orders_not_ending_in_0)
print("Total orders not ending in '_0':", len(orders_not_ending_in_0))
