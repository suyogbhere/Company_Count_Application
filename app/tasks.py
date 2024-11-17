from celery import shared_task
import pandas as pd
from app.models import File, Company_data


@shared_task
def create_db(file_path):
    """
    Celery task to process the CSV file and populate the database.
    """
    df = pd.read_csv(file_path, delimiter=',')
    list_of_csv = [list(row)  for row in df.values]
    for l in list_of_csv:
        Company_data.objects.create(
            id = l[0],
            name = l[1],
            domain = l[2],
            year_founded = l[3],
            industry = l[4],
            size_range = l[5],
            locality = l[6],
            country = l[7],
            linkedin_url = l[8],
            current_employee_estimate = l[9],
            total_employee_estimate = l[10],
        )
    # return "Database creation completed."