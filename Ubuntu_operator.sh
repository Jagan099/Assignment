#operator practice 
#author- Jagan

read -p "Enter First word " firstword
read -p "Enter Second word "  secondword

if [ $firstword ==  $secondword ]
then
echo "Both words are equal"
fi

if [ $firstword !=  $secondword ]
then
echo "Both words are not  equal"
fi

read -p "Enter third  word " thirdword

if [ -z $thirdword ]    
then
echo "Third  word is  null"
else
echo "Third  word  is not null"
fi

if [ -n $thirdword ]   
then
echo "third  word is not null/size of string is not-zero"
else
echo "third  word  is null/size of string is zero"
fi


file="operator_script.sh"

if [ -f $file ]    
then
echo "file exist"
else
echo "file not exist"
fi
