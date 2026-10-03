invoice_amount = 55000

if invoice_amount < 1000:
    invoice_approver = "Supervisor"

elif invoice_amount >= 50000:
    invoice_approver = "Manager and Director"

elif invoice_amount > 25000:
    invoice_approver = "Manager"

else:
    invoice_approver = "No approver defined"

print("Invoice Amount:", invoice_amount)
print("Invoice Approver:", invoice_approver)


invoice_amount = 50000

match invoice_amount:
    case amount if amount < 1000:
        invoice_approver = "Supervisor"

    case amount if amount >= 50000:
        invoice_approver = "Manager and Director"

    case amount if amount > 25000:
        invoice_approver = "Manager"

    case _:
        invoice_approver = "No approver required"

print("Invoice Amount:", invoice_amount)
print("Invoice Approver:", invoice_approver)