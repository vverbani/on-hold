# Transform Spread Sheets

Map out only useful information for On-Hold Support Clients to a new spreadsheet. Ues the new spreadsheet to manage on-hold Zendesk/Jira tickets to minimize Americas client churn risk - from a Support/Consulting perspective.

### Before

| Ticket ID | Requester	| Request Email	| Requester Domain | Requester Name | Assignee | Group | Subject | Tags | Ticket Status | .... |
| --------- | --------- | ------------- | ---------------- | -------------- | -------- | ----- | ------- | ---- | ------------- | ---- |

### After

| Ticket ID | Requester	| Requester Email | Requester Domain | Subject | Priority | Created At | Updated At | Jira Issue | Jira Status |
| --------- | --------- | --------------- | ---------------- | ------- | -------- | ---------- | ---------- | ---------- | ----------- |

Jira status is updated by spreadsheet owner. This columns outlines what the status of the Jira ticket is. Possible Jira Status values:

1. Client

We are waiting on the clent.

2. Support/ Consulting

Internal is waiting for a Support or Consulting Engineer feedback

3. Internal

We are waiting for an Internal Engineer to pick up/look at the Jira ticket. In times like this, make sure

## Prerequisites

Install [Docker](www.docker.com) on your machine

## Steps

1. Export `On Hold, By Org` Spreadsheet as a `.csv` file from the org Google Drive. This script is designed to only work with `.csv` files because of faster processing times and will not work with any other format.

2. Save as `on-hold`

3. Place sheet under `/src` folder

4. Run command:

```bash

docker-compose up

```

*** Re-running this will overwrite both csv and excel output files, re-run at own risk ***