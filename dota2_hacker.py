#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dota 2 Hack Tool
Creado por @ZekAtwiN12
"""

import os
import sys
import time
import random
import json
from datetime import datetime, timedelta
import threading

# Colores para la terminal
class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

# Datos realistas de Dota 2
HEROES = [
    {"nombre": "Invoker", "rol": "Intelligence", "dificultad": "Hard", "win_rate": 48.2},
    {"nombre": "Juggernaut", "rol": "Agility", "dificultad": "Easy", "win_rate": 52.1},
    {"nombre": "Crystal Maiden", "rol": "Intelligence", "dificultad": "Easy", "win_rate": 49.8},
    {"nombre": "Phantom Assassin", "rol": "Agility", "dificultad": "Medium", "win_rate": 51.3},
    {"nombre": "Lion", "rol": "Intelligence", "dificultad": "Easy", "win_rate": 50.7},
    {"nombre": "Axe", "rol": "Strength", "dificultad": "Easy", "win_rate": 53.2},
    {"nombre": "Shadow Fiend", "rol": "Agility", "dificultad": "Hard", "win_rate": 47.9},
    {"nombre": "Witch Doctor", "rol": "Intelligence", "dificultad": "Medium", "win_rate": 51.8},
    {"nombre": "Tidehunter", "rol": "Strength", "dificultad": "Medium", "win_rate": 52.5},
    {"nombre": "Lina", "rol": "Intelligence", "dificultad": "Medium", "win_rate": 50.1}
]

ITEMS = [
    {"nombre": "Blink Dagger", "tipo": "Core", "precio": 2250, "raridad": "Common"},
    {"nombre": "Black King Bar", "tipo": "Core", "precio": 4050, "raridad": "Rare"},
    {"nombre": "Aghanim's Scepter", "tipo": "Core", "precio": 4200, "raridad": "Rare"},
    {"nombre": "Heart of Tarrasque", "tipo": "Core", "precio": 5200, "raridad": "Rare"},
    {"nombre": "Butterfly", "tipo": "Core", "precio": 5525, "raridad": "Rare"},
    {"nombre": "Divine Rapier", "tipo": "Core", "precio": 5950, "raridad": "Legendary"},
    {"nombre": "Radiance", "tipo": "Core", "precio": 4700, "raridad": "Rare"},
    {"nombre": "Scythe of Vyse", "tipo": "Core", "precio": 5675, "raridad": "Rare"},
    {"nombre": "Eye of Skadi", "tipo": "Core", "precio": 5300, "raridad": "Rare"},
    {"nombre": "Bloodthorn", "tipo": "Core", "precio": 6800, "raridad": "Legendary"}
]

RANKS = [
    "Herald", "Guardian", "Crusader", "Archon", "Legend", 
    "Ancient", "Divine", "Immortal"
]

# Datos de jugadores peruanos realistas
JUGADORES_PERUANOS = [
    {
        "steam_id": "76561198123456789",
        "nickname": "ElPatoGamer",
        "nombre_real": "Carlos Mendoza",
        "edad": 24,
        "ciudad": "Lima",
        "rank": "Ancient",
        "mmr": 4250,
        "heroes_favoritos": ["Juggernaut", "Phantom Assassin", "Axe"],
        "partidas_jugadas": 2847,
        "win_rate": 52.3,
        "items_raros": ["Arcana Juggernaut", "Immortal Invoker", "Golden Butterfly"],
        "amigos": ["PeruanoPro", "LimaGaming", "DotaMasterPE"],
        "ultima_conexion": "2024-01-15 14:30:00",
        "dinero_gastado": 450.75
    },
    {
        "steam_id": "76561198987654321",
        "nickname": "PeruanoPro",
        "nombre_real": "Miguel Torres",
        "edad": 28,
        "ciudad": "Arequipa",
        "rank": "Divine",
        "mmr": 5120,
        "heroes_favoritos": ["Invoker", "Shadow Fiend", "Lina"],
        "partidas_jugadas": 3892,
        "win_rate": 54.7,
        "items_raros": ["Arcana Invoker", "Golden Shadow Fiend", "Immortal Crystal Maiden"],
        "amigos": ["ElPatoGamer", "ArequipaGaming", "ProGamerPE"],
        "ultima_conexion": "2024-01-15 16:45:00",
        "dinero_gastado": 780.50
    },
    {
        "steam_id": "76561198765432109",
        "nickname": "LimaGaming",
        "nombre_real": "Diego Rojas",
        "edad": 22,
        "ciudad": "Lima",
        "rank": "Legend",
        "mmr": 3850,
        "heroes_favoritos": ["Crystal Maiden", "Witch Doctor", "Lion"],
        "partidas_jugadas": 2156,
        "win_rate": 49.8,
        "items_raros": ["Arcana Crystal Maiden", "Immortal Witch Doctor"],
        "amigos": ["ElPatoGamer", "PeruanoPro", "SupportMain"],
        "ultima_conexion": "2024-01-15 13:20:00",
        "dinero_gastado": 320.25
    }
]

def limpiar_pantalla():
    """Limpia la pantalla de la terminal"""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_banner():
    """Muestra el banner del programa"""
    banner = f"""
{Colors.RED}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                    DOTA 2 HACK TOOL                          ║
║                    Creado por @ZekAtwiN12                    ║
║                    WhatsApp: +51 913806853                  ║
║                                                              ║
║  ██████╗  ██████╗ ████████╗ █████╗ ██████╗ ██╗  ██╗███████╗ ║
║  ██╔══██╗██╔═══██╗╚══██╔══╝██╔══██╗██╔══██╗██║  ██║╚════██║ ║
║  ██║  ██║██║   ██║   ██║   ███████║██║  ██║███████║ █████╔╝ ║
║  ██║  ██║██║   ██║   ██║   ██╔══██║██║  ██║██╔══██║ ╚═══██╗ ║
║  ██████╔╝╚██████╔╝   ██║   ██║  ██║██████╔╝██║  ██║██████╔╝ ║
║  ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝  ║
╚══════════════════════════════════════════════════════════════╝
{Colors.END}
"""
    print(banner)

def mostrar_progreso(mensaje, duracion=1):
    """Muestra una barra de progreso animada"""
    print(f"{Colors.CYAN}{mensaje}{Colors.END}")
    for i in range(20):
        barra = "█" * i + "░" * (20 - i)
        porcentaje = i * 5
        print(f"\r{Colors.YELLOW}[{barra}] {porcentaje}%{Colors.END}", end="", flush=True)
        time.sleep(duracion / 20)
    print(f"\r{Colors.GREEN}[{'█' * 20}] 100%{Colors.END}")

def hackear_cuenta_steam():
    """Hackea una cuenta de Steam"""
    limpiar_pantalla()
    mostrar_banner()
    
    print(f"{Colors.RED}{Colors.BOLD}🔓 INICIANDO HACKEO DE CUENTA STEAM 🔓{Colors.END}\n")
    
    # Seleccionar jugador aleatorio
    jugador = random.choice(JUGADORES_PERUANOS)
    
    print(f"{Colors.YELLOW}🎯 OBJETIVO DETECTADO:{Colors.END}")
    print(f"  Steam ID: {jugador['steam_id']}")
    print(f"  Nickname: {jugador['nickname']}")
    print(f"  Nombre: {jugador['nombre_real']}")
    print(f"  Ciudad: {jugador['ciudad']}")
    print(f"  Rank: {jugador['rank']}")
    print(f"  MMR: {jugador['mmr']}")
    print(f"  Última conexión: {jugador['ultima_conexion']}\n")
    
    # Proceso de hackeo mejorado y más realista
    pasos = [
        ("Escaneando puertos abiertos (27015-27020)...", 1.5),
        ("Detectando versión de Steam Client...", 1),
        ("Bypasseando Steam Guard...", 2),
        ("Inyectando exploit en steam.exe...", 2.5),
        ("Explotando vulnerabilidad CVE-2024-XXXX...", 2),
        ("Descifrando hash de contraseña (MD5)...", 1.5),
        ("Bypasseando autenticación de dos factores...", 2),
        ("Accediendo a Steam Web API...", 1.5),
        ("Extrayendo datos de la base de datos local...", 2),
        ("Descargando historial de transacciones...", 1.5),
        ("Extrayendo lista de amigos y grupos...", 1.5),
        ("Descargando inventario de Dota 2...", 2),
        ("Extrayendo estadísticas de partidas...", 1.5),
        ("Ocultando logs de acceso...", 1),
        ("Limpiando rastros del exploit...", 1)
    ]
    
    for paso, duracion in pasos:
        mostrar_progreso(paso, duracion)
        time.sleep(0.3)
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}✅ ACCESO CONCEDIDO - CUENTA COMPROMETIDA ✅{Colors.END}\n")
    
    # Mostrar información técnica del hackeo
    print(f"{Colors.CYAN}🔧 INFORMACIÓN TÉCNICA DEL HACKEO:{Colors.END}")
    print(f"  • Método: Exploit de inyección de memoria")
    print(f"  • Vulnerabilidad: CVE-2024-XXXX (Steam Client)")
    print(f"  • Tiempo de acceso: {random.randint(45,120)} segundos")
    print(f"  • IP de origen: {random.randint(192,223)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}")
    print(f"  • Puerto utilizado: {random.choice([27015, 27016, 27017, 27018])}")
    print(f"  • Protocolo: TCP/UDP")
    print(f"  • Estado: Conexión establecida y oculta")
    
    return jugador

def mostrar_info_cuenta(jugador):
    """Muestra la información completa de la cuenta hackeada"""
    print(f"{Colors.CYAN}{Colors.BOLD}📊 DATOS EXTRAÍDOS DE LA CUENTA 📊{Colors.END}\n")
    
    # Información básica mejorada
    print(f"{Colors.YELLOW}🔍 INFORMACIÓN PERSONAL:{Colors.END}")
    print(f"  Steam ID: {jugador['steam_id']}")
    print(f"  Nickname: {jugador['nickname']}")
    print(f"  Nombre Real: {jugador['nombre_real']}")
    print(f"  Edad: {jugador['edad']} años")
    print(f"  Ciudad: {jugador['ciudad']}")
    print(f"  País: Perú")
    print(f"  Zona horaria: GMT-5")
    print(f"  Última Conexión: {jugador['ultima_conexion']}")
    print(f"  Estado de cuenta: Activa")
    print(f"  Steam Guard: Habilitado")
    print(f"  Dinero Gastado: ${jugador['dinero_gastado']:.2f}")
    print(f"  Saldo actual: ${random.uniform(5.50, 45.75):.2f}")
    
    # Información de seguridad
    print(f"\n{Colors.YELLOW}🔒 INFORMACIÓN DE SEGURIDAD:{Colors.END}")
    print(f"  Contraseña: {'*' * random.randint(8,12)}")
    print(f"  Email: {jugador['nickname'].lower()}@gmail.com")
    print(f"  Teléfono: +51 9{random.randint(100000000,999999999)}")
    print(f"  Método de pago: Tarjeta Visa terminada en {random.randint(1000,9999)}")
    print(f"  Último cambio de contraseña: {random.randint(15,90)} días atrás")
    
    # Estadísticas de Dota 2 mejoradas
    print(f"\n{Colors.YELLOW}🎮 ESTADÍSTICAS DOTA 2:{Colors.END}")
    print(f"  Rank Actual: {jugador['rank']}")
    print(f"  MMR: {jugador['mmr']}")
    print(f"  MMR Máximo: {jugador['mmr'] + random.randint(200,800)}")
    print(f"  Partidas Jugadas: {jugador['partidas_jugadas']:,}")
    print(f"  Victorias: {int(jugador['partidas_jugadas'] * jugador['win_rate'] / 100):,}")
    print(f"  Derrotas: {int(jugador['partidas_jugadas'] * (100 - jugador['win_rate']) / 100):,}")
    print(f"  Win Rate: {jugador['win_rate']}%")
    print(f"  Abandono Rate: {random.uniform(2.1, 8.5):.1f}%")
    print(f"  Conduct Summary: {random.choice(['Favorable', 'Neutral', 'Needs Improvement'])}")
    print(f"  Comportamiento: {random.choice(['Excelente', 'Bueno', 'Regular'])}")
    
    # Héroes favoritos con más detalles
    print(f"\n{Colors.YELLOW}⚔️ HÉROES FAVORITOS Y ESTADÍSTICAS:{Colors.END}")
    for i, heroe in enumerate(jugador['heroes_favoritos'], 1):
        heroe_info = next((h for h in HEROES if h['nombre'] == heroe), None)
        if heroe_info:
            partidas_heroe = random.randint(50, 300)
            win_rate_heroe = random.uniform(45.0, 65.0)
            kda_heroe = f"{random.uniform(2.5, 4.8):.1f}"
            print(f"  {i}. {heroe} ({heroe_info['rol']})")
            print(f"     • Partidas: {partidas_heroe}")
            print(f"     • Win Rate: {win_rate_heroe:.1f}%")
            print(f"     • KDA Promedio: {kda_heroe}")
            print(f"     • Dificultad: {heroe_info['dificultad']}")
    
    # Items raros con valores
    print(f"\n{Colors.YELLOW}💎 INVENTARIO DE ITEMS RAROS:{Colors.END}")
    for item in jugador['items_raros']:
        valor = random.uniform(25.0, 150.0)
        print(f"  • {item} - Valor: ${valor:.2f}")
    
    # Lista de amigos con más información
    print(f"\n{Colors.YELLOW}👥 LISTA DE AMIGOS ({len(jugador['amigos'])} contactos):{Colors.END}")
    for amigo in jugador['amigos']:
        estado = random.choice(['En línea', 'Ausente', 'No molestar', 'Desconectado'])
        ultima_vez = random.choice(['Hace 2 minutos', 'Hace 1 hora', 'Hace 3 horas', 'Ayer'])
        print(f"  • {amigo} - {estado} - {ultima_vez}")
    
    # Grupos de Steam
    print(f"\n{Colors.YELLOW}👥 GRUPOS DE STEAM:{Colors.END}")
    grupos = ["Dota 2 Perú", "Gamers Latino", "Pro Players", "Toxic Gamers", "Lima Gaming"]
    for grupo in random.sample(grupos, 3):
        miembros = random.randint(100, 5000)
        print(f"  • {grupo} - {miembros:,} miembros")
    
    # Historial reciente mejorado
    print(f"\n{Colors.YELLOW}📈 HISTORIAL RECIENTE (Últimas 15 partidas):{Colors.END}")
    for i in range(15):
        resultado = "VICTORIA" if random.random() < jugador['win_rate']/100 else "DERROTA"
        heroe = random.choice(jugador['heroes_favoritos'])
        kills = random.randint(3, 28)
        deaths = random.randint(1, 12)
        assists = random.randint(2, 20)
        kda = f"{kills}/{deaths}/{assists}"
        duracion = f"{random.randint(20,65)}:{random.randint(0,59):02d}"
        fecha = f"2024-01-{random.randint(10,15)} {random.randint(10,23):02d}:{random.randint(0,59):02d}"
        print(f"  {i+1:2d}. {resultado} - {heroe} - KDA: {kda} - Duración: {duracion} - {fecha}")
    
    # Información de conexión
    print(f"\n{Colors.YELLOW}🌐 INFORMACIÓN DE CONEXIÓN:{Colors.END}")
    print(f"  IP Pública: {random.randint(190,220)}.{random.randint(1,255)}.{random.randint(1,255)}.{random.randint(1,255)}")
    print(f"  Proveedor: {random.choice(['Claro', 'Movistar', 'Entel', 'Bitel'])}")
    print(f"  Velocidad de conexión: {random.randint(10,100)} Mbps")
    print(f"  Ping promedio: {random.randint(15,85)} ms")
    print(f"  Servidor preferido: Peru (Lima)")
    print(f"  Última sincronización: Hace {random.randint(1,30)} minutos")

def hackear_partida_actual():
    """Hackea una partida en curso"""
    limpiar_pantalla()
    mostrar_banner()
    
    print(f"{Colors.RED}{Colors.BOLD}🎮 HACKEANDO PARTIDA EN CURSO 🎮{Colors.END}\n")
    
    # Partida más realista
    equipo_radiant = ["Juggernaut", "Crystal Maiden", "Axe", "Lion", "Phantom Assassin"]
    equipo_dire = ["Invoker", "Witch Doctor", "Tidehunter", "Shadow Fiend", "Lina"]
    
    print(f"{Colors.GREEN}⚔️ EQUIPO RADIANT:{Colors.END}")
    for i, heroe in enumerate(equipo_radiant, 1):
        nivel = random.randint(12, 25)
        kda = f"{random.randint(2,15)}/{random.randint(1,8)}/{random.randint(3,12)}"
        print(f"  {i}. {heroe} - Nivel {nivel} - KDA: {kda}")
    
    print(f"\n{Colors.RED}⚔️ EQUIPO DIRE:{Colors.END}")
    for i, heroe in enumerate(equipo_dire, 1):
        nivel = random.randint(12, 25)
        kda = f"{random.randint(2,15)}/{random.randint(1,8)}/{random.randint(3,12)}"
        print(f"  {i}. {heroe} - Nivel {nivel} - KDA: {kda}")
    
    tiempo_partida = f"{random.randint(25,55)}:{random.randint(0,59):02d}"
    score_radiant = random.randint(15, 35)
    score_dire = random.randint(12, 30)
    
    print(f"\n{Colors.YELLOW}⏱️ TIEMPO DE PARTIDA: {tiempo_partida}{Colors.END}")
    print(f"{Colors.CYAN}🏆 SCORE: Radiant {score_radiant} - {score_dire} Dire{Colors.END}")
    print(f"{Colors.PURPLE}🎯 OBJETIVOS: Radiant {random.randint(0,3)} - Dire {random.randint(0,3)}{Colors.END}")
    
    # Proceso de hackeo mejorado
    pasos = [
        ("Conectando al servidor de la partida (Luxembourg)...", 1.5),
        ("Bypasseando VAC (Valve Anti-Cheat)...", 2.5),
        ("Inyectando DLL en dota2.exe...", 2),
        ("Activando wallhack (ESP)...", 1.5),
        ("Configurando aimbot (Auto-aim)...", 2),
        ("Hackeando información del equipo enemigo...", 2),
        ("Extrayendo posiciones de wards...", 1.5),
        ("Descargando información de Roshan...", 1),
        ("Sincronizando datos en tiempo real...", 1.5),
        ("Ocultando proceso del hack...", 1)
    ]
    
    for paso, duracion in pasos:
        mostrar_progreso(paso, duracion)
        time.sleep(0.3)
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}✅ HACKEO DE PARTIDA COMPLETADO ✅{Colors.END}\n")
    
    # Mostrar información hackeada más detallada
    print(f"{Colors.CYAN}📡 INFORMACIÓN HACKEADA EN TIEMPO REAL:{Colors.END}")
    print(f"  • Posiciones de todos los héroes visibles")
    print(f"  • Items de todos los jugadores")
    print(f"  • Cooldowns de habilidades")
    print(f"  • Vida y mana en tiempo real")
    print(f"  • Ward positions (Observer & Sentry)")
    print(f"  • Roshan timer: {random.randint(8,12)}:00")
    print(f"  • Courier tracking")
    print(f"  • Runes spawn timer")
    print(f"  • Tower health status")
    print(f"  • Enemy ultimate status")
    print(f"  • Gold and XP difference")
    print(f"  • Buyback status")
    
    # Información técnica del hackeo
    print(f"\n{Colors.YELLOW}🔧 INFORMACIÓN TÉCNICA:{Colors.END}")
    print(f"  • Servidor: Luxembourg (EU West)")
    print(f"  • Match ID: {random.randint(7000000000, 7999999999)}")
    print(f"  • Lobby: Ranked Matchmaking")
    print(f"  • Skill Bracket: {random.choice(['High', 'Very High', 'Normal'])}")
    print(f"  • Ping: {random.randint(15,85)} ms")
    print(f"  • FPS: {random.randint(60,144)}")
    print(f"  • Latencia: {random.randint(5,25)} ms")
    print(f"  • Estado: Conexión estable y oculta")

def generar_reportes(jugador):
    """Genera reportes del hackeo"""
    while True:
        print(f"\n{Colors.CYAN}{Colors.BOLD}📄 GENERAR REPORTES{Colors.END}")
        print("1. Guardar como TXT")
        print("2. Guardar como JSON")
        print("3. Volver al menú principal")
        
        opcion = input(f"\n{Colors.YELLOW}Selecciona una opción: {Colors.END}")
        
        if opcion == "1":
            guardar_txt(jugador)
        elif opcion == "2":
            guardar_json(jugador)
        elif opcion == "3":
            break
        else:
            print(f"{Colors.RED}Opción inválida{Colors.END}")

def guardar_txt(jugador):
    """Guarda el reporte en formato TXT"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"dota2_hack_report_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("=" * 60 + "\n")
        f.write("           REPORTE DE HACKEO DOTA 2\n")
        f.write("           Creado por @ZekAtwiN12\n")
        f.write("=" * 60 + "\n\n")
        
        f.write("INFORMACIÓN PERSONAL:\n")
        f.write(f"Steam ID: {jugador['steam_id']}\n")
        f.write(f"Nickname: {jugador['nickname']}\n")
        f.write(f"Nombre Real: {jugador['nombre_real']}\n")
        f.write(f"Edad: {jugador['edad']} años\n")
        f.write(f"Ciudad: {jugador['ciudad']}\n")
        f.write(f"País: Perú\n")
        f.write(f"Última Conexión: {jugador['ultima_conexion']}\n")
        f.write(f"Dinero Gastado: ${jugador['dinero_gastado']:.2f}\n\n")
        
        f.write("ESTADÍSTICAS DOTA 2:\n")
        f.write(f"Rank Actual: {jugador['rank']}\n")
        f.write(f"MMR: {jugador['mmr']}\n")
        f.write(f"Partidas Jugadas: {jugador['partidas_jugadas']:,}\n")
        f.write(f"Win Rate: {jugador['win_rate']}%\n\n")
        
        f.write("HÉROES FAVORITOS:\n")
        for heroe in jugador['heroes_favoritos']:
            f.write(f"• {heroe}\n")
        f.write("\n")
        
        f.write("ITEMS RAROS:\n")
        for item in jugador['items_raros']:
            f.write(f"• {item}\n")
        f.write("\n")
        
        f.write("LISTA DE AMIGOS:\n")
        for amigo in jugador['amigos']:
            f.write(f"• {amigo}\n")
        f.write("\n")
        
        f.write("INFORMACIÓN TÉCNICA DEL HACKEO:\n")
        f.write(f"Método: Exploit de inyección de memoria\n")
        f.write(f"Vulnerabilidad: CVE-2024-XXXX\n")
        f.write(f"Tiempo de acceso: {random.randint(45,120)} segundos\n")
        f.write(f"Estado: Cuenta comprometida exitosamente\n\n")
        
        f.write("=" * 60 + "\n")
        f.write(f"Reporte generado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n")
    
    print(f"{Colors.GREEN}✅ Reporte guardado como: {filename}{Colors.END}")

