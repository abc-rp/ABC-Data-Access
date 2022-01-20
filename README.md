# ABC-RP Data Access
This page will explain how to access the building data stored in the ABC-RP data lake. Before you can access the data you will need to acquire a Google Service account key file. Please submit a data access request via the [ABC-RP Data Application Form](https://www.github.com "ABC-RP").
## Data structure

The raw building data is held in a Google BigQuery table. The supporting metadata is held in a Google Sheet. API access to both Sheets and BigQuery is required to make use of the data. Please see Python examples of this in the PythonExample folder.

Data stored in the Big Query data lake is very lightweight. The data stored is anonymized. Only those with access to the relevant Google Sheet will be able to associate data within the data lake to a particular property. 

**The metadata for each data point is stored once and associated with many entries in the BigQuery data lake:**

<img width="500" alt="One to many" src="https://abc-rp.com/wp-content/uploads/2022/01/onetomany.png">

**Here is an example of the supporting metadata in Sheets:**

| Field name    |  Example |
| :------------ |:-----|
| pointuid         | 164a9a94460a4f06aaea555f08fb6455|
| Device      | 1/1/BTH/W |
| Building   | Plot 1 |
| Sensor      | MTS-01 |
| Point Name  | air_temperature_sensor|
| Serves  | Kitchen|
| Section   |GF_KITCHEN|

**Here is an example of an entry from the BigQuery data lake:**


| Field name    | Type            | Example |
| :------------ |:---------------| :-----|
| pointuid          | STRING| 164a9a94460a4f06aaea555f08fb6455|
| instance      | STRING        |   csv |
| application   | STRING        |    developer-test|
| timestamp     | TIMESTAMP       |    2021-12-18 09:55:00 UTC |
| presentvalue  | NUMERIC       |    22.5|



Additional data may be added to the Sheets metadata as it becomes available.


The BigQuery table has millions of entries, each with a pointuid that corresponds to an entry in a Sheet.

**Note: The pointuid of the example BigQuery entry above is the same as the example Sheets entry. Using the combination of the above data we can access the kitchen temperature readings of the building on Plot 1. To do so we would query BigQuery for all pointuid's of 164a9a94460a4f06aaea555f08fb6469.**

Shown here is a simple SQL example query, requesting a single temperature reading from the kitchen.

```
SELECT * FROM `udmi.telemetry_main` WHERE pointuid = "164a9a94460a4f06aaea555f08fb6469" LIMIT 1
```

By combing the pointuid's found in the Sheets, we can build complex SQL statements to access building data. The following example retrieves the lowest temperature recorded in the kitchen of the building in plot 1 between the 15th and 22nd of January 2022.

```
SELECT * FROM `udmi.telemetry_main` 
WHERE pointuid = "164a9a94460a4f06aaea555f08fb6469" AND timestamp BETWEEN "2022-01-15" AND "2022-01-22"  
ORDER BY timestamp ASC 
LIMIT 1
```

When a Service Account key has been provided, you can access the [BigQuery API](https://cloud.google.com/bigquery/docs/quickstarts/quickstart-client-libraries#client-libraries-install-python "BigQuery API") via C#, Go, Java, Node.js, PHP, Python, or Ruby. 

We have provided Python examples in the PythonExample folder. 

We have not provided a Service Account key in the PythonExample folder. A Service Account key and list of final instructions will be provided once you have been approved for data access. 

**Note: The Service Accounts have data access frequency caps in place. The data should be accessed and stored on your platform if you are intending to access the same data frequently, such as in a web app.**