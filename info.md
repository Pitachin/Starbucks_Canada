+ An example of JSON result from a store.

{
  "distance": 0.3089,
  "isFavorite": false,
  "isNearby": true,
  "isPrevious": false,
  "recommendationReason": "NEARBY",
  "store": {
    "id": "1054604",
    "closingSoon": false,
    "storeNumber": "83343-312956",
    "name": "Shenzhen Nanshan Ruiyinli Stor",
    "ownershipTypeCode": "CO",
    "phoneNumber": null,
    "open": false,
    "isOpen24Hours": false,
    "openStatusFormatted": "",
    "hoursStatusFormatted": "Store hours aren't available",
    "address": {
      "lines": [
        "The second floor above ground of the com",
        "Shenzhen, 44 518000"
      ],
      "singleLine": "The second floor above ground of the com, Shenzhen",
      "streetAddressLine1": "The second floor above ground of the com",
      "streetAddressLine2": null,
      "streetAddressLine3": "mercial po",
      "city": "Shenzhen",
      "countrySubdivisionCode": "44",
      "countryCode": "CN",
      "postalCode": "518000"
    },
    "schedule": null,
    "amenities": [],
    "pickUpOptions": [],
    "coordinates": {
      "latitude": 22.55237,
      "longitude": 113.99016
    },
    "mobileOrdering": {
      "availability": "NOT_ELIGIBLE",
      "guestOrdering": false,
      "stallQuantity": null
    },
    "regulations": [],
    "acceptsNonSvcMop": false,
    "acceptedCampusCardIssuers": null,
    "warningLabels": [
      {
        "code": "CL",
        "label": "Closed"
      }
    ],
    "slug": "shenzhen-nanshan-ruiyinli-stor-the-second-floor-above-ground-of-the-com-mercial-p",
    "timeZone": {
      "timeZoneId": "GMT+08:00 Asia/Shanghai"
    },
    "internalFeatures": [],
    "marketBusinessUnitCode": null
  }
}

+ Case 2: Downtown Toronto

{
  "distance": 0.3244,
  "isFavorite": false,
  "isNearby": true,
  "isPrevious": false,
  "recommendationReason": "NEARBY",
  "store": {
    "id": "1034072",
    "closingSoon": false,
    "storeNumber": "53764-276491",
    "name": "203 College Street",
    "ownershipTypeCode": "CO",
    "phoneNumber": "+1 437-690-0990",
    "open": false,
    "isOpen24Hours": false,
    "openStatusFormatted": "Opens Monday at 5:30 AM",
    "hoursStatusFormatted": "Open 5:30 AM-10:00 PM",
    "address": {
      "lines": [
        "203 College Street",
        "Toronto, ON M5T 1P9"
      ],
      "singleLine": "203 College Street, Toronto",
      "streetAddressLine1": "203 College Street",
      "streetAddressLine2": null,
      "streetAddressLine3": null,
      "city": "Toronto",
      "countrySubdivisionCode": "ON",
      "countryCode": "CA",
      "postalCode": "M5T 1P9"
    },
    "schedule": [
      {
        "dayFormatted": "Monday",
        "dayOfWeek": "MONDAY",
        "hoursFormatted": "5:30 AM to 10:00 PM",
        "holidayFormatted": "",
        "open": true
      },
      {
        "dayFormatted": "Tuesday",
        "dayOfWeek": "TUESDAY",
        "hoursFormatted": "5:30 AM to 10:00 PM",
        "holidayFormatted": "",
        "open": true
      },
      {
        "dayFormatted": "Wednesday",
        "dayOfWeek": "WEDNESDAY",
        "hoursFormatted": "5:30 AM to 10:00 PM",
        "holidayFormatted": "",
        "open": true
      },
      {
        "dayFormatted": "Thursday",
        "dayOfWeek": "THURSDAY",
        "hoursFormatted": "5:30 AM to 10:00 PM",
        "holidayFormatted": "",
        "open": true
      },
      {
        "dayFormatted": "Friday",
        "dayOfWeek": "FRIDAY",
        "hoursFormatted": "5:30 AM to 10:00 PM",
        "holidayFormatted": "",
        "open": true
      },
      {
        "dayFormatted": "Saturday",
        "dayOfWeek": "SATURDAY",
        "hoursFormatted": "7:00 AM to 9:00 PM",
        "holidayFormatted": "",
        "open": true
      },
      {
        "dayFormatted": "Sunday",
        "dayOfWeek": "SUNDAY",
        "hoursFormatted": "7:00 AM to 8:00 PM",
        "holidayFormatted": "",
        "open": true
      }
    ],
    "amenities": [
      {
        "code": "CS",
        "name": "Café Seating"
      },
      {
        "code": "16",
        "name": "In Store"
      },
      {
        "code": "XO",
        "name": "Mobile Order and Pay"
      },
      {
        "code": "AS",
        "name": "MOP ASAP + Scheduled Ordering"
      },
      {
        "code": "NB",
        "name": "Nitro Cold Brew"
      },
      {
        "code": "WA",
        "name": "Oven-warmed Food"
      },
      {
        "code": "DR",
        "name": "Redeem Rewards"
      },
      {
        "code": "GO",
        "name": "Starbucks Wi-Fi"
      }
    ],
    "pickUpOptions": [
      {
        "code": "16",
        "name": "In store",
        "available": false
      }
    ],
    "coordinates": {
      "latitude": 43.65859,
      "longitude": -79.39557
    },
    "mobileOrdering": {
      "availability": "NOT_ELIGIBLE",
      "guestOrdering": true,
      "stallQuantity": null
    },
    "regulations": [],
    "acceptsNonSvcMop": true,
    "acceptedCampusCardIssuers": null,
    "warningLabels": [
      {
        "code": "CL",
        "label": "Closed"
      }
    ],
    "slug": "203-college-street-203-college-street-toronto-on-m-5-t-1-p-9-ca",
    "timeZone": {
      "timeZoneId": "GMT-04:00 America/Toronto"
    },
    "internalFeatures": [
      {
        "code": "SE",
        "name": "Mobile Multi Tender"
      },
      {
        "code": "GC",
        "name": "Guest Checkout"
      },
      {
        "code": "AS",
        "name": "MOP ASAP + Scheduled Ordering"
      }
    ],
    "marketBusinessUnitCode": null
  }
}

