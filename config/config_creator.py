import configparser


config = configparser.ConfigParser()

config.add_section('BotBook')
config.set('BotBook', 'token', '6020407519:AAHnaQ__ebILpXt1DdfCZl5Uih8auzqdHmg')
config.set('BotBook', 'admin_ids', '573619968, 573619968')

with open('config_data', 'w') as config_data:
    config.write(config_data)
