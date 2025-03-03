import logging




try:
    a = 1/0
    print (a)

except ZeroDivisionError as e:
    print(str(e))

except ValueError as e:
    pass

except Exception as e:
    logging.exception(e)

