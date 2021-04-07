from trade_handler import TradeController

def setup_routing(api):
    # one endpoint required with different methods (GET,POST,PUT,DELETE defined in TradeController)
    api.add_resource(TradeController, "/api/trade/")
