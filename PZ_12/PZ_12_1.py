# 1. Даны значения роста 20 юношей. Определить, сколько юношей будут направлены в баскетбольную команду (рост от 190) и сколько в футбольную (остальные).

import random

def generate_heights(min_height, max_height, length):
    return [random.randint(min_height, max_height) for _ in range(length)]

def determine_teams(heights):
    return {
        'basketball':[guy for guy in heights if guy >= 190],
        'football':[guy for guy in heights if guy < 190]
        }

heights = generate_heights(170, 210, 20)
teams = determine_teams(heights)

print(f'Рост юношей: {heights}')
print(f'Количество юношей в баскетбольной команде: {len(teams['basketball'])}')
print(f'Количество юношей в футбольной команде: {len(teams['football'])}')
