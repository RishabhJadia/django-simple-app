from apscheduler.schedulers.background import BackgroundScheduler
from scheduler.tasks import scheduler_candidate_joining_in_next_90days


def start():
	scheduler = BackgroundScheduler()
	# scheduler.add_job(my_task, 'interval', minutes=1)
	scheduler.add_job(scheduler_candidate_joining_in_next_90days, 'interval', hours=10)
	scheduler.start()