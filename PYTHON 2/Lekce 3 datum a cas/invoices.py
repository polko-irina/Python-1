import pandas
import numpy
import datetime
today_day = datetime.datetime(2021, 9, 1)

invoices = pandas.read_csv("invoices.csv")
invoices["invoice_date_converted"] = pandas.to_datetime(invoices["invoice_date"])

invoices["invoice_date_converted"] = pandas.to_datetime(invoices["invoice_date"], dayfirst=True) # psat vždy !!! dayfirst - den na začatku

invoices["due_date"] = invoices["invoice_date_converted"] + pandas.Timedelta("P60D")

invoices["status"] = numpy.where(invoices["due_date"] < today_day, "owerdue", "before due date")

# print(invoices.groupby("status")["amount"].sum())


# print(invoices.head())