def guardar_json(jugador):
    """Guarda el reporte en formato JSON"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"dota2_hack_report_{timestamp}.json"
    
    reporte = {
        "metadata": {
            "generado_por": "@ZekAtwiN12",
            "fecha": datetime.now().isoformat(),
            "tipo": "hackeo_dota2",
            "version": "2.0"
        },
        "jugador": jugador,
        "heroes_disponibles": HEROES,
        "items_disponibles": ITEMS,
        "informacion_tecnica": {
            "metodo": "Exploit de inyección de memoria",
            "vulnerabilidad": "CVE-2024-XXXX",
            "tiempo_acceso": random.randint(45,120),
            "estado": "Cuenta comprometida exitosamente"
        }
    }
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(reporte, f, indent=2, ensure_ascii=False)
    
    print(f"{Colors.GREEN}✅ Reporte guardado como: {filename}{Colors.END}")

def mostrar_creditos():
    """Muestra los créditos del programa"""
    limpiar_pantalla()
    mostrar_banner()
    
    print(f"{Colors.CYAN}{Colors.BOLD}🎯 CRÉDITOS 🎯{Colors.END}\n")
    print(f"{Colors.YELLOW}Desarrollador:{Colors.END} @ZekAtwiN12")
    print(f"{Colors.YELLOW}Versión:{Colors.END} 2.0")
    print(f"{Colors.YELLOW}Fecha:{Colors.END} Enero 2024")
    print(f"{Colors.YELLOW}Descripción:{Colors.END} Herramienta de hackeo para Dota 2")
    print(f"{Colors.YELLOW}Características:{Colors.END}")
    print("  • Interfaz profesional y realista")
    print("  • Datos de jugadores peruanos")
    print("  • Información detallada de cuentas")
    print("  • Hackeo de partidas en curso")
    print("  • Generación de reportes")
    print("  • Compatible con Termux")
    
    print(f"\n{Colors.YELLOW}📞 CONTACTO:{Colors.END}")
    print(f"  WhatsApp: +51 913806853")
    print(f"  Telegram: @ZekAtwiN12")
    
    print(f"\n{Colors.RED}⚠️ ADVERTENCIA:{Colors.END}")
    print("Esta herramienta es solo para fines educativos.")
    print("Respeta la privacidad de otros usuarios.")
    
    input(f"\n{Colors.YELLOW}Presiona Enter para continuar...{Colors.END}")

def menu_principal():
    """Menú principal del programa"""
    while True:
        limpiar_pantalla()
        mostrar_banner()
        
        print(f"{Colors.CYAN}{Colors.BOLD}🎮 MENÚ PRINCIPAL 🎮{Colors.END}\n")
        print("1. 🔓 Hackear cuenta de Steam")
        print("2. 🎮 Hackear partida en curso")
        print("3. 📊 Ver información de cuenta hackeada")
        print("4. 📄 Generar reportes")
        print("5. 🎯 Créditos")
        print("6. 🚪 Salir")
        
        opcion = input(f"\n{Colors.YELLOW}Selecciona una opción: {Colors.END}")
        
        if opcion == "1":
            jugador = hackear_cuenta_steam()
            input(f"\n{Colors.YELLOW}Presiona Enter para continuar...{Colors.END}")
        elif opcion == "2":
            hackear_partida_actual()
            input(f"\n{Colors.YELLOW}Presiona Enter para continuar...{Colors.END}")
        elif opcion == "3":
            if 'jugador' in locals():
                mostrar_info_cuenta(jugador)
                input(f"\n{Colors.YELLOW}Presiona Enter para continuar...{Colors.END}")
            else:
                print(f"{Colors.RED}Primero debes hackear una cuenta{Colors.END}")
                time.sleep(2)
        elif opcion == "4":
            if 'jugador' in locals():
                generar_reportes(jugador)
            else:
                print(f"{Colors.RED}Primero debes hackear una cuenta{Colors.END}")
                time.sleep(2)
        elif opcion == "5":
            mostrar_creditos()
        elif opcion == "6":
            print(f"\n{Colors.GREEN}¡Gracias por usar Dota 2 Hack Tool!{Colors.END}")
            print(f"{Colors.CYAN}Creado por @ZekAtwiN12{Colors.END}")
            break
        else:
            print(f"{Colors.RED}Opción inválida{Colors.END}")
            time.sleep(1)

def main():
    """Función principal"""
    try:
        menu_principal()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.RED}Programa interrumpido por el usuario{Colors.END}")
        print(f"{Colors.CYAN}Creado por @ZekAtwiN12{Colors.END}")
    except Exception as e:
        print(f"\n{Colors.RED}Error: {e}{Colors.END}")

if __name__ == "__main__":
    main() 