from rest_framework import serializers
from .models import *

class MemberSerialzier(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'

class EventSerializers(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'

class WeeklyReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeeklyReport
        fields = '__all__'