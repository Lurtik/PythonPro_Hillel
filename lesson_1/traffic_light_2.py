def traffic_light(colour):
    answer = "невідомий сигнал"
    match colour:
        case "red":
            answer = "зупинитися"
        case "yellow":
            answer = "очікувати або підготуватися відповідно до навчальної моделі"
        case "green":
            answer = "рух дозволено за умови безпеки"
    return answer

print(traffic_light(input("Enter the traffic light colour: ")))