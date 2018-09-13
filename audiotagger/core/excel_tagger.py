import pandas as pd
from mutagen.mp4 import MP4Tags
from audiotagger.data.fields import Fields as fld
from audiotagger.utils.utils import AudioTaggerUtils


class ExcelTagger(object):
    def __init__(self, logger, input_data):
        self.log = logger
        self.metadata = input_data.get_metadata()
        self.utils = AudioTaggerUtils()

    def get_audio_files(self):
        paths = self.metadata["PATH"].tolist()
        m4a_obj = self.utils.convert_to_m4a(paths)
        return m4a_obj

    def metadata_to_tags(self, df_metadata):
        df_metadata[fld.TRACK_NUMBER] = df_metadata[
            ["TRACK_NO", "TOTAL_TRACKS"]].apply(tuple, axis="columns")
        df_metadata[fld.DISC_NUMBER] = df_metadata[
            ["DISC_NO", "TOTAL_DISCS"]].apply(tuple, axis="columns")
        df_metadata.drop(["TRACK_NO", "TOTAL_TRACKS",
                          "DISC_NO", "TOTAL_DISCS"],
                         axis="columns", inplace=True)
        df_metadata[fld.YEAR] = df_metadata[fld.YEAR].astype(str)
        df_metadata = df_metadata.applymap(lambda x: [x])

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

    def save_tags_to_audio_files(self):
        metadata = self.metadata
        tag_dict = self.metadata_to_tags(df_metadata=metadata)
        for k in tag_dict:
            self.log.info(f"Saving {tag_dict[k]} to {k}")
            tag_dict[k].save(k)

    def rename_file(self):
        metadata = self.metadata

        import os
        base_dir = metadata["PATH"].apply(os.path.dirname)
        metadata["NEW_FILE_NAME"] = metadata[fld.DISC_NO].astype(str) + "-" + \
                                    metadata[fld.TRACK_NO].astype(str) + " " + \
                                    metadata[fld.TITLE] + ".m4a"

        print(metadata)
