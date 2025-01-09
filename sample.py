import pandas as pd
import psycopg2 

import streamlit as st
st.write("Retail order analysis ajay")
a=st.selectbox("Question", ['1.Find top 10 highest revenue generating products',
'2.Find the top 5 cities with the highest profit margins',
'3. Calculate the total discount given for each category ',
'4.Find the average sale price per product category ',
'5.Find the region with the highest average sale price',
'6.Find the total profit per category',
'7.Identify the top 3 segments with the highest quantity of orders',
'8.Determine the average discount percentage given per region',
'9.Find the product category with the highest total profit',
'10.Calculate the total revenue generated per year',
'11.Top-Selling Products by Revenue',
'12.Year-Over-Year Monthly Sales Comparison',
'13.Best Performing Products by Revenue',
'14.Region-Wise Performance',
'15.Impact of Discounts on Sales',
'16.Category Performance Metrics',
'17.Monthly Regional Sales Analysis',
'18.Revenue from Discounted Sales',
'19.Products with Sales more than 50,000 Revenue',
'20.top-performing product categories in each region based on total revenue',



])
#st.write(a)
connection = psycopg2.connect(
        database="project1",  # Replace with your database name
        user="postgres",          # Replace with your PostgreSQL username
        password="061101",      # Replace with your PostgreSQL password
        host="localhost",              # Replace with your host (default: localhost)
        port="5432"                    # Replace with your port (default: 5432)
    )
cursor = connection.cursor()
if a=='1.Find top 10 highest revenue generating products':
    st.write(a)
   

# Connect to PostgreSQL database

    

    # Execute the query
    cursor.execute('''
       SELECT "Product_Id" AS product_id, SUM("Sale_price") AS sales
    FROM df4
    GROUP BY "Product_Id"
    ORDER BY sales DESC
    LIMIT 10;

    ''')


    # Fetch the results
    table1 = cursor.fetchall()

    # Convert to Pandas DataFrame
    answer_1 = pd.DataFrame(table1, columns=['product_id', 'sale_price'])
    


    st.dataframe(answer_1)

if a=='2.Find the top 5 cities with the highest profit margins':
    st.write(a)
    # Connect to PostgreSQL database

    # Execute the query
    cursor.execute('''
       SELECT "City" AS "city", SUM("Profit") AS total_Profit
    FROM
    "df4"
    GROUP BY 
        "City"
    ORDER BY 
        total_Profit DESC
    LIMIT 5;
    ''')

    # Fetch the results
    table1 = cursor.fetchall()

    # Convert to Pandas DataFrame
    answer_2 = pd.DataFrame(table1, columns=['City', 'total_Profit'])

    st.dataframe(answer_2)

        
if a=='3. Calculate the total discount given for each category ':
    st.write(a)

    cursor.execute('''
    SELECT 
        "Category" AS "Category",SUM("Discount") AS total_discount
    FROM 
        df4  -- Replace with your actual table name
    GROUP BY 
        "Category"
    ORDER BY 
        total_discount DESC;
    ''')
    
    # Fetch the results
    table1 = cursor.fetchall()

    # Convert to Pandas DataFrame
    answer_3 = pd.DataFrame(table1, columns=['Category', 'total_discount'])
    

    st.dataframe(answer_3)

if a=='4.Find the average sale price per product category ':
    st.write(a)

    cursor.execute('''
    SELECT 
        "Category" AS "Category", AVG("Sale_price") AS average_sale_price
    FROM 
        df4  -- Replace with your actual table name
    GROUP BY 
        "Category"
    ORDER BY 
        average_sale_price DESC;
    ''')
    

    # Fetch the results
    table1 = cursor.fetchall()

    # Convert to Pandas DataFrame
    answer_4 = pd.DataFrame(table1, columns=['Category', 'average_sale_price'])
    
    st.dataframe(answer_4)

if a=='5.Find the region with the highest average sale price':
    st.write(a)

    cursor.execute('''
   
     SELECT 
          "Region" AS "Region", AVG("Sale_price") AS avg_sale_price
     FROM df4
     GROUP BY "Region"
     ORDER BY avg_sale_price DESC
     LIMIT 1;
     ''')
     

#     # Fetch the results
    table1 = cursor.fetchall()

#     # Convert to Pandas DataFrame
    answer_5 = pd.DataFrame(table1, columns=['Region', 'average_sale_price'])
#    


    st.dataframe(answer_5)

if a=='6.Find the total profit per category':
    st.write(a)


    cursor.execute('''
   
    SELECT 
        "Category" AS "Category", SUM("Sale_price" - "cost_price") AS total_profit
    FROM df4
    GROUP BY "Category"
    ORDER BY total_profit DESC;
    ''')
    
  

    # Fetch the results
    table1 = cursor.fetchall()

    # Convert to Pandas DataFrame with the correct columns
    answer_6 = pd.DataFrame(table1, columns=['Category', 'total_profit'])
    st.dataframe(answer_6)


