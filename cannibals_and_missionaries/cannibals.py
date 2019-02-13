from search import Problem


def is_valid(state):
    no_missionaries_left, no_cannibals_left, direction, no_missionaries_right, no_cannibals_right = state

    if no_missionaries_left < no_cannibals_left and no_missionaries_left != 0:
        return False

    if no_missionaries_right < no_cannibals_right and no_missionaries_right != 0:
        return False

    return True


class Cannibals(Problem):
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

        if current_state[2] == 'RIGHT':

            if current_state[3] > 0:
                new_state = (current_state[0] + 1, current_state[1], 'LEFT', current_state[3] - 1, current_state[4])

                if is_valid(new_state):
                    actions.append(new_state)

            if current_state[4] > 0:
                new_state = (current_state[0], current_state[1] + 1, 'LEFT', current_state[3], current_state[4] - 1)

                if is_valid(new_state):
                    actions.append(new_state)

            if current_state[3] > 1:
                new_state = (current_state[0] + 2, current_state[1], 'LEFT', current_state[3], current_state[4])

                if is_valid(new_state):
                    actions.append(new_state)

            if current_state[4] > 1:
                new_state = (current_state[0], current_state[1] + 2, 'LEFT', current_state[3], current_state[4] - 2)

                if is_valid(new_state):
                    actions.append(new_state)

            if current_state[3] > 0 and current_state[4] > 0:
                new_state = (current_state[0] + 1, current_state[1] + 1, 'LEFT', current_state[3] - 1, current_state[4] - 1)

                if is_valid(new_state):
                    actions.append(new_state)

        else:

            if current_state[0] > 0:
                new_state = (current_state[0] - 1, current_state[1], 'RIGHT', current_state[3] + 1, current_state[4])

                if is_valid(new_state):
                    actions.append(new_state)

            if current_state[1] > 0:
                new_state = (current_state[0], current_state[1] - 1, 'RIGHT', current_state[3], current_state[4] + 1)

                if is_valid(new_state):
                    actions.append(new_state)

            if current_state[0] > 1:
                new_state = (current_state[0] - 2, current_state[1], 'RIGHT', current_state[3] + 2, current_state[4])

                if is_valid(new_state):
                    actions.append(new_state)

            if current_state[1] > 1:
                new_state = (current_state[0], current_state[1] - 2, 'RIGHT', current_state[3], current_state[4] + 2)

                if is_valid(new_state):
                    actions.append(new_state)

            if current_state[0] > 0 and current_state[1] > 0:
                new_state = (current_state[0] - 1, current_state[1] - 1, 'RIGHT', current_state[3] + 1, current_state[4] + 1)

                if is_valid(new_state):
                    actions.append(new_state)

        return actions
