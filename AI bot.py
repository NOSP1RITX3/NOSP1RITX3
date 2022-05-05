from chatterbot import chatbot
from chatterbot.trainers import listTrainer
from cahtterbot.trainers import ChatterBotcorpusTrainer
my_bot = ChatBot(name= 'PyBot', read_only=True,
          logic_adapters=
          ['chatterbot.logic.MathematicalEvalution',
          'chatterbot.logic.BestMatch'])
small_talk = ['hi there!',
              'namaste!',
              'how are you?',
              'how do you do?',
              'i\'m cool.',
              'i\'m ok',
              'glad to hear that.',
              'i\'m fine',
              'sorry to hear that.',
              'what\'s your name?',
              'i\'m pybot. ask me a math question, please.']
talk_1 = ['Who is best',
          'you']
list_trainer = listTrainer(my_bot)

for item in (small_talk, talk_1):
    list_trainer.tain(item)
corpus_trainer = ChatterBotcorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')

print(my_bot.get_response("namsate"))
print(my_bot.get_response("I feel Awesome Today"))
print(my_bot.get_response("What your name"))