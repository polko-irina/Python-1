import pandas
invoices_2 = pandas.read_csv("invoices_2.csv")
invoices_2 = invoices_2.dropna().reset_index()
invoices_2["invoice_date"] = pandas.to_datetime(invoices_2["invoice_date"], dayfirst=True)

invoices_2["payment_date"] = pandas.to_datetime(invoices_2["payment_date"], dayfirst=True)
invoices_2["paid_in"] = invoices_2["payment_date"] - invoices_2["invoice_date"]

print(invoices_2["paid_in"].mean()) # pruměr ze sloupečka "paid_in"

print(invoices_2.groupby("customer")["paid_in"].mean())