if a== '7.Identify the top 3 segments with the highest quantity of orders':
    st.write(a)

    cursor.execute('''
    SELECT 
        "Segment" AS Segment, COUNT(*) AS total_orders
    FROM 
        df4
    GROUP BY 
        "Segment"
    ORDER BY 
        total_orders DESC
    LIMIT 3;
    ''')
    
   

    # Fetch the results
    table1 = cursor.fetchall()

    # Convert the results to a Pandas DataFrame
    answer_7 = pd.DataFrame(table1, columns=['Segment', 'total_orders'])
    
    st.dataframe(answer_7)

if a== '8.Determine the average discount percentage given per region':
    st.write(a)

    cursor.execute('''

    SELECT
        "Region" AS Region, 
        AVG("Discount") AS average_discount
    FROM 
        df4
    GROUP BY 
        "Region"
    ORDER BY 
        average_discount DESC;
    ''')
    
    
    # Fetch the results
    table1 = cursor.fetchall()

    # Convert the results to a Pandas DataFrame with the correct column names
    answer_8 = pd.DataFrame(table1, columns=['Region', 'Average_Discount'])
    
    st.dataframe(answer_8)
    

if a== '9.Find the product category with the highest total profit':
    st.write(a)

    cursor.execute('''

    SELECT 
        "Category" AS product_category, 
        SUM("Profit") AS total_profit
    FROM 
        df4
    GROUP BY 
        "Category"
    ORDER BY 
        total_profit DESC
    LIMIT 1;
    ''')
    
    

    # Fetch the results
    table1 = cursor.fetchall()

    # Convert the results to a Pandas DataFrame with the correct column names
    answer_9 = pd.DataFrame(table1, columns=['Product_category', 'total_profit'])
   
    st.dataframe(answer_9)
if a=='10.Calculate the total revenue generated per year':
    st.write(a)

    cursor.execute('''
 
    SELECT 
        EXTRACT(YEAR FROM "Orde_Date"::DATE) AS year, 
        SUM("Sale_price") AS total_revenue
    FROM 
        df4
    GROUP BY 
        year
    ORDER BY 
        total_revenue DESC;
    ''')
    
   

    # Fetch the results
    table1 = cursor.fetchall()

    # Convert the results to a Pandas DataFrame with the correct column names
    answer_10 = pd.DataFrame(table1, columns=['Year', 'Total_Revenue'])
    
    st.dataframe(answer_10)

  
if a== '11.Top-Selling Products by Revenue':
    st.write(a)

        

    # Updated SQL Query
    cursor.execute('''
    SELECT 
        p."Product_Id",  
        s."Sub_Category", 
        SUM(s."Quantity" * s."Sale_price") AS totalrevenue
    FROM 
        df5 s  
    FULL JOIN
        df1 p  
    ON 
        s."Product_Id" = p."Product_Id"  
    GROUP BY 
        p."Product_Id", s."Sub_Category"
    ORDER BY
        totalrevenue DESC
    LIMIT 10;
    ''')

    # Execute query
    
    table1 = cursor.fetchall()

    # Convert to DataFrame
    answer_11 = pd.DataFrame(table1,columns = ['Product_Id', 'Sub_Category', 'Totalrevenue'])
    
    
    st.dataframe(answer_11)
if a=='12.Year-Over-Year Monthly Sales Comparison':
    st.write(a)

    cursor.execute('''
   WITH MonthlySales AS (
    SELECT
        DATE_PART('year', "Order_Date"::DATE) AS sale_year,
        DATE_PART('month', "Order_Date"::DATE) AS sale_month,
        SUM("Sale_price") AS total_sales
    FROM
        df4
    GROUP BY
        DATE_PART('year', "Order_Date"::DATE),
        DATE_PART('month', "Order_Date"::DATE) 
),
YoYComparison AS (
    SELECT
        curr.sale_year,
        curr.sale_month,
        curr.total_sales AS current_year_sales,
        prev.total_sales AS previous_year_sales,
        (curr.total_sales - prev.total_sales) AS sales_difference,
        CASE
            WHEN prev.total_sales = 0 THEN NULL
            ELSE ((curr.total_sales - prev.total_sales) / prev.total_sales) * 100
        END AS percentage_change
    FROM
        MonthlySales curr
    LEFT JOIN
        MonthlySales prev
    ON
        curr.sale_month = prev.sale_month
        AND curr.sale_year = prev.sale_year + 1
)
SELECT
    sale_month,
    sale_year,
    current_year_sales,
    previous_year_sales,
    sales_difference,
    percentage_change
FROM
    YoYComparison
ORDER BY
    sale_month, sale_year;
    ''')
    
    # Execute the query

    table1 = cursor.fetchall()

    # Convert results to a DataFrame
    answer_12 = pd.DataFrame(table1,columns = ['Sale_Month', 'Sale_Year', 'Current_Year_Sales', 'Previous_Year_Sales', 'Sales_Difference', 'Percentage_Change'])
    st.dataframe(answer_12)
