@echo off
copy subject_table_bkup.json subject_table.json
python "ui to py.py"
python Argo_Notifier.py
pause