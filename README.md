# sqlalchemy-challenge
mod 10 challenge
### Part 1: Climate Analysis and Exploration
#### Precipitation Analysis
* Found the most recent date in the dataset.
* Retrieved the previous 12 months of precipitation data by querying the 12 previous months of data. 
* Selected only the `date` and `prcp` values.
* Loaded the query results into a Pandas DataFrame, and set the index to the date column.
* Sorted the DataFrame values by `date`.
* Plotted the results by using the DataFrame `plot` method, as shown in the following image:
* UsedPandas to print the summary statistics for the precipitation data.

#### Station Analysis
* Designed a query to calculate the total number of stations in the dataset.
* Designed a query to find the most active stations (the stations with the most rows).
    * Listed the stations and observation counts in descending order.
    * Using the most active station id, calculated the lowest, highest, and average temperatures.
* Designed a query to retrieve the previous 12 months of temperature observation data (TOBS).
    * Filtered by the station with the highest number of observations.
    * Queried the previous 12 months of temperature observation data for this station.
    * Plotted the results as a histogram with `bins=12`, as shown in the following image:

### Part 2: Design Your Climate App
Created flask routes:
* `/`
    * Homepage.
    * List all available routes.
* `/api/v1.0/precipitation`
    * Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    * Return the JSON representation of your dictionary.
* `/api/v1.0/stations`
    * Return a JSON list of stations from the dataset.
* `/api/v1.0/tobs`
    * Query the dates and temperature observations of the most active station for the previous year of data.
    * Return a JSON list of temperature observations (TOBS) for the previous year.
* `/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`
    * Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.
    * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than or equal to the start date.
    * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates from the start date through the end date (inclusive).
