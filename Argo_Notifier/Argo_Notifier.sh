#!/bin/bash
cp subject_table_bkup.json subject_table.json
python3 "ui to py.py"
python3 Argo_Notifier.py
pause
