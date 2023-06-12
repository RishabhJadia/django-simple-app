import pandas as pd
import io

from datetime import timedelta, date
from deni_apps.models import CandidateDetails



def scheduler_candidate_joining_in_next_90days():
    today = date.today()
    next_90_day = today + timedelta(days=90)

    rec = CandidateDetails.objects.all()
    candidate_joining_in_next_90days = [{'Name': candidate.name, "candiate_doj": candidate.candiate_doj, "candiate_email_id": candidate.candiate_email_id, "hiring_manager": candidate.hiring_manager, "hiring_manager_email_id": candidate.hiring_manager_email_id} for candidate in rec if candidate.candiate_doj <= next_90_day]
    df = pd.DataFrame(candidate_joining_in_next_90days)
    df.to_excel("candidate_joining_in_next_90days.xlsx", sheet_name='Sheet1', index=False)
    print(candidate_joining_in_next_90days)
    print('Hello from APScheduler!')
