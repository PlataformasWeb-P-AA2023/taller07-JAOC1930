from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# se importa la clase(s) del 
# archivo genera_tablas
from genera_tablas import Club, Jugador

# se importa información del archivo configuracion
from configuracion import cadena_base_datos
# se genera enlace al gestor de base de
# datos
# para el ejemplo se usa la base de datos
# sqlite
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


archivo = open('data/datos_clubs.txt', 'r')

listaClub = archivo.readlines()


for l in listaClub:
    li = l.split(";")
    club = Club(nombre= li[0], deporte= li[1], \
                fundacion = int(li[2][0:4]))
    
    session.add(club)


archivo2 = open('data/datos_jugadores.txt', 'r')

listaJugador = archivo2.readlines()


for l2 in listaJugador:
    li2 = l2.split(";")
    print(li2)
    club = session.query(Club).filter_by(nombre =li2[0]).one()
    jugador = Jugador(nombre =li2[3], dorsal = int(li2[2]), posicion = li2[1], club = club) 

    session.add(jugador)

archivo.close()

archivo2.close()

session.commit()
