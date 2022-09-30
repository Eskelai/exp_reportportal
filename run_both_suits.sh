#!/bin/bash

python -m pytest --reportportal -m first_suit first-suit/tests.py
python -m pytest --reportportal -m second_suit second-suit/tests.py