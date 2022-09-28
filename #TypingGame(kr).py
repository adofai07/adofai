#TypingGame(kr)
from math import *
from time import time
import os
os.system("pip install pygame")
os.system("pip install keyboard")
import keyboard
import pygame
import random

words = [
    "가", "가뇨", "가니", "가니오", "가니와", "가라", "가량", 
"가마리", "가시니", "가옷", "가웃", "가웆", "가지라", "가지다",
"각", "간", "간디", "간디니", "간디니라", "간디라", "간마",
"갈", "감", "갑다", "개", "개니라", "객", "거",
"거고", "거고나", "거나", "거냐", "거녀", "거뇨", "거늘",
"거니", "거니라", "거니오", "거니와", "거니나", "거다", "거던",
"거드면", "거든", "거들랑", "거디라", "거라", "거를", "거리",
"거리다", "거마", "거사", "거스라", "거시나", "거시뇨", "거시늘",
"거시니", "거시니오", "거시니와", "거시다", "거시든", "거시", "거신",
"거신마", "거아", "거야", "거이다", "거지라", "거지다", "거징이다",
"건", "건고", "건대", "건댄", "건덴", "건마는", "건마", 
"건만", "건져", "걸랑", "걸아", "것다", "것마는", "것마",
"겄", "게", "게겐", "게끔", "게나", "게라", "게르",
"게리다", "게시리", "게아", "게야", "게노잇가", "게다", "겐",
"겟", "겠", "결", "경", "곁", "계", "고",
"고나", "고녀", "고는", "고뎌", "고도", "고라", "고라쟈",
"고려", "고말고", "고사", "고서", "고야", "고자", "고장",
"고쟈", "고저", "고져", "고졔니", "고프다", "곡", "곤",
"곤대", "곤여", "곰", "곱", "공", "곶", "과",
"과댜", "과뎌", "과라", "과소라", "과쟈", "과녜니라", "과여",
"과다", "관", "관대", "관데", "관뎌", "관듸", "광",
"괴야", "구", "구나", "구래", "구레", "구려", "구로",
"구료", "구마는", "구만", "구먼", "구면", "국", "군",
"궂다", "권", "귀", "그러", "그레", "그로", "금",
"급", "긔", "긧고", "기", "기나", "기로", "기로니",
"기로서", "기로서니", "기로선들", "기에", "기요", "길래", "까장",
"까짓", "깔", "꺼니", "꺼마", "껏", "께", "껜",
"꼬", "꼴", "꾸러기", "꾸마", "꾼", "끔", "끼",
"끼리", "나", "나기", "나뇨", "나니", "나다", "나도",
"나든", "나따나", "나라", "나마", "나새나", "나시든", "나시",
"나이까", "나이다", "나지라", "난", "남", "남동", "낭",
"내", "내기", "냐", "냐고", "냐네", "냐는", "냐니",
"냐니까", "냐며", "냐면", "냐면서", "냔", "냘", "냬",
"냬요", "냰", "너라", "너이다", "네", "녀", "년",
"노", "노니", "노니라", "노닛가", "노다", "노라", "노라고",
"노라니", "노라니까", "노라면", "노매", "노매라", "노믜라", "노소니",
"노소라", "노소다", "노쇠", "노왜라", "노이다", "노잇가", "논",
"논가", "논뎌", "논디라", "놋다", "놋도다", "놋", "농",
"농이다", "뇌", "뇌다", "뇨", "누", "누나", "누라구",
"누만", "누먼", "뉘", "느냐", "느냐고", "느냐네", "느냐는",
"느냐니", "느냐니까", "느냐며", "느냐면", "느냐면서", "느냔", "느냘",
"느냬", "느냬요", "느뇨", "느니", "느니라", "느니만", "느니만치",
"느니만큼", "느라", "느라고", "느라니", "느라니까", "느라면", "느마",
"느매", "느슨다", "는", "는가", "는감", "는강", "는걸",
"는고", "는공", "는과니", "는교", "는구나", "는구려", "는구료",
"는구마", "는구만", "는구매", "는구먼", "는구면", "는군", "는궈니",
"는다", "는다고", "는다꼬", "는다나", "는다냐", "는다네", "는다느냐",
"는다느니", "는다는", "는다니", "는다니까", "는다더라", "는다마는", "는다만",
"는다며", "는다면", "는다면서", "는다손", "는다오", "는다이", "는다지",
"는단", "는단다", "는달", "는담", "는답니까", "는답니다", "는답디까",
"는답디다", "는답시고", "는대", "는대도", "는대서", "는대서야", "는대야",
"는대요", "는댄다", "는댔자", "는데", "는뎁쇼", "는도다", "는디",
"는맥세", "는바", "는이", "는지", "는지고", "는지라", "늬라고",
"니", "니까", "니까나", "니까느루", "니까는", "니까니", "니깐",
"니꺼니", "니께니", "니껴", "니끼니", "니라", "니만치", "니만큼",
"니아", "니야", "니여", "니오", "니이껴", "니이다", "니잇가",
"니잇고", "니다", "니가", "니고", "닌댄", "님", "닛가",
"닝까", "다", "다가", "다가는", "다가며", "다가셔", "다각",
"다간", "다감", "다고", "다나", "다네", "다느냐", "다느니",
"다는", "다니", "다니까", "다니라", "다더라", "다라", "다라니",
"다랗다", "다롸", "다마는", "다마다", "다만", "다며", "다면",
"다면서", "다문", "다소니", "다소라", "다손", "다스피", "다시피",
"다오", "다요", "다우", "다이", "다지", "다다", "단",
"단다", "단디면", "단딘댄", "달", "담", "답", "답니까",
"답니다", "답다", "답디까", "답디다", "답시고", "닷", "닷다",
"당", "당께", "당께로", "당하다", "닿다", "대", "대가리",
"대끼", "대다", "대도", "대서", "대서야", "대야", "대요",
"대이다", "댁", "댄다", "댔자", "댕이", "더", "더가",
"더거", "더구나", "더구려", "더구료", "더구만", "더구먼", "더구면",
"더군", "더냐", "더냐고", "더냬", "더녀", "더뇨", "더니",
"더니라", "더니마는", "더니만", "더니이까", "더니이다", "더니다", "더니가",
"더니고", "더든", "더라", "더라고", "더라나", "더라네", "더라는",
"더라니", "더라니까", "더라도", "더라며", "더라면", "더라면서", "더라손",
"더라지", "더람", "더랍니까", "더랍니다", "더랍디까", "더랍디다", "더래",
"더래도", "더래요", "더만", "더시", "더시니", "더시니라", "더시다",
"더시든", "더신", "더신가", "더신고", "더이까", "더이다", "더다",
"던", "던가", "던감", "던걸", "던고", "던다", "던댄",
"던데", "던덴", "던들", "던디", "던바", "던지", "덜",
"덧", "데", "데기", "데끼", "데요", "덴", "뎌이고",
"도", "도고야", "도괴야", "도다", "도록", "도록애", "도롬",
"도리", "도소뇨", "도소니", "도소니야", "도소다", "도쇠", "도쇠이다",
"도여", "도이다", "돗", "돗다", "돗더", "동", "동이",
"되", "되다", "되야", "두", "두구나", "두나", "두다",
"두락", "두록", "두마는", "두셰라", "둔", "둥이", "뒈",
"드", "드구나", "드구료", "드구면", "드군", "드냐", "드니",
"드니라", "드라", "드라도", "드라면", "드래도", "드랴", "드룩",
"드리다", "드시", "드키", "득기", "든", "든가", "든걸",
"든고", "든데", "든들", "든지", "들", "들이", "듯",
"듯이", "디", "디기", "디다", "디록", "디마는", "디만",
"디시", "디옷", "디외", "디요", "디웨", "디위", "디이",
"딕기", "딱지", "땀", "때기", "떼까", "뚱", "뜨기",
"뜨리다", "라", "라고", "라구", "라나", "라네", "라느냐",
"라느니", "라는", "라니", "라니까", "라도", "라라", "라마",
"라며", "라면", "라면서", "라서", "라손", "라스라", "라야",
"라야만", "라오", "라우", "라우요", "라지", "라타", "라다",
"락", "란", "란다", "랄", "람", "랍", "랍니까",
"랍니다", "랍데", "랍디까", "랍디다", "랍시고", "랏다", "랑",
"랑근에", "랑께", "래", "래도", "래디", "래문", "래서",
"래서야", "래야", "래야만", "래요", "래이", "랜", "랬자",
"랴", "랴르", "랴마는", "러", "러니", "러니라", "러니이까",
"러니이다", "러니고", "러든", "러라", "러시니", "러시니다", "러시다",
"러시든", "러이까", "러이다", "러다", "런가", "런고", "런들",
"레", "려", "려거든", "려고", "려기에", "려나", "려네",
"려녀", "려뇨", "려느냐", "려는", "려는가", "려는고", "려는데",
"려는지", "려니", "려니오", "려니와", "려니녀", "려닛", "려다",
"려다가", "려더니", "려더라", "려던", "려던가", "려도", "려든",
"려료", "려마", "려면", "려무나", "려므나", "려서는", "려서야",
"려야", "려오", "력", "련", "련노라", "련다", "련뎌",
"련마는", "련마", "련만", "렴", "렴으나", "렴은", "렵니까",
"렵니다", "렷노라", "렷다", "령", "례니라", "롓다", "로",
"로고", "로고나", "로구나", "로구려", "로구료", "로구만", "로구먼", 
"로구면", "로군", "로니", "로다", "로되", "로라", "로새라",
"로서니", "로세", "로소니", "로소이다", "로쇠", "로외", "록",
"론", "롭다", "롯다", "롯더라", "롸", "뢰", "료",
"루", "류", "률", "르샷다", "리", "리까", "리니",
"리니라", "리다", "리라", "리라다", "리랏", "리랏다", "리러니",
"리러니라", "리러라", "리러시다", "리런댄", "리로다", "리로소냐", "리로소녀",
"리로소니", "리로소니여", "리로소다", "리로손여", "리로", "리만치", "리만큼",
"리며", "리샤다", "리아", "리야", "리어늘", "리어니", "리어니와",
"리어다", "리어며", "리어", "리언마", "리여", "리오", "리오마",
"리온", "리요마", "리우", "리이다", "리잇가", "리잇고", "리가",
"리고", "린", "린댄", "린뎌", "릴", "림", "링다",
"링이다", "링잇가", "마", "마고", "마르는", "막", "만",
"맞다", "맞이", "맡", "매", "맨", "먀", "머리",
"멍", "메", "메서란", "메선", "멘", "며", "며셔",
"면", "면서", "면셔", "명셔", "모", "모로", "몬",
"무", "문", "물", "므는", "므로", "믄", "믄서",
"미", "민", "바가지", "박이", "받다", "발", "방",
"방서", "방이", "배", "배기", "백", "뱅이", "버릇",
"범", "법", "별", "보", "복", "본", "부",
"분", "분지", "붙이", "브티", "비", "빼기", "뻘",
"사", "사오", "사오니까", "사오리까", "사오리다", "사오리이까", "사오리이다",
"사오이다", "사옵", "사옵나이까", "사옵나이다", "사옵니까", "사옵니다", "사옵디까",
"사옵디다", "사옵시", "사와", "사외다", "사이다", "사주", "사다",
"산", "살가", "살이", "삽", "상", "상이다", "새",
"새근여", "새다", "새이다", "생", "샤", "샤나", "샤도",
"샤리라", "샤다", "샨", "샨다", "샨디라", "샬", "샬뎬",
"샬딘댄", "샬뗸", "샴", "샷다", "석", "선", "설",
"성", "세", "세나", "세요", "센", "셔", "셔뇨",
"셔요", "션", "션디", "셰", "셰라", "셰야", "소",
"소니", "소니까", "소다", "소라", "소서", "소야", "소오",
"소오리까", "소옵니까", "소와요", "소웨", "소이", "소이까", "소이다",
"손", "손뎌", "솝", "송와", "쇠다", "쇼셔", "쇼",
"수", "수다", "수다레", "수와", "순", "술", "쉐",
"슈", "슈셔", "스러", "스럽다", "스레하다", "스름하다", "슨다",
"슴", "슴두", "슴둥", "슴메", "습꾸마", "습꿔니", "습나",
"습네", "습네다", "습네다레", "습늰다", "습니", "습니까", "습니다",
"습닌다", "습데", "습데게레", "습동와", "습디까", "습디다", "습디다레",
"습디여", "습딘다", "습마", "습머니", "습머이", "습메게레", "습메다",
"습메다레", "습무다", "습무다레", "습세", "습세다", "습죠", "습지요",
"시", "시거시니", "시게소", "시겨", "시곤대", "시과뎌", "시노소다",
"시논", "시놋다", "시니다", "시다", "시다다", "시단", "시단딘댄",
"시덩이다", "시도소다", "시라", "시라요", "시려뇨", "시련마", "시리",
"시리라다", "시리러뇨", "시리러라", "시리여", "시리오", "시릴", "시소",
"시압", "시어요", "시이소", "시키다", "시뇨", "시니", "시니시니라",
"시니고", "시잇고", "시가", "시고", "식", "신대", "실",
"실가", "실고", "심", "심니껴", "심더", "십니꺼", "십사",
"십시다", "십시오", "싸다", "썩", "씨", "씩", "아",
"아뇨", "아늘", "아니", "아니와", "아다", "아다가", "아도",
"아든", "아디라", "아따", "아라", "아라우", "아리아", "아리여", 
"아리가", "아마", "아서", "아셔", "아숌", "아스라", "아시나",
"아시뇨", "아시니", "아시든", "아시라", "아시리오", "아시며", "아시",
"아신", "아실", "아쎠", "아야", "아야만", "아야지", "아요",
"아웃", "아져", "아지라", "아지이다", "아지다", "아치", "악",
"안", "안게", "안다", "안마", "안에", "암", "암직",
"앗", "앗거든", "앗건마", "앗다가", "앗니", "앗이다", "앗다",
"았", "았었", "았자", "앙", "앙근", "앙근에", "앙이다",
"애"
]

