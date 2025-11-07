import csv
import matplotlib.pyplot as plt

def read(file_path):
    """Read CSV and return a list of dictionaries"""
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        data = [row for row in reader]
    return data


def calculate(data):
    """Get population (in millions) of ASEAN countries from 2004–2014"""
    # ASEAN countries (standardized names)
    asean = [
        'brunei darussalam', 'cambodia', 'indonesia', 'lao pdr',
        'malaysia', 'myanmar', 'philippines', 'singapore',
        'thailand', 'vietnam'
    ]

    # Handle country name variations found in dataset
    country_aliases = {
        "brunei": "brunei darussalam",
        "lao people's democratic republic": "lao pdr",
        "viet nam": "vietnam",
        "myanmar (burma)": "myanmar",
        "the philippines": "philippines"
    }

    years = list(range(2004, 2015))
    result = {country: [] for country in asean}

    for country in asean:
        for year in years:
            pop = 0
            for row in data:
                region = row['Region'].strip().lower()
                region = country_aliases.get(region, region)  # normalize names

                if region == country and row['Year'] == str(year):
                    if row['Population'] not in ('', 'None'):
                        pop = float(row['Population']) / 1_000_000  # convert to millions
                    break
            result[country].append(pop)

    return years, result


def plot(years, population_data):
    """Plot grouped bar chart for ASEAN countries (2004–2014)"""
    countries = list(population_data.keys())
    num_countries = len(countries)
    bar_width = 0.8 / num_countries
    x_positions = list(range(len(years)))

    plt.figure(figsize=(15, 8))

    for i, country in enumerate(countries):
        x_shifted = [x + i * bar_width for x in x_positions]
        plt.bar(x_shifted, population_data[country], width=bar_width,label=country.title())

    plt.xlabel("Year", fontsize=12)
    plt.ylabel("Population (in millions)", fontsize=12)
    plt.title("ASEAN Countries Population (2004–2014)", fontsize=14)
    plt.xticks([x + 0.4 for x in x_positions], years, rotation=45)
    plt.legend(fontsize=8)
    plt.tight_layout()

    plt.savefig("plots/ASEAN_population_grouped_bar.png", dpi=300)
    plt.show()


def execute():
    file_path = "data/Population_estimate_data.csv"
    data = read(file_path)
    years, population_data = calculate(data)
    plot(years, population_data)


if __name__ == "__main__":
    execute()
