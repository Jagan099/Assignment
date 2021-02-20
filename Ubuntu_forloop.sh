#practice for loop
#Author-Jagan

for i in 1 2 3 4 5 6 7 
do 
   echo $i             
      if [ $((i%2)) -eq 0 ]
       then
           echo "$i is an Even Number"
       fi
       
       if [ $((i%2)) -ne 0 ]
       then
    	  echo "$i is an Odd Number"
       fi
done

for ((i=1;i<8;i++))    
do
   echo $i
done
