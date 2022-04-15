print('Welcome to my Computer Quiz!')
playing = input("Do you want to play? ")
if playing.lower() != 'yes':
    quit()
else:
    print('Okay! Lets play :)\n')
    print('You will be asked with some sequence of questions, which are based on general knowledge\n')
    print('You can do this!')
score = 0
answer = input('What does CPU stand for? ')
if answer.lower()=='central processing unit':
        print('Correct!')
        score += 1
else:
 print('Incorrect!')
answer = input('What is Zumba? ')
if answer.lower()=='a dance workout':
  print('Correct!')
  score += 1
else:
 print('Incorrect!')
answer = input('Is the temperature of the moon higher or lower during the day? ')
if answer.lower()=='higher':
          print('Correct!')
          score += 1
else:
 print('Incorrect!')
answer = input('which planet is the smallest:Neptune,Mara,Mercury? ')
if answer.lower()=='mercury':
        print('Correct!')
        score += 1
else:
 print('Incorrect!')
answer = input('What is the square root of 144? ')
if answer.lower()=='12':
         print('Correct!')
         score += 1
else:
 print('Incorrect!')
answer = input('Who is the father of AI? ')
if answer.lower()=='John McCarthy':
        print('Correct!')
        score += 1
else:
 print('Incorrect!')
answer = input('In what year AI come into existence? ')
if answer.lower()=='1960':
        print('Correct!')
        score += 1
else:
 print('Incorrect!')
answer = input('What does AI stand for? ')
if answer.lower()=='artificial intelligence':
        print('Correct!')
        score += 1
else:
 print('Incorrect!')
answer = input('What is the another word of lexicon? ')
if answer.lower()=='dictionary':
        print('Correct!')
        score += 1
else:
    print('Incorrect!')
answer = input('Which is the biggest word in english? ')
if answer.lower()=='supercalifragilisticexpialidocious':
        print('Correct!')
        score += 1
else:
    print('Incorrect!')
answer = input('Which one is the fully supported 64 bit operating system? ')
if answer.lower()=='linux':
        print('Correct!')
        score += 1
else:
    print('Incorrect!')
answer = input('Which protocol is used to send e-mail? ')
if answer.lower()=='SMTP':
        print('Correct!')
        score += 1
else:
    print('Incorrect!')
answer = input('Which computer program converts assembly language to machine language ? ')
if answer.lower()=='assembler':
        print('Correct!')
        score += 1
else:
    print('Incorrect!')

print('You got '+str(score)+' questions correct!')
print('You got '+str((score/13)*100)+'%')



