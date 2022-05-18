import yaml


class action:
    def __init__(self, name, qty, unit, cost, frq, first, building):
        self.name = name
        self.qty = qty
        self.unit = unit
        self.cost = cost
        self.frq = frq
        self.first = first
        self.building = building


def load_actions():
    actions = []
    with open("actions.yaml", "r") as stream:
        actions_input_string = yaml.safe_load(stream)
        for action_input in actions_input_string:
            print(action_input)
            action_input_obj = yaml.dump(action_input)
            new_action = action(action_input.get("name"), action_input.get("qty"), action_input.get("unit"), action_input.get("cost"), action_input.get("frq"), action_input.get("first"), action_input.get("building"))






def main():
    load_actions()

if __name__ == "__main__":
    main()
