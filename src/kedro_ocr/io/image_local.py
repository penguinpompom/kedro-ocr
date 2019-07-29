"""ExcelLocalDataSet loads and saves data to a local Excel file. The
underlying functionality is supported by pandas, so it supports all
allowed pandas options for loading and saving Excel files.
"""
from os.path import isfile, isdir
import glob
from pathlib import Path
from typing import Any, Union, Dict

import pandas as pd
import cv2

from kedro.io import AbstractDataSet

class ImageLocalDataSet(AbstractDataSet):
    """``ImageLocalDataSet`` loads and saves data into a specified folder. The
    underlying functionality is supported by opencv.

    """

    def _describe(self) -> Dict[str, Any]:
        return dict(filepath=self._filepath,
                    engine=self._engine,
                    load_args=self._load_args,
                    save_args=self._save_args)

    def __init__(
        self,
        filepath: str,
        engine: str = None,
        load_args: Dict[str, Any] = None,
        save_args: Dict[str, Any] = None,
    ) -> None:
        """Creates a new instance of ``ImageLocalDataSet`` pointing to a concrete
        filepath.

        Args:
            engine: None.

            filepath: path to an directory.

        """
        self._filepath = filepath
        default_save_args = {}
        default_load_args = {}

        self._load_args = {**default_load_args, **load_args} \
            if load_args is not None else default_load_args
        self._save_args = {**default_save_args, **save_args} \
            if save_args is not None else default_save_args
        self._engine = engine

    def _load(self) -> list:
        images = [cv2.imread(file) for file in glob.glob(self._filepath + '*.jpg')]
        return images 
        

    def _save(self, data: list) -> None:
        save_path = Path(glob.glob(self._filepath)[0])
        save_path.parent.mkdir(parents=True, exist_ok=True)
        for i, dt in enumerate(data):
        	cv2.imwrite(str(save_path) + str(i + 1) + '.jpg', dt)  

    def _exists(self) -> bool:
        return isdir(self._filepath)