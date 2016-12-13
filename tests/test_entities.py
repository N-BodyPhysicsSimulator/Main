from nbp.io.input_providers import CSVInputProvider, JSONInputProvider
from nbp.io.output_writers import JSONOutputWriter, CSVOutputWriter, WSOutputWriter, CSVOneFileOutputWriter
from nbp.modifiers import DeltaTimeModifier, CalculationModifier

def test_entity_names():
    assert CSVInputProvider.entity_name == "csv"
    assert JSONInputProvider.entity_name == "json"

    assert JSONOutputWriter.entity_name == "json"
    assert CSVOutputWriter.entity_name == "csv"
    assert CSVOneFileOutputWriter.entity_name == "csv_one_file"
    assert WSOutputWriter.entity_name == "ws"

    assert DeltaTimeModifier.entity_name == "delta_time"
    assert CalculationModifier.entity_name == "calculation"

def test_entity_cli_argments():
    entities = [CSVInputProvider, JSONInputProvider,
                JSONOutputWriter, CSVOutputWriter, CSVOneFileOutputWriter,
                WSOutputWriter, DeltaTimeModifier, CalculationModifier]

    for entity in entities:
        assert isinstance(entity.get_cli_arguments(), list)
