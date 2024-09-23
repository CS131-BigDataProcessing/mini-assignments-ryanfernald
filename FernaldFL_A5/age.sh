age=$1

if [ $age -lt 13 ]; then 
	echo "You are a child"
elif [ $age -lt 20 -a $age -gt 13 ]; then
	echo "You are a teen"
elif [ $age -lt 65 -a $age -gt 20 ]; then
	echo "You are an adult"
else 
	echo "You are elderly"

fi
