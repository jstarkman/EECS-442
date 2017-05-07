module load python/3.5.2
jupyter-notebook --no-browser > /dev/null 2> /dev/null &
sleep 3
jupyter notebook list
