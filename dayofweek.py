def zellers_congruence(day: int, month: int, year: int) -> str:
    """
    Calculates the day of the week for any Gregorian calendar date.
    
    Parameters:
    day (int): 1-31
    month (int): 1-12 (1=Jan, 2=Feb, ..., 12=Dec)
    year (int): 4-digit year (e.g., 2026)
    
    Returns:
    str: The name of the day of the week.
    """
    # 1. Adjust January and February to months 13 and 14 of the previous year
    if month < 3:
        month += 12
        year -= 1

    # 2. Extract components for the formula
    q = day
    m = month
    K = year % 100
    J = year // 100

    # 3. Apply the Gregorian Zeller's Congruence formula
    h = (q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) + (5 * J)) % 7

    # 4. Map the integer outcome to the corresponding day name
    # 0 = Saturday, 1 = Sunday, 2 = Monday, ..., 6 = Friday
    days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    
    return days[h]


# --- Example Verification ---
if __name__ == "__main__":
    # Test for Halloween 2026 (October 31, 2026)
    test_day, test_month, test_year = 31, 10, 2026
    result = zellers_congruence(test_day, test_month, test_year)
    print(f"The date {test_year}-{test_month:02d}-{test_day:02d} falls on a {result}.")
    # Output: The date 2026-10-31 falls on a Saturday.
