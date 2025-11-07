import csv
import matplotlib.pyplot as plt

def read(file_path):
    """Read CSV and return a list of dictionaries"""
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data


def calculate(data):
    """Filter and prepare India's population data over the years"""
    years = []
    populations = []

    for row in data:
        if row['Region'].strip().lower() == 'india':
            years.append(int(row['Year']))
            populations.append(float(row['Population']) / 1_000_000)  # convert to millions

    return years, populations


def plot(years, populations):
    """Plot bar chart of India's population over the years (in millions)"""
    plt.figure(figsize=(10, 6))
    plt.bar(years, populations, color='orange', edgecolor='black')

    plt.title("India Population Over the Years", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Population (in millions)", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save figure
    plt.savefig("plots/india_population_over_years.png", dpi=300)


    plt.show()


def execute():
    file_path = "data/Population_estimate_data.csv"
    data = read(file_path)
    years, populations = calculate(data)
    plot(years, populations)


# Run
if __name__ == "__main__":
    execute()
