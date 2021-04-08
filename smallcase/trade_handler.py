from models import User, TickerSymbol,PortfolioList,TradeHistory
from exceptions import BadRequestException
from django.core.exceptions import ObjectDoesNotExist

class trade_handle:
    
    def add_trade(self,user,trade_info):
        
        try:
            ticker_symbol = trade_info.get('ticker_symbol')
            buy_price = trade_info.get('buy_price')
            shares = trade_info.get('shares')
        except Exception as e:
            raise BadRequestException(message=str(e))
        
        if buy_price < 0 or shares <= 0:
            raise BadRequestException(message='invalid buy price or share quantity')

        try:
            ticker = TickerSymbol.get(comp_symbol=ticker_symbol)
        except ObjectDoesNotExist:
            raise BadRequestException(message="invalid company")
        
        # find if a trade already exist for this ticker
        try:
            old_trade = PortfolioList.objects.get(ticker=ticker,user=user,shares__gt=0)
            # add it in TradeHistory
            trade_hist = TradeHistory()
            trade_hist.user = user
            trade_hist.trade_type = 'add'
            trade_hist.portfolio_state_id = old_trade.id
            trade_hist.buy_price = old_trade.buy_price
            trade_hist.shares = old_trade.shares
            trade_hist.is_active = True
            trade_hist.save()
            new_buy = (old_trade.buy_price*old_trade.shares + buy_price*shares) / (old_trade.shares + shares)
            old_trade.buy_price = new_buy
            old_trade.shares += shares
            old_trade.save()
        except ObjectDoesNotExist:
            trade = PortfolioList()
            trade.user = user
            trade.ticker = ticker
            trade.buy_price = buy_price
            trade.shares = shares
            trade.save()

            # add it in the TradeHistory
            # store portfolio id and other fields as NULL indicating that this is the first trade made for that user
            trade_hist = TradeHistory()
            trade_hist.user = user
            trade_hist.trade_type = 'add'
            trade_hist.portfolio_state_id = None
            trade_hist.buy_price = None
            trade_hist.shares = None
            trade_hist.is_active = True
            trade_hist.save()
        
        return {"success":True,"message":"Trade added successfully"}


    def sell_trade(self,user,trade_info):

        portfolio_state_id = trade_info.get('portfolio_state_id',None)
        shares = trade_info.get('shares',None)

        try:
            portfolio = PortfolioList.objects.get(id=portfolio_state_id)
        except ObjectDoesNotExist:
            raise BadRequestException(message='invalid portfolio id')
        
        if shares is None or shares > portfolio.shares:
            raise BadRequestException(message='invalid shares quantity')

        # add current state in TradeHistory
        trade_hist = TradeHistory()
        trade_hist.user = user
        trade_hist.trade_type = 'sell'
        trade_hist.portfolio_state_id = portfolio.id
        trade_hist.buy_price = portfolio.buy_price
        trade_hist.shares = portfolio.shares
        trade_hist.is_active = True
        trade_hist.save()

        portfolio.shares -= shares
        portfolio.save() 

        return {"success":True,"message":"Trade sold successfully"}
    
    def update_trade(self,user,trade_info):
        portfolio_state_id = trade_info.get('portfolio_state_id',None)
        shares = trade_info.get('shares',None)
        if shares is not None and shares < 0:
            raise BadRequestException(message='invalid shares quantity')
        ticker_id = trade_info.get('ticker_id',None)
        buy_price = trade_info.get('buy_price',None)

        if shares is None and ticker_id is None and buy_price is None:
            return {"success":True,"message":"Nothing to update"}

        try:
            portfolio = PortfolioList.objects.get(id=portfolio_state_id)

            # add it to TradeHistory
            trade_hist = TradeHistory()
            trade_hist.user = user
            trade_hist.trade_type = 'update'
            trade_hist.portfolio_state_id = portfolio.id
            trade_hist.buy_price = portfolio.buy_price
            trade_hist.shares = portfolio.shares
            trade_hist.is_active = True
            trade_hist.save()


            if shares is not None:
                portfolio.shares = shares
            
            if buy_price is not None:
                portfolio.buy_price = buy_price
            
            if ticker_id is not None:
                ticker = TickerSymbol.objects.get(id=ticker_id)
                portfolio.ticker = ticker
            
            portfolio.save()

        except ObjectDoesNotExist:
            raise BadRequestException(message='invalid portfolio id')


    def remove_trade(self,user,trade_info):
        trade_id = trade_info('trade_id',None)
        if trade_id is None:
            raise BadRequestException(message='trade id is must')
        try:
            trade_hist = TradeHistory.objects.get(id=trade_id,is_active=True)
            portfolio = PortfolioList.objects.get(id=trade_hist.portfolio_state_id)
            trade_hist.is_active = False
            portfolio.buy_price = trade_hist.buy_price
            portfolio.shares = trade_hist.shares
            portfolio.save()
            trade_hist.save()
            return {"success":True,"message":"trade removed"}
        except:
            raise BadRequestException(message='invalid trade id')
        

    def fetch_trade(self,user,trade_info):
        ticker_id = trade_info.objects.get('ticker_id',None)

        if ticker_id is None:
            raise BadRequestException(message='ticker is required')
        else:
            try:
                ticker = TickerSymbol.objects.get(id=ticker_id)
            except:
                raise BadRequestException(message='invalid ticker_id')
        
        resp = dict()
        try:
            trade = PortfolioList.objects.get(user=user,ticker=ticker)
            resp['buy_price'] = trade.buy_price
            resp['shares'] = trade.shares
            resp['current_share_price'] = ticker.current_share_price
            return resp
        except:
            return resp
    
    def fetch_portfolio(self,user):
        portfolio = PortfolioList.objects.get(user=user)

        resp = []

        for p in portfolio:
            abcd = dict()
            abcd['ticker'] = p.ticker
            abcd['buy_price'] = p.buy_price
            abcd['shares'] = p.buy_price

            resp.append(abcd)
        
        return resp
    
    def fetch_returns(self,user):
        portfolio = PortfolioList.objects.get(user=user,shares__gt=0)

        total = 0

        for p in portfolio:
            current_price = ticker.current_share_price # is Rs 100 by default as mentioned in docs
            avg_price = p.buy_price

            total += (current_price-avg_price)*p.shares
        
        return total







        