import pynmeagps
import datetime
from .chaines import fich2chaine



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
                msg2={"latitude":msg.lat, "longitude":msg.lon}
                if msg.msgID == 'GGA':
                    msg2["altitude"]=msg.alt
                    msg2["num_sats"]=msg.numSV
                    msg2["horizontal_dil"]=msg.HDOP
                if msg.msgID == 'RMC':
                    msg2["speed"]=pynmeagps.nmeahelpers.knots2spd(msg.spd, 'KMPH') 
                    msg2["true_course"]=msg.cog
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
