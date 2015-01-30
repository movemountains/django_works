for i in 1..40
   if i%2 == 0 && i%4 == 0
     puts 'fizzbuzz'
   elsif i%2 == 0
     puts 'fizz'
    elsif i%4 == 0
      puts 'buzz'
    elsif i%2 != 0 && i%4 != 0
      puts i    
i += 1
   end
end

