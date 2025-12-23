
class EmotionEngine:
    def __init__(self):
        self.emotion = "idle"

    def update_emotion(self, event):
        if event == "voice_detected":
            self.emotion = "happy"
        elif event == "no_interaction":
            self.emotion = "bored"
        else:
            self.emotion = "idle"

        return self.emotion

    def get_emotion(self):
        return self.emotion

