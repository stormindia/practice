# API Documentation

1. The route is present in router.py. 
2. The methods (GET/POST/PUT/DELETE) are present in trade_controller.py. 
3. Schema is present in models.py
4. trade_handler.py handles the logic behind the functions
5. exceptions.py is used to raise an exception in case of invalid values/missing values

## Models (DB tables)

1. User - store the user info
2. TickerSymbol - Store the info about the company such as name/symbol/current share price
3. PortfolioList - Store the current Portfolio state of the user
4. TradeHistory - Store the last snapshot of the PortfolioList before making a change so that it can be used later to revert the changes

## Trade handler

Functions - 
1. add_trade
2. sell_trade
3. update_trade
4. remove_trade
5. fetch_trade
6. fetch_portfolio
7. fetch_returns


#### Please Note
This is just a demo code for illustration purpose to demonstrate SCHEMA design and API and handlers for the functions mentioned in the [document](https://github.com/stormindia/practice/blob/master/smallcase/smallcase%20Backend%20Task%20-%20Revised.pdf)