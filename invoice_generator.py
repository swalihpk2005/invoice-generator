print("==== INVOICE GENERATOR ====")
items=[]
customer_name=input("Enter name of the customer: ")
while True:
    product=input("Enter name of product: ")
    quantity=int(input("Quantity: "))
    unit_price=float(input("Price of One unit: "))

    total=quantity*unit_price

    items.append({
        "Product": product,
        "Quantity": quantity,
        "Price": unit_price,
        "Total": total  
    })

    add_more=input("Add another product(yes/no): ").lower()
    if add_more=="no":
        break

excluding_tax=0
      

print("\n========== INVOICE ==========")
print(f"Customer : {customer_name}")
print("----------------")
for item in items:
    print(f"Product  : {item['Product']}")
    print(f"Quantity : {item['Quantity']}")
    print(f"Unit Price: ₹{item['Price']:.2f}")
    print(f"Total    : ₹{item['Total']:.2f}")
    print("--------------")
    excluding_tax+=item['Total']
gst=(18/100) * excluding_tax
grand_total=excluding_tax+ gst
#note: 18% tax value indicate GST value for common products in India. 
print(f"GST: ₹{gst:.2f}")
print(f"Grand total: ₹{grand_total:.2f}")

print("=============================")