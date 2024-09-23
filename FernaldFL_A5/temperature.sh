#!/bin/bash

temp=$1

if [ $temp -gt 85 ]; then
	echo "It's very hot"
else
	if [ $temp -gt 67 ]; then 
		echo "Nice weather"
	else
		if [ $temp -ge 55 ]; then
			echo "Cold"
		else
			echo "Freezing"
		fi
	fi
fi
