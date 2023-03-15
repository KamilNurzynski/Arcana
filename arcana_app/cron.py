from arcana_app.models import Truck
from twilio.rest import Client
from datetime import date, timedelta


def my_scheduled_job():
    '''
    Background task with interval set in settings. Function send SMS when is information that MOT expires
    '''
    
    trucks = Truck.objects.all()
    today = date.today()
    for truck in trucks:
        if (truck.expire_MOT - today) <= timedelta(days=20):
            account_sid = 'AC931cc13744e2966e9fe68736eaae9741'
            auth_token = '0024a27e3eff3ae261ddfb221405898d'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                body=f"{truck.color} {truck.brand} with reg numbers {truck.registration_number} has 20 days to MOT",
                from_='+16198536183',
                to='+48732190892'
            )
            ##########
            print(message.sid)
            print(truck.expire_MOT - date.today())
            ##########