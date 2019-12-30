from deepspeech import load

class DeepSpeechSpeechToText:
    def __init__(self, full_path):
        self.full_path = full_path        
        self.text = ''

    def transcript_audio(self):
        deepspeech = load('pl')
        files = [self.full_path]
        sentences = deepspeech(files)
        return sentences