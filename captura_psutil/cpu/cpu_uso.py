import psutil as ps
from interfaces import Executavel


class CpuUso(Executavel.Executavel):

    def executar(self):
        cpu_percent = ps.cpu_percent()
        print(cpu_percent)