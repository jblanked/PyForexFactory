import asyncio
from pyppeteer import launch


async def main():
    # Launch a headless browser
    browser = await launch({"headless": False, "args": ["--start-minimized"]})

    # Create a new page and navigate to the economic calendar
    page = await browser.newPage()
    await page.goto('https://www.forexfactory.com')

    # create a screenshot of the page and save it
    await page.screenshot({"path": "python.png"})

    await page.waitForSelector('#flexBox_flex_calendar_mainCalCopy1 > table > tbody > tr:nth-child(5)', {'timeout': 0})

    # Find all rows in the table and extract the data
    rows = await page.querySelectorAll('tr.calendar__row')

    for row in rows:
        event_time = await row.querySelector('td.calendar__cell.calendar__time.time')
        event_name = await row.querySelector("td.calendar__cell.calendar__event.event > div > span.calendar__event-title")
        currency = await row.querySelector('td.calendar__cell.calendar__currency.currency')
        date = await row.querySelector("td.calendar__cell.calendar__date.date")
        actual_data = await row.querySelector("td.calendar__cell.calendar__actual.actual")
        forecast_data = await row.querySelector("td.calendar__cell.calendar__forecast.forecast")
        previous_data = await row.querySelector("td.calendar__cell.calendar__previous.previous")

        if event_time and currency:
            event_time_prop = await event_time.getProperty('textContent')
            event_time_txt = await event_time_prop.jsonValue()

            currency_prop = await currency.getProperty('textContent')
            currency_txt = await currency_prop.jsonValue()

            event_name_prop = await event_name.getProperty('textContent')
            event_name_txt = await event_name_prop.jsonValue()

            date_prop = await date.getProperty('textContent')
            date_txt = await date_prop.jsonValue()

            actual_data_prop = await actual_data.getProperty('textContent')
            actual_data_txt = await actual_data_prop.jsonValue()

            forecast_data_prop = await forecast_data.getProperty('textContent')
            forecast_data_txt = await forecast_data_prop.jsonValue()

            previous_data_prop = await previous_data.getProperty('textContent')
            previous_data_txt = await previous_data_prop.jsonValue()

            full = f'{date_txt}\n\n{currency_txt}{event_name_txt} {event_time_txt}\nActual: {actual_data_txt} Forecast: {forecast_data_txt} Previous: {previous_data_txt}'

            print(full)

    # Close the browser
    await browser.close()

# Run the main function asynchronously
asyncio.get_event_loop().run_until_complete(main())
