def get_field(field, d_type = str):
    return lambda x: d_type(x[field])

def get_records(file):
    data = [line.strip().split('\t') for line in file.readlines()]
    fields = data.pop(0)
    return [{fields[i]:record[i] for i in range(len(fields))} for record in data]

with open('games.csv', 'r') as games:
    records = get_records(games)
    records.sort(key = get_field('unit_price', float), reverse=True)
    most_expensive = records[0]['title']
    print(most_expensive)

with open('customers.csv', 'r') as cust:
    records = get_records(cust)
    records.sort(key = get_field('dob'))
    oldest = records[0]['cust_name']
    print(oldest)