if a=='13.Best Performing Products by Revenue':
    st.write(a)
    
    cursor.execute('''
    SELECT
        p."Product_Id",
        p."Sub_Category",
        SUM(s."Quantity" * s."Sale_price") AS Total_Revenue
    FROM
        df1 p
    JOIN
        df5  s
    ON
        p."Product_Id" = s."Product_Id"
    GROUP BY
        p."Product_Id", p."Sub_Category"
    ORDER BY
        Total_Revenue DESC
    LIMIT 10;
    ''')
    table1 = cursor.fetchall()
    answer_13 = pd.DataFrame(table1,columns = ['Product_Id', 'Sub_Category', 'Total_Revenue'])
    st.dataframe(answer_13)
if a=='14.Region-Wise Performance':  
    st.write(a)
    cursor.execute('''
SELECT
        r."Region",
        SUM(s."Quantity" * s."Sale_price") AS Total_Sales,
        SUM(s."Profit") AS Total_Profit,
        COUNT(s."Order_id") AS Total_Orders
    FROM
        df1 r
    JOIN
        df4 s
    ON
        r."Postal_Code" = s."Postal_Code"
    GROUP BY
        r."Region"
    ORDER BY
        Total_Sales DESC;
    ''')

    # Execute the query
    
    table1 = cursor.fetchall()

    # Convert results to a DataFrame
    answer_14 = pd.DataFrame(table1,columns = ['Region', 'Total_Sales', 'Total_Profit', 'Total_Orders'])
    st.dataframe(answer_14)
if a==  '15.Impact of Discounts on Sales':
    st.write(a)  
    cursor.execute('''
SELECT
        p."Product_Id",
        p."Sub_Category",
        SUM(s."Quantity" * s."List_Price") AS Total_Sales_Before_Discount,
        SUM(s."Quantity" * (s."Sale_price")) AS Total_Sales_After_Discount,
        SUM(s."Discount") AS Total_Discount_Given,
        SUM(s."Quantity" * s."List_Price") - SUM(s."Quantity" * s."Sale_price") AS Discount_Impact,
        CASE
            WHEN SUM(s."Quantity" * s."List_Price") = 0 THEN NULL
            ELSE ((SUM(s."Quantity" * (s."Sale_price")) - SUM(s."Quantity" * s."List_Price")) / SUM(s."Quantity" * s."List_Price")) * 100
        END AS Discount_Impact_Percentage,
        SUM(s."Profit") AS Total_Profit
    FROM
        df1 p
    JOIN
        df5 s
    ON
        p."Product_Id" = s."Product_Id"
    GROUP BY
        p."Product_Id", p."Sub_Category"
    ORDER BY
        Discount_Impact DESC;
    ''')

    # Execute the query
    
    table1 = cursor.fetchall()

    # Convert results to a DataFrame
    answer_15 = pd.DataFrame(table1,columns = [
        'Product_Id', 'Sub_Category',
        'Total_Sales_Before_Discount', 'Total_Sales_After_Discount',
        'Total_Discount_Given', 'Discount_Impact', 'Discount_Impact_Percentage',
        'Total_Profit'])
    st.dataframe(answer_15)
if a== '16.Category Performance Metrics':
    st.write(a)
    
    cursor.execute('''
     SELECT
        p."Category",
        SUM(s."Quantity" * s."List_Price") AS Total_Sales_Before_Discount,
        SUM(s."Quantity" * s."Sale_price") AS Total_Sales_After_Discount,
        SUM(s."Discount") AS Total_Discount_Given,
        SUM(s."Quantity" * s."List_Price") - SUM(s."Quantity" * s."Sale_price") AS Discount_Impact,
        CASE
            WHEN SUM(s."Quantity" * s."List_Price") = 0 THEN NULL
            ELSE ((SUM(s."Quantity" * s."Sale_price") - SUM(s."Quantity" * s."List_Price")) / SUM(s."Quantity" * s."List_Price")) * 100
        END AS Discount_Impact_Percentage,
        SUM(s."Profit") AS Total_Profit,
        SUM(s."Quantity") AS Total_Quantity_Sold
    FROM
        df1 p
    JOIN
        df5 s
    ON
        p."Product_Id" = s."Product_Id"
    GROUP BY
        p."Category"
    ORDER BY
        Total_Sales_Before_Discount DESC;
    ''')

    # Execute the query
    
    table1 = cursor.fetchall()

    # Convert results to a DataFrame
    answer_16 = pd.DataFrame(table1, columns = [
        'Category', 'Total_Sales_Before_Discount', 'Total_Sales_After_Discount',
        'Total_Discount_Given', 'Discount_Impact', 'Discount_Impact_Percentage',
        'Total_Profit', 'Total_Quantity_Sold'
    ])
    st.dataframe(answer_16)
