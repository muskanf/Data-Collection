import re

def extract_info(file_path, output_file_path):
    with open(file_path, 'r') as file:
        content = file.readlines()

    with open(output_file_path, 'w') as output_file:
        for line in content:
            # Find the title using regex, assuming it always follows the year and ends before 'In Proceedings'
            title_search = re.search(r'\d{4}\. (.*?)\. In Proceedings', line)
            title = title_search.group(1) if title_search else ''

            # Find the https link using regex
            link_search = re.search(r'(https://doi\.org/\d+\.\d+/\d+)', line)
            link = link_search.group(1) if link_search else ''

            # Write the title and link to the output file
            output_file.write(f'{title}\n {link}')

# Example usage:
input_file_path = 'acm.txt'  # Replace with your actual input file path
output_file_path = 'extracted_data.txt'  # The output file where the data will be written
extract_info(input_file_path, output_file_path)


