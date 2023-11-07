import os
from box.exceptions import BoxTypeError
from ensure import ensure_annotations
from box import ConfigBox
import sys
import json
from pathlib import Path
from cnnClassifier import logger
import base64
import yaml

def load_json(path:Path) ->ConfigBox:

    try:
        with open(path) as f:
            content=json.load(f)
        logger.info(f"json file loaded successfully from:{path}")
    except Exception as e:
        logger.info(e)
        raise e
    
