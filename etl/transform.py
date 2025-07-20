def is_valid_row(row):
    required_fields = ["customer_name", "drink", "quantity", "price", "branch", "payment_type", "card_number", "date_time"]
    for field in required_fields:
        if field not in row or not row[field].strip():
            return False
    try:
        float(row["price"])
        int(row["quantity"])
    except ValueError:
        return False
    return True

def transform_data(data):
    cleaned_data = []
    for row in data:
        if is_valid_row(row):
            # Remove PII: customer_name, card_number
            cleaned_row = {
                "drink": row["drink"],
                "qty": int(row["quantity"]),
                "price": float(row["price"]),
                "branch": row["branch"],
                "payment_type": row["payment_type"],
                "datetime": row["date_time"]
            }
            cleaned_data.append(cleaned_row)
    return cleaned_data