# June 16 Experiment 1

radius=0.4, step=0.03

```
toronto_finer = make_grid(43.6532, -79.3832, radius=0.4, step=0.03)
print(f"Points: {len(toronto_finer)}")
stores = scrape_all(toronto_finer)
df = pd.DataFrame(stores).drop_duplicates(subset="store_id")
print(f"Toronto (finer): {len(df)}")
```
930

Request Failed (43.4732, -79.6432): HTTPSConnectionPool(host='www.starbucks.com', port=443): Read timed out. (read timeout=15)

status code: 500

Request Failed (43.8532, -79.5832): HTTPSConnectionPool(host='www.starbucks.com', port=443): Read timed out. (read timeout=15)

Request Failed (43.8732, -79.6232): HTTPSConnectionPool(host='www.starbucks.com', port=443): Read timed out. (read timeout=15)

Request Failed (43.8732, -79.5232): HTTPSConnectionPool(host='www.starbucks.com', port=443): Read timed out. (read timeout=15)

>>> df = pd.DataFrame(stores).drop_duplicates(subset="store_id")
>>> print(f"Toronto stores: {len(df)}")
Toronto stores: 356

# June 16 Experiment 2
radius=0.4, step=0.02
1640 / 1640
Toronto (finer): 392

# 1393

8188 / 8188
province_code
ON    596
BC    318
AB    215
QC    116
SK     43
MB     39
NS     29
NB     21
NL     10
PE      4
YT      1
NT      1
Name: count, dtype: int64
Total stores: 1393 stores
====== 🎉 Total Workflow Time: 3377.7694sec ======
--- Finished: scraper.py successfully ---

--- Starting: visualize.py ---
/Users/qiuzhulin/Desktop/Starbucks in Canada/.venv/lib/python3.9/site-packages/urllib3/__init__.py:35: NotOpenSSLWarning: urllib3 v2 only supports OpenSSL 1.1.1+, currently the 'ssl' module is compiled with 'LibreSSL 2.8.3'. See: https://github.com/urllib3/urllib3/issues/3020
  warnings.warn(
⏱️ compute_distances took 0.0092sec
Map saved: output/Canada_map.html
⏱️ make_map took 1.2153sec