from __future__ import annotations

from pathlib import Path

from pydantic.dataclasses import dataclass
from pyfedappwrap.learning.run_runfig import AppConfig, AppOutputConfig, AppInputConfig
from pyfedappwrap.types.databaseadopter.base_importer import BaseExtractorAdopterAPP


@dataclass
class DiabetesUS130ClinicsConfig(AppConfig):
    pass


@dataclass
class DiabetesUS130ClinicsInputConfig(AppInputConfig):
    pass


@dataclass
class DiabetesUS130ClinicsOutput(AppOutputConfig):
    data: Path | None = None
    ids: Path | None = None


class DiabetesUS130ClinicsApp(
    BaseExtractorAdopterAPP[
        DiabetesUS130ClinicsConfig, DiabetesUS130ClinicsInputConfig, DiabetesUS130ClinicsOutput]):

    def __init__(self):
        super().__init__()

    def run_adopter(self) -> DiabetesUS130ClinicsOutput:
        data_path = Path("data/diabetic_data.csv")
        ids_path = Path("data/IDS_mapping.csv")
        return DiabetesUS130ClinicsOutput(data=data_path, ids=ids_path)
