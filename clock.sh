while :
do
	clear
	time=$(date "+%T")
	python toilet2.py $time
	sleep 1
done