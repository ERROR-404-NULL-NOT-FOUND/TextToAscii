while :
do
	clear
	time=$(date "+%T")
	python t2a.py -t $time
	sleep 1
done
