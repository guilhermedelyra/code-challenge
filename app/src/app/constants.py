table_idx = {
    "categories": ['category_id'],
    "suppliers": ['supplier_id'], 
    "products": ['product_id'], # category e suppliers

    "customer_demographics": ['customer_type_id'], 
    "customer_customer_demo": ['customer_id', 'customer_type_id'], # customer_demographics
    "customers": ['customer_id'], # customer_customer_demo 

    "region": ['region_id'], 
    "territories": ['territory_id', 'region_id'], # region
    "employees": ['reports_to', 'employee_id'], # employees
    "employee_territories": ['employee_id', 'territory_id'], # territories, employees
    
    "us_states": ['state_id'], 
    
    "shippers": ['shipper_id'], 
    "orders": ['order_id'], # customer,  shipper, 
    
    "order_details": ['order_id', 'product_id']
}

table_relationships = {
    "products": ['categories', 'suppliers'],
    "customer_customer_demo": ['customer_demographics'],
    "customers": ['customer_customer_demo'],
    "territories": ['region'],
    "employees": ['employees'],
    "employee_territories": ['territories', 'employees'],
    "orders": ['customers', 'shippers', 'employees'],
    "order_details": ['orders', 'products']
}