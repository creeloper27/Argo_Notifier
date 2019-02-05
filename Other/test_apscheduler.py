from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.add_job(funzione, "interval", minutes/hours/...=intero)
scheduler.add_job(funzione, "cron", minute/hour/...=intero)
scheduler.add_job(funzione, "date", minute/hour/...=intero)
ritornano una variabile "job" che può essere usato per rimuoverlo


