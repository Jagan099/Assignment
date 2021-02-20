#Practice while loop 
#Author -Jagan

count=1
while [ $count -lt 5 ]    
do
  echo " $count "
  count=`expr $count + 1`
done

echo "----"

count1=0
while [ $count1 -lt 5 ]
do
  echo " $count1 "
   if [ $count1 -eq 2 ]
   then
        break       
   fi
   count1=`expr $count1 + 1`
done
echo "-----"



