import csv
import matplotlib.pyplot as plt
import os

def read(file_path):
    """Read CSV and return a list of dictionaries"""
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data


def calculate(data):
    """Filter and prepare ASEAN countries' population data for 2014"""
    asean_countries = [
        "brunei darussalam", "cambodia", "indonesia", "lao people's democratic republic",
        "malaysia", "myanmar", "philippines", "singapore", "thailand", "viet nam"
    ]

    countries = []
    populations = []

    for row in data:
        if int(row['Year']) == 2014 and row['Region'].strip().lower() in asean_countries:
            countries.append(row['Region'])
            populations.append(float(row['Population']) / 1_000_000)  # convert to millions

    return countries, populations


def plot(countries, populations):
    """Plot bar chart of ASEAN countries' population for 2014 (in millions)"""
    plt.figure(figsize=(10, 6))
    plt.bar(countries, populations, color='orange', edgecolor='black')

    plt.title("ASEAN Countries Population in 2014", fontsize=14)
    plt.xlabel("Country", fontsize=12)
    plt.ylabel("Population (in millions)", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()

    # Ensure plots directory exists
    os.makedirs("plots", exist_ok=True)

    # Save figure
    plt.savefig("plots/asean_population_2014.png", dpi=300)
    plt.show()


def execute():
    file_path = "data/Population_estimate_data.csv"
    data = read(file_path)
    countries, populations = calculate(data)
    plot(countries, populations)


# Run
if __name__ == "__main__":
    execute()