def open_window(score, kpm):
    global screen, screen_size
    currentTime = time()

    pygame.init()
    Color = (0, 0, 0)
    screen = pygame.display.set_mode((screen_size*16, screen_size*9))
    done = False
    clock = pygame.time.Clock()

    idle_start = 300

    while True:
        screen.fill((0, 0, 0))
        delay = time() - currentTime
        currentTime = time()

        idle_start -= delay

        blit(f"현재 화면 크기: {screen_size}", 60, (0.5, 0.5), (255, 255, 255), False)
        blit(f"점수: {score}", 60, (0.5, 0.65), (255, 255, 255), False)
        blit("분당 입력 수: {:.1f}".format(kpm), 60, (0.5, 0.8), (255, 255, 255), False)
        blit("엔터 키를 눌러 시작!", 60, (0.5, 0.2), (255, 255, 255), False)
        blit("{:07.3f}".format(idle_start), 30, (0.1, 0.9), (255, 255, 255), True)

        if keyboard.is_pressed("up arrow"):
            key_was_pressed["up arrow"] = 1
            screen_size += 1
            break
        if keyboard.is_pressed("down arrow"):
            key_was_pressed["down arrow"] = 1
            screen_size -= 1
            break
        if keyboard.is_pressed("enter") and not key_was_pressed["enter"]:
            key_was_pressed["enter"] = 1
            startGame()

        if idle_start <= 0:
            startGame()

        if key_was_pressed["enter"] and not keyboard.is_pressed("enter"):
            key_was_pressed["enter"] = 0
    
    pygame.quit()
    open_window("", 0.0)

