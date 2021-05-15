# superstore-api
Time series predictions for the Superstore dataset.

## Usage

The API is available at [superstore-api.azurewebsites.net](https://superstore-api.azurewebsites.net/)

### Endpoints

#### Sales

[superstore-api.azurewebsites.net/v1/sales](https://superstore-api.azurewebsites.net/v1/sales/?weeks=1)

Args:

* weeks (int) - Number of weeks ahead to predict.

Return:

Total sales for each week.
