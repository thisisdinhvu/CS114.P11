import pandas as pd
import sys

df = pd.read_csv(sys.stdin, encoding='unicode_escape', encoding_errors='replace')

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
last_date_byID = df.groupby('CustomerID')['InvoiceDate'].max().reset_index()
oldest_date = last_date_byID['InvoiceDate'].min()
last_date_byID['score'] = (last_date_byID['InvoiceDate'] - oldest_date).dt.days

res = last_date_byID.sort_values('CustomerID')[['CustomerID', 'score']]

print(f"{'CustomerID':>11} {'score':>7}")
for _, row in res.iterrows():
    sys.stdout.write(f"{row['CustomerID']:>11.1f}{int(row['score']):>7}\n")