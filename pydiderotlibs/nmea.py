import tkinter as Tk
import tkinter.filedialog as tkf
import pynmeagps
import datetime
from .chaines import fich2chaine

#dans nmea2csv, revoir l'affichage du texte "vous n'avez pas précisé de fichier..."
#dans nmea2csv, revoir l'endroit où entree etst recherché par défaut
#et l'endroit où le csv est sauvegardé (plus voir comment être sûr que le suffixe est bien csv)

def mk_dict(msg):
    """
    Crée un dictionnaire à partir d'une trame GGA ou RMC
    Argument :
        msg (pynmeagps.nmeamessage.NMEAMessage) : trame NMEA de type GGA ou RMC
    """
    msg2={"latitude":msg.lat, "longitude":msg.lon}
    if msg.msgID == 'GGA':
        msg2["altitude"]=msg.alt
        msg2["num_sats"]=msg.numSV
        msg2["horizontal_dil"]=msg.HDOP
    if msg.msgID == 'RMC':
        msg2["speed"]=pynmeagps.nmeahelpers.knots2spd(msg.spd, 'KMPH') 
        msg2["true_course"]=msg.cog
    return(msg2)

def mk_list(msg,origin = None):
    """
    Crée une liste à partir d'une trame GGA ou RMC.
    La liste contient les éléments suivants :
    [type, date, time, nombre de secondes depuis origin, lat, lon, alt, speed, num_sats, horiz_dil, true_course]
    Argument :
        msg (pynmeagps.nmeamessage.NMEAMessage) : trame NMEA de type GGA ou RMC
        origin (datetime.date) : optionnel. S'il est présent, le 4 élément de la liste (d'index 3) contient le nombre de secondes depuis origin. S'il n'est pas précisé (égal à None), cet élément est vide.
    """
    typ, date, time, chrono, lat, lon, alt, speed, num_sats, horiz_dil, true_course=['']*11
    typ,time,lat,lon = msg.msgID,msg.time,msg.lat,msg.lon
    if typ == 'GGA':
        alt=msg.alt
        num_sats=msg.numSV
        horiz_dil=msg.HDOP
    if msg.msgID == 'RMC':
        speed=pynmeagps.nmeahelpers.knots2spd(msg.spd, 'KMPH') 
        true_course=msg.cog
        date=msg.date
    if origin != None:
        if date == '':
            date2 = origin.date()
        else:
            date2 = date
            date = date.strftime("%d %B %Y")
        t = datetime.datetime.combine(date2, time)-origin #t est la durée entre origin et msg.timestamp
        chrono = t.total_seconds() #s est le nombre de secondes depuis le début de la trame NMEA
    return([typ, date, time.strftime("%H : %M : %S.%f"), str(chrono), str(lat), str(lon), str(alt), str(speed), str(num_sats), str(horiz_dil), str(true_course)])



def nmea_timedata(datatype,fichier='optionnel'):
    """
    Retourne une liste de coordonnées de points extraits du fichier ``fichier``.

    Si aucun fichier n'est précisé, ouvre une boite de dialogue pour le choisir.
    Le fichier doit contenir à chaque ligne une trame nmea (obtenue grâce à une puce GPS
    et à un outil comme par exemple "nmeatools" pour Android).
    Les abscisses des points sont les horaires (comptés en secondes à compter de l'horaire de la première trame nmea du fichier).
    Les ordonnées sont les données du type "datatype" correspondantes.

    Arguments:
        datatype : Un type de donnée (numérique) contenue dans les trames nmea. Voici la liste des types de données reconnues :
        - latitude
        - longitude
        - altitude
        - speed (vitesse)
        - true_course (cap)
        - num_sats (number of satellites)
        - horizontal_dil (horizontal dilution)
        
        fichier (file,optionnel): Le nom complet (avec le chemin) d'un fichier contenant des trames nmea.
    """
    ch = fich2chaine(fichier)
    liste = []
    typ = []
    origin = None
    if datatype in ['latitude','longitude','altitude','num_sats','horizontal_dil']:
        typ+=['GGA']
    if datatype in ['latitude','longitude','speed','true_course']:
        typ+=['RMC']
    excep=0
    for line in ch.split("\n"):
        try:
            msg = pynmeagps.NMEAReader.parse(line)
            if msg.msgID == 'RMC' and origin == None:
                origin = datetime.datetime.combine(msg.date, msg.time) #origin est le premier horaire, à la date du relevé nmea
                d=msg.date
            if msg.msgID in typ and origin != None:
                msg2 = mk_dict(msg)
                if msg.msgID == 'RMC':
                    d=msg.date
                t=msg.time
                t = datetime.datetime.combine(d, t)-origin #t est la durée entre origin et msg.timestamp
                s = t.total_seconds() #s est le nombre de secondes depuis le début de la trame NMEA
                liste+=[(s,float(msg2.get(datatype)))]
        except Exception as e:
            excep=1
    if excep==1:
        print('Error while parsing.')
    return(liste)


def nmea2csv(entree='optionnel', fichier='optionnel'):
    """
    Enregistre sous le nom ``fichier`` le contenu reformaté des trames nmea contenues dans le fichier ``entree``.

    Si entree et/ou fichier n'est pas précisé, ouvre une boite de dialogue pour le sélectionner.

    Arguments:
        entree (file, otionnel): Le nom complet (avec le chemin) d'un fichier contenant des trames nmea au format texte brut.
        fichier (file, optionnel): Le nom complet (avec le chemin) d'un fichier au format csv.
    """
    if entree == 'optionnel':
        fen = Tk.Tk()
        tex1 = Tk.Label(fen, text='Vous n''avez pas précisé de fichier contenant les trames nmea')
        tex1.pack()
        fich = tkf.askopenfilename(initialdir=".",title="Choisissez un fichier",filetypes=(("text","*.txt"),("all files", "*.*"))) 
        try:
            fen.destroy()
        except BaseException:
            pass
        if fich is not None:
            entree = fich
    if fichier == 'optionnel':
        fen = Tk.Tk()
        tex1 = Tk.Label(fen, text='Vous n''avez pas précisé de fichier pour l''enregistrement au format csv')
        tex1.pack()
        fich = tkf.asksaveasfile(
            parent=fen,
            mode='w',
            title="Choisissez un fichier")
        try:
            fen.destroy()
        except BaseException:
            pass
        if fich is not None:
            fichier = fich.name
    if entree != 'optionnel':
        ch = fich2chaine(entree)
        if fichier != 'optionnel':
            filout = open(fichier, 'w')
            intitules = "'type', 'date', 'heure', 'chrono (s)', 'latitude (° décimaux)', 'longitude (° décimaux)', 'altitude (m)', 'vitesse (km/h)', 'num_sats', 'horizontal dilution of precision (m)', 'cap vrai (°)'"
            intitules = intitules.replace('\'','\"')
            filout.write(intitules)
            excep = 0
            origin = None
            for line in ch.split("\n"):
                try:
                    msg = pynmeagps.NMEAReader.parse(line)
                    if msg.msgID == 'RMC' and origin == None:
                        origin = datetime.datetime.combine(msg.date, msg.time) #origin est le premier horaire, à la date du relevé nmea
                    msg2 = mk_list(msg,origin)
                    msg2 = str(msg2).replace('[','')
                    msg2 = msg2.replace(']','\n')
                    msg2 = msg2.replace('.', ',')
                    msg2 = msg2.replace('\'', '\"')
                    filout.write(msg2)
                except Exception as e:
                    excep=1
            if excep==1:
                print('Error while parsing.')
            filout.close()
            return True
        else:
            return False
    else:
        return False
