from . import utils
#################################################
"""            INSTRUMENT                """
#################################################
def Instrument(symbol):
    symbol = str(symbol).upper()
    return {
        '__symbol' : symbol,
        'Sym'      : symbol,
        'SecTyp'   : 'CS',
        '__type'   : 'equity'
    }

#################################################
def Equity(symbol):
    return Instrument(symbol)

#################################################
def Option (instrument, maturity_date, strike):
    return {
        **{
            'MatDt'      : str(maturity_date) + 'T00:00:00.000-05:00',
            'StrkPx'     : str(int(strike)),
            'SecTyp'     : 'OPT',
            '__maturity' : str(maturity_date),
            '__strike'   : str(int(strike))
        },
        **instrument
    }

#################################################
def Call (instrument, maturity_date, strike):
    # Let Option do some lifting
    x = {
        **{ 'CFI':'OC' },
        **Option(instrument, maturity_date, strike)
    }
    x['__underlying'] = x['Sym']
    x['__type']       = 'call'
    x['__symbol']     = utils.option_format(
        symbol        = x['Sym'],
        exp_date      = x['__maturity'],
        strike        = x['__strike'],
        direction     = 'C'
    )
    return x
        
#################################################
def Put (instrument, maturity_date, strike):
    # Let Option do some lifting
    x = {
        **{ 'CFI':'OP' },
        **Option(instrument, maturity_date, strike)
    }
    x['__underlying'] = x['Sym']
    x['__type']       = 'put'
    x['__symbol']     = utils.option_format(
        symbol        = x['Sym'],
        exp_date      = x['__maturity'],
        strike        = x['__strike'],
        direction     = 'P'
    )
    return x