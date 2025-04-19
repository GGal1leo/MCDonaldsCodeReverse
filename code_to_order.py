from datetime import datetime, timedelta
code = "9HYW-XRZH-PTB3"

# First 3 chars is store ID 
# next 3 chars is usually order id last 2 digits + (reg number * 100)
# next 5 chars is Date/time of purchase (represented as number of minutes since 2016-02-01 00:00).
# Last char is Check digit (Luhn mod N algorithm; uses 25 as a base).
# The check digit is the last character of the code.

#Values are encoded using the following base 25 system:
# Decimal	0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	21	22	23	24
# Base 25	C	M	7	W	D	6	N	4	R	H	F	9	Z	L	3	X	K	Q	G	V	P	B	T	J	Y
# The base 25 system is used to encode the values in the code.

CHARS = "CM7WD6N4RHF9ZL3XKQGVPBTJY"
BASE = len(CHARS)
EPOCH_BEGIN = datetime(2016, 2, 1)

# decode the code
code = code.replace("-", "")
store_id = code[:3]
#decode store id 
def decode_base25(code):
    num = 0 
    for x,c in enumerate(code):
        num += CHARS.index(c) * (BASE ** (len(code) - x - 1))
    return num

store_id = decode_base25(store_id)

# decode order id 
order_id = code[3:6]
order_id = decode_base25(order_id) 
order_id = order_id % 100

# decode date/time of purchase
time = code[6:11]
time = decode_base25(time)

# decode check digit 
check_digit = code[11]
check_digit = CHARS.index(check_digit)


print("Order ID:", order_id)
#print("Time:", time)
print("Store ID:", store_id)

# convert time to datetime object
time = EPOCH_BEGIN + timedelta(minutes=time)

time = time.strftime("%d-%m-%Y %H:%M:%S")
print("Time:", time)
