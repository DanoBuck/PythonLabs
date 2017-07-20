def pounds_to_kilos(pounds):
    kg_conversion_rate = 0.453592
    converted = pounds * kg_conversion_rate
    return round(converted, 4)


def kilos_to_pounds(pounds):
    kg_conversion_rate = 0.453592
    converted = pounds / kg_conversion_rate
    return round(converted, 4)

print("*********LBS to KG*********")
print("12 LBS to KG is", pounds_to_kilos(12))
print("15 LBS to KG is", pounds_to_kilos(15))
print("40 LBS to KG is", pounds_to_kilos(40))

print("\n*********KG to LBS*********")
print("7.5 KG to LBS is", kilos_to_pounds(7.5))
print("20 KG to LBS is", kilos_to_pounds(20))
print("30 KG to LBS is", kilos_to_pounds(30))