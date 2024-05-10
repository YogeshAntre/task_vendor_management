from django.db import models
from django.db.models import F,Count, Avg

class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)

    def __str__(self):
        return self.name
    def update_performance_metrics(self):
        try:
            completed_orders = self.purchaseorder_set.filter(status='completed')
            total_completed_orders = completed_orders.count()
            
            # On-Time Delivery Rate
            on_time_delivery_orders = completed_orders.filter(delivery_date__lte=F('acknowledgment_date')).count()
            self.on_time_delivery_rate = (on_time_delivery_orders / total_completed_orders) * 100 if total_completed_orders > 0 else 0

            # Quality Rating Average
            quality_ratings = completed_orders.exclude(quality_rating=None).aggregate(avg_rating=Avg('quality_rating'))['avg_rating']
            self.quality_rating_avg = quality_ratings if quality_ratings else 0

            # Average Response Time
            response_times = completed_orders.exclude(acknowledgment_date=None).aggregate(avg_time=Avg(F('acknowledgment_date') - F('issue_date')))['avg_time']
            self.average_response_time = response_times.total_seconds() if response_times else 0

            # Fulfilment Rate
            successful_orders = completed_orders.filter(issue_date__lte=F('acknowledgment_date'))
            self.fulfillment_rate = (successful_orders.count() / total_completed_orders) * 100 if total_completed_orders > 0 else 0

            self.save()
        except Exception as e:
            return e

class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=50, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50)
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.po_number

class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()


    def __str__(self):
        return f"{self.vendor} - {self.date}"


