def traffic_light(colour):
    answer = "невідомий сигнал"
    if colour == "red":
        answer = "зупинитися"
    elif colour == "yellow":
        answer = "очікувати або підготуватися відповідно до навчальної моделі"
    elif colour == "green":
        answer = "рух дозволено за умови безпеки"
    return answer

print(traffic_light(input("Enter the traffic light colour: ")))