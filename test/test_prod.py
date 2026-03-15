import importlib
import sys
import types
from datetime import datetime, timedelta
from unittest.mock import Mock


def test_convert_time_zone():
    """
    test_convert_time_zone function.

    Args:
        None

    Returns:
        Any: Function result.
    """
    if "dateutil" not in sys.modules:
        fake_dateutil = types.ModuleType("dateutil")
        fake_dateutil.parser = types.SimpleNamespace(
            parse=lambda s: datetime.strptime(s, "%Y-%m-%d %H:%M")
        )
        sys.modules["dateutil"] = fake_dateutil

    module = importlib.import_module("functions.prod.convert_time_zone")
    module.timedelta = timedelta

    from_response = Mock()
    from_response.raise_for_status.return_value = None
    from_response.json.return_value = {"utc_offset": "-05:00"}

    to_response = Mock()
    to_response.raise_for_status.return_value = None
    to_response.json.return_value = {"utc_offset": "+00:00"}

    calls = iter([from_response, to_response])
    module.requests.get = lambda *args, **kwargs: next(calls)

    result = module.convert_time_zone("2024-01-01 12:00", "America/New_York", "Europe/London")
    assert isinstance(result, dict)
    assert result["original_time"] == "2024-01-01 12:00"
    assert result["from_timezone"] == "America/New_York"
    assert result["to_timezone"] == "Europe/London"
    assert isinstance(result["converted_time"], str)
    assert result["converted_time"] == "2024-01-01 17:00"