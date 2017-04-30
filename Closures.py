def getDayOfWeek(language):
    def getDay(i):
        if i >= 1 and i <= 7:
            irishDaysList = ["Dé Luain", "Dé Máirt", "Dé Céadaoin", "Déardaoin", "Dé hAoine", "Dé Sathairn", "Dé Domhnaigh"]
            daysInEnglish = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            if language == "Irish":
                return irishDaysList[i-1]
            elif language == "English":
                return daysInEnglish[i-1]
        else:
            return "Incorrect Number Specified"
    return getDay

irishDay = getDayOfWeek("Irish")
print("******Days in Irish******")
print(irishDay(1))
print(irishDay(2))
print(irishDay(3))
print(irishDay(4))
print(irishDay(5))
print(irishDay(6))
print(irishDay(7))
print(irishDay(8))

englishDay = getDayOfWeek("English")
print("\n******Days in English******")
print(englishDay(1))
print(englishDay(2))
print(englishDay(3))
print(englishDay(4))
print(englishDay(5))
print(englishDay(6))
print(englishDay(7))
print(englishDay(8))
