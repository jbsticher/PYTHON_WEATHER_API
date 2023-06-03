import requests, config

while True:
    try:
        user_input = input('\nEnter city: ')
        weather_data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={config.api_key}')
        weather = weather_data.json()['weather'][0]['main']
        temp = weather_data.json()['main']['temp']
        print(f'\nThe current condition in {user_input.title()} is {weather}.')
        print(f'The temperature is currently {temp} degrees Farenheit.')
        print('\nDo you want to see the weather for another City? (yes or no)')
        if not input('> ').lower().startswith('y'):
            break
    except:
        print('City not found...try again.')

print('\nHave a nice day.\n')

        
            


