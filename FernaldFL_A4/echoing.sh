#Activity 1
echo ""
echo "----------"
echo "Activity 1"
echo "----------"
echo ""

echo "Lets see the time and date"
echo $(date)
echo ""
echo "lets see who logged into the system"
echo $(who)
echo ""
echo "For $USER, the home directory is $HOME"

#Activity 2
echo ""
echo "----------"
echo "Activity 2"
echo "----------"
echo ""

name=$1
money=$2

echo "My name is $name, and I have $ $money, in my wallet"

#Activity 3
echo ""
echo "----------"
echo "Activity 3"
echo "----------"
echo ""

mathvar1=$[1 + 5]
mathvar2=$[mathvar1 * 20]
mathvar3=$[10]
mathvar4=$[mathvar1 * (mathvar2 + mathvar3)]

echo "Variable 1 is $mathvar1. Variable 2 is $mathvar2. Using $mathvar3 for Variable 3 our final Variable 4 is $mathvar4"

#Activity 4

echo ""
echo "----------"
echo "Activity 4"
echo "----------"
echo ""


floating=$(echo "scale=3; 4.5/1.7" |bc)
echo "Our floating variable is $floating"
