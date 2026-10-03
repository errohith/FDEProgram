import csv
from pathlib import Path
from socket import close

DATA_DIR = Path(__file__).resolve().parent.parent / 'data'

field1 = 'Invoice Number'
field2 = 'Vendor'
field3 = 'Amount'
field4 = 'status'

FIELDNAMES = [field1, field2, field3, field4]
with open(DATA_DIR / 'homework_invoices.csv', mode='r') as file:
    csv_reader = csv.DictReader(file, fieldnames=FIELDNAMES) # can also be read with reader, can be accessed using row[0], row[1], etc. but DictReader allows access by column name.
    next(csv_reader)  # Skip the header row - comment this out if you don't want to skip the header row
    with open(DATA_DIR / 'homework_invoices_output.csv', mode='w', newline='') as output_file:
        csv_writer = csv.DictWriter(output_file, fieldnames=FIELDNAMES)
        csv_writer.writeheader()
        processedCount = 0
        validRowCount = 0
        invalidRowCount = 0
        for row in csv_reader:
            try: 
                invoice_number = row[field1]
                vendor = row[field2]
                amount = float(row[field3])  # Convert amount to float
                status = row[field4]
                if vendor and amount and status:  # Check if all required fields are present
                    print(f"Invoice Number: {invoice_number}, Vendor: {vendor}, Amount: {amount}, Status: {status}")
                    if amount > 100000:
                        csv_writer.writerow({field1: invoice_number, field2: vendor, field3: amount, field4: status})
                        processedCount += 1
                    validRowCount += 1
                else:
                 raise ValueError("Missing required fields or invalid amount")
            except ValueError as e:
                invalidRowCount += 1
                print(f"Error reading row: {e}")
output_file.close()
file.close()
print(f"Total Invoices Read: {validRowCount + invalidRowCount}, \nValid rows: {validRowCount}, \nInvalid rows: {invalidRowCount}")
print(f"Total Matches Found for amount > 100000: {processedCount}")
print(f"Number of rows with missing values or invalid amounts: {invalidRowCount + validRowCount - processedCount}")