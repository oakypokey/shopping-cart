from shopping_cart import getHumanFriendlyTimestamp
import datetime

def test_to_human_friendly_timestamp_now():
    dt = datetime.datetime.now()
    result = getHumanFriendlyTimestamp(dt)
    assert result == dt.strftime("%D %I:%M%p")

def test_to_human_friendly_timestamp_predefined():
    dt = datetime.datetime(2020,3,1,10,10)
    result = getHumanFriendlyTimestamp(dt)
    assert result == '03/01/20 10:10AM'