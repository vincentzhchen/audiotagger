# PROJECT LIB
from audiotagger.data import _base_io, loader
from audiotagger.util import input_output_util as ioutil


class AudioTaggerInput(_base_io.AudioTaggerBaseInputOutput):
    """Holds all necessary inputs for audiotagger project.

    """
    def write_to_excel(self):
        file_path = ioutil.generate_excel_path("audiotagger_input")
        ioutil.write_metadata_to_excel(self.metadata, file_path=file_path)
        self.logger.info("Saved input metadata to %s", file_path)

    def write_to_csv(self):
        # TODO: implement this
        pass

    def set_metadata(self, df):
        self.logger.info("Setting metadata in input object.")
        super().set_metadata(df)

    def load_metadata(self, src):
        """Loads metadata from loader.

        Args:
            src (str): Path to Excel/csv/m4a or directory of m4a.

        Returns:
            void
        """
        ldr = loader.AudioTaggerMetadataLoader(src=src, logger=self.logger)
        self.set_metadata(ldr.load_metadata_df())

    def get_metadata(self):
        """Get cleaned metadata.

        All cleaning should be done at loading.  Do not modify here.

        Returns:
            df (pd.DataFrame): Returns a metadata dataframe.
        """
        if self.metadata.columns.tolist() == []:
            raise AttributeError("[metadata] was not set.")

        df = self.metadata.copy(deep=True)
        return df
