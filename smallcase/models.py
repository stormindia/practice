#SCHEMA

class User:
    name = models.CharField(null=False, max_length=255)

class TickerSymbol:
    comp_name = models.CharField(null=False, max_length=512)
    comp_symbol = models.CharField(null=False, max_length=255)
    current_share_price = models.FloatField(null=False,default=100.00)

class PortfolioList:
    user = models.ForeignKey(User)
    ticker = models.ForeignKey(TickerSymbol)
    buy_price = models.FloatField(null=False)
    shares =  models.IntegerField(null=False)

# to be used to revert a change
# store trade_id and the portfolio condition of that particular state at the time of execution of the trade_id
class TradeHistory:
    TRADE_CHOICES = (
        ('add','add'),
        ('sell','sell'),
        ('update','update')
    )
    trade_id = models.IntegerField(null=False,auto_increment=True)
    trade_type = models.CharField(null=False, max_length=255,choices=TRADE_CHOICES)
    user = models.ForeignKey(User)
    portfolio_state_id = models.IntegerField(null=True)
    buy_price = models.FloatField(null=False)
    shares =  models.IntegerField(null=False)
    is_active = models.BooleanField()