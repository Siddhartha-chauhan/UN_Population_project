import csv
import matplotlib.pyplot as plt

def read(file_path):
    """Read CSV and return a list of dictionaries"""
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data


def calculate(data):
    """Calculate total SAARC population per year"""
    saarc_countries = {
        'afghanistan', 'bangladesh', 'bhutan', 'india',
        'maldives', 'nepal', 'pakistan', 'sri lanka'
    }

    population_by_year = {}

    for row in data:
        country = row['Region'].strip().lower()
        if country in saarc_countries:
            year = int(row['Year'])
            pop_value = row['Population'].strip()

            # Skip rows with missing or invalid population values
            if not pop_value or pop_value.lower() == 'none':
                continue

            try:
                population = float(pop_value)
            except ValueError:
                continue

            population_by_year[year] = population_by_year.get(year, 0) + population

    # Convert to millions for plotting
    years = sorted(population_by_year.keys())
    populations = [population_by_year[year] / 1_000_000 for year in years]

    return years, populations


def plot(years, populations):
    """Plot bar chart of Total SAARC Population vs. Year"""
    plt.figure(figsize=(10, 6))
    plt.bar(years, populations, color='orange', edgecolor='black')

    plt.title("Total SAARC Population Over the Years", fontsize=14)
    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Total Population (in millions)", fontsize=12)
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save figure
    plt.savefig("plots/saarc_total_population_over_years.png", dpi=300)

    plt.show()


def execute():
    file_path = "data/Population_estimate_data.csv"
    data = read(file_path)
    years, populations = calculate(data)
    plot(years, populations)


# Run
if __name__ == "__main__":
    execute()
