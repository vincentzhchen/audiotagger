from audiotagger.core.clear_tags import ClearTags
from audiotagger.core.excel_tagger import ExcelTagger
from audiotagger.core.rename_file import RenameFile
from audiotagger.data.input import AudioTaggerInput
from audiotagger.settings import settings as settings


class AudioTagger(object):
    def __init__(self, logger, options, **kwargs):
        self.log = logger
        self.src = options.src
        self.options = options
        self.input_data = AudioTaggerInput(src=self.options.src,
                                           logger=self.log,
                                           xl_input_file=options.xl_input_file)

    def main(self):
        if self.options.tag_file:
            et = ExcelTagger(logger=self.log, input_data=self.input_data)
            et.save_tags_to_audio_files()

        if self.options.rename_file:
            if self.options.rename_dst is not None:
                rename_dst = self.options.rename_dst
            else:
                rename_dst = settings.AUDIO_DIRECTORY

            rf = RenameFile(base_dst_dir=rename_dst, logger=self.log,
                            input_data=self.input_data)
            rf.rename_file()

        if self.options.is_clear_tags:
            ct = ClearTags(root=self.options.src, logger=self.log)
            ct.clear_tags()

        if self.options.write_to_excel:
            self.input_data.write_to_excel(self.options.xl_output_file)
