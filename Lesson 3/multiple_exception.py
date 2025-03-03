import logging


try:
    a = 1/0
    print (a)

except (ZeroDivisionError, ValueError) as e:
    print(str(e))

except AttributeError as e:
    pass

except Exception as e:
    logging.exception(e)