if  a=='17.Monthly Regional Sales Analysis': 
    st.write(a)
    cursor.execute('''
        SELECT
    EXTRACT(YEAR FROM TO_DATE(s."Order_Date", 'YYYY-MM-DD')) AS Year,
    EXTRACT(MONTH FROM TO_DATE(s."Order_Date", 'YYYY-MM-DD')) AS Month,
    r."Region",
    SUM(s."Quantity" * s."Sale_price") AS Total_Sales,
    SUM(s."Profit") AS Total_Profit,
    COUNT(s."Order_id") AS Total_Orders
FROM
    df4 s
JOIN
    df1 r
ON
    s."Postal_Code" = r."Postal_Code"
GROUP BY
    Year, Month, r."Region"
ORDER BY
    Year, Month, r."Region";
    ''')

    # Execute the query
    
    table1 = cursor.fetchall()

    # Convert results to a pandas DataFrame
    answer_17 = pd.DataFrame(table1,columns = ['Year', 'Month', 'Region', 'Total_Sales', 'Total_Profit', 'Total_Orders'])
    
    st.dataframe(answer_17)

if a== '18.Revenue from Discounted Sales':
    st.write(a)
    cursor.execute('''
    SELECT
        p."Product_Id",
        p."Category",
        SUM(s."Quantity" * s."Sale_price") AS Total_Revenue_After_Discount,
        SUM(s."Quantity" * p."List_Price") AS Total_Revenue_Before_Discount,
        SUM(s."Discount") AS Total_Discount_Given,
        SUM(s."Quantity" * p."List_Price") - SUM(s."Quantity" * s."Sale_price") AS Discount_Impact
    FROM
        df4 p
    JOIN
        df5 s
    ON
        p."Product_Id" = s."Product_Id"
    GROUP BY
        p."Product_Id", p."Category"
    ORDER BY
        Discount_Impact DESC;
    ''')

    
    
    table1 = cursor.fetchall()

    answer_18 = pd.DataFrame(table1,columns = ['Product_Id', 'Category', 'Total_Revenue_After_Discount', 
               'Total_Revenue_Before_Discount', 'Total_Discount_Given', 'Discount_Impact'])
    
    st.dataframe(answer_18)

if a== '19.Products with Sales more than 50,000 Revenue':
    st.write(a)
    cursor.execute('''
    SELECT
        p."Product_Id",
        p."Sub_Category",
        p."Category",
        SUM(s."Quantity" * s."Sale_price") AS Total_Revenue
    FROM
        df4 p
    JOIN
        df5 s
    ON
        p."Product_Id" = s."Product_Id"
    GROUP BY
        p."Product_Id", p."Sub_Category", p."Category"
    HAVING
        SUM(s."Quantity" * s."Sale_price") > 50000
    ORDER BY
        Total_Revenue DESC;
    ''')

    # Execute the query

    table1 = cursor.fetchall()

    # Convert results to a DataFrame
    answer_19 = pd.DataFrame(table1,columns = ['Product_Id', 'Sub_Category', 'Category', 'Total_Revenue'])
    
    st.dataframe(answer_19)
if a== '20.top-performing product categories in each region based on total revenue':
    st.write(a)
    cursor.execute('''
    WITH RegionalSales AS (
        SELECT
            r."Region" AS Region, 
            p."Category" AS Category,
            SUM(s."Quantity" * s."Sale_price" - s."Discount") AS Total_Revenue,
            SUM(s."Profit") AS Total_Profit
        FROM
            df1 r
            JOIN df5 s ON r."Postal_Code" = s."Postal_Code"
            JOIN df3 p ON s."Product_Id" = p."Product_Id"
        GROUP BY
            r."Region", p."Category"
    ),
    TopCategories AS (
        SELECT
            Region,
            Category,
            Total_Revenue,
            Total_Profit,
            RANK() OVER (PARTITION BY Region ORDER BY Total_Revenue DESC) AS Rank
        FROM
            RegionalSales
    )
    SELECT
        Region,
        Category,
        Total_Revenue,
        Total_Profit
    FROM
        TopCategories
    WHERE
        Rank = 1
    ORDER BY
        Region;
    ''')
    
    table1 = cursor.fetchall()

    # Convert results to a DataFrame
    answer_20 = pd.DataFrame(table1,columns = ['Region', 'Category', 'Total_Revenue', 'Total_Profit'])
    
    st.dataframe(answer_20) 





   