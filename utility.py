from datetime import date
import yfinance as yf
import datetime


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
    settings_file[-1] = settings_file[-1].split(',')

    return settings_file


def get_keywords(ticker: str) -> list:
    company = yf.Ticker(ticker).info
    names = [ticker, company['shortName']]
    first_word = company['longName'].split()[0]
    # get rid of , at the end of name's first word (like "tesla, inc." => "tesla")
    if first_word[-1] == ',':
        first_word = first_word[:-1]
    names.append(first_word)
    if first_word[-4:] == ".com":
        names.append(first_word[:-4])
    names = [name.lower() for name in names]
    return list(set(names))


def daterange(start_date, end_date):
    return [start_date + datetime.timedelta(n) for n in range(int((end_date - start_date).days))]
