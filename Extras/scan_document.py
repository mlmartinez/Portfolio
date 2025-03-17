'''
Qualification using Python.
The output of this application will show uppercase letters in 
the form of a blank grid and unicode characters.
'''
from bs4 import BeautifulSoup
import requests
# Default URL is empty
GOOGLE_DOC_URL = ""

def main():
    """Main  function that coordinates processing."""
    url = get_document_url(GOOGLE_DOC_URL)
    print(f"Using URL: {url}")
    html_content = scan_document(url)
    if html_content:
        create_coordinates(html_content)

def get_document_url(default_url: str) -> str:
    """
    Retrieves URL, using default if valid or prompting user.
    """
    cleaned_url = default_url.strip()
    if not cleaned_url:  # If default is empty/whitespace
        return input("Enter Google Doc URL: ").strip()
    return cleaned_url

def scan_document(url):
    """
    Retrieves HTML content from  URL.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except ImportError as e:
        print(f"Error fetching document: {e}")
        return None

def extract_tables(html_content):
    """
    Parses HTML content to extract structured table data.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    return [
        [
            [cell.get_text(separator=' ', strip=True)
            for cell in row.find_all(['th', 'td'])]
            for row in table.find_all('tr')
            if row.find_all(['th', 'td'])
        ]
        for table in soup.find_all('table')
    ]

def split_columns(table):
    """
    Divides a table into three vertical columns, excluding header row.
    """
    column_one, column_two, column_three = [], [], []
    for row in table[1:]:  # Skip header
        if len(row) >= 3:
            column_one.append(row[0])
            column_two.append(row[1])
            column_three.append(row[2])
    return column_one, column_two, column_three

def create_coordinates(html_content):
    """
    Processes extracted HTML content to generate coordinate grids from tables.
    """
    tables = extract_tables(html_content)
    for table in tables:
        if table:  # Only process non-empty tables
            col1, col2, col3 = split_columns(table)
            print_letter_grid(col1, col3, col2)

def print_letter_grid(x_coords, y_coords, column_two):
    """
    Creates and displays a grid with uppercase values at specified coordinates.
    """
    try:
        x_coords = [int(x) for x in x_coords]
        y_coords = [int(y) for y in y_coords]
    except ValueError:
        print("Coordinates must be integers.")
        return

    if not x_coords or not y_coords or not column_two:
        print("Missing coordinate data.")
        return

    max_x, max_y = max(x_coords), max(y_coords)
    grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for i, (x, y) in enumerate(zip(x_coords, y_coords)):
        if 0 <= y <= max_y and 0 <= x <= max_x:
            grid[max_y-y][x] = str(column_two[i])

    for row in grid:
        print(' '.join(row))

if __name__ == "__main__":
    main()
