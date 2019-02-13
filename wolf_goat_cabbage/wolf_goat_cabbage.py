from search import Problem


def is_valid(state):
    wolf_left, goat_left, cabbage_left, boat, wolf_right, goat_right, cabbage_right = state

    if wolf_left == goat_left == 1 and boat == 'RIGHT':
        return False
    if goat_left == cabbage_left == 1 and boat == 'RIGHT':
        return False
    if wolf_right == goat_right == 1 and boat == 'LEFT':
        return False
    if cabbage_right == goat_right == 1 and boat == 'LEFT':
        return False

    return True


class WolfGoatCabbage(Problem):
    def result(self, state, action):
        return action

    def value(self, state):
        pass

    def __init__(self, initial, goal):
        self.goal = goal
        self.initial = initial
        Problem.__init__(self, self.initial, self.goal)

    def __repr__(self):
        return "< State (%s, %s) >" % (self.initial, self.goal)

    def goal_test(self, state):
        return state == self.goal

    def actions(self, current_state):
        actions = []

        if current_state[3] == 'LEFT':
            new_state = (0, current_state[1], current_state[2], 'RIGHT', 1, current_state[5], current_state[6])
            if is_valid(new_state):
                actions.append(new_state)

            new_state = (current_state[0], current_state[1], 0, 'RIGHT', current_state[4], current_state[5], 1)
            if is_valid(new_state):
                actions.append(new_state)

            new_state = (current_state[0], 0, current_state[2], 'RIGHT', current_state[4], 1, current_state[6])
            if is_valid(new_state):
                actions.append(new_state)
        else:
            new_state = (1, current_state[1], current_state[2], 'LEFT', 0, current_state[5], current_state[6])
            if is_valid(new_state):
                actions.append(new_state)

            new_state = (current_state[0], 1, current_state[2], 'LEFT', current_state[4], 0, current_state[6])
            if is_valid(new_state):
                actions.append(new_state)

            new_state = (current_state[0], current_state[1], 1, 'LEFT', current_state[4], current_state[5], 0)
            if is_valid(new_state):
                actions.append(new_state)

            new_state = (current_state[0], current_state[1], current_state[2], 'LEFT',
                         current_state[4], current_state[5], current_state[6])
            if is_valid(new_state):
                actions.append(new_state)

        return actions
