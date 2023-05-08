#create a variable with painting's name and one with the date its painted
paintings = [
    'The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope',
    'Self Portrait With Monkeys'
]
dates = [1939, 1933, 1946, 1940]

#putting togheter lists painting and dates
paintings = list(zip(paintings, dates))
print(paintings)

#adding new key, value to painting list
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wounded Deer', 1946))
paintings.append(('Me and My Doll', 1937))
print(paintings)

#generating index for audio
print(len(paintings))
audio_tour_number = list(range(1, len(paintings) + 1))
print(audio_tour_number)

#putting togheter audio tour number and paintings
master_list = list(zip(audio_tour_number, paintings))
print(master_list)
