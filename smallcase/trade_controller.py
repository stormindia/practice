from models import User
from trade_handler import trade_handle
from exceptions import BadRequestException
from flask import session, request

class TradeController:
    def __init__(self):
        self.handler = trade_handle()
        self.possible_get_actions = ['portfolio','trade','returns']
        self.possible_post_actions = ['add','sell']
        self.possible_put_actions = ['update']
        self.possible_delete_actions = ['delete']

    def validate_user(self,filters):
        user_id = filters.get("user_id", None)
        if user_id is None:
            raise BadRequestException(message='user_id is a must')

        try:
            user = User.objects.get(id=user_id)
        except:
            raise BadRequestException(message='user not found')
        
        return user
    
    def get(self):
        filters = request.args
        action = filters.get("action", None)
        if action not in self.possible_get_actions:
            raise BadRequestException(message='invalid action')
        
        user = self.validate_user(filters)
        trade_info = filters.get("trade_info",None)
        
        if action is 'portfolio':
            resp = self.handler.fetch_portfolio(user,trade_info)
        
        if action is 'trade':
            resp = self.handler.fetch_trade(user,trade_info)
        
        if action is 'returns':
            resp = self.handler.fetch_trade(user,trade_info)
        
        return resp
        

    def post(self):
        filters = request.args

        action = filters.get("action", None)

        if action not in self.possible_post_actions:
            raise BadRequestException(message='invalid action')
        
        user = self.validate_user(filters)

        trade_info = filters.get("trade_info",None)

        if trade_info is None:
            raise BadRequestException(message='trade info is required')

        if action is 'add':
            resp = self.handler.add_trade(user,trade_info)
        
        if action is 'sell':
            resp = self.handler.sell_trade(user,trade_info)
        
        return resp
    
    def put(self):
        filters = request.args

        action = filters.get("action", None)

        if action not in self.possible_put_actions:
            raise BadRequestException(message='invalid action')
        
        user = self.validate_user(filters)

        trade_info = filters.get("trade_info",None)
        
        resp = self.handler.update_trade(user,trade_info)
        return resp
    
    def delete(self):
        filters = request.args

        action = filters.get("action", None)

        if action not in self.possible_delete_actions:
            raise BadRequestException(message='invalid action')
        
        user = self.validate_user(filters)

        trade_info = filters.get("trade_info",None)
        
        resp = self.handler.remove_trade(user,trade_info)
        return resp

        
        


        

