import sys

path = "/home/remusaxys/sistema_gastos_empresa/sistema_gastos_empresa"
if path not in sys.path:
    sys.path.insert(0, path)

from app import app as application