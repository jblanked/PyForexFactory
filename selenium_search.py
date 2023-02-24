from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# use choose by selector :)
# just right click on whichever you want when inspecting
# then click "copy selector"
# usually looks like the line below:
# flexBox_flex_calendar_mainCalCopy1 > table > tbody > tr.calendar__row.calendar_row.calendar__row--grey.calendar__row--new-day.newday

# the path we want starts after tbody
# its a string
first_event = "tr.calendar__row.calendar_row.calendar__row--grey.calendar__row--new-day.newday"

# couldnt extract second event, seems like every event except first isnt individually named
second_event = "tr.calendar__row.calendar_row.calendar__row--grey"


# flexBox_flex_calendar_mainCalCopy1 > table > tbody > tr.calendar__row.calendar_row.calendar__row--grey.calendar__row--new-day.newday


# flexBox_flex_calendar_mainCalCopy1 > table > tbody > tr:nth-child(6) > td.calendar__cell.calendar__time.time

# flexBox_flex_calendar_mainCalCopy1 > table > tbody > tr:nth-child(12) > td.calendar__cell.calendar__time.time

# since theyre practically identical, we can use the nth-child to separate everything

# like this:
# time = table_row.find_element(By.CSS_SELECTOR, "td.calendar__cell.calendar__time.time:nth-child(1)").text
# instead of :
# time = table_row.find_element(By.CSS_SELECTOR, "td.calendar__cell.calendar__time.time").text

# flexBox_flex_calendar_mainCalCopy1 > table > tbody > tr:nth-child(12) > td.calendar__cell.calendar__time.time

# so instead used the selector to get the ID of the calender
calender = "flexBox_flex_calendar_mainCalCopy1"


def get_forex_factory_results():
    browser = webdriver.Chrome()
    browser.get("https://www.forexfactory.com")

    # used find elements (instead of find element)
    # since multiple css classes with same name
    table_rows = browser.find_elements(
        By.CSS_SELECTOR, second_event)

    currency_list = []
    time_list = []
    event_list = []
    actual_data_list = []
    forecast_list = []
    previous_data_list = []

    # now its a list, so we iterate through each
    # to find the requested values :)
    for item in table_rows:
        date = item.find_element(
            By.CSS_SELECTOR, "td.calendar__cell.calendar__date.date").text

        currency = item.find_element(
            By.CSS_SELECTOR, "td.calendar__cell.calendar__currency.currency").text

        time = item.find_element(
            By.CSS_SELECTOR, "td.calendar__cell.calendar__time.time").text

        if time != "":
            time_text = f"{time} EST -"
        if time == "":
            time_text = time

        event = item.find_element(
            By.CSS_SELECTOR, "td.calendar__cell.calendar__event.event > div > span.calendar__event-title").text

        actual_data = item.find_element(
            By.CSS_SELECTOR, "td.calendar__cell.calendar__actual.actual").text

        forecast = item.find_element(
            By.CSS_SELECTOR, "td.calendar__cell.calendar__forecast.forecast").text

        previous = item.find_element(
            By.CSS_SELECTOR, "td.calendar__cell.calendar__previous.previous").text

        currency_list.append(currency)
        time_list.append(time)
        event_list.append(event)
        actual_data_list.append(actual_data)
        forecast_list.append(forecast)
        previous_data_list.append(previous)

        full = f'{date}\n\n{currency} - {time_text} {event}\nActual: {actual_data} Forecast: {forecast} Previous: {previous}'

        print(full)

    df = pd.DataFrame({"Currency": currency_list,
                       "Time": time_list,
                       "Event": event_list,
                       "Actual": actual_data_list,
                       "Forecast": forecast_list,
                       "Previous": previous_data_list})

    # display all rows and columns
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    # print(df)


def forex_factory_event(name_of_event):

    event_name = name_of_event.lower()

    browser = webdriver.Chrome()
    browser.get("https://www.forexfactory.com")

    # used find elements (instead of find element)
    # since multiple css classes with same name
    table_rows = browser.find_elements(
        By.CSS_SELECTOR, second_event)

    currency_list = []
    time_list = []
    event_list = []
    actual_data_list = []
    forecast_list = []
    previous_data_list = []

    # now its a list, so we iterate through each
    # to find the requested values :)
    for item in table_rows:
        date = item.find_element(
            By.CSS_SELECTOR, "td.calendar__cell.calendar__date.date").text

        currency = item.find_element(
            By.CSS_SELECTOR, "td.calendar__cell.calendar__currency.currency").text

        time = item.find_element(
            By.CSS_SELECTOR, "td.calendar__cell.calendar__time.time").text

        if time != "":
            time_text = f"{time} EST -"
        if time == "":
            time_text = time

        event = item.find_element(
            By.CSS_SELECTOR, "td.calendar__cell.calendar__event.event > div > span.calendar__event-title").text

        actual_data = item.find_element(
            By.CSS_SELECTOR, "td.calendar__cell.calendar__actual.actual").text

        forecast = item.find_element(
            By.CSS_SELECTOR, "td.calendar__cell.calendar__forecast.forecast").text

        previous = item.find_element(
            By.CSS_SELECTOR, "td.calendar__cell.calendar__previous.previous").text

        currency_list.append(currency)
        time_list.append(time)
        event_lowered = event.lower()
        event_list.append(event_lowered)
        actual_data_list.append(actual_data)
        forecast_list.append(forecast)
        previous_data_list.append(previous)

        if event_name in event_lowered:
            full = f'{currency} - {time_text} {event}\nActual: {actual_data} Forecast: {forecast} Previous: {previous}'
            print(full)
        else:
            continue


forex_factory_event("NHPI")
