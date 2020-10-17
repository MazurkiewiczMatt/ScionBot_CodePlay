from datetime import date
import yfinance as yf


def read_settings(filename: str) -> list:
    try:
        f = open(filename)
        settings_file = f.readlines()
    finally:
        f.close()

    # check whether the file is valid
    if not len(settings_file) == 4:
        raise Exception("Invalid settings file: 4 lines expected, " + str(len(settings_file)) + " received.")

    # remove whitespace
    for i in range(len(settings_file)):
        settings_file[i] = settings_file[i].strip()

    # convert timeframe to dates
    try:
        settings_file[1] = date.fromisoformat(settings_file[1])
        settings_file[2] = date.fromisoformat(settings_file[2])
    except:
        raise Exception("Invalid data format: " + str(settings_file[1]) + ", " + str(settings_file[2]))

    # convert string containing subreddit names to a list
    settings_file[-1] = settings_file[-1].split(', ')

    return settings_file


def get_keywords(ticker: str) -> list:
    company = yf.Ticker(ticker)
    names = [ticker, company.info['longName'], company.info['shortName'], company.info['longName'].split()[0]]
    return list(set(names))
