import csv
from meta_tags_parser import parse_tags_from_url

# Define the path to the CSV file
csv_file = 'sample.csv'

# Open the CSV file in read mode
with open(csv_file, 'r', newline='', encoding='utf-8') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    # Skip the header row if it exists
    next(reader, None)

    # Loop through each row in the CSV file
    for row in reader:
        # Extract the domain name from the row
        domain = row[0]

        try:
            # Create a MetaTagsParser object for the domain
            meta_tags = parse_tags_from_url(f"https://{domain}")

            # Print the results
            print(f"Domain: {domain}")
            print(f"Meta Tags: {meta_tags}")
            print()
        except Exception as e:
            # Print any exceptions that occur
            print(e)
