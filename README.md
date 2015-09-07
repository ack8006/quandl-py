QuandlPy: Simple Quandl Python Wrapper
======================================

This is an example that covers all options:

```python
import quandlpy as qp
qp.get('YAHOO','AAPL',api_key='xxxxxx', start_date='2010-01-01', 
		end_date='2014-12-31', order='dsc', rows=10, column_index=3,
		collapse='weekly', transform='rdiff')

```

All parameters except the dataset (YAHOO) and the ticker (AAPL) are optional
