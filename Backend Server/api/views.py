from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import *
from .models import *

from datetime import datetime, timedelta, date
# Create your views here.

@api_view(['POST'])
def postEvent(request):

    id = request.data['id']
    member = request.data['member']
    event = request.data['event']

    checkMember = Member.objects.filter(_id=id)
    
    prevMemberEvents = Event.objects.filter(member___id=id).order_by('-id')[:1]
    prevSerializer = EventSerializers(prevMemberEvents, many=True)

    print(prevSerializer.data)

    if len(checkMember) == 0:
        member2 = Member.objects.create(name=member, _id=id)
        member2.save()

        event2 = Event.objects.create(
            name=event,
            member=member2
        )
        event2.save()
    else:
        event2 = Event.objects.create(
            name=event,
            member=Member.objects.get(_id=id)
        )
        event2.save()

    memberEvents = Event.objects.filter(member___id=id).order_by('-id')[:1]
    serializer = EventSerializers(memberEvents, many=True)

    print(serializer.data)

    print("********************************************************")

    if (serializer.data[0]['name'] == 'Left'):
        if (len(prevSerializer.data) > 0):
            if (prevSerializer.data[0]['name'] == 'Joined'):
                if ((memberEvents[0].time - prevMemberEvents[0].time).total_seconds() < 0):
                    report = Report.objects.create(
                    member=Member.objects.get(_id=id),
                    time_spent=str(memberEvents[0].time + timedelta(hours=24, minutes=0, seconds=0) - prevMemberEvents[0].time)[:-10],
                    date_created=memberEvents[0].time
                    )
                elif prevMemberEvents[0].time == memberEvents[0].time:
                    report = Report.objects.create(
                        member=Member.objects.get(_id=id),
                        time_spent=str(timedelta(hours=24, minutes=0, seconds=0))[:-10],
                        date_created=memberEvents[0].time
                    )
                else:
                    print("Current Event Time", prevMemberEvents[0].time, "Previous Event Time", memberEvents[0].time)
                    report = Report.objects.create(
                        member=Member.objects.get(_id=id),
                        time_spent=str(memberEvents[0].time - prevMemberEvents[0].time)[:-10],
                        date_created=memberEvents[0].time
                    )
                report.save()

    
    reportSerializer = ReportSerializer(Report.objects.filter(member___id=id).order_by('-id')[:1], many=True)
    return Response({
        "Previous Event": prevSerializer.data,
        "Current Event": serializer.data,
        "Report": reportSerializer.data
    })


# Add Cron Job Code
@api_view(['GET'])
def weeklyReport(request): 
    members = Member.objects.all()
    for member in members:
        reports = Report.objects.filter(member=member)
        for report in reports:
            pass
