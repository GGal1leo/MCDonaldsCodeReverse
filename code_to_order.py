from datetime import datetime, timedelta

# Character mapping for base-25 encoding
CHARS = "CM7WD6N4RHF9ZL3XKQGVPBTJY"
BASE = len(CHARS)
EPOCH_BEGIN = datetime(2016, 2, 1)

def decode_base25(code):
    """Decode a string from base-25 to decimal number."""
    num = 0 
    for x, c in enumerate(code):
        num += CHARS.index(c) * (BASE ** (len(code) - x - 1))
    return num

def decode_receipt_code(code):
    """
    Decode a McDonald's Ireland receipt code.
    
    Args:
        code (str): The receipt code in format XXXX-XXXX-XXXX
        
    Returns:
        dict: A dictionary containing:
            - store_id: The store identifier
            - order_id: The last 2 digits of the order ID
            - timestamp: The purchase timestamp
            - check_digit: The check digit value
    """ 
    code = code.replace("-", "") 
    # Extract and decode store ID (first 3 chars)
    store_id = decode_base25(code[:3])
    # Extract and decode order ID (next 3 chars)
    order_id = decode_base25(code[3:6]) % 100
    # Extract and decode timestamp (next 5 chars)
    time_minutes = decode_base25(code[6:11])
    timestamp = EPOCH_BEGIN + timedelta(minutes=time_minutes) 
    check_digit = CHARS.index(code[11])
    
    return {
        "store_id": store_id,
        "order_id": order_id,
        "timestamp": timestamp.strftime("%d-%m-%Y %H:%M:%S"),
        "check_digit": check_digit
    }

# Example usage
if __name__ == "__main__":
    example_code = "9HYW-XRZH-PTB3"
    result = decode_receipt_code(example_code)
    
    print("Decoded Receipt Information:")
    print(f"Store ID: {result['store_id']}")
    print(f"Order ID: {result['order_id']}")
    print(f"Purchase Time: {result['timestamp']}")
    print(f"Check Digit: {result['check_digit']}")
