# Data Dictionary 

This section defines all the data records used within our COVID-19 Hub for Zimbabwe for all publicly available and accessible data. 

__Which Data has been made public?__

- Infections Time Series
- Vaccination Progress Time Series
- Provincial Tracker Time Series
- Vaccination Centers 
- Testing Centers 

## Infections Time Series

| Data Variable | Description (Human Readable Format)|
| --------------| -----------------------------------|
| `FID`         |    Unique indentifier for the data records                                  |
| `Date`        |   corresponding date to the data records                                  |
| `Total_Cumu`  |   The total number of cumulative cases recorded on the `Date` stated.                                 |
| `New_Cases`     |   New coronavirus confirmed and recorded infections on the date                                 |
| `PCR`           |   Number of PCR tests conducted on the date                                 |
| `Recovered`     |   Number of people who recovered on that particular date                                 |
| `Deaths`      |     Number of people who have succumbed to the virus on that date                               |
| `Daily_Posi`    |   Daily Positivity Rate. `Daily_Posi = ( New_Cases / PCR) * 100`                                 |
| `Country`    |      Country                              |
| `RDT`      |       Rapid Diagnostic Tests conducted on the day (__Deprecated__)                             |
| `Local_Tran`    |   Local transmissions recorded on the date                                 |
| `Imported_C`    |   Imported/Foreign Transmissions recorded on the day                                 |
| `Cum_Deaths`   |   Total number of Cumulative COVID-19 related deaths                                 |
| `Cum_Recove`   |   Total cumulative number of people who have recovered from the coronavirus infection                               |
| `CFR_`       |     Case fatality ration within the country (__Deprecated__)                               |
| `ObjectId`    |    Unique indentifier for the data records                                |
| `CreationDa`   |   Date on which the data record was created (__Note__: This is not the date of the records. Data can be recorded the following day but records corresponding to the previous day )                                |
| `Creator`       |   the creator                                 |
| `EditDate`      |  Date and time on which the data was edited                                  |
| `Editor`      |     The data editor                               |
| `active_ca`     |  The current number of active cases in the country                                  |
| `hospitaliz`  |    The total number of COVID-19 patients who are currently hospitalized                                |
| `condition_`   |   COVID-19 patients who have Mild to Moderate symptomatic conditions                                 |
| `conditio_1`    |   COVID-19 patients who are in a severe state                                 |
| `conditio_2`     |    COVID-19 patients who are in the Intensive Care unit (ICU)                                |
| `asymptomat`     |  Number of COVID-19 patients who are Asymptomatic                                  |
| `total_vacc`      | Number of people who have received the first dose of the COVID-19 vaccine            |
| `total_vacc_2`        |    Number of people who have received the second dose of the COVID-19 vaccine                                |
| `hotspot_cities`       |  Names of cities within the country that have been declared as hotspot areas/locations                                  |
| `lockdown_update`       |  Current lockdown status for the nation                                 |
| `keyNotes`              |  Any additional key points to note within the recorded data for the date                                  |
| `newHosp`              |   Number of patients admitted into Hospitals due to COVID-19 infection on the date                                 |
|               |                                    |

## Vaccination Progress Time Series

| Data Variable | Description (Human Readable Format) |
| --------------| ------------------------------------|
| `OBJECTID` |   A unique identifier of the records          |
| `date_reported` |  the date corresponding to the data records           |
|  `*vac_name` |    the name of the vaccine that has been donated         |
| `*new_doses_received` |   number of vaccine doses that have been received          |
| `doses_administered` |  total number of vaccine doses that have been administered `doses_administered = first_doses + second_doses`           |
| `first_doses` |  First (Partial) series vaccinations that have been conducted on the day           |
| `second_doses` |  Second (Full) series vaccinations that have been conducted on the day           |
| `*conType` |   The type of consignment of the vaccine received.           |
| `*donor` |   vaccine donor name if the consignment was a donation          |
| `*Story` |  official story published in the media           |
| `source` |  the source of the story           |

__Note__: the fields marked with an asterik (`*`) only apply when there has been a new batch of coronavirus vaccine doses that have been received within the country. Ignore the `vac_name` field if there was no new consignment received on the date. 

## Provincial Tracker Time Series

This was recently introduced after noticing the need to track Provincial progression and development. The data does not start from the beginning of the pandemic. 

The columns have been categorized and named with the same convention in the format `<data_category><province_name>` for example `active_totalManicaland` describes the total number of __Active__ cases in __Manicaland__ province. 

The Data table below describes the `<data_category>` only 

| Data Variable  | Description | 
| ---------------------| ------------|
| `reportDate`      |  Date corresponding to the records          |
| `pcr_new`   |   latest record of PCR tests conducted         |
| `case_new`   |  latest record of confirmed and recorded cases        |
| `recov_new`     | latest record of new recoveries           |
| `death_new` | latest number of recorded deaths due to COVID-19    |
| `case_total`   | current total of confirmed COVID-19 cases            |
| `recov_total`    |  current total of all recovered patients          |
| `active_total`   | current total of active cases           |
| `death_total`    |  current total of all recorded COVID-19 related deaths          |
| `reportStatus`    |  Wether all provincial records are accounted for on the date of the report either `yes` or `no`          |
| `didNotReport`    | If `reportStatus` = `no` then which Provinces did not report           |
| `Photos and Files`   | link to the official COVID-19 daily report by MoHCC           |


## Vaccination Centers


| Data Variable | Description (Human Readable Format) |
| --------------| ------------------------------------|
| `FID`        |   A unique idenitifer for each facility                |
| `ID`        |     A unique idenitifer for each facility               |
| `DISTRICT`        |   the district name in which the facility is in                |
| `LONGITUDE`        | Longitudinal value for the coordinates                  |
| `LATITUDE`        |  Latitude value for the coordinate                 |
| `NAMEOFFACI`        |   Name of the facility                |
| `OWNERSHIP`        |   Ownership status of the facility                |
| `TYPEOFFACI`        |  The type of the facility                 |
| `COMMENTS` |   Any comments about the center                   |

## Testing Centers

