def test_convert_time_zone():
    from functions.prod.convert_time_zone import convert_time_zone

    result = convert_time_zone("2024-01-01 12:00", "America/New_York", "Europe/London")
    assert result["original_time"] == "2024-01-01 12:00"
    assert result["from_timezone"] == "America/New_York"
    assert result["to_timezone"] == "Europe/London"
    assert result["converted_time"] == "2024-01-01 17:00"  # Assuming EST to GMT conversion