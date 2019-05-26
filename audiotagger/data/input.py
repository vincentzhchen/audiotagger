# PROJECT LIB
from audiotagger.data import base_io, loader
from audiotagger.util import input_output_util as ioutil


class AudioTaggerInput(base_io.AudioTaggerBaseInputOutput):
    """Holds all necessary inputs for audiotagger project.

    """

    def __init__(self, logger):
        super().__init__(logger)

    def write_to_excel(self):
        file_path = ioutil.generate_excel_path("audiotagger_input")
        ioutil.write_metadata_to_excel(self.metadata, file_path=file_path)
        self.log.info(f"Saved input metadata to {file_path}")

    def write_to_csv(self):
        # TODO: implement this
        pass

    def set_metadata(self, df):
        super().set_metadata(df)

    def load_metadata(self, src):
        """Loads metadata from loader.

        Args:
            src (str): Path to Excel/csv/m4a or directory of m4a.

        Returns:
            void
        """
        ldr = loader.AudioTaggerMetadataLoader(src=src, logger=self.log)
        self.set_metadata(ldr.load_metadata_df())

    def get_metadata(self):
        """Get cleaned metadata.

        All cleaning should be done at loading.  Do not modify here.

        Returns:
            df (pd.DataFrame): Returns a metadata dataframe.
        """
        if not hasattr(self, "metadata"):
            raise ValueError("[metadata] was not set.")

        df = self.metadata.copy(deep=True)  # TODO: is this needed?
        return df
