class GameStateManager:

    def __init__(self):
        self.current_hand = None

    def start_hand(self, hand_data):
        self.current_hand = hand_data

    def get_hand(self):
        return self.current_hand

    def update_action(self, action):
        if not self.current_hand:
            return

        self.current_hand.setdefault("action_history", [])
        self.current_hand["action_history"].append(action)

    def update_board(self, board):
        if not self.current_hand:
            return

        self.current_hand["board"] = board

    def reset(self):
        self.current_hand = None

    def update_state(self, board=None, actions=None):
        if not self.current_hand:
            return

        if board is not None:
            self.current_hand["board"] = board

        if actions:

            self.current_hand.setdefault("action_history", [])

            for action in actions:
                self.current_hand["action_history"].append(action)


game_state = GameStateManager()
        