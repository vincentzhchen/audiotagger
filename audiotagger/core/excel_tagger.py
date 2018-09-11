import pandas as pd
from mutagen.mp4 import MP4Tags
from audiotagger.data.fields import Fields as fld
from audiotagger.utils.utils import AudioTaggerUtils


class ExcelTagger(object):
    def __init__(self, logger, xl_input_file):
        self.log = logger
        self.metadata = pd.read_excel(xl_input_file)
        self.utils = AudioTaggerUtils()

    def get_metadata(self):
        self.metadata[fld.TRACK_NUMBER] = self.metadata[
            ["TRACK_NO", "TOTAL_TRACKS"]].apply(tuple, axis="columns")
        self.metadata[fld.DISC_NUMBER] = self.metadata[
            ["DISC_NO", "TOTAL_DISCS"]].apply(tuple, axis="columns")
        self.metadata.drop(["TRACK_NO", "TOTAL_TRACKS",
                            "DISC_NO", "TOTAL_DISCS"],
                           axis="columns", inplace=True)
        self.metadata[fld.YEAR] = self.metadata[fld.YEAR].astype(str)
        self.metadata = self.metadata.applymap(lambda x: [x])
        return self.metadata

    def get_audio_files(self):
        paths = self.get_metadata()["PATH"].tolist()
        m4a_obj = self.utils.convert_to_m4a(paths)
        return m4a_obj

    def metadata_to_tags(self, df_metadata):
        tag_dict = {}
        df_metadata.columns = [
            fld.field_to_ID3.get(c, c) for c in df_metadata.columns]
        metadata_dicts = df_metadata.to_dict(orient="records")
        for d in metadata_dicts:
            path = d.pop("PATH")[0]
            tags = MP4Tags()
            tags.update(d)
            tag_dict.update({path: tags})
        return tag_dict

    def tag_audio_files(self):
        metadata = self.get_metadata()
        tag_dict = self.metadata_to_tags(df_metadata=metadata)
        for k in tag_dict:
            self.log.info(f"Saving {tag_dict[k]} to {k}")
            tag_dict[k].save(k)