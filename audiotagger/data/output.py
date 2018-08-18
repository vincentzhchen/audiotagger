class AudioTaggerOutput(object):
    def __init__(self, logger):
        self.output = []

    def add_output(self, df):
        self.output.append(df)
