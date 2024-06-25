from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    RunReportRequest,
)
import csv

#-------------加上try-except---------------------#
def sample_run_report(property_id="property_id"):
    """Runs a simple report on a Google Analytics 4 property."""
    try:
        # Using a default constructor instructs the client to use the credentials
        # specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
        client = BetaAnalyticsDataClient()

        # request = RunReportRequest(
        #     property=f"properties/{property_id}",
        #     dimensions=[Dimension(name="city")],
        #     metrics=[Metric(name="activeUsers")],
        #     date_ranges=[DateRange(start_date="2020-03-31", end_date="today")],
        # )

        request = RunReportRequest(
            property=f"properties/{property_id}",
            dimensions=[
                # Dimension(name="userAgeBracket"),
                # Dimension(name="userGender")
                Dimension(name="dateHour"),
                Dimension(name="dayOfWeekName"),
                # Dimension(name="hour"),
                Dimension(name="itemBrand"),
                Dimension(name="itemId"),
                Dimension(name="itemName"),
                Dimension(name="itemVariant"),
                Dimension(name="country"),
                Dimension(name="transactionId"),
                Dimension(name="pagePath")
            ],
            metrics=[
                Metric(name="itemsViewed"),
                Metric(name="itemsAddedToCart"),
                Metric(name="itemsPurchased")
            ],
            date_ranges=[
                DateRange(start_date="2018-01-01", end_date="2023-08-31")
            ],
        )
        
        response = client.run_report(request)

        print("Report result:")
        
        # 創CSV 寫入欄位名
        with open('report_start2018.csv', mode='w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            
            # 動態產生欄位名
            header = ['dateHour', 'itemId', 'itemBrand', 'itemName', 'country', 'itemPromotionId']
            header += [metric.name for metric in request.metrics]
            csv_writer.writerow(header)

            for row in response.rows:
                data = [dimension.value for dimension in row.dimension_values]
                data += [metric.value for metric in row.metric_values]
                csv_writer.writerow(data)
                print(*data)

    except Exception as e:
        print("An error occurred:", str(e))

# 呼叫函式
sample_run_report()




#-----------官方原始程式碼---------------#
# def sample_run_report(property_id="property_id"):
#     """Runs a simple report on a Google Analytics 4 property."""
#     # TODO(developer): Uncomment this variable and replace with your
#     #  Google Analytics 4 property ID before running the sample.
#     # property_id = "YOUR-GA4-PROPERTY-ID"

#     # Using a default constructor instructs the client to use the credentials
#     # specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
#     client = BetaAnalyticsDataClient()

#     request = RunReportRequest(
#         property=f"properties/{property_id}",
#         dimensions=[Dimension(name="city")],
#         metrics=[Metric(name="activeUsers")],
#         date_ranges=[DateRange(start_date="2020-03-31", end_date="today")],
#     )
#     response = client.run_report(request)

#     print("Report result:")
#     for row in response.rows:
#         print(row.dimension_values[0].value, row.metric_values[0].value)

