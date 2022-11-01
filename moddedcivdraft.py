from multiprocessing.reduction import duplicate
import random
#randomizes a number to represent each civ
def randomciv():
    #num of civs=   
    numberofcivs=random.randrange(1, 182)   
    return numberofcivs

#starts by checking how many players there are and how many civs each want
#everyone gets the same amount of civs, as are the rules of civ draft
numinputmode=True
while numinputmode:
    numofplayers=int(input("how many players? (max 12): "))
    numofcivs=int(input("how many civs/player?(max 3): "))
    #checks the inputs follows the rules of draft
    if numofcivs <= 3 and numofcivs > 0 and numofplayers <= 12 and numofplayers > 0:
        numinputmode=False
    else:
        print("incorrect range")
#creates an empty output list
draftlist=[]
#a for loop for each player
for x in range(numofplayers):
    playerchoices=[]
    civnumlist=[]
    #a for loop for each player
    for y in range(numofcivs):
        civnum=randomciv()
        civnumlist.append(civnum)
        duplicatecheckmode=True
        while duplicatecheckmode:
            if civnum in civnumlist:
                civnum=randomciv()
            else:
                duplicatecheckmode=False
        match civnum:
            #here are the civs. (one could optimize the code with a database or an array)
            case 1:
                playerchoices.append("Choice " + str(y+1) + ": Adolf Hitler's Germany")
            case 2:
                playerchoices.append("Choice " + str(y+1) + ": Afonso I's Portugal")
            case 3:
                playerchoices.append("Choice " + str(y+1) + ": Afonso I's Kongo")
            case 4:
                playerchoices.append("Choice " + str(y+1) + ": Ahmad Al-Mansur's Morocco")
            case 5:
                playerchoices.append("Choice " + str(y+1) + ": Ahmad Shah Durrani's Afghanistan")
            case 6:
                playerchoices.append("Choice " + str(y+1) + ": Akhenaten's Egypt")    
            case 7:
                playerchoices.append("Choice " + str(y+1) + ": Albert I's Monaco")
            case 8:
                playerchoices.append("Choice " + str(y+1) + ": Aleksandr Nevsky's Novgorod")
            case 9:
                playerchoices.append("Choice " + str(y+1) + ": Alexander's Greece")
            case 10:
                playerchoices.append("Choice " + str(y+1) + ": Alexander I's Russia")
            case 11:
                playerchoices.append("Choice " + str(y+1) + ": Alexios I's Byzantium")
            case 12:
                playerchoices.append("Choice " + str(y+1) + ": Alfred's Anglo-Saxons")
            case 13:
                playerchoices.append("Choice " + str(y+1) + ": Alfredo Stroessner's Paraguay")
            case 14:
                playerchoices.append("Choice " + str(y+1) + ": Arminius's Germans")
            case 15:
                playerchoices.append("Choice " + str(y+1) + ": Ashurbanipal's Assyria")
            case 16:
                playerchoices.append("Choice " + str(y+1) + ": Askia's Songhai")
            case 17:
                playerchoices.append("Choice " + str(y+1) + ": Attila's Huns")
            case 18:
                playerchoices.append("Choice " + str(y+1) + ": Augustus Ceasar's Rome")
            case 19:
                playerchoices.append("Choice " + str(y+1) + ": Benito Mussolini's Italy")
            case 20:
                playerchoices.append("Choice " + str(y+1) + ": Bill Clinton's America")
            case 21: 
                playerchoices.append("Choice " + str(y+1) + ": Bogd Gegeen's Great Mongolia")
            case 22:
                playerchoices.append("Choice " + str(y+1) + ": Bokassa I's Central Africa")
            case 23:
                playerchoices.append("Choice " + str(y+1) + ": Boudicca's Celts")
            case 24:
                playerchoices.append("Choice " + str(y+1) + ": Brian Boru's Ireland")
            case 25:
                playerchoices.append("Choice " + str(y+1) + ": Brighan Young's Deseret")
            case 26:
                playerchoices.append("Choice " + str(y+1) + ": Bulan's Khazaria")
            case 27:
                playerchoices.append("Choice " + str(y+1) + ": Cakobau's Fiji")
            case 28:
                playerchoices.append("Choice " + str(y+1) + ": Canute's Anglo-Norse")
            case 29:
                playerchoices.append("Choice " + str(y+1) + ": Caracalla's Rome")  
            case 30:
                playerchoices.append("Choice " + str(y+1) + ": Carlos I's Portugal")
            case 31:
                playerchoices.append("Choice " + str(y+1) + ": Casimir III's Poland")                
            case 32:
                playerchoices.append("Choice " + str(y+1) + ": Catherine's Russia")
            case 33:
                playerchoices.append("Choice " + str(y+1) + ": Charlemange's Francia")
            case 34:
                playerchoices.append("Choice " + str(y+1) + ": Charles De Gaulle's France")
            case 35:
                playerchoices.append("Choice " + str(y+1) + ": Charles V's Holy Rome")
            case 36:
                playerchoices.append("Choice " + str(y+1) + ": Christian IV's Denmark-Norway")
            case 37:
                playerchoices.append("Choice " + str(y+1) + ": Christian X's Denmark")
            case 38:
                playerchoices.append("Choice " + str(y+1) + ": Cixi's Great Qing")
            case 39:
                playerchoices.append("Choice " + str(y+1) + ": Clemenceau's France")
            case 40:
                playerchoices.append("Choice " + str(y+1) + ": Constantine's Rome")
            case 41:
                playerchoices.append("Choice " + str(y+1) + ": Darius I's Persia")
            case 42:
                playerchoices.append("Choice " + str(y+1) + ": Dido's Carthage")
            case 43:
                playerchoices.append("Choice " + str(y+1) + ": Djoser's Egypt")
            case 44:
                playerchoices.append("Choice " + str(y+1) + ": Eleanor's Aquitaine")
            case 45:
                playerchoices.append("Choice " + str(y+1) + ": Elisabeth's Russia")
            case 46:
                playerchoices.append("Choice " + str(y+1) + ": Elizabeth's England")
            case 47:
                playerchoices.append("Choice " + str(y+1) + ": Elizabeth Bathory's Royal Hungary")
            case 48:
                playerchoices.append("Choice " + str(y+1) + ": Elizabeth II's Great Britan")
            case 49:
                playerchoices.append("Choice " + str(y+1) + ": Enrico Dandolo's Venice")
            case 50:          
                playerchoices.append("Choice " + str(y+1) + ": Eri's Nri")
            case 51:          
                playerchoices.append("Choice " + str(y+1) + ": Erik's Swedes")
            case 52:          
                playerchoices.append("Choice " + str(y+1) + ": Ernest Augustus's Hanover")
            case 53:          
                playerchoices.append("Choice " + str(y+1) + ": Fa Ngum's Laos")
            case 54:          
                playerchoices.append("Choice " + str(y+1) + ": Ferdinand I's León")
            case 55:          
                playerchoices.append("Choice " + str(y+1) + ": Ferdinand I's Two Sicilies")
            case 56:          
                playerchoices.append("Choice " + str(y+1) + ": Francis II's Holy Rome")   
            case 57:          
                playerchoices.append("Choice " + str(y+1) + ": Franklin Roosevelt's America")
            case 58:          
                playerchoices.append("Choice " + str(y+1) + ": Frederick Augustus I's Saxony")
            case 59:          
                playerchoices.append("Choice " + str(y+1) + ": Frederick II's Prussia")
            case 60:          
                playerchoices.append("Choice " + str(y+1) + ": Gajah Mada's Indonesia")
            case 61:          
                playerchoices.append("Choice " + str(y+1) + ": Gandhi's India")
            case 62:
                playerchoices.append("Choice " + str(y+1) + ": Gedimina's Lithuania")
            case 63:
                playerchoices.append("Choice " + str(y+1) + ": Genghis Khan's Mongolia")
            case 64:
                playerchoices.append("Choice " + str(y+1) + ": George V's United Kingdom")
            case 65:
                playerchoices.append("Choice " + str(y+1) + ": George Washington's America")
            case 66:
                playerchoices.append("Choice " + str(y+1) + ": Gian Galeazzo's Milan")
            case 67:
                playerchoices.append("Choice " + str(y+1) + ": Gustavus Adolphus's Sweden")
            case 68:
                playerchoices.append("Choice " + str(y+1) + ": Haakan IV's Norway")
            case 69:
                playerchoices.append("Choice " + str(y+1) + ": Haakan VII's Norway")
            case 70:
                playerchoices.append("Choice " + str(y+1) + ": Haile Selassie's Ethiopia")
            case 71:
                playerchoices.append("Choice " + str(y+1) + ": Hammurabi's Babylon")
            case 72:
                playerchoices.append("Choice " + str(y+1) + ": Hannibal's Carthage")
            case 73:
                playerchoices.append("Choice " + str(y+1) + ": Harald Bluetooth's Denmark")
            case 74:
                playerchoices.append("Choice " + str(y+1) + ": Harun Al-Rashid's Arabia")
            case 75:
                playerchoices.append("Choice " + str(y+1) + ": Hatshepsut's Egypt")
            case 76:
                playerchoices.append("Choice " + str(y+1) + ": Henri Dufaur's Switzerland")
            case 77:
                playerchoices.append("Choice " + str(y+1) + ": Henry V's England")
            case 78:
                playerchoices.append("Choice " + str(y+1) + ": Henry VIII's England")
            case 79:
                playerchoices.append("Choice " + str(y+1) + ": Hiawatha's Iroquois")
            case 80:
                playerchoices.append("Choice " + str(y+1) + ": Hideki Tojo's Japan")
            case 81:
                playerchoices.append("Choice " + str(y+1) + ": Hirohito's Japan")
            case 82:
                playerchoices.append("Choice " + str(y+1) + ": Hussein I's Jordan")
            case 83:
                playerchoices.append("Choice " + str(y+1) + ": Ingolfur Arnarson's Iceland")
            case 84:
                playerchoices.append("Choice " + str(y+1) + ": Innocent III's Papal States")
            case 85:
                playerchoices.append("Choice " + str(y+1) + ": Isabel Montezuma's Aztecs")
            case 86:
                playerchoices.append("Choice " + str(y+1) + ": Isabella's Castile")
            case 87:
                playerchoices.append("Choice " + str(y+1) + ": Ivan IV's Muscovy")
            case 88:
                playerchoices.append("Choice " + str(y+1) + ": Ivan Sirko's Zaporizhzhia")
            case 89:
                playerchoices.append("Choice " + str(y+1) + ": James VI's Scotland")
            case 90:
                playerchoices.append("Choice " + str(y+1) + ": Jean Valette's Malta")
            case 91:
                playerchoices.append("Choice " + str(y+1) + ": Jigme Dorji Wangchuck's Bhutan")
            case 92:
                playerchoices.append("Choice " + str(y+1) + ": Jimmu's Japan")
            case 93:
                playerchoices.append("Choice " + str(y+1) + ": John Paul II's Vatican City")
            case 94:
                playerchoices.append("Choice " + str(y+1) + ": Joseph II's Austria")
            case 95:
                playerchoices.append("Choice " + str(y+1) + ": Joseph Stalin's Soviet Union")
            case 96:
                playerchoices.append("Choice " + str(y+1) + ": Jozef Pilsudski's Poland")
            case 97:
                playerchoices.append("Choice " + str(y+1) + ": Julian's Rome")
            case 98:
                playerchoices.append("Choice " + str(y+1) + ": Julius Caesar's Rome")
            case 99:
                playerchoices.append("Choice " + str(y+1) + ": Justinian I's Byzantine")
            case 100:
                playerchoices.append("Choice " + str(y+1) + ": Kamehameha's Polynesia")
            case 101:
                playerchoices.append("Choice " + str(y+1) + ": Karl XII's Sweden")
            case 102:
                playerchoices.append("Choice " + str(y+1) + ": Keith Holyoake's New Zealand")
            case 103:
                playerchoices.append("Choice " + str(y+1) + ": Leopold II's Belgium")
            case 104:
                playerchoices.append("Choice " + str(y+1) + ": Lili'uokalani's Hawai'i")
            case 105:
                playerchoices.append("Choice " + str(y+1) + ": Lincoln's United States")
            case 106:
                playerchoices.append("Choice " + str(y+1) + ": Louis XIV's France")    
            case 107:
                playerchoices.append("Choice " + str(y+1) + ": Louis XVI's France")
            case 108:
                playerchoices.append("Choice " + str(y+1) + ": Ludwig II's Bavaria")
            case 109:
                playerchoices.append("Choice " + str(y+1) + ": Mackenzie King's Canada")
            case 110:
                playerchoices.append("Choice " + str(y+1) + ": Manuel I's Portugal")
            case 111:
                playerchoices.append("Choice " + str(y+1) + ": Maria I's Portugal")
            case 112:
                playerchoices.append("Choice " + str(y+1) + ": Maria Theresa's Austria")
            case 113:
                playerchoices.append("Choice " + str(y+1) + ": Maximilian I's Mexico")
            case 114:
                playerchoices.append("Choice " + str(y+1) + ": Mehmed II's Ottomans")
            case 115:
                playerchoices.append("Choice " + str(y+1) + ": Meiji's Japan")
            case 116:
                playerchoices.append("Choice " + str(y+1) + ": Menander I's Indo-Greeks")
            case 117:
                playerchoices.append("Choice " + str(y+1) + ": Mountbatten's Brittish Raj")
            case 118:
                playerchoices.append("Choice " + str(y+1) + ": Moytoy's Cherokees")
            case 119:
                playerchoices.append("Choice " + str(y+1) + ": Napoleon's France")
            case 120:
                playerchoices.append("Choice " + str(y+1) + ": Nebuchadnezzar II's Neo-Babylon")
            case 121: 
                playerchoices.append("Choice " + str(y+1) + ": Nicholas II's Russia")
            case 122:
                playerchoices.append("Choice " + str(y+1) + ": Nizam al-Mulk's Great Seljuqs")
            case 123:
                playerchoices.append("Choice " + str(y+1) + ": Nominoe's Brittany")
            case 124:
                playerchoices.append("Choice " + str(y+1) + ": Oda Nobunaga's Japan")
            case 125:
                playerchoices.append("Choice " + str(y+1) + ": Oscar II's Sweden-Norway")
            case 126:
                playerchoices.append("Choice " + str(y+1) + ": Otto von Bismarck's Germany")
            case 127:
                playerchoices.append("Choice " + str(y+1) + ": Pecal's Maya")
            case 128:
                playerchoices.append("Choice " + str(y+1) + ": Pachacuti's Inca")
            case 129:
                playerchoices.append("Choice " + str(y+1) + ": Pedro I's Brazil")  
            case 130:
                playerchoices.append("Choice " + str(y+1) + ": Pedro II's Brazil")
            case 131:
                playerchoices.append("Choice " + str(y+1) + ": Peter's Russia")                
            case 132:
                playerchoices.append("Choice " + str(y+1) + ": Peter II's Yugoslavia")
            case 133:
                playerchoices.append("Choice " + str(y+1) + ": Philip II's Spain")
            case 134:
                playerchoices.append("Choice " + str(y+1) + ": Philip III's Burgundy")
            case 135:
                playerchoices.append("Choice " + str(y+1) + ": Pius IX's Papal States")
            case 136:
                playerchoices.append("Choice " + str(y+1) + ": Pocatello's Shoshone")
            case 137:
                playerchoices.append("Choice " + str(y+1) + ": Rama V's Siam")
            case 138:
                playerchoices.append("Choice " + str(y+1) + ": Ramesses II's Egypt")
            case 139:
                playerchoices.append("Choice " + str(y+1) + ": Ramkhamhaeng's Siam")
            case 140:
                playerchoices.append("Choice " + str(y+1) + ": Ranjit Singh's Punjab")
            case 141:
                playerchoices.append("Choice " + str(y+1) + ": Richard I's England")
            case 142:
                playerchoices.append("Choice " + str(y+1) + ": Robrecht III's Flanders")
            case 143:
                playerchoices.append("Choice " + str(y+1) + ": Seddon's New Zealand")
            case 144:
                playerchoices.append("Choice " + str(y+1) + ": Sejong's Korea")
            case 145:
                playerchoices.append("Choice " + str(y+1) + ": Selim I's Ottomans")
            case 146:
                playerchoices.append("Choice " + str(y+1) + ": Shaka's Zulus")
            case 147:
                playerchoices.append("Choice " + str(y+1) + ": Shengzong's Great Liao")
            case 148:
                playerchoices.append("Choice " + str(y+1) + ": Shizong's Great Jin")
            case 149:
                playerchoices.append("Choice " + str(y+1) + ": Sigismund II's Poland-Lithuania")
            case 150:          
                playerchoices.append("Choice " + str(y+1) + ": Stefan Dusan's Serbia")
            case 151:          
                playerchoices.append("Choice " + str(y+1) + ": Stephen I's Hungary")
            case 152:          
                playerchoices.append("Choice " + str(y+1) + ": Suleiman's Ottomans")
            case 153:          
                playerchoices.append("Choice " + str(y+1) + ": Theodora's Byzantine")
            case 154:          
                playerchoices.append("Choice " + str(y+1) + ": Theodore Roosevelt's America")
            case 155:          
                playerchoices.append("Choice " + str(y+1) + ": Tiglath-Pileser III's Assyria")
            case 156:          
                playerchoices.append("Choice " + str(y+1) + ": Tigranes II's Greater Armenia")   
            case 157:          
                playerchoices.append("Choice " + str(y+1) + ": Tiridates III's Armenia")
            case 158:          
                playerchoices.append("Choice " + str(y+1) + ": Tutankhamun's Egypt")
            case 159:          
                playerchoices.append("Choice " + str(y+1) + ": Tvrtko I's Bossnia")
            case 160:          
                playerchoices.append("Choice " + str(y+1) + ": Tygyn Darkhan's Yakuts")
            case 161:          
                playerchoices.append("Choice " + str(y+1) + ": Umberto I's Italy")
            case 162:
                playerchoices.append("Choice " + str(y+1) + ": Vaclav II's Bohemia")
            case 163:
                playerchoices.append("Choice " + str(y+1) + ": Victor Emmanuel II's Sardinia-Piedmont")
            case 164:
                playerchoices.append("Choice " + str(y+1) + ": Victor Emmanuel III's Italy")
            case 165:
                playerchoices.append("Choice " + str(y+1) + ": Victoria's Great Britain")
            case 166:
                playerchoices.append("Choice " + str(y+1) + ": Vlad III Tepes' Wallachia")
            case 167:
                playerchoices.append("Choice " + str(y+1) + ": Vladimir Lenin's Soviet Russia")
            case 168:
                playerchoices.append("Choice " + str(y+1) + ": Vladimir Putin's Russia")
            case 169:
                playerchoices.append("Choice " + str(y+1) + ": Vladimir's Vsevolod")
            case 170:
                playerchoices.append("Choice " + str(y+1) + ": Walter Ulbricht's East Germany")
            case 171:
                playerchoices.append("Choice " + str(y+1) + ": Wilhelmina's Netherlands")
            case 172:
                playerchoices.append("Choice " + str(y+1) + ": William I's Netherlands")
            case 173:
                playerchoices.append("Choice " + str(y+1) + ": Winston Churchill's Great Britain")
            case 174:
                playerchoices.append("Choice " + str(y+1) + ": Wu's Han")
            case 175:
                playerchoices.append("Choice " + str(y+1) + ": Wu Zeitan's Tang")
            case 176:
                playerchoices.append("Choice " + str(y+1) + ": Yongle's Great Ming")
            case 177:
                playerchoices.append("Choice " + str(y+1) + ": Zahir Shah's Afghanistan")
            case 178:
                playerchoices.append("Choice " + str(y+1) + ": Zheng's Qin")
            case 179:
                playerchoices.append("Choice " + str(y+1) + ": William I's Normandy")
            case 180:
                playerchoices.append("Choice " + str(y+1) + ": Genseric's Vandals")
            case 181:
                playerchoices.append("Choice " + str(y+1) + ": Montezuma's Aztecs")
    print("\nPlayer "+str(x+1)+" gets the following choices:\n")
    for i in playerchoices:
        print (i)