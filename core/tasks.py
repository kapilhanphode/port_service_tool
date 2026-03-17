from celery import shared_task


@shared_task
def send_rfq_notification(rfq_id):
    print(f"Sending RFQ notification for RFQ>>>>>>>>>>>> {rfq_id}")
