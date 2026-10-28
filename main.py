from pyfedappwrap.engine.runtime import FedDBEngine

from app import DiabetesUS130ClinicsApp

engine = FedDBEngine()
engine.register(DiabetesUS130ClinicsApp())

if __name__ == '__main__':
    engine.start()
    engine.wait_until_stop()
