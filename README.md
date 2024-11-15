# Ecommerce Order Tracking Analysis

## Author
**Ayush Meher**  
*Data Scientist*  
Experienced in analyzing Ecommerce, Marketing, CRM, and Healthcare datasets.

---

## Project Overview
This project addresses an order-tracking issue on our ecommerce platform. The goal is to determine the volume of orders affected by tracking issues compared to the total number of orders.

## Problem Statement
Some orders are not following the expected tracking format, potentially affecting order processing. Specifically, we need to:
1. Identify **Base Orders** with IDs ending in `_0`.
2. Detect **Upselling Orders** with IDs ending in `-1_0`, `-2_0`, etc., which indicate higher quantity or premium versions of the original product.

## Objective
Analyze how many orders exhibit this issue compared to the total number of correctly processed orders using the provided data.

---

## Approach 1: Python Solution

### Steps
1. **Load Order Data** from Excel, where each row contains an Order ID.
2. **Initialize Storage** to categorize orders by their base Order ID.
3. **Separate Base and Upselling Orders**:
   - For each Order ID, extract the base order (before `-` or `_` suffixes).
   - Store each Order ID under its base order.
4. **Identify Missing Base Orders** (`_0` suffix):
   - Check if the base order includes an initial order ending in `_0`.
   - If `_0` is missing, add this order to the issue list.
5. **Calculate and Report Issues**:
   - Count and list problematic orders.
   - Calculate the percentage of problematic orders out of all orders.
6. **Identify Orders Not Ending in `_0`**.
7. **Output and Save Results**:
   - Print problematic orders and those not ending in `_0`.
   - Save issue data to a CSV file.

### Output Example
- Problematic Orders:  
  `{ 'D4587E914A': ['D4587E914A-4_0'], '543D480FE6': ['543D480FE6-1_0'] }`
- Total problematic orders: 3549 out of 30174 (11.76%).

---

## Approach 2: Excel Solution

### Steps
1. **Identify Relevant Orders**: Filter for base orders (`_0`) and exclude others (like `-2_0`).
2. **Calculate Total Orders**.
3. **Extract Unique Order Numbers** using a Pivot Table.
4. **Verify Base Sequence** for each unique order.
5. **Calculate Missing Base Sequences**.

### Link to Spreadsheet:
[Excel Analysis Template](https://docs.google.com/spreadsheets/d/1jMdOoL66a3xGbUYlwJEhVbAhlgE_KTI1PJHc-brLE_A/edit?usp=sharing)

---

## Conclusion
Using both Python and Excel approaches, we identify orders with tracking issues and calculate the extent of the problem, providing insights into areas needing correction.
