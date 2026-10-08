# Working with Lists
from pyscript import document
# Variables
country = ("China", "Japan", "South Korea", "North Korea", "Mongolia", "Taiwan", "Hong Kong","Macau")
nickname = ("The Red Dragon","Land of the Rising Sun", "Land of the Morning Calm", "The Hermit Kingdom","Land of the Eternal Blue Sky","The Beautiful Island", "Asia's World City","Las Vegas of Asia")

# Function
def show_name(e):
    selected_country = document.getElementById("country").value

    selected_nickname = nickname[int(selected_country)]

    document.getElementById("result").innerText = selected_nickname
