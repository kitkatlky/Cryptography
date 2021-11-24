import pygame
import random

global win
lvlButton=[pygame.image.load('L1B.png'),pygame.image.load('L1A.png'),
           pygame.image.load('L2B.png'),pygame.image.load('L2A.png'),
           pygame.image.load('L3B.png'),pygame.image.load('L3A.png')]

def check(l,input):
    global win
    ans="0"
    if l==1:
        ans="3"
    elif l==2:
        ans="FYYFHP"
    elif l==3 :
        ans="castle"
    elif l==4:
        ans="2"
    elif l==5:
        ans="JRTOMP"
    elif l==6:
        ans="angpow"
    elif l==7:
        ans="CRYPTO"
    elif l==8:
        ans="THIEZCSIVB"
    elif l==9:
        ans="technology"
    elif l==10:
        ans="4"
    elif l==11:
        ans="MICPHISOACMLSESNOID"
    elif l==12:
        ans="iloveyou"
    elif l==13:
        ans="42718356"
    elif l==14:
        ans="HITEEUYORRHNTEU!AY!D"
    elif l==15:
        ans="iamjamesbond"

    checking=True
    while checking:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                checking = False
                quitGame(check,l,input)

        pygame.draw.rect(win, (255, 255, 125), (100, 100, 600, 400))
        solve = pygame.image.load("SOLVED.png")
        win.blit(solve, (200, 170))
        font7 = pygame.font.SysFont("High Tower Text", 50, False, True)
        if input==ans:
            checkText_1 = font7.render('Congratulation!', 1, (0, 0, 0))
            checkText_2 = font7.render('You answered it correctly!', 1, (0, 0, 0))
            win.blit(checkText_1, (180, 390))
            win.blit(checkText_2, (150, 120))
        else:
            checkText_1 = font7.render('Opps, your answer is wrong. ', 1, (0, 0, 0))
            checkText_2 = font7.render(' Try again!', 1, (0, 0, 0))
            win.blit(checkText_1, (130, 110))
            win.blit(checkText_2, (240, 390))

        mouse_4 = pygame.mouse.get_pos()
        click_4 = pygame.mouse.get_pressed()
        if 500 + 150 > mouse_4[0] > 500 and 350 + 100 > mouse_4[1] > 350:
            pygame.draw.rect(win, (0, 255, 0), (500, 350, 150, 100))
            if click_4[0]==1:
                checking=False
                if input==ans:
                    gameLoop(l+1)
                else:
                    gameLoop(l)
        else:
            pygame.draw.rect(win, (255, 0, 0), (500, 350, 150, 100))
        okText=font7.render(' OK', 1, (0, 0, 0))
        win.blit(okText, (525,380))

        pygame.display.flip()

def endGame():
    global win
    music("Detective Conan Soundtrack 1.mp3")
    end=True
    while end:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False
                quitGame(endGame)
        win.fill((255, 255, 125))
        final = pygame.image.load("FIN.png")
        win.blit(final, (150, 90))
        font8 = pygame.font.SysFont("High Tower Text", 90, False, True)
        winText = font8.render('YOU WIN', 1, (0, 0, 0))
        font9 = pygame.font.SysFont("Tahoma", 70, False, True)
        again = font9.render('PLAY AGAIN ?', 1, (0, 0, 0))
        win.blit(winText, (200, 10))
        win.blit(again, (190, 320))

        mouse_5 = pygame.mouse.get_pos()
        click_5 = pygame.mouse.get_pressed()

        font2 = pygame.font.SysFont("Tahoma", 80, False, True)
        if 100 + 250 > mouse_5[0] > 100 and 445 + 100 > mouse_5[1] > 445:
            pygame.draw.rect(win, (0, 255, 0), (100, 445, 250, 100))
            if click_5[0] == 1:
                end = False
                chooseLVL()
        else:
            pygame.draw.rect(win, (0, 100, 0), (100, 445, 250, 100))
        yes_txt = font2.render('YES', 1, (0, 0, 0))
        win.blit(yes_txt, (145, 440))

        if 450 + 250 > mouse_5[0] > 450 and 445 + 100 > mouse_5[1] > 445:
            pygame.draw.rect(win, (255, 0, 0), (450, 445, 250, 100))
            if click_5[0] == 1:
                end=False
                game()
        else:
            pygame.draw.rect(win, (100, 0, 0), (450, 445, 250, 100))
        no_txt = font2.render('NO', 1, (0, 0, 0))
        win.blit(no_txt, (515, 440))

        pygame.display.flip()

