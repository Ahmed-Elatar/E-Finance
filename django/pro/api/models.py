from django.db import models
from django.utils import timezone

# Create your models here.



class Ticker(models.Model):

    symbol =models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)

    current_price =models.FloatField(default=0.0,null=True, blank=True )
    price_change = models.FloatField(default=0.0,null=True, blank=True)
    price_change_per = models.FloatField(default=0.0,null=True, blank=True)
    current_volume =models.FloatField(default=0.0,null=True, blank=True)
    volume_change = models.FloatField(default=0.0,null=True, blank=True)
    volume_change_per = models.FloatField(default=0.0,null=True, blank=True)
    last_update = models.DateTimeField(default=timezone.now )

    def __str__(self) -> str:
        return self.name
 


class History(models.Model):

    ticker =models.ForeignKey(Ticker,related_name='history', on_delete=models.CASCADE)
    price=models.FloatField()
    volume=models.FloatField()
    date= models.DateTimeField(auto_now=True,null=True, blank=True)



    # Calculate price and volume changes and percentage then save the Current value
    def save(self, *args, **kwargs):

        previous_price = self.ticker.current_price
        self.ticker.price_change = self.price - previous_price
        self.ticker.price_change_per=(self.price - previous_price) / max(previous_price,1)
        self.ticker.current_price = self.price


        previous_volume = self.ticker.current_volume
        self.ticker.volume_change = self.volume - previous_volume
        self.ticker.volume_change_per = (self.volume - previous_volume) / max(previous_volume,1)
        self.ticker.current_volume =self.volume

        self.ticker.last_update = timezone.now()

        # Save the updated Ticker
        self.ticker.save()

        # Call the parent save method to save the Current instance
        super(History, self).save(*args, **kwargs)


    def __str__(self) -> str:
        return f"{self.ticker.name}" 