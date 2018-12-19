import random
import os
import pickle

class Bot():
    def __init__(self):
        self.options = {
            'commands'  : self.get_commands,
            'worship'   : self.worship,
            'stats'     : self.stats,
            '1st'       : self.first_place,
            '2nd'       : self.second_place,
        }

        self.records = {
            'first'     : 2,
            'second'    : 0,
            'worse'     : 0,
        }

        if os.path.isfile("stats.pk1"):
            with open("stats.pk1", "rb") as records:
                self.records = pickle.load(records)
            records.close()

        self.praises = []
        with open('praises.txt', 'r') as praise_file:
            for line in praise_file:
                self.praises.append(line)
        praise_file.close()

    def get_commands(self, message):
        return 'Befehle: ' + str(self.options.keys())
    
    def worship(self, message):
        praise = random.choice(self.praises)
        user_name = str(message.author.name)

        return praise.replace("<Name>", user_name)

    def stats(self, message):
        games = self.records['first'] + self.records['second'] + self.records['worse']
        points = 3*self.records['first'] + self.records['second']
        average = points/games

        stats_str =  "Ihr habt " + str(points) + " Punkte in insgesamt " + str(games) + " Spielen gesammelt. Das sind durchschnittlich " + str(average) + " Punkte pro Spiel."
        
        sentence_str = ""
        if average > 1.0:
            sentence_str = "Nicht schlecht, gratuliere!"
        else:
            sentence_str = "Ihr Versager! Eine Schande, dass ihr dieses Spiel überhaupt spielt!"

        return stats_str + sentence_str

    def first_place(self, message):
        victories = self.records['first']
        self.records['first'] = victories +1
        with open("stats.pk1", "wb") as records:
            pickle.dump(self.records, records)
        records.close()

        return "Erster Platz, ich bin beeindruckt! Wobei, eigentlich war es ja auch nicht anders zu erwarten... ;). Nehmt diese 3 Punkte als Zeichen meiner Anerkennung entgegen"

    def second_place(self, message):
        second = self.records['second']
        self.records['second'] = second +1
        with open("stats.pk1", "wb") as records:
            pickle.dump(self.records, records)
        records.close()

        return "Was? Nur Zweiter? Da ist aber noch Luft nach oben... Naja, ein einzelnes Pünktchen erhaltet ihr trotzdem noch. Aber nur, weil ihr es seid."
         
        
    def create_response_string(self, message):
        message_str = message.content
        command = message_str.split(' ')[0][1:]

        response_function = self.options.get(command, lambda m: "Kein Command, N00b")
        
        return response_function(message)



             
           