def gameLoop(i):
    global win
    run=True
    user=False
    user_text=""
    randommusic()

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                quitGame(gameLoop,i)
            elif event.type == pygame.KEYDOWN:
                if user and len(user_text) < 21:
                    if event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        win.fill((25,25,112))
        font6 = pygame.font.SysFont('Comic Sans MS', 40)
        mouse_3 = pygame.mouse.get_pos()
        click_3 = pygame.mouse.get_pressed()
        if i==1:
            win.blit(pygame.image.load('caesar.png'), (25, 30))
            info1_1 = font6.render('Based on table above, determine the ', 1, (255, 255, 255))
            info1_2 = font6.render('key of Ceasar Cipher. ', 1, (255, 255, 255))
            info1_3 = font6.render('(Hint : value 0-25.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 210)))
            win.blit(info1_2,((30,270)))
            win.blit(info1_3, ((30, 330)))

        elif i==2:
            win.blit(pygame.image.load('caesarOri.png'), (25, 30))
            info1_1 = font6.render('Encrypt message m = \'attack\' by using', 1, (255, 255, 255))
            info1_2 = font6.render('Caesar Cipher with e = 5. ', 1, (255, 255, 255))
            info1_3 = font6.render('(Hint : write in Caps Lock.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 250)))
            win.blit(info1_2, ((30, 310)))
            win.blit(info1_3, ((30, 370)))

        elif i==3:
            win.blit(pygame.image.load('caesarOri.png'), (25, 30))
            info1_1 = font6.render('Decrypt message C = \'JHZASL\' by using ', 1, (255, 255, 255))
            info1_2 = font6.render('Caesar Cipher with d = 7. ', 1, (255, 255, 255))
            info1_3 = font6.render('(Hint : remember unlock Caps Lock.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 250)))
            win.blit(info1_2, ((30, 310)))
            win.blit(info1_3, ((30, 370)))

        elif i==4:
            win.blit(pygame.image.load('affine.png'), (25, 30))
            info1_1 = font6.render('Based on table above, determine the ', 1, (255, 255, 255))
            info1_2 = font6.render('value of \u03B2 of Affine Cipher, given that ', 1, (255, 255, 255))
            info1_3 = font6.render(' \u03B1 = 9. (Hint : value 0-25.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 210)))
            win.blit(info1_2, ((30, 270)))
            win.blit(info1_3, ((30, 330)))

        elif i==5:
            win.blit(pygame.image.load('affineOri.png'), (25, 30))
            info1_1 = font6.render('Encrypt message m = \'simple\' by using ', 1, (255, 255, 255))
            info1_2 = font6.render('Affine Cipher with \u03B1 = 7 and \u03B2 = 13. ', 1, (255, 255, 255))
            info1_3 = font6.render('(Hint : write in Caps Lock.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 240)))
            win.blit(info1_2, ((30, 300)))
            win.blit(info1_3, ((30, 370)))

        elif i==6:
            win.blit(pygame.image.load('affineOri.png'), (25, 30))
            info1_1 = font6.render('Decrypt message C = \'HUVQFP\' by using ', 1, (255, 255, 255))
            info1_2 = font6.render('Affine Cipher with \u03B1 = 37 and \u03B2 = 7. ', 1, (255, 255, 255))
            info1_3 = font6.render('(Hint : remember unlock Caps Lock.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 240)))
            win.blit(info1_2, ((30, 300)))
            win.blit(info1_3, ((30, 370)))

        elif i==7:
            win.blit(pygame.image.load('vigenere.png'), (25, 30))
            info1_1 = font6.render('Table above show a text encrypt by ', 1, (255, 255, 255))
            info1_2 = font6.render('using Vigenere Cipher. Determine the ', 1, (255, 255, 255))
            info1_3 = font6.render('key used. (Hint : a 6 letter word.)', 1, (255, 255, 255))
            info1_4 = font6.render('(Hint : write in Caps Lock.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 180)))
            win.blit(info1_2, ((30, 240)))
            win.blit(info1_3, ((30, 300)))
            win.blit(info1_4, ((30, 360)))

        elif i==8:
            info1_1 = font6.render('Sophia want to send a secret message', 1, (255, 255, 255))
            info1_2 = font6.render('m = \'strawberry\' to Isabella. They ', 1, (255, 255, 255))
            info1_3 = font6.render('agree to use the Vigenere Cipher with ', 1, (255, 255, 255))
            info1_4 = font6.render('secret key e = d = BORED. What should ', 1, (255, 255, 255))
            info1_5 = font6.render('Sophia send to Isabella? ', 1, (255, 255, 255))
            info1_6 = font6.render('(Hint : write in Caps Lock.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 30)))
            win.blit(info1_2, ((30, 90)))
            win.blit(info1_3, ((30, 150)))
            win.blit(info1_4, ((30, 210)))
            win.blit(info1_5, ((30, 270)))
            win.blit(info1_6, ((30, 330)))

        elif i==9:
            info1_1 = font6.render('Isabella recieve a secret message', 1, (255, 255, 255))
            info1_2 = font6.render('C = \'AETKUOCRNY\' from Sophia. Since ', 1, (255, 255, 255))
            info1_3 = font6.render('they agree to use the Vigenere Cipher ', 1, (255, 255, 255))
            info1_4 = font6.render('with secret key e = d = HARD , so what ', 1, (255, 255, 255))
            info1_5 = font6.render('message did Sophia send to Isabella? ', 1, (255, 255, 255))
            info1_6 = font6.render('(Hint : remember unlock Caps Lock.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 30)))
            win.blit(info1_2, ((30, 90)))
            win.blit(info1_3, ((30, 150)))
            win.blit(info1_4, ((30, 210)))
            win.blit(info1_5, ((30, 270)))
            win.blit(info1_6, ((30, 330)))

        elif i == 10:
            win.blit(pygame.image.load('rfc1.png'), (25, 30))
            info1_1 = font6.render('Based on table above, determine the ', 1, (255, 255, 255))
            info1_2 = font6.render('key of Rail Fence Cipher. ', 1, (255, 255, 255))
            info1_3 = font6.render('(Hint : value 0-20.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 240)))
            win.blit(info1_2, ((30, 300)))
            win.blit(info1_3, ((30, 360)))

        elif i == 11:
            info1_1 = font6.render('Tom wants to send a secret message', 1, (255, 255, 255))
            info1_2 = font6.render('M = \'missionaccomplished\' to Anna. Since ', 1, (255, 255, 255))
            info1_3 = font6.render('they agree to use the Rail Fence Cipher ', 1, (255, 255, 255))
            info1_4 = font6.render('with secret key k = 3, so what ', 1, (255, 255, 255))
            info1_5 = font6.render('is the ciphertext? ', 1, (255, 255, 255))
            info1_6 = font6.render('(Hint : write in Caps Lock.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 30)))
            win.blit(info1_2, ((30, 90)))
            win.blit(info1_3, ((30, 150)))
            win.blit(info1_4, ((30, 210)))
            win.blit(info1_5, ((30, 270)))
            win.blit(info1_6, ((30, 330)))

        elif i == 12:
            info1_1 = font6.render('Krystal recieve a secret message', 1, (255, 255, 255))
            info1_2 = font6.render('C = \'IOEOLVYU\' from Noah. Since ', 1, (255, 255, 255))
            info1_3 = font6.render('they agree to use the Rail Fence Cipher ', 1, (255, 255, 255))
            info1_4 = font6.render('with secret key k = 2, so what ', 1, (255, 255, 255))
            info1_5 = font6.render('message did Noah send to Krystal? ', 1, (255, 255, 255))
            info1_6 = font6.render('(Hint : remember unlock Caps Lock.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 30)))
            win.blit(info1_2, ((30, 90)))
            win.blit(info1_3, ((30, 150)))
            win.blit(info1_4, ((30, 210)))
            win.blit(info1_5, ((30, 270)))
            win.blit(info1_6, ((30, 330)))

        elif i == 13:
            win.blit(pygame.image.load('KEYED1.PNG'), (25, 30))
            info1_1 = font6.render('Based on table above, determine the ', 1, (255, 255, 255))
            info1_2 = font6.render('key of Keyed Transposition Cipher. ', 1, (255, 255, 255))
            info1_3 = font6.render('(Hint : value 1-8.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 240)))
            win.blit(info1_2, ((30, 300)))
            win.blit(info1_3, ((30, 360)))

        elif i == 14:
            info1_1 = font6.render('Black wants to send a secret message', 1, (255, 255, 255))
            info1_2 = font6.render('M = \'eitheryouruntheday!!\' to Pink. They', 1, (255, 255, 255))
            info1_3 = font6.render('agree to use the Keyed Transposition', 1, (255, 255, 255))
            info1_4 = font6.render('Cipher with secret key k = 42351,', 1, (255, 255, 255))
            info1_5 = font6.render('so what is the ciphertext? ', 1, (255, 255, 255))
            info1_6 = font6.render('(Hint : write in Caps Lock.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 30)))
            win.blit(info1_2, ((30, 90)))
            win.blit(info1_3, ((30, 150)))
            win.blit(info1_4, ((30, 210)))
            win.blit(info1_5, ((30, 270)))
            win.blit(info1_6, ((30, 330)))

        elif i == 15:
            info1_1 = font6.render('Amy recieve a secret message', 1, (255, 255, 255))
            info1_2 = font6.render('C = \'JMIAMAOBENDS\' from Mich. They', 1, (255, 255, 255))
            info1_3 = font6.render('agree to use the Keyed Transposition', 1, (255, 255, 255))
            info1_4 = font6.render('Cipher with secret key k = 431562, what', 1, (255, 255, 255))
            info1_5 = font6.render('message did Mich send to Amy? ', 1, (255, 255, 255))
            info1_6 = font6.render('(Hint : remember unlock Caps Lock.)', 1, (255, 255, 255))
            win.blit(info1_1, ((30, 30)))
            win.blit(info1_2, ((30, 90)))
            win.blit(info1_3, ((30, 150)))
            win.blit(info1_4, ((30, 210)))
            win.blit(info1_5, ((30, 270)))
            win.blit(info1_6, ((30, 330)))

        else:
            endGame()

        ans_place = font6.render('Answer : ', 1, (255, 255, 255))
        win.blit(ans_place, ((30, 445)))
        if click_3[0] == 1:
            if 220 + 400 > mouse_3[0] > 220 and 440 + 70 > mouse_3[1] > 440:
                user = True
            else:
                user = False

        if user:
            pygame.draw.rect(win, (255, 255, 255), (220, 440, 530, 70))
        else:
            pygame.draw.rect(win, (192, 192, 192), (220, 440, 530, 70))
        user_ans = font6.render(user_text, 1, (0, 0, 0))
        win.blit(user_ans, ((220, 445)))

        if 580 + 190 > mouse_3[0] > 580 and 520 + 60 > mouse_3[1] > 520:
            pygame.draw.rect(win, (255, 154, 0), (580, 520, 190, 60))
            if click_3[0] == 1:
                run=False
                check(i, user_text)
        else:
            pygame.draw.rect(win, (247, 95, 28), (580, 520, 190, 60))
        submit = font6.render(' SUBMIT ', 1, (255, 255, 255))
        win.blit(submit, ((580, 520)))

        if 10 + 65 > mouse_3[0] > 10 and 530 + 60 > mouse_3[1] > 30:
            win.blit(pygame.image.load('menuAft.png'), (10, 530))
            if click_3[0] == 1:
                run=False
                chooseLVL()
        else:
            win.blit(pygame.image.load('menuB4.png'), (10, 530))

        pygame.display.flip()

def chooseLVL():
    global win
    music("Detective Conan Soundtrack 1.mp3")
    lvl = True
    while lvl:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                lvl = False
                quitGame(chooseLVL)

        win.fill((25,25,112))
        mouse_2 = pygame.mouse.get_pos()
        click_2 = pygame.mouse.get_pressed()
        font5 = pygame.font.SysFont("mono", 40, True, True)
        if 180 > mouse_2[0] > 10 and 55 > mouse_2[1] > 5:
            txt = font5.render("<< BACK", 1, (255, 154, 0))
            if click_2[0] == 1:
                lvl=False
                game()
        else:
            txt = font5.render("<< BACK", 1, (247, 95, 28))
        win.blit(txt, (10, 0))

        win.blit(pygame.image.load('board.png'), (2, 25))

        font4 = pygame.font.SysFont('Arial', 30, True, True)
        text = font4.render(' Caesar Cipher', 1, (0, 0, 0))
        win.blit(text, ((110, 75)))

        if 110 + 150 > mouse_2[0] > 110 and 109 + 60 > mouse_2[1] > 109:
            win.blit(lvlButton[1], (110, 109))
            if click_2[0] == 1:
                lvl=False
                gameLoop(1)
        else:
            win.blit(lvlButton[0], (110, 109))

        if 320 + 150 > mouse_2[0] > 320 and 109 + 60 > mouse_2[1] > 109:
            win.blit(lvlButton[3], (320, 109))
            if click_2[0] == 1:
                lvl=False
                gameLoop(2)
        else:
            win.blit(lvlButton[2], (320, 109))

        if 530 + 150 > mouse_2[0] > 530 and 109 + 60 > mouse_2[1] > 109:
            win.blit(lvlButton[5], (530, 109))
            if click_2[0] == 1:
                lvl=False
                gameLoop(3)
        else:
            win.blit(lvlButton[4], (530, 109))

        textA = font4.render(' Affine Cipher', 1, (0, 0, 0))
        win.blit(textA, ((110, 164)))
        if 110 + 160 > mouse_2[0] > 110 and 198 + 60 > mouse_2[1] > 198:
            win.blit(lvlButton[1], (110, 198))
            if click_2[0] == 1:
                lvl = False
                gameLoop(4)
        else:
            win.blit(lvlButton[0], (110, 198))

        if 320 + 160 > mouse_2[0] > 320 and 198 + 60 > mouse_2[1] > 198:
            win.blit(lvlButton[3], (320, 198))
            if click_2[0] == 1:
                lvl = False
                gameLoop(5)
        else:
            win.blit(lvlButton[2], (320, 198))

        if 530 + 160 > mouse_2[0] > 530 and 198 + 60 > mouse_2[1] > 198:
            win.blit(lvlButton[5], (530, 198))
            if click_2[0] == 1:
                lvl = False
                gameLoop(6)
        else:
            win.blit(lvlButton[4], (530, 198))

        textV = font4.render(' Vigenere Cipher', 1, (0, 0, 0))
        win.blit(textV, ((110, 253)))
        if 110 + 160 > mouse_2[0] > 110 and 287 + 60 > mouse_2[1] > 287:
            win.blit(lvlButton[1], (110, 287))
            if click_2[0] == 1:
                lvl = False
                gameLoop(7)
        else:
            win.blit(lvlButton[0], (110, 287))

        if 320 + 160 > mouse_2[0] > 320 and 287 + 60 > mouse_2[1] > 287:
            win.blit(lvlButton[3], (320, 287))
            if click_2[0] == 1:
                lvl = False
                gameLoop(8)
        else:
            win.blit(lvlButton[2], (320, 287))

        if 530 + 160 > mouse_2[0] > 530 and 287 + 60 > mouse_2[1] > 287:
            win.blit(lvlButton[5], (530, 287))
            if click_2[0] == 1:
                lvl = False
                gameLoop(9)
        else:
            win.blit(lvlButton[4], (530, 287))

        textS = font4.render(' Keyless Transposition Cipher', 1, (0, 0, 0))
        win.blit(textS, ((110, 342)))
        if 110 + 160 > mouse_2[0] > 110 and 376 + 60 > mouse_2[1] > 376:
            win.blit(lvlButton[1], (110, 376))
            if click_2[0] == 1:
                lvl = False
                gameLoop(10)
        else:
            win.blit(lvlButton[0], (110, 376))

        if 320 + 160 > mouse_2[0] > 320 and 376 + 60 > mouse_2[1] > 376:
            win.blit(lvlButton[3], (320, 376))
            if click_2[0] == 1:
                lvl = False
                gameLoop(11)
        else:
            win.blit(lvlButton[2], (320, 376))

        if 530 + 160 > mouse_2[0] > 530 and 376 + 60 > mouse_2[1] > 376:
            win.blit(lvlButton[5], (530, 376))
            if click_2[0] == 1:
                lvl = False
                gameLoop(12)
        else:
            win.blit(lvlButton[4], (530, 376))

        textK = font4.render(' Keyed Transpositon Cipher', 1, (0, 0, 0))
        win.blit(textK, ((110, 431)))
        if 110 + 160 > mouse_2[0] > 110 and 465 + 60 > mouse_2[1] > 465:
            win.blit(lvlButton[1], (110, 465))
            if click_2[0] == 1:
                lvl = False
                gameLoop(13)
        else:
            win.blit(lvlButton[0], (110, 465))

        if 320 + 160 > mouse_2[0] > 320 and 465 + 60 > mouse_2[1] > 465:
            win.blit(lvlButton[3], (320, 465))
            if click_2[0] == 1:
                lvl = False
                gameLoop(14)
        else:
            win.blit(lvlButton[2], (320, 465))

        if 530 + 160 > mouse_2[0] > 530 and 465 + 60 > mouse_2[1] > 465:
            win.blit(lvlButton[5], (530, 465))
            if click_2[0] == 1:
                lvl = False
                gameLoop(15)
        else:
            win.blit(lvlButton[4], (530, 465))

        pygame.display.flip()

def quitGame(action,num=None,user=None):
    music("DETECTIVE CONAN - ORIGINAL SOUNDTRACK 009.mp3")
    stop=True
    while stop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                stop = False
                quitGame(quitGame)

        pygame.draw.rect(win, (255, 255, 125), (100, 100, 600, 400))
        ran = pygame.image.load("RRAN.png")
        win.blit(ran, (200, 170))
        font3 = pygame.font.SysFont("Kristen ITC", 42, False, True)
        quitStatement_1 = font3.render('Do you really want to quit?', 1, (0, 0, 0))
        win.blit(quitStatement_1, (130, 120))
        mouse_1 = pygame.mouse.get_pos()
        click_1 = pygame.mouse.get_pressed()

        if 130 + 250 > mouse_1[0] > 130 and 365 + 100 > mouse_1[1] > 365:
            pygame.draw.rect(win, (0, 255, 0), (130, 365, 250, 100))
            if click_1[0] == 1:
                stop = False
                pygame.quit()
                quit()
        else:
            pygame.draw.rect(win, (0, 100, 0), (130, 365, 250, 100))
        yes_txt = font3.render('YES', 1, (0, 0, 0))
        win.blit(yes_txt, (200, 390))

        if 420 + 250 > mouse_1[0] > 420 and 365 + 100 > mouse_1[1] > 365:
            pygame.draw.rect(win, (255, 0, 0), (420, 365, 250, 100))
            if click_1[0] == 1:
                stop = False
                if num!=None and user!=None:
                    action(num,user)
                elif num!=None and user==None:
                    action(num)
                else:
                    action()
        else:
            pygame.draw.rect(win, (100, 0, 0), (420, 365, 250, 100))
        no_txt = font3.render('NO', 1, (0, 0, 0))
        win.blit(no_txt, (500, 390))

        pygame.display.flip()

def music(namem):
    pygame.mixer.music.load(namem)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1.0)

def randommusic():
    L = ['DETECTIVE CONAN - ORIGINAL SOUNDTRACK 012.mp3', 'DETECTIVE CONAN - ORIGINAL SOUNDTRACK 005.mp3', 'DETECTIVE CONAN - ORIGINAL SOUNDTRACK 007.mp3']
    filename = random.choice(L)
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(1.0)

def game():
    global win
    pygame.init()
    win = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("MINI GAME")
    background = pygame.image.load("CONAN.png")
    music("Detective Conan Soundtrack 1.mp3")

    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False
                quitGame(game)

        win.blit(background, (0,0))
        font1 = pygame.font.SysFont("Algerian", 95, False, True)
        title = font1.render('CRYPTOGRAPHY', 1, (255, 255, 255))
        title_1 = font1.render('GAME', 1, (255, 255, 255))
        win.blit(title, (45, 10))
        win.blit(title_1, (270, 80))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        font2 = pygame.font.SysFont("Tahoma", 80, False, True)
        if 50 + 250 > mouse[0] > 50 and 450 + 100 > mouse[1] > 450:
            pygame.draw.rect(win, (0, 255, 0), (50, 450, 250, 100))
            if click[0] == 1:
                intro=False
                chooseLVL()
        else:
            pygame.draw.rect(win, (0, 100, 0), (50, 450, 250, 100))
        txt = font2.render('PLAY', 1, (0, 0, 0))
        win.blit(txt, (90, 450))

        if 500 + 250 > mouse[0] > 500 and 450 + 100 > mouse[1] > 450:
            pygame.draw.rect(win, (255, 0, 0), (480, 450, 250, 100))
            if click[0] == 1:
                intro=False
                quitGame(game)
        else:
            pygame.draw.rect(win, (100, 0, 0), (480, 450, 250, 100))
        q_txt = font2.render('QUIT', 1, (0, 0, 0))
        win.blit(q_txt, (510, 450))

        pygame.display.flip()

game()
