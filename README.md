# Parking-Monitor-Firebase

This is an extension of the project completed by Ryan Charnoky, Anton Franzluebbers, and Nithin Jino during Project 2 for CSEE 2210. The repository for the project can be found at https://github.com/AntonFranzluebbers/Parking-Monitor. The website is hosted on Firebase, which allows the database to be displayed and updated in realtime.

## Data Generation

Random data for the spots are created when the Python script sendRandomData.py is run. This allows for testing of the site without using many sensors.

## Working Components

### Fill Percent

The percentage displayed when hovering over the Drift link on the map page is correct according to the randomly generated data and updates in realtime.

### Individual Spot Status

The red and green colors on the individual spots on the diagram of the parking lot reflect the last reported value by the random generator.

### Day of Week graph

The bars on the day of week graph at the bottom of the drift page represent the relative fill level on different days of the week. Currently, the system tallies the total updates (full or empty) recorded in the database for each day of the week. This is not correct behaviour.

### Hourly graph

The bars on the hourly graph at the bottom of the drift page should represent the relative fill level during different hours of the day. Currently, the system tallies the total updates (full or empty) recorded in the database for each hour. This is not correct behaviour.
