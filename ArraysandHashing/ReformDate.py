class Solution:
    def reformatDate(self, date: str) -> str:
        days = {"1":"01", "2":"02", "3":"03", "4":"04", "5":"05", "6":"06", "7":"07", "8":"08", "9":"09"}
        format = []
        dates = 0
        i = 0
        while date[i] != " ":
            if date[i] not in "0123456789":
                pass
            else:
                dates = dates * 10 + int(date[i])
            i += 1

        if dates > 9:
            format.append(str(dates))
        else:
            two_digit_date = "0" + str(dates)
            format.append(two_digit_date)

        i += 1
        month = ""
        months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10","Nov":"11", "Dec":"12"}
        while date[i] != " ":
            month += date[i]
            i += 1
        format.append(months[month])

        i += 1
        year =  ""
        while i < len(date):
            year += date[i]
            i += 1
        
        format.append(year)

        result = ""
        while format:
            result += format.pop() + "-"

        return result[0:-1]
        