def blit(message, fontSize, coord, color, condition):
    font = pygame.font.SysFont('malgungothic', (screen_size*fontSize//50)) 
    text = font.render(str(message), True, color)
    textRect = text.get_rect()
    textRect.center = (int(coord[0]*screen_size*16), int(coord[1]*screen_size*9))
    screen.blit(text, textRect)
    if condition:
        pygame.display.update()

def inputIsCorrect():
    global mission, currentInput
    good = 1
    for i in range(min(len(currentInput)-1, len(mission[0]))):
        if currentInput[i+1] != mission[0][i]: good = 0
    if currentInput == "-": good = 1
    return good

def eng_to_kor(text): # 영어 문자열을 한글로 변환
    caps = ["Q", "W", "E", "R", "T", "O", "P"]
    first = {"r" : "ㄱ", "R" : "ㄲ", "s" : "ㄴ", "e" : "ㄷ", "E" : "ㄸ", "f" : "ㄹ", "a" : "ㅁ", "q" : "ㅂ", "Q" : "ㅃ", "t" : "ㅅ", "T" : "ㅆ", "d" : "ㅇ", "w" : "ㅈ", "W" : "ㅉ", "c" : "ㅊ", "z" : "ㅋ", "x" : "ㅌ", "v" : "ㅍ", "g" : "ㅎ"}
    second = {"k" : "ㅏ", "o" : "ㅐ", "i" : "ㅑ", "O" : "ㅒ", "j" : "ㅓ", "p" : "ㅔ", "u" : "ㅕ", "P" : "ㅖ", "h" : "ㅗ", "hk" : "ㅘ", "ho" : "ㅙ", "hl" : "ㅚ", "y" : "ㅛ", "n" : "ㅜ", "nj" : "ㅝ", "np" : "ㅞ", "nl" : "ㅟ", "b" : "ㅠ", "m" : "ㅡ", "ml" : "ㅢ", "l" : "ㅣ"}
    third = {"" : "", "r" : "ㄱ", "R" : "ㄲ", "rt" : "ㄳ", "s" : "ㄴ" , "sw" : "ㄵ", "sg" : "ㄶ", "e" : "ㄷ", "f" : "ㄹ", "fr" : "ㄺ", "fa" : "ㄻ", "fq" : "ㄼ", "ft" : "ㄽ", "fx" : "ㄾ", "fv" : "ㄿ", "fg" : "ㅀ", "a" : "ㅁ", "q" : "ㅂ", "qt" : "ㅄ", "t" : "ㅅ", "T" : "ㅆ", "d" : "ㅇ", "w" : "ㅈ", "c" : "ㅊ", "z" : "ㅋ", "x" : "ㅌ", "v" : "ㅍ", "g" : "ㅎ"}

    for i in range(len(text)): # 대문자 처리하기
        if text[i] not in caps:
            text = text[:i] + text[i].lower() + text[i+1:]
    
    text = list(text)

    i = -1 # 이중 모음 합치기
    while True:
        if len(text) == 0: break
        i += 1
        if i >= len(text)-1: break

        if "".join(text[i:i+2]) in list(second.keys()):
            text = text[:i] + ["".join(text[i:i+2])] + text[i+2:]
            i -= 1

    i = -1 # 쌍자음 합치기
    while True:
        if len(text) == 0: break
        i += 1
        if i >= len(text)-1: break

        if text[i] in list(first.keys()) and text[i+1] in list(first.keys()) and (i == len(text) - 2 or text[i+2] not in list(second.keys())) and "".join(text[i:i+2]) in list(third.keys()):
            text = text[:i] + ["".join(text[i:i+2])] + text[i+2:]
            i -= 1

    i = -1
    while True: # 단어 조합하기
        if len(text) == 0: break
        i += 1
        if i >= len(text) - 1: break

        # 받침이 없는 단어 조합하기
        if text[i] in list(first.keys()) and text[i+1] in list(second.keys()) and (i >= len(text) -2 or (i <= len(text) - 3 and text[i+2] not in list(first.keys()) and text[i+2] not in list(third.keys())) or (i <= len(text) - 4 and text[i+2] in list(first.keys()) and text[i+3] in list(second.keys()))):
            # print("2-character letter detected")
            text = text[:i] + [text[i:i+2] + [""]] + text[i+2:]
            i -= 1
        
        # 받침이 있는 단어 조합하기
        if i <= len(text) - 3 and text[i] in list(first.keys()) and text[i+1] in list(second.keys()) and text[i+2] in list(third.keys()) and (i >= len(text) - 3 or text[i+3] not in list(second.keys())):
            # print("3-character letter detected")
            text = text[:i] + [text[i:i+3]] + text[i+3:]

    for i in range(len(text)): # 조합된 단어를 한글로 변환하기
        if type(text[i]) == str:
            if text[i] in list(first.keys()): text[i] = first[text[i]]
            if text[i] in list(second.keys()): text[i] = second[text[i]]
            if text[i] in list(third.keys()): text[i] = third[text[i]]
        
        if type(text[i]) == list:
            text[i] = chr(588*(list(first.keys()).index(text[i][0])) + 28*(list(second.keys()).index(text[i][1])) + list(third.keys()).index(text[i][2]) + 44032)

    for i in range(text.count("`")): # "`" 제거하기 (믈ㅅ셕 같은 단어 입력용)
        text.remove("`")

    return "".join(text) # 조합된 단어를 반환하기

def kor_to_eng(text):
    first = {"r" : "ㄱ", "R" : "ㄲ", "s" : "ㄴ", "e" : "ㄷ", "E" : "ㄸ", "f" : "ㄹ", "a" : "ㅁ", "q" : "ㅂ", "Q" : "ㅃ", "t" : "ㅅ", "T" : "ㅆ", "d" : "ㅇ", "w" : "ㅈ", "W" : "ㅉ", "c" : "ㅊ", "z" : "ㅋ", "x" : "ㅌ", "v" : "ㅍ", "g" : "ㅎ"}
    second = {"k" : "ㅏ", "o" : "ㅐ", "i" : "ㅑ", "O" : "ㅒ", "j" : "ㅓ", "p" : "ㅔ", "u" : "ㅕ", "P" : "ㅖ", "h" : "ㅗ", "hk" : "ㅘ", "ho" : "ㅙ", "hl" : "ㅚ", "y" : "ㅛ", "n" : "ㅜ", "nj" : "ㅝ", "np" : "ㅞ", "nl" : "ㅟ", "b" : "ㅠ", "m" : "ㅡ", "ml" : "ㅢ", "l" : "ㅣ"}
    third = {"" : "", "r" : "ㄱ", "R" : "ㄲ", "rt" : "ㄳ", "s" : "ㄴ" , "sw" : "ㄵ", "sg" : "ㄶ", "e" : "ㄷ", "f" : "ㄹ", "fr" : "ㄺ", "fa" : "ㄻ", "fq" : "ㄼ", "ft" : "ㄽ", "fx" : "ㄾ", "fv" : "ㄿ", "fg" : "ㅀ", "a" : "ㅁ", "q" : "ㅂ", "qt" : "ㅄ", "t" : "ㅅ", "T" : "ㅆ", "d" : "ㅇ", "w" : "ㅈ", "c" : "ㅊ", "z" : "ㅋ", "x" : "ㅌ", "v" : "ㅍ", "g" : "ㅎ"}
    result = ""

    for i in range(len(text)):
        if not 44032 <= ord(text[i]) <= 55203:
            result += text[i]
            continue
        first1, second1, third1 = (ord(text[i])-44032)//588, ((ord(text[i])-44032)%588)//28, ((ord(text[i])-44032)%588)%28
        result += list(first.keys())[first1] + list(second.keys())[second1] + list(third.keys())[third1]
    return result

def startGame():
    global currentInput, mission

    screen.fill((0, 0, 0))

    gameStarted = 0
    score = 0
    gameStartTime = time()
    timeLeft = timeLimit
    gameOver = 0
    gameStartTime = time()
    typedKeys = 0
    correctlyTypedKeys = 0
    accuracy = 0

    mission = []
    currentInput = "-"

    while True:
        if gameStarted:
            delay = time() - currentTime
            currentTime = time()
            timeLeft -= delay
            elapsedTime = time() - gameStartTime
        else:
            currentTime = time()
            gameStartTime = time()

            

        for _ in range(3 - len(mission)):
            mission.append((words[random.randrange(0, len(words))]))

        for i in range(97, 123):
            if keyboard.is_pressed(chr(i)) and not key_was_pressed[chr(i)]:
                gameStarted = 1
                if keyboard.is_pressed("shift"):
                    currentInput += chr(i-32)
                else:
                    currentInput += chr(i)
                key_was_pressed[chr(i)] = 1

                typedKeys += 1
                if inputIsCorrect() : correctlyTypedKeys += 1
            
            if key_was_pressed[chr(i)] and not keyboard.is_pressed(chr(i)):
                key_was_pressed[chr(i)] = 0
        
        if keyboard.is_pressed("backspace") and not key_was_pressed["backspace"]:
            if currentInput != "-": currentInput = currentInput[:len(currentInput)-1]
            key_was_pressed["backspace"] = 1
        
        if keyboard.is_pressed("enter") and not key_was_pressed["enter"]:
            currentInput = "-"
            key_was_pressed["enter"] = 1

        
        if key_was_pressed["backspace"] and not keyboard.is_pressed("backspace"):
            key_was_pressed["backspace"] = 0
        
        if key_was_pressed["enter"] and not keyboard.is_pressed("enter"):
            key_was_pressed["enter"] = 0

        if currentInput[1:] == mission[0]:
            score += len(eng_to_kor(mission[0]))
            mission.remove(mission[0])
            currentInput = "-"
            timeLeft += bonusTime

        if timeLeft <= 0: gameOver = 1

        if gameOver: open_window(score, 60*correctlyTypedKeys/elapsedTime)

        screen.fill((0, 0, 0))
        blit((eng_to_kor(currentInput[1:]) if len(currentInput) >= 2 else "-"), 80, (0.5, 0.5), ((0, 255, 0) if inputIsCorrect() else (255, 0, 0)), False)
        blit(eng_to_kor(mission[0]), 80, (0.5, 0.25), (255, 255, 255), False)
        blit(eng_to_kor(mission[1]), 60, (0.5, 0.08), (123, 123, 123), False)
        blit("{:.3f}".format(timeLeft), 60, (0.13, 0.6), ((0, 0, 255) if timeLeft > 5 else (255, 0, 0)), False)
        blit(f"점수 : {score}", 70, (0.5, 0.85), (255, 255, 127), True)


screen_size = 79
key_was_pressed = {chr(i) : 0 for i in range(97, 123)}
for i in range(10):
    key_was_pressed[str(i)] = 0
key_was_pressed["shift"] = 0
key_was_pressed["enter"] = 0
key_was_pressed["space"] = 0
key_was_pressed["backspace"] = 0
key_was_pressed["up arrow"] = 0
key_was_pressed["down arrow"] = 0
key_was_pressed["left arrow"] = 0
key_was_pressed["right arrow"] = 0

inhibited = ["ㄱ", "ㄲ", "ㄴ", "ㄷ", "ㄸ", "ㄹ", "ㅁ", "ㅂ", "ㅃ", "ㅅ", "ㅆ", "ㅇ", "ㅈ", "ㅉ", "ㅊ", "ㅋ", "ㅌ", "ㅍ", "ㅎ"] + [str(i) for i in range(9)]

i = -1
while True:
    if len(words) == 0: break
    i += 1
    if i >= len(words): break

    for j in range(len(words[i])):
        if words[i][j] in inhibited:
            words.remove(words[i])
            break

for i in range(len(words)):
    words[i] = kor_to_eng(words[i])

print(words)

timeLimit = 30
bonusTime = 0.1
kps = 0
accuracy = 0


open_window("데이터 없음", 0.0)