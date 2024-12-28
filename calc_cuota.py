# Loan calculation
# Loan amount (principal)
principal = 50000000  # COP
# Annual effective interest rate
annual_interest_rate = 0.0149  # 1.49% E.A.
# Loan duration in months
loan_duration_months = 12

# Monthly interest rate derived from annual rate
monthly_interest_rate = (1 + annual_interest_rate)**(1/12) - 1

# Calculate the monthly payment using the annuity formula
# Monthly payment formula for an installment loan: P * (r * (1 + r)^n) / ((1 + r)^n - 1)
monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate)**loan_duration_months) / ((1 + monthly_interest_rate)**loan_duration_months - 1)

monthly_payment, monthly_interest_rate
