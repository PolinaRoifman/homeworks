 class Batch:
    def __init__(self, catalyst_1: str, catalyst_2: str):
        self.catalyst_1 = catalyst_1
        self.catalyst_2 = catalyst_2


class Filter:
    def __init__(self, firm: str, model: str, percent_dirty: float):
        self.firm = firm
        self.model = model
        self.percent_dirty = percent_dirty

    def check(self):
        return self.percent_dirty

    def replace(self):
        if self.percent_dirty >= 0.8: #можно поставить любое значение как критическое для загрязнения фильтра
            return 'replace filter'

class Ammonium_stage:
    def __init__(self, temperature: float, pressure: float, addict: dict, catalyst_1: str):
        self.temperature = temperature
        self.pressure = pressure
        self.addict = addict
        self.catalyst_1 = catalyst_1

    def produce(self) -> Batch:
        return Batch(self.catalyst_1, '')

class Oxidation_stage:
    def __init__(self, O2: float, catalyst_2: str):
        self.O2 = O2
        self.catalyst_2 = catalyst_2

    def oxidation(self, input_batch: Batch) -> Batch:
        input_batch.catalyst_2 = self.catalyst_2
        pass

class Absorbtion_stage:
    def __init__(self, filter: Filter):
        self.filter = filter

    def absorption(self, input_batch: Batch) -> Batch:
        pass


class Final_stage:
    def __init__(self, acid_concentration: float, total_flow: float):
        self.acid_concentration = acid_concentration
        self.total_flow = total_flow

    def concentration(self, acid_concentration: float):
        return self.acid_concentration

    def dehydration(self, input_batch: Batch) -> Batch:#сколько воды убрали
        return self.total_flow-self.acid_concentaration
