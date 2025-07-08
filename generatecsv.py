import csv
filename = input("Input the file name: ")
if not filename.lower().endswith('.csv'):
    filename += '.csv'
with open(filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['number', 'solved', 'mode', 'solution'])
    for number in range(1000, 3000):
        writer.writerow([number, 'FALSE', '', ''])
print(f"CSV file '{filename}' generated successfully.")
