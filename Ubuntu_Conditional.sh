#conditional Practice
#Author-Jagan

read -p "Enter first number " first_number

#if statement
if [ $((first_number%2)) -eq 0 ]
then
echo "Number is even"
fi
echo "-------"

#if else statement
if [ $((first_number%2)) -eq 0 ]
then
echo "Number is even"
else
echo "The number is odd"
fi
echo "-------"

#if elif
if [ $((first_number%2)) -eq 0 ]
then
echo "number is EVEN"
elif [ $((first_number%2)) -eq 1 ]
then
echo "Number is ODD"
else
echo "Input ivalid"
fi


