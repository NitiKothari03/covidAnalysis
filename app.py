import matplotlib.pyplot as plt
import pandas as pd


def deaths_cases(country_name):
    covid_data = pd.read_csv('WHO-COVID-19-global-data.csv')

    if country_name in covid_data["Country"].unique():

        country_data = covid_data[covid_data["Country"] == country_name]

        cases_data = country_data.groupby("Date_reported", as_index=False).agg(
            {"Cumulative_cases": "sum"})

        death_data = country_data.groupby("Date_reported", as_index=False).agg(
            {"Cumulative_deaths": "sum"})

        cases_data.plot(kind="line", x="Date_reported", color="orange",
                        figsize=(12, 8))
        plt.xlabel("Date")
        plt.ylabel("Total Number of Cases")
        plt.title("COVID-19 Cases in " + country_name)

        death_data.plot(kind="line", x="Date_reported", color="red",
                        figsize=(12, 8))
        plt.xlabel("Date")
        plt.ylabel("Total Number of Cases")
        plt.title("COVID-19 Deaths in " + country_name)
        plt.show()

    else:
        print("Please Try Entering Country Name Again!")


def oneplusDose_vaccines(country1, country2):
    covid_data = pd.read_csv('vaccination-data.csv')

    countries = [country1, country2]

    if all(elem in covid_data["COUNTRY"].tolist() for elem in countries):

        country_data = covid_data[covid_data["COUNTRY"].isin(countries)]

        # Data Collection For Country1
        oneplusDose_country1 = country_data[
            country_data["COUNTRY"] == country1].groupby("COUNTRY",
                                                         as_index=False).agg(
            {"PERSONS_VACCINATED_1PLUS_DOSE": "sum"})

        # Data Collection For Country2
        oneplusDose_country2 = country_data[
            country_data["COUNTRY"] == country2].groupby("COUNTRY",
                                                         as_index=False).agg(
            {"PERSONS_VACCINATED_1PLUS_DOSE": "sum"})

        oneplusDose = pd.concat([oneplusDose_country1, oneplusDose_country2])

        oneplusDose.plot(kind="bar", x="COUNTRY",
                         y='PERSONS_VACCINATED_1PLUS_DOSE', figsize=(10, 8),
                         color='red')
        plt.xlabel("Country")
        plt.ylabel("Number Of People Vaccinated")
        plt.title("Vaccination in " + country1 + " & " + country2)
        plt.show()

    else:
        print("Please Try Entering Country Name Again!")


def fullyVaccinated_vaccines(country1, country2):
    covid_data = pd.read_csv('vaccination-data.csv')

    countries = [country1, country2]

    if all(elem in covid_data["COUNTRY"].tolist() for elem in countries):

        country_data = covid_data[covid_data["COUNTRY"].isin(countries)]

        # Data Collection For Country1
        fullyVaccinated_country1 = country_data[
            country_data["COUNTRY"] == country1].groupby("COUNTRY",
                                                         as_index=False).agg(
            {"PERSONS_FULLY_VACCINATED": "sum"})

        # Data Collection For Country2
        fullyVaccinated_country2 = country_data[
            country_data["COUNTRY"] == country2].groupby("COUNTRY",
                                                         as_index=False).agg(
            {"PERSONS_FULLY_VACCINATED": "sum"})

        fullyVaccinated = pd.concat(
            [fullyVaccinated_country1, fullyVaccinated_country2])

        fullyVaccinated.plot(kind="bar", x="COUNTRY",
                             y='PERSONS_FULLY_VACCINATED', figsize=(10, 8),
                             color='orange')
        plt.xlabel("Country")
        plt.ylabel("Number Of People Vaccinated")
        plt.title("Vaccination in " + country1 + " & " + country2)
        plt.show()

    else:
        print("Please Try Entering Country Name Again!")


def BoosterDose_vaccines(country1, country2):
    covid_data = pd.read_csv('vaccination-data.csv')

    countries = [country1, country2]

    if all(elem in covid_data["COUNTRY"].tolist() for elem in countries):

        country_data = covid_data[covid_data["COUNTRY"].isin(countries)]

        # Data Collection For Country1
        BoosterDose_country1 = country_data[
            country_data["COUNTRY"] == country1].groupby("COUNTRY",
                                                         as_index=False).agg(
            {"PERSONS_BOOSTER_ADD_DOSE": "sum"})

        # Data Collection For Country2
        BoosterDose_country2 = country_data[
            country_data["COUNTRY"] == country2].groupby("COUNTRY",
                                                         as_index=False).agg(
            {"PERSONS_BOOSTER_ADD_DOSE": "sum"})

        BoosterDose = pd.concat([BoosterDose_country1, BoosterDose_country2])

        BoosterDose.plot(kind="bar", x="COUNTRY", y='PERSONS_BOOSTER_ADD_DOSE',
                         figsize=(10, 8), color='magenta')
        plt.xlabel("Country")
        plt.ylabel("Number Of People Vaccinated")
        plt.title("Vaccination in " + country1 + " & " + country2)
        plt.show()

    else:
        print("Please Try Entering Country Name Again!")


print('''         Welcome To COVID-19 Analysis !!
         Press 1 to Know deaths and cases of a country
         Press 2 to Compare data of two countries for People vaccinated with One-Plus Dose
         Press 3 to Compare data of two countries for People Fully Vaccinated
         Press 4 to Compare data of two countries for People vaccinated with Booster Dose
         Any Other Number to quit.\n''')

choice = int(input("Enter Your Choice : "))

if choice == 1:
    deaths_cases(input("Enter Country Name : "))
elif choice == 2:
    oneplusDose_vaccines(input("Enter Country1 Name : "),
                         input("Enter Country2 Name : "))
elif choice == 3:
    fullyVaccinated_vaccines(input("Enter Country1 Name : "),
                             input("Enter Country2 Name : "))
elif choice == 4:
    BoosterDose_vaccines(input("Enter Country1 Name : "),
                         input("Enter Country2 Name : "))
else:
    print('Thank You For Visiting!')
