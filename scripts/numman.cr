def h(x)
puts "you entered '+"+x+"'"
if x=="1"
puts "it corresponds to the united states"
puts "and has the format:\n+1(area code)carrier code-user code"
elsif x=="44"
puts "and it corresponds to the united kingdom"
puts "which has many formats"
elsif x=="52"
puts "and it corresponds to mexico"
puts "which is in the format +52 area code-user code"
else
puts "that country code has not been added yet :("
end
end
def init()
puts "enter area code:"
x=read_line.chomp
return x.gsub("+","")
end
def main()
return h(init())
end
main()