while IFS=, read -r col1 col2 col3 col4 col5 col6
do
    echo "$col1  $col2 $col3 $col4"
done < plan2.csv
