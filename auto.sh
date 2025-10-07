#!/bin/bash
#——————————————
# ذکر نکردن منبع پیگرد ناموسی خواهد داشت
# Dev:@TELE_ATLAS
# Date:1404/6/9
#MyTeam:@Winston_source
# ---------------------------------------

WORKDIR="/home/a1176921/selfsaz"
VENV="$WORKDIR/myenv/bin/activate"
cd $WORKDIR
source $VENV

DATE=$(date +%F)

declare -A SCRIPTS
SCRIPTS=( ["helper.py"]="helper" ["botself.py"]="bot" )

for script in "helper.py" "botself.py"; do
    LOG="${SCRIPTS[$script]}-$DATE.log"
    PIDFILE="${SCRIPTS[$script]}.pid"

    if [ ! -f "$PIDFILE" ] || ! kill -0 $(cat "$PIDFILE") 2>/dev/null; then
        echo "$(date) - Starting $script ..."
        nohup python3 "$script" > "$LOG" 2>&1 &
        echo $! > "$PIDFILE"
        sleep 3
    fi
done


