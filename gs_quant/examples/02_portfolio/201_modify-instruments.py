# Portfolio instruments can be updated

from gs_quant.common import PayReceive, Currency  # import constants
from gs_quant.instrument import IRSwaption  # import instruments
from gs_quant.markets.portfolio import Portfolio
from gs_quant.session import Environment, GsSession  # import sessions

client_id = None  # Supply your application id
client_secret = None  # Supply your client secret
scopes = ('run_analytics',)
GsSession.use(Environment.PROD, client_id, client_secret, scopes)

swaption1 = IRSwaption(PayReceive.Pay, '5y', Currency.EUR, expiration_date='3m', name='EUR-3m5y')
swaption2 = IRSwaption(PayReceive.Pay, '5y', Currency.EUR, expiration_date='6m', name='EUR-6m5y')
swaption3 = IRSwaption(PayReceive.Pay, '5y', Currency.EUR, expiration_date='9m', name='EUR-9m5y')

portfolio = Portfolio((swaption1, swaption2))
portfolio.instruments = (swaption1, swaption2, swaption3)