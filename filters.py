
def apply_filters(matches, source):
    result = []
    for m in matches:
        filters_passed = []

        if m.get("under2_5") == "Yes" and m.get("btts") == "Yes":
            filters_passed.append("Filter 1")
        if m["odds"]["1"] < m["odds"]["2"] and m["htft"].get("1/2", 0) > 20:
            filters_passed.append("Filter 2")
        if m["odds"]["1"] < m["odds"]["2"] and m["dnb"]["2"] < m["dnb"]["1"]:
            filters_passed.append("Filter 3")
        if m["odds"]["1"] < m["odds"]["2"] and m["htft"].get("2/2", 0) < m["htft"].get("1/1", 100):
            filters_passed.append("Filter 4")
        if m["odds"]["1"] > 2.0:
            filters_passed.append("Filter 5")

        if filters_passed:
            result.append(f"*{source}* - *{m['home']} vs {m['away']}*
Passed: {', '.join(filters_passed)}
Home odds: {m['odds']['1']}
")

    return result
