# audiotagger
Cross platform metadata editor and manager for audio files.

## Dependencies
- [mutagen](https://github.com/quodlibet/mutagen): Developed on 1.41.1 and
    higher.  May work for earlier versions.
- [pandas](https://github.com/pandas-dev/pandas): Developed on 0.20.3 and
    higher.  May work for earlier versions.
- [openpyxl](https://bitbucket.org/openpyxl/openpyxl/src): Developed on 2.5.11
    and higher.  May work for earlier versions.

## Setup
All commands are executed from `audiotagger.audiotagger.api.main`.  First run
the following to generate a configuration file.
```buildoutcfg
--generate-config
```
This generates a configuration file in the `~/.audiotagger` directory.

## Example
* This extracts the metadata from a single audio file.  Passing `-x` writes
the output to an Excel (.xlsx) file.
    ```text
    -s /path/to/file -x
    ```

* Similar to the above, you can extract metadata from several files by
passing in a directory.
    ```text
    -s /path/to/album -x
    ```

* To tag audio file(s) using a metadata input file, change the source to
a metadata input file and pass the `-t` option.
    ```text
    -s /path/to/metadata_input_file.xlsx -t
    ```


