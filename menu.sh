while true; do
    echo "1) Factorial"
    echo "2) Length of string and Vowel count"
    echo "3) Exit"
    read -p "Enter your choice: " ch
    case $ch in
    1)
        read -p "Enter a number: " num
        fact=1
        for ((i = 1; i <= num; i++)); do
            fact=$((fact * i))
        done
        echo "Factorial of $num is $fact"
        ;;
    2)
        read -p "Enter a string: " str
        len=${#str}
        echo "Length of the string is $len"
        
        vowels=0
        for ((i=0; i<len; i++)); do
            char=${str:$i:1}
            if [[ "$char" == [aeiouAEIOU] ]]; then
                vowels=$((vowels + 1))
            fi
        done
        echo "Number of vowels in the string is $vowels"
        ;;
    3)
        echo "Exiting..."
        exit
        ;;
    esac
done
