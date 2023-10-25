import csv
from gtts import gTTS

# Open the CSV file
with open('decks.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')

    # Iterate through the rows in the CSV
    for row in csv_reader:
        namefile = row[0]
        sentence = row[1]

        # Generate a German MP3 for the sentence
        tts = gTTS(sentence, lang='de')

        # Save the MP3 as "namefile.mp3"
        mp3_filename = f'{namefile}.mp3'
        tts.save(mp3_filename)

        print(f'Generated German MP3 for "{sentence}" as {mp3_filename}')