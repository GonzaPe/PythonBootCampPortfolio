print('''
*******************************************************************************
                __------__
              /~          ~\
             |    //^\\//^\|
           /~~\  ||  o| |o|:~\
          | |6   ||___|_|_||:|
           \__.  /      o  \/'
            |   (       O   )
   /~~~~\    `\  \         /
  | |~~\ |     )  ~------~`\
 /' |  | |   /     ____ /~~~)\
(_/'   | | |     /'    |    ( |
       | | |     \    /   __)/ \
       \  \ \      \/    /' \   `\
         \  \|\        /   | |\___|
           \ |  \____/     | |
           /^~>  \        _/ <
          |  |         \       \
          |  | \        \        \
          -^-\  \       |        )
               `\_______/^\______/
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the jade monkey before the next full moon.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You don't remember anything but a note in your pocket says that the jade monkey is in your own house and there's an adress because (oh, surprise, you don't remember it too). Also, the note says that the jade monkey has to be with you if you want to avoid being converted into a jade monkey too.")
go_or_no = input('What do you want to do? Go to your house or ignore the note? Type "go" or "ignore"').lower()
if go_or_no == "ignore":
  print("You ignore the note and the world continues as usual. To get converted into a jade monkey is physically impossible, of course.")
  print("Game over")
else:
  print("You walk straight to the address... at least a jade monkey would be curious to see.\nAlso you suspect the veracity of the note (of course a jade monkey legend is not suspicious), so you doubt about entering from the door or by the window...")
  entrance = input('To use the door type "door" but if you prefeer the window type "window"').lower()
  if entrance == "window":
    print("A policeman sees you getting inside by the window and arrests you. When you try to explain to him about the jade monkey, the story makes you win a free vacation in Arkham Asylum.")
    print("Game over")
  else:
    print("Of course you prefer to enter by the door like a normal person... to be an esoteric guy who believes in a jade monkey legend found in a note in your pocket doesn't make you a vulgar who enters a house by the window.\nAlso you don't see the monkey anywhere but there are two doors, a white one and a yellow. At this moment you think the situation is very strange and you don't feel very confortable.")
    inside = input('If you want to leave and make something productive type "leave" but if you prefer to follow your dubious common sense and get inside one of the doors type its color (white or yellow).').lower()
    if inside == "leave":
      print("The situation is very strange even for a man wich can't remember anything and follow a note in his pocket.\nYou left the house, find a low pay job while making a Python full stack developer course to get a better one.")
      print("Game over")
    elif inside == "white":
      print("There is a nice granny inside who screams because of your entrance into her room. A neighbor calls the police who arrive extremely quickly and arrest you. When you try to explain to him about the jade monkey, the story makes you win a free vacation in Arkham Asylum.")
      print("Game over")
    elif inside == "yellow":
      print('It\'s a bathroom and there is a note in the mirror: "The jade monkey is in Mr. Burns\'s glove compartment". A nice granny screams because of you, a strange in her bathroom. A neighbor calls the police who arrive extremely quickly and arrest you. When you try to explain to him about the jade monkey, the story makes you win a free vacation in Arkham Asylum.')
      print("Game over")