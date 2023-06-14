import pandas as pd
import io

from datetime import timedelta, date
from deni_apps.models import CandidateDetails



def scheduler_candidate_joining_in_next_90days():
    today_date = date.today()


    # next_90_day = today + timedelta(days=90)
    rec = CandidateDetails.objects.all()
    rec1 = [candidate.candiate_email_id for candidate in rec]
    for cand in rec:
        print(type(cand), "------------")
        # print(cand.candiate_doj - today_date)
        # print((cand.candiate_doj - today_date).days)

        if (cand.candiate_doj - today_date).days >= 15 and (cand.candiate_doj - today_date).days <= 90:
            if cand.candiate_email_id not in rec1:  # not in
                CandidateDetails.objects.create(
                    name=cand.name,
                    offer_accepted_date=cand.offer_accepted_date,
                    candiate_doj=cand.candiate_doj,
                    candiate_email_id=cand.candiate_email_id,
                    hiring_manager=cand.hiring_manager,
                    hiring_manager_email_id=cand.hiring_manager_email_id,
                    email_sent_date=cand.offer_accepted_date + timedelta(days=1)
                )
        #         create
        #         email_sent_date = offer_accepted
            else:
                CandidateDetails.objects.update(
                    candiate_doj=cand.candiate_doj
                )
                print("000000000000000")

        #         write joining_date field



        # try:
        #     obj, created = CandidateDetails.objects.get_or_create(
        #         candiate_email_id=cand.candiate_email_id,
        #         defaults={
        #             'name': cand.name,
        #             'offer_accepted_date': cand.offer_accepted_date,
        #             'candiate_doj': cand.candiate_doj,
        #             'hiring_manager': cand.hiring_manager,
        #             'hiring_manager_email_id': cand.hiring_manager_email_id,
        #             'email_sent_date': cand.offer_accepted_date + timedelta(days=1),
        #         }
        #     )
        #     if not created: # If the object already existed in the database and was retrieved
        #         obj.candiate_doj = cand.candiate_doj
        #         obj.save()
        # except Exception as e:
        #     # Handle the exception if the object creation/update fails
        #     print(e)




#     # candidate_joining_in_next_90days = [{'Name': candidate.name, "candiate_doj": candidate.candiate_doj, "candiate_email_id": candidate.candiate_email_id, "hiring_manager": candidate.hiring_manager, "hiring_manager_email_id": candidate.hiring_manager_email_id} for candidate in rec if candidate.candiate_doj <= next_90_day]
#     # df = pd.DataFrame(candidate_joining_in_next_90days)
#     # df.to_excel("candidate_joining_in_next_90days.xlsx", sheet_name='Sheet1', index=False)
#     # print(candidate_joining_in_next_90days)
#     print('Hello from APScheduler!')




# def scheduler_to_send_mail_in_every_15_days():
#     today = date.today()
#     rec = CandidateDetails.objects.all()

#     if joining_date - today_date == 15:
#         email sent

#     elif email_sent_date < joining_date and email_sent_date + 15 == today_date:
#         email sent
#         email_sent_date = today_date

#     elif email_sent_date < joining_date and offer_accepted+15 != email_sent_date and offer_accepted+15 > email_sent_date:
#         email_sent_date = offer_accepted + 15


#     offer accept - 15 june
#     joingn - 31 july
#     1 july







#     candidate_joining_in_next_90days = [{'Name': candidate.name, "candiate_doj": candidate.candiate_doj, "candiate_email_id": candidate.candiate_email_id, "hiring_manager": candidate.hiring_manager, "hiring_manager_email_id": candidate.hiring_manager_email_id} for candidate in rec if todaycandidate.candiate_doj <= next_90_day]


#     next_90_day = today + timedelta(days=90)

#     rec = CandidateDetails.objects.all()
#     candidate_joining_in_next_90days = [{'Name': candidate.name, "candiate_doj": candidate.candiate_doj, "candiate_email_id": candidate.candiate_email_id, "hiring_manager": candidate.hiring_manager, "hiring_manager_email_id": candidate.hiring_manager_email_id} for candidate in rec if candidate.candiate_doj <= next_90_day]
#     df = pd.DataFrame(candidate_joining_in_next_90days)
#     df.to_excel("candidate_joining_in_next_90days.xlsx", sheet_name='Sheet1', index=False)
#     print(candidate_joining_in_next_90days)
#     print('Hello from APScheduler!')
