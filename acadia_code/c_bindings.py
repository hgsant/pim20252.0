
import ctypes, os, platform

def _lib_name():
    return "c_module.dll" if platform.system() == "Windows" else "libc_module.so"

def load_lib():
    name = _lib_name()
    here = os.path.dirname(__file__)
    cand = os.path.join(here, name)
    if os.path.exists(cand):
        name = cand
    elif not os.path.exists(name):
        return None
    lib = ctypes.CDLL(name)
    lib.media.argtypes = [ctypes.c_float, ctypes.c_float, ctypes.c_float]
    lib.media.restype  = ctypes.c_float
    lib.situacao.argtypes = [ctypes.c_float, ctypes.c_int, ctypes.c_int]
    lib.situacao.restype  = ctypes.c_int
    lib.normaliza.argtypes = [ctypes.c_float]
    lib.normaliza.restype  = ctypes.c_float
    return lib

LIB = load_lib()

def calc_media(n1, n2, n3):
    if LIB: return float(LIB.media(n1, n2, n3))
    return (n1+n2+n3)/3.0

def get_situacao(media, faltas, total_aulas):
    if LIB:
        code = int(LIB.situacao(media, faltas, total_aulas))
    else:
        freq = 1.0 - (faltas/total_aulas if total_aulas>0 else 1.0)
        if total_aulas <= 0: code = 1
        elif freq < 0.75: code = 0
        elif media >= 6.0: code = 2
        else: code = 1
    return {0:"Reprovado por falta", 1:"Reprovado por nota", 2:"Aprovado"}[code]
