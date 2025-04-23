# variables
paper_packs = 500
staples = 60
printers = 20
chairs = 75

# Calculations
staples += 10
num_printers = printers <= 25

total = paper_packs + staples + printers + chairs

# Print results
print(f"Paper pack: {paper_packs}")
print(f"Staples: {staples}")
print(f"Printers: {printers}")
print(f"Chairs: {chairs}")

print(f"Is the printer less than or equal to 25: {num_printers}")