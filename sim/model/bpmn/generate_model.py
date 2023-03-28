from casymda.bpmn.bpmn_parser import parse_bpmn as csa_parsing

BPMN_PATH = "sim/model/bpmn/diagram.bpmn"
TEMPLATE_PATH = "sim/model/bpmn/model_template.py"
JSON_PATH = "sim/model/bpmn/_temp_bpmn.json"
MODEL_PATH = "sim/model/model.py"


def parse_bpmn():
    csa_parsing(BPMN_PATH, JSON_PATH, TEMPLATE_PATH, MODEL_PATH)


if __name__ == "__main__":
    parse_bpmn()
