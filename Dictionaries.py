
monthConversions = {
    0 : "January",
    "Feb" : "February",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December"
}

print(monthConversions)
print(monthConversions[0])
print(monthConversions.get("May"))
print(monthConversions.get("Luv" , "Not a